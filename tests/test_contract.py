import base64
from datetime import datetime, timezone, timedelta
import gzip
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import wiki_core as w
import news

SOURCE=Path(__file__).resolve().parents[1]

class WikiContract(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name).resolve()
        for name in ('data/schemas.yaml','data/refresh-cutoff.yaml','data/retrieval-aliases.yaml','data/report-settings.yaml','data/sources.yaml','tags/domains.yaml'):
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(SOURCE/name,p)
        shutil.copytree(SOURCE/'_templates',self.root/'_templates')
        (self.root/'index.md').write_text('# index\n')
        self.patch=patch.object(w,'ROOT',self.root);self.patch.start()
    def tearDown(self):
        self.patch.stop();self.temp.cleanup()
    def filled(self,slug='alpha',typ='entity',domain='companies',**meta):
        path=w.draft(typ,slug,[domain],slug,None)
        pg=w.page(path);pg['metadata'].update(summary='模型服务与公司发展趋势',evidence_kind='reported',**meta)
        body='# '+slug+'\n\n这是来源明确报告的模型服务动态，保留发布日期、适用条件和未独立核验的边界。\n\n## Evidence\n\n来源为测试使用的原始记录，用于验证发布完整流程，不代表任何真实公司。\n'
        w.atomic_write(self.root/path,w.serialize(pg['metadata'],body))
        with (self.root/'index.md').open('a') as f:f.write(f'\n[[{path[:-3]}|{slug}]]\n')
        return path
    def test_publication_and_retrieval_visibility(self):
        path=self.filled(aliases=['深度求索'])
        self.assertEqual(w.search('深度求索')['status'],'empty')
        self.assertEqual(w.get_page(path)['status'],'not-found')
        w.review([path],'Test reviewer')
        self.assertEqual(w.search('深度求索')['status'],'empty')
        w.finalize([path])
        self.assertEqual(w.search('DeepSeek')['results'][0]['path'],path)
        self.assertEqual(w.get_page(path)['metadata']['verification'],'unchecked')
        self.assertEqual(len(list((self.root/'queries').glob('*.md'))),6)
    def test_edit_invalidates_review(self):
        path=self.filled();w.review([path],'Test')
        with (self.root/path).open('a') as f:f.write('additional content\n')
        with self.assertRaisesRegex(ValueError,'changed after review'):w.finalize([path])
    def test_scaffold_cannot_publish(self):
        path=w.draft('source','unfinished',['models'],'unfinished')
        with self.assertRaisesRegex(ValueError,'unfinished scaffold'):w.review([path],'Test')
    def test_isolated_cycle_not_reachable(self):
        one=self.filled('one');two=self.filled('two')
        for p,target in [(one,two),(two,one)]:
            pg=w.page(p);pg['metadata']['related']=[target];w.atomic_write(self.root/p,w.serialize(pg['metadata'],pg['body']))
        (self.root/'index.md').write_text('# index\n')
        w.review([one,two],'Test')
        with self.assertRaisesRegex(ValueError,'Unreachable'):w.finalize([one,two])
    def test_ambiguous_and_broken_explicit_path(self):
        self.filled('one',aliases=['duplicate']);self.filled('two',aliases=['duplicate'])
        self.assertEqual(w.resolve('duplicate',w.pages())['status'],'ambiguous')
        self.assertEqual(w.resolve('reference/absent/one.md',w.pages())['status'],'unresolved')
    def test_verified_requires_evidence_and_not_review_date(self):
        path=self.filled(verification='source-checked')
        with self.assertRaisesRegex(ValueError,'checked claims require'):w.review([path],'Test')
    def test_raw_is_immutable_and_versioned(self):
        a=w.archive(b'first','article.txt','https://example.org/a')
        again=w.archive(b'first','article.txt','https://example.org/a')
        b=w.archive(b'second','article.txt','https://example.org/a')
        self.assertEqual(a['raw_path'],again['raw_path']);self.assertNotEqual(a['raw_path'],b['raw_path'])
        self.assertEqual((self.root/a['raw_path']).read_bytes(),b'first')
    def test_batch_failure_rolls_back_pages_and_indices(self):
        path=self.filled();w.review([path],'Test')
        before=(self.root/path).read_bytes();real=w.atomic_write
        hit=[False]
        def fail(path,data):
            if str(path).endswith('by-type.md') and not hit[0]:hit[0]=True;raise OSError('simulated replacement failure')
            return real(path,data)
        with patch.object(w,'atomic_write',side_effect=fail):
            with self.assertRaises(OSError):w.finalize([path])
        self.assertEqual((self.root/path).read_bytes(),before)
        self.assertFalse((self.root/'queries/by-domain.md').exists())
    def test_interruption_recovered_on_next_write(self):
        path=self.filled();original=(self.root/path).read_bytes()
        (self.root/'.cache').mkdir(exist_ok=True)
        w.json_write(self.root/'.cache/publication.json',{'before':{path:base64.b64encode(original).decode()}})
        (self.root/path).write_text('interrupted partial file')
        with w.write_lock():self.assertEqual((self.root/path).read_bytes(),original)
    def test_filters_and_tfidf(self):
        path=self.filled();w.review([path],'Test');w.finalize([path])
        self.assertTrue(w.search('模型服务',tfidf=True)['results'])
        self.assertEqual(w.search('模型服务',{'domain':['infra']})['status'],'empty')
    def test_deprecated_hidden(self):
        path=self.filled();w.review([path],'Test');w.finalize([path])
        pg=w.page(path);pg['metadata']['lifecycle']='deprecated';w.atomic_write(self.root/path,w.serialize(pg['metadata'],pg['body']))
        self.assertEqual(w.get_page(path)['status'],'not-found')
        self.assertEqual(w.get_page(path,include=True)['status'],'success')
    def test_future_verification_rejected(self):
        path=self.filled(last_verified='2999-01-01')
        self.assertTrue(any('future' in e for e in w.validate()))

