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
import yaml
from unittest.mock import patch
from urllib.error import HTTPError
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
        self.assertIn('洛杉矶时间，右端不含',text)
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
    def test_los_angeles_daily_cutoff_and_local_date(self):
        with patch.object(news,'now',return_value=datetime(2026,10,2,0,59,59,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['date'],'2026-09-30')
            with self.assertRaisesRegex(ValueError,'not closed'):news.due_window('2026-10-01')
        with patch.object(news,'now',return_value=datetime(2026,10,2,1,0,tzinfo=timezone.utc)):
            window=news.due_window()
            self.assertEqual(window['date'],'2026-10-01')
            self.assertEqual(window['timezone'],'America/Los_Angeles')
            self.assertEqual(window['start'],'2026-09-30T18:00:00-07:00')
            self.assertEqual(window['end'],'2026-10-01T18:00:00-07:00')
            self.assertEqual(news.due_window('2026-10-01'),window)
        with patch.object(news,'now',return_value=datetime(2026,12,2,1,59,59,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['date'],'2026-11-30')
        with patch.object(news,'now',return_value=datetime(2026,12,2,2,0,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['end'],'2026-12-01T18:00:00-08:00')

    def test_dst_windows_are_contiguous_and_packets_respect_boundaries(self):
        cases=[
            ('daily','2026-03-07T18:00:00-08:00','2026-03-08T18:00:00-07:00',23),
            ('daily','2026-10-31T18:00:00-07:00','2026-11-01T18:00:00-08:00',25),
            ('weekly','2026-03-06T18:00:00-08:00','2026-03-13T18:00:00-07:00',167),
            ('weekly','2026-10-30T18:00:00-07:00','2026-11-06T18:00:00-08:00',169),
        ]
        for period,start_text,end_text,hours in cases:
            start,end=map(datetime.fromisoformat,(start_text,end_text))
            with self.subTest(period=period,end=end_text),patch.object(news,'now',return_value=end.astimezone(timezone.utc)):
                window=news.due_window(period=period)
                self.assertEqual((window['start'],window['end']),(start_text,end_text))
                self.assertEqual(end-start,timedelta(hours=hours))
                self.assertEqual(news.due_window(start.date().isoformat(),period)['end'],start_text)
                self.assertEqual(news.due_window(end.date().isoformat(),period),window)
                raw=w.archive(b'source','article.txt')
                ids={}
                for label,stamp in [('before',start-timedelta(seconds=1)),('start',start),('last',end-timedelta(seconds=1)),('end',end)]:
                    ids[label],_=news.save_article({'url':f'https://example.org/{period}/{end.date()}/{label}',
                        'title':label,'text':'Source text','published_at':stamp.isoformat(),'date_basis':'published'},news.sources()[0],raw)
                pkt,_=news.packet(period=period)
                included={a['id'] for a in pkt['articles']}
                self.assertEqual(included & set(ids.values()),{ids['start'],ids['last']})

    def test_report_timezone_does_not_reinterpret_source_dates(self):
        self.assertEqual(news.parse_date('2026-10-01'),'2026-10-01T00:00:00+08:00')

    def test_arxiv_feed_date_is_announcement_not_submission(self):
        rss='<rss><channel><item><title>Paper</title><link>https://arxiv.org/abs/2609.12345</link><pubDate>Thu, 01 Oct 2026 00:00:00 -0400</pubDate><description>Abstract</description></item></channel></rss>'
        entry=news.feed_entries(rss)[0]
        self.assertEqual(entry['date_basis'],'announced')
        self.assertIsNone(entry['published_at'])
        self.assertTrue(entry['announced_at'].startswith('2026-10-01'))

    def test_date_only_marks_boundary_uncertainty(self):
        aid=self.article(precision='date-only')
        pkt,_=news.packet()
        self.assertTrue(pkt['articles'][0]['date_boundary_uncertain'])
        path=self.root/'editorial.json';w.json_write(path,self.editorial(pkt,aid))
        result=news.report(path)
        self.assertIn('无法确认 18:00 边界',(self.root/result['report_path']).read_text())

    def test_metadata_only_cannot_support_report(self):
        aid=self.article();pkt,_=news.packet();ed=self.editorial(pkt,aid)
        pkt['articles'][0]['text']=''
        with self.assertRaisesRegex(ValueError,'Source text is missing'):
            news.validate_editorial(ed,pkt)

    def test_weekly_cutoff_and_seven_day_window(self):
        with patch.object(news,'now',return_value=datetime(2026,10,3,0,59,59,tzinfo=timezone.utc)):
            self.assertEqual(news.due_window()['date'],'2026-10-01')
            self.assertEqual(news.due_window(period='weekly')['date'],'2026-09-25')
        with patch.object(news,'now',return_value=datetime(2026,10,3,1,0,tzinfo=timezone.utc)):
            window=news.due_window(period='weekly')
            self.assertEqual(window['date'],'2026-10-02')
            self.assertEqual(window['timezone'],'America/Los_Angeles')
            self.assertEqual(window['start'],'2026-09-25T18:00:00-07:00')
            self.assertEqual(window['end'],'2026-10-02T18:00:00-07:00')
            self.assertEqual(news.due_window()['end'],window['end'])
            self.assertEqual(datetime.fromisoformat(window['end'])-datetime.fromisoformat(window['start']),timedelta(days=7))

    def test_weekly_cross_year_and_missed_run(self):
        with patch.object(news,'now',return_value=datetime(2027,1,4,12,tzinfo=timezone.utc)):
            window=news.due_window(period='weekly')
            self.assertEqual(window['date'],'2027-01-01')
            self.assertEqual(window['start'],'2026-12-25T18:00:00-08:00')
            self.assertTrue(str(news.report_folder('weekly',window['date'])).endswith('weekly/2027/01/2027-01-01'))

    def test_weekly_explicit_date_rejects_incomplete_or_wrong_day(self):
        with patch.object(news,'now',return_value=datetime(2026,10,2,12,tzinfo=timezone.utc)):
            with self.assertRaisesRegex(ValueError,'Friday'):news.due_window('2026-10-01','weekly')
            with self.assertRaisesRegex(ValueError,'not closed'):news.due_window('2026-10-02','weekly')
            with self.assertRaisesRegex(ValueError,'YYYY-MM-DD'):news.due_window('2026-10-01T18:00:00')

    def test_weekly_packet_includes_earlier_days_and_excludes_previous_week(self):
        with patch.object(news,'now',return_value=datetime(2026,10,3,1,tzinfo=timezone.utc)):
            raw=w.archive(b'source','article.txt')
            for day in (24,25,29):
                news.save_article({'url':f'https://example.org/{day}','title':str(day),'text':'Archived source text','published_at':f'2026-09-{day}T18:00:00-07:00','date_basis':'published'},news.sources()[0],raw)
            daily,_=news.packet();weekly,_=news.packet(period='weekly')
            self.assertEqual(daily['articles'],[])
            self.assertEqual({a['title'] for a in weekly['articles']},{'25','29'})

    def test_daily_weekly_reports_and_edits_are_separate(self):
        with patch.object(news,'now',return_value=datetime(2026,10,3,1,tzinfo=timezone.utc)):
            aid=self.article();daily,_=news.packet();weekly,_=news.packet(period='weekly')
            ed=self.editorial(daily,aid)
            with self.assertRaisesRegex(ValueError,'period'):news.validate_editorial(ed,weekly)
            path=self.root/'editorial.json';w.json_write(path,ed)
            d=news.report(path)
            ed=self.editorial(weekly,aid);ed['period']='weekly'
            with self.assertRaisesRegex(ValueError,'outlook'):news.validate_editorial(ed,weekly)
            ed['outlook']=['观察新功能能否在相同负载下稳定工作。'];w.json_write(path,ed)
            result=news.report(path,period='weekly')
            self.assertEqual(d['report_path'],'reports/daily/2026/10/2026-10-02/report.md')
            self.assertEqual(result['report_path'],'reports/weekly/2026/10/2026-10-02/report.md')
            content=(self.root/result['report_path']).read_text()
            self.assertIn('AI 产业分析周报',content);self.assertIn('下周观察',content)
            self.assertTrue(news.report(path,period='weekly')['unchanged'])
            old_hash=result['editorial_sha256'];ed['overview']='补充后的周度判断。';w.json_write(path,ed)
            news.report(path,period='weekly')
            self.assertEqual((self.root/result['report_path']).parent.joinpath('revisions',old_hash,'report.md').read_text(),content)
            self.assertTrue((self.root/d['report_path']).exists())
            self.assertIn('2026/10/2026-10-02/report.md',(self.root/'reports/weekly/index.md').read_text())

    def test_legacy_migration_preserves_text_evidence_and_revisions(self):
        old=self.root/'reports/daily/2026-10-02';old.mkdir(parents=True)
        (old/'report.md').write_text('Original report with source links.\n')
        (old/'editorial.json').write_text('{"unchanged":true}\n')
        manifest={'date':'2026-10-02','report_path':'reports/daily/2026-10-02/report.md','packet_path':'data/packets/old.json','events':1,'status':'analyzed'}
        w.json_write(old/'manifest.json',manifest)
        w.json_write(old/'revisions/abc/manifest.json',manifest)
        news.migrate_reports()
        target=self.root/'reports/daily/2026/10/2026-10-02'
        self.assertEqual((target/'report.md').read_text(),'Original report with source links.\n')
        moved=json.loads((target/'manifest.json').read_text())
        self.assertEqual(moved['packet_path'],'data/packets/old.json')
        self.assertEqual(moved['report_path'],'reports/daily/2026/10/2026-10-02/report.md')
        self.assertTrue((target/'revisions/abc/manifest.json').exists())
        self.assertFalse(old.exists());self.assertEqual(news.migrate_reports()['moved'],[])

    def test_migration_refuses_collision_before_moving_anything(self):
        for date_value in ('2026-10-01','2026-10-02'):
            (self.root/'reports/daily'/date_value).mkdir(parents=True)
        news.report_folder('daily','2026-10-02').mkdir(parents=True)
        with self.assertRaisesRegex(ValueError,'already exists'):news.migrate_reports()
        self.assertTrue((self.root/'reports/daily/2026-10-01').exists())


NOW=datetime(2026,10,2,3,0,tzinfo=timezone.utc)  # 20:00 Los Angeles; daily window 10-01 01:00Z to 10-02 01:00Z

def rss(*items):
    rows=''.join(f'<item><title>{t}</title><link>{u}</link><pubDate>{d}</pubDate><description>{x}</description></item>' for t,u,d,x in items)
    return f'<?xml version="1.0"?><rss><channel>{rows}</channel></rss>'

class CollectContract(unittest.TestCase):
    setUp = WikiContract.setUp
    tearDown = WikiContract.tearDown
    def configure(self,*rows):
        defaults={'section':1,'group':'media','kind':'feed','enabled':True}
        w.atomic_write(self.root/'data/sources.yaml',yaml.safe_dump({'sources':[dict(defaults,**r) for r in rows]},allow_unicode=True))
    def serve(self,pages,calls=None):
        def fake(req,timeout=None):
            if calls is not None:calls.append(req.full_url)
            if req.full_url not in pages:raise HTTPError(req.full_url,404,'Not Found',{},io.BytesIO(b''))
            body=pages[req.full_url]
            class Response(io.BytesIO):
                headers={'Content-Type':'text/html'};status=200
                def geturl(self):return req.full_url
            return Response(body.encode() if isinstance(body,str) else body)
        return patch.object(news,'urlopen',side_effect=fake)
    def collect(self,pages,**kw):
        with self.serve(pages),patch.object(news,'now',return_value=kw.pop('at',NOW)):return news.collect(**kw)
    def test_config_requires_group_and_valid_options(self):
        self.configure({'id':'a','name':'A','url':'https://example.org/feed','group':'blogs'})
        with self.assertRaisesRegex(ValueError,'group'):news.validate_config()
        self.configure({'id':'a','name':'A','url':'https://example.org/feed','link_pattern':'('})
        with self.assertRaisesRegex(ValueError,'link_pattern'):news.validate_config()
        self.configure({'id':'a','name':'A','url':'https://example.org/feed','poll_hours':0})
        with self.assertRaisesRegex(ValueError,'poll_hours'):news.validate_config()
    def test_repository_sources_validate(self):
        shutil.copyfile(SOURCE/'data/sources.yaml',self.root/'data/sources.yaml')
        self.assertGreater(news.validate_config()['sources'],50)
        self.assertTrue(all(s.get('group') in news.GROUPS for s in news.sources()))
    def test_chinese_feed_date_and_gbk_page(self):
        self.assertEqual(news.parse_date('2026-09-30 19:38:45  +0800'),'2026-09-30T19:38:45+08:00')
        page='<html><head><meta charset="gb2312"></head><body><a href="/news/1/a1.html">算力新闻</a></body></html>'.encode('gb18030')
        text,charset=news.decode(page,{})
        self.assertEqual(charset,'gb18030');self.assertIn('算力新闻',text)
    def test_keyword_filter_and_feed_gap_reach_report(self):
        self.configure({'id':'wire','name':'Wire','url':'https://example.org/feed','include':['AI','芯片']})
        w.json_write(self.root/news.STATE,{'wire':{'last_ok_at':'2026-10-01T10:00:00+00:00','last_attempt_at':'2026-10-01T10:00:00+00:00'}})
        feed=rss(('New AI chip','https://example.org/a','Thu, 01 Oct 2026 22:00:00 GMT','x'),
                 ('Said and paid','https://example.org/b','Thu, 01 Oct 2026 21:00:00 GMT','no keyword'),
                 ('国产芯片涨价','https://example.org/c','Thu, 01 Oct 2026 20:00:00 GMT','x'))
        run=self.collect({'https://example.org/feed':feed})
        result=run['sources'][0]
        self.assertEqual(result['filtered'],1);self.assertEqual(result['saved'],2)
        self.assertEqual(result['gap']['to'],'2026-10-01T20:00:00+00:00')
        with patch.object(news,'now',return_value=NOW):
            pkt,_=news.packet()
            self.assertEqual(pkt['coverage']['gaps'][0]['source_id'],'wire')
            w.atomic_write(self.root/'data/watchlist.yaml',yaml.safe_dump({'discovery':{'searches':[{'id':'wire-exclusives','query':'site:example.org'},{'id':'policy','query':'x'}]}}))
            ed={'date':pkt['window']['date'],'packet_sha256':pkt['packet_sha256'],'overview':'测试窗口。','items':[],
                'source_checks':[{'source_id':'wire-exclusives','status':'checked','note':'按窗口检索，未发现新独家'}]}
            path=self.root/'editorial.json';w.json_write(path,ed)
            text=(self.root/news.report(str(path))['report_path']).read_text()
        self.assertIn('可能漏采 2026-10-01T10:00 至 2026-10-01T20:00',text)
        self.assertIn('- wire-exclusives：checked；按窗口检索，未发现新独家。',text);self.assertIn('- policy：not-checked；本次未执行。',text)
    def test_search_results_are_leads_not_evidence(self):
        self.configure({'id':'agg','name':'Aggregator','url':'https://news.example.org/rss?q=ai','group':'aggregator'})
        self.collect({'https://news.example.org/rss?q=ai':rss(('Exclusive: deal - Wire','https://news.example.org/a/1','Thu, 01 Oct 2026 21:00:00 GMT','Exclusive: deal Wire'))})
        article=news.load_articles()[0]
        self.assertTrue(article['lead']);self.assertEqual(article['extraction'],'metadata-only');self.assertEqual(article['summary'],'Exclusive: deal Wire')
        with patch.object(news,'now',return_value=NOW):pkt,_=news.packet()
        ed={'date':pkt['window']['date'],'packet_sha256':pkt['packet_sha256'],'overview':'测试。','source_checks':[],
            'items':[{'event_key':'deal','title':'交易','section':1,'article_ids':[article['id']],'facts':['据报道。'],'analysis':'判断。','reviewed':True,'locators':{article['id']:'标题'}}]}
        with self.assertRaisesRegex(ValueError,'Source text is missing'):news.validate_editorial(ed,pkt)
    def test_listing_baseline_then_new_link_becomes_lead(self):
        self.configure({'id':'lab','name':'Lab','url':'https://lab.example.org/news','kind':'web','group':'official','link_pattern':r'/news/[a-z0-9-]+$'})
        page='<a href="/news/old-post">Old</a><a href="/about">About</a>'
        first=self.collect({'https://lab.example.org/news':page},at=NOW-timedelta(days=1))['sources'][0]
        self.assertEqual(first['status'],'needs-review');self.assertTrue(first['baseline']);self.assertEqual(news.load_articles(),[])
        page='<a href="/news/new-model">New model <span>Sep 30</span></a>'+page
        # Discovered at 14:00 Los Angeles, inside the 10-01 daily window that closes at 18:00.
        second=self.collect({'https://lab.example.org/news':page},at=NOW-timedelta(hours=6))['sources'][0]
        self.assertEqual((second['status'],second['new_links'],second['leads']),('ok',1,1))
        lead=news.load_articles()[0]
        self.assertEqual((lead['url'],lead['date_basis'],lead['title']),('https://lab.example.org/news/new-model','discovered','New model Sep 30'))
        with patch.object(news,'now',return_value=NOW):pkt,_=news.packet()
        self.assertTrue(pkt['articles'][0]['date_boundary_uncertain']);self.assertEqual(pkt['coverage']['leads'],1)
        third=self.collect({'https://lab.example.org/news':'<p>Rendering placeholder</p>'},at=NOW+timedelta(hours=1))['sources'][0]
        self.assertEqual(third['status'],'failed')
        self.assertEqual(json.loads((self.root/news.STATE).read_text())['lab']['raw_path'],second['raw_path'])
    def test_page_change_detection_creates_one_lead_per_version(self):
        self.configure({'id':'log','name':'Change Log','url':'https://docs.example.org/updates','kind':'web','group':'official'})
        base='<main>'+'<p>Date: 2026-09-01 Model A released with a documented context window.</p>'*5+'</main>'
        self.collect({'https://docs.example.org/updates':base},at=NOW-timedelta(days=1))
        same=self.collect({'https://docs.example.org/updates':base},at=NOW-timedelta(hours=12))['sources'][0]
        self.assertFalse(same['changed']);self.assertEqual(news.load_articles(),[])
        changed=base.replace('<main>','<main><p>Date: 2026-10-01 Model A kept after user demand.</p>')
        result=self.collect({'https://docs.example.org/updates':changed})['sources'][0]
        self.assertTrue(result['changed']);self.assertIn('+Date: 2026-10-01 Model A kept after user demand.',result['diff'])
        lead=news.load_articles()[0]
        self.assertTrue(lead['lead']);self.assertIn('kept after user demand',lead['summary']);self.assertEqual(lead['text'],'')
    def test_due_mode_respects_poll_hours_and_browser_sources_are_not_fetched(self):
        self.configure({'id':'fast','name':'Fast','url':'https://fast.example.org/feed','poll_hours':4},
                       {'id':'slow','name':'Slow','url':'https://slow.example.org/feed','poll_hours':24},
                       {'id':'js','name':'JS','url':'https://js.example.org/','kind':'web','group':'official','fetch':'browser'})
        recent=(NOW-timedelta(hours=5)).isoformat()
        w.json_write(self.root/news.STATE,{'fast':{'last_attempt_at':recent},'slow':{'last_attempt_at':recent},'js':{'last_attempt_at':recent}})
        calls=[]
        with self.serve({'https://fast.example.org/feed':rss()},calls),patch.object(news,'now',return_value=NOW):
            self.assertEqual(news.due_sources(),['fast'])
            run=news.collect(due=True)
            self.assertEqual([r['source_id'] for r in run['sources']],['fast'])
            runs=len(list((self.root/'data/runs').glob('*.json')))
            self.assertIsNone(news.collect(due=True)['id'])
            self.assertEqual(len(list((self.root/'data/runs').glob('*.json'))),runs)
            run=news.collect(selected=['js'])
        self.assertEqual([c for c in calls if not c.endswith('/robots.txt')],['https://fast.example.org/feed'])
        self.assertEqual(run['sources'][0]['status'],'needs-browser')
    def test_scheduled_collection_obeys_robots_txt(self):
        self.configure({'id':'closed','name':'Closed','url':'https://closed.example.org/rss/search?q=ai'},
                       {'id':'open','name':'Open','url':'https://open.example.org/feed'})
        calls=[]
        pages={'https://closed.example.org/robots.txt':'User-agent: *\nDisallow: /\nAllow: /$\n','https://open.example.org/feed':rss()}
        with self.serve(pages,calls),patch.object(news,'now',return_value=NOW):run=news.collect()
        status={r['source_id']:r for r in run['sources']}
        self.assertEqual(status['closed']['status'],'failed');self.assertIn('robots.txt',status['closed']['error'])
        self.assertEqual(status['open']['status'],'ok')
        self.assertNotIn('https://closed.example.org/rss/search?q=ai',calls)
    def test_feed_scan_never_replaces_agent_imported_records(self):
        self.configure({'id':'wire','name':'Wire','url':'https://example.org/feed'})
        raw=w.archive(b'notes','notes.txt','https://example.org/a')
        imported={'url':'https://example.org/a','title':'Read','text':'Agent notes from the full page.','published_at':'2026-10-01T10:00:00+00:00',
                  'date_basis':'published','extraction':'browser-read; source-notes archived','retrieval_method':'web-reader-notes'}
        aid,_=news.save_article(imported,news.sources()[0],raw)
        self.collect({'https://example.org/feed':rss(('Read','https://example.org/a','Thu, 01 Oct 2026 10:00:00 GMT','Short AI summary'))})
        article=json.loads((self.root/'data/articles'/(aid+'.json')).read_text())
        self.assertEqual(article['text'],'Agent notes from the full page.')
        self.assertFalse((self.root/'data/article-history'/aid).exists())
    def test_same_url_in_two_feeds_keeps_richer_text(self):
        self.configure({'id':'short','name':'Short','url':'https://a.example.org/feed'},{'id':'long','name':'Long','url':'https://b.example.org/feed'})
        item=lambda text:rss(('AI launch','https://example.org/post','Thu, 01 Oct 2026 10:00:00 GMT',text))
        pages={'https://a.example.org/feed':item('Short AI note'),'https://b.example.org/feed':item('A much longer AI article body with details.')}
        for _ in range(2):self.collect(pages)
        article=news.load_articles()[0]
        self.assertEqual(article['source_id'],'long');self.assertIn('much longer',article['text'])
        self.collect(pages,selected=['short'])
        self.assertEqual(news.load_articles()[0]['source_id'],'long')
    def test_truncation_counts_only_entries_not_already_archived(self):
        self.configure({'id':'wire','name':'Wire','url':'https://example.org/feed'})
        items=[(f'AI item {i}',f'https://example.org/{i}',f'Thu, 01 Oct 2026 {10+i}:00:00 GMT','x') for i in range(5)]
        self.assertEqual(self.collect({'https://example.org/feed':rss(*items)},limit=3)['sources'][0]['truncated'],2)
        self.assertEqual(self.collect({'https://example.org/feed':rss(*items)},limit=5)['sources'][0]['truncated'],0)
        self.assertEqual(self.collect({'https://example.org/feed':rss(*items)},limit=3)['sources'][0]['truncated'],0)

if __name__=='__main__':unittest.main()