class DailyContract(unittest.TestCase):
    setUp = WikiContract.setUp
    tearDown = WikiContract.tearDown
    def article(self,dated=True,precision='timestamp',title='A new release'):
        end=datetime.fromisoformat(news.due_window()['end'])
        text='Release source content. New serving feature with documented limits.'
        raw=w.archive(text.encode(),'article.txt','https://example.org/article')
        aid,_=news.save_article({'url':'https://example.org/article','title':title,'text':text,'published_at':(end-timedelta(hours=1)).isoformat() if dated else None,'date_basis':'published' if dated else 'unknown','date_precision':precision,'extraction':'full-text'},news.sources()[0],raw)
        return aid
    def editorial(self,pkt,aid):
        return {'date':pkt['window']['date'],'packet_sha256':pkt['packet_sha256'],'overview':'本期新增一项发布，测试中不代表实际新闻。','source_checks':[],
                'items':[{'event_key':'one-release','title':'新版本','section':3,'article_ids':[aid],'facts':['据官方发布说明新增一项功能。'],'analysis':'判断：需验证生产环境效果。','reviewed':True,'locators':{aid:'Release notes'}}]}
    def test_atom_original_date_and_gzip(self):
        atom='<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Version</title><id>id</id><link href="https://example.org/a"/><published>2026-01-01T00:00:00Z</published><updated>2026-02-01T00:00:00Z</updated><content>Text</content></entry></feed>'
        row=news.feed_entries(atom)[0]
        self.assertEqual(row['date_basis'],'published');self.assertTrue(row['published_at'].startswith('2026-01-01'))
        class Response(io.BytesIO):
            headers={'Content-Encoding':'gzip'};status=200
            def geturl(self):return 'https://example.org/feed'
        with patch.object(news,'urlopen',return_value=Response(gzip.compress(atom.encode()))):
            text,raw=news.fetch('https://example.org/feed','test')
        self.assertEqual(text,atom);self.assertTrue((self.root/raw['raw_path']).read_bytes().startswith(b'\x1f\x8b'))
    def test_unknown_dates_do_not_become_today(self):
        self.article(dated=False)
        pkt,_=news.packet();self.assertEqual(pkt['articles'],[]);self.assertEqual(pkt['coverage']['excluded']['undated'],1)
    def test_report_requires_review_and_real_ids(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid)
        ed['items'][0]['article_ids']=['invented']
        with self.assertRaisesRegex(ValueError,'Evidence ID'):news.validate_editorial(ed,pkt)
        ed=self.editorial(pkt,aid);ed['items'][0]['reviewed']=False
        with self.assertRaisesRegex(ValueError,'reviewed'):news.validate_editorial(ed,pkt)
    def test_window_and_packet_change_invalidate_editorial(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid)
        ed['date']='2020-01-01'
        with self.assertRaises(ValueError):news.validate_editorial(ed,pkt)
        ed=self.editorial(pkt,aid);ed['packet_sha256']='stale'
        with self.assertRaises(ValueError):news.validate_editorial(ed,pkt)
    def test_duplicate_events_rejected(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid);ed['items']*=2
        with self.assertRaisesRegex(ValueError,'Duplicate'):news.validate_editorial(ed,pkt)
    def test_report_and_idempotence(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid)
        path=self.root/'editorial.json';w.json_write(path,ed)
        result=news.report(path)
        text=(self.root/result['report_path']).read_text()
        self.assertIn('AI Infra社区',text);self.assertIn('https://example.org/article',text)
        self.assertTrue(news.report(path)['unchanged'])
    def test_no_candidate_does_not_imply_no_news(self):
        result=news.report()
        self.assertIn('不代表行业没有新闻',(self.root/result['report_path']).read_text())
    def test_candidate_requires_editorial(self):
        self.article()
        with self.assertRaisesRegex(ValueError,'editorial review required'):news.report()
    def test_full_text_survives_feed_refresh(self):
        aid=self.article();raw=w.archive(b'short','feed.xml')
        news.save_article({'url':'https://example.org/article','title':'A new release','text':'short','published_at':None,'extraction':'feed-content'},news.sources()[0],raw)
        self.assertEqual(news.load_articles()[0]['extraction'],'full-text')
    def test_beijing_window_is_independent_of_us_dst(self):
        with patch.object(news,'now',return_value=datetime(2026,10,1,23,59,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['date'],'2026-10-01')
        with patch.object(news,'now',return_value=datetime(2026,10,2,0,0,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['date'],'2026-10-02')
        with patch.object(news,'now',return_value=datetime(2026,12,2,0,0,tzinfo=timezone.utc)):
            self.assertTrue(news.due_window()['end'].endswith('08:00:00+08:00'))

    def test_arxiv_feed_date_is_announcement_not_submission(self):
        rss='<rss><channel><item><title>Paper</title><link>https://arxiv.org/abs/2609.12345</link><pubDate>Thu, 01 Oct 2026 00:00:00 -0400</pubDate><description>Abstract</description></item></channel></rss>'
        entry=news.feed_entries(rss)[0]
        self.assertEqual(entry['date_basis'],'announced')
        self.assertIsNone(entry['published_at'])
        self.assertTrue(entry['announced_at'].startswith('2026-10-01'))

    def test_date_only_marks_boundary_uncertainty(self):
        self.article(precision='date-only')
        pkt,_=news.packet()
        self.assertTrue(pkt['articles'][0]['date_boundary_uncertain'])

    def test_metadata_only_cannot_support_report(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid)
        pkt['articles'][0]['text']=''
        with self.assertRaisesRegex(ValueError,'Source text is missing'):
            news.validate_editorial(ed,pkt)

if __name__=='__main__':unittest.main()
