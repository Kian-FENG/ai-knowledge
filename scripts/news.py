"""Auditable collection → packet → reviewed editorial → daily Markdown.
The agent supplies analysis. Collection never fabricates an editorial report.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import gzip
import hashlib
from html import unescape
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from urllib.request import Request, urlopen
import uuid
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
import wiki_core as w


def now():
    return datetime.now(timezone.utc)


def settings():
    return w.config('data/report-settings.yaml')


def sources():
    return w.config('data/sources.yaml')['sources']


def canonical(url):
    p = urlsplit(url)
    if p.scheme not in ('http','https') or not p.hostname or p.username or p.password:
        raise ValueError('A public HTTP(S) source URL is required')
    if p.hostname in ('localhost','127.0.0.1','::1'):
        raise ValueError('Local addresses cannot be news sources')
    query = [(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True) if not k.startswith('utm_') and k not in ('fbclid','gclid')]
    return urlunsplit((p.scheme,p.netloc.lower(),p.path or '/',urlencode(query),''))


def parse_date(value):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.strip().replace('Z','+00:00'))
    except ValueError:
        try:
            dt = parsedate_to_datetime(value)
        except (ValueError, TypeError, OverflowError):
            return None
    if dt.tzinfo is None:
        # Date-only source values have no implied publication hour.
        dt = dt.replace(tzinfo=ZoneInfo(settings()['timezone']))
    return dt.isoformat()


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
        self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style','noscript','svg'):
            self.skip+=1
        if tag in ('p','div','li','br','h1','h2','h3') and not self.skip:
            self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style','noscript','svg') and self.skip:
            self.skip-=1
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)


def html_text(text):
    parser=TextExtractor()
    parser.feed(text)
    return '\n'.join(x.strip() for x in ''.join(parser.parts).splitlines() if x.strip())


def fetch(url,source_id):
    url=canonical(url)
    maximum=settings()['max_response_bytes']
    req=Request(url,headers={'User-Agent':'AI-Knowledge/1.0 (public source research)','Accept-Encoding':'gzip','Accept':'application/atom+xml, application/rss+xml, text/html, */*'})
    status=200
    headers={}
    fetched=now().isoformat()
    try:
        with urlopen(req,timeout=settings()['timeout_seconds']) as response:
            headers=dict(response.headers.items())
            body=response.read(maximum+1)
            final_url=response.geturl()
            status=response.status
    except HTTPError as error:
        body=error.read(maximum+1)
        headers=dict(error.headers.items())
        final_url=url
        status=error.code
    clipped=len(body)>maximum
    record=w.archive(body[:maximum], 'http-response.body',url)
    record.update(source_id=source_id,status=status,headers=headers,final_url=final_url,fetched_at=fetched,truncated=clipped)
    w.json_write(w.ROOT/'data/fetches'/(uuid.uuid4().hex+'.json'),record)
    if status>=400:
        raise ValueError(f'HTTP {status}; raw={record["raw_path"]}')
    if clipped:
        raise ValueError(f'Response exceeds {maximum} bytes; truncated raw preserved')
    if body.startswith(b'\x1f\x8b'):
        with gzip.GzipFile(fileobj=io.BytesIO(body)) as z:
            decoded=z.read(maximum+1)
        if len(decoded)>maximum:raise ValueError('Decompressed response exceeds size limit')
        body=decoded
    return body.decode('utf-8',errors='replace'),record


def feed_entries(text):
    root=ET.fromstring(text)
    ns={'a':'http://www.w3.org/2005/Atom'}
    entries=[]
    for element in root.findall('.//item')+root.findall('a:entry',ns):
        def val(*names):
            for name in names:
                node=element.find(name,ns)
                if node is not None:
                    value=''.join(node.itertext()).strip()
                    if value:return value
            return ''
        url=val('link')
        if not url:
            for link in element.findall('a:link',ns):
                if link.get('rel','alternate')=='alternate':
                    url=link.get('href','')
                    break
        if not url:url=val('a:id')
        published=val('pubDate','a:published')
        updated=val('a:updated')
        text_body=val('a:content','{http://purl.org/rss/1.0/modules/content/}encoded','description','a:summary')
        is_arxiv_rss='arxiv.org' in url and element.tag=='item'
        entries.append({'url':url,'title':val('title','a:title'),'text':html_text(text_body),
                        'published_at':None if is_arxiv_rss else parse_date(published),
                        'announced_at':parse_date(published) if is_arxiv_rss else None,
                        'updated_at':parse_date(updated),
                        'date_basis':'announced' if is_arxiv_rss and published else 'published' if published else 'updated' if updated else 'unknown',
                        'extraction':'abstract' if 'arxiv.org' in url else 'feed-content','date_precision':'timestamp'})
    return entries


def save_article(article,src,raw):
    url=canonical(article['url'])
    aid=hashlib.sha256(url.encode()).hexdigest()[:20]
    full=dict(article,id=aid,url=url,source_id=src['id'],source_name=src['name'],section=src['section'],
              raw_path=raw['raw_path'],source_sha256=raw['sha256'],fetched_at=raw['fetched_at'])
    full.setdefault('published_at',None)
    full.setdefault('date_basis','unknown')
    full.setdefault('date_precision','timestamp')
    full.setdefault('extraction','full-text')
    if not full.get('title'):
        raise ValueError('Article title is required')
    if not full.get('text', '').strip():
        full['text'] = ''
        full['extraction'] = 'metadata-only'
    path=w.ROOT/'data/articles'/(aid+'.json')
    if path.exists():
        old=json.loads(path.read_text())
        # A later feed scan must not replace full evidence with a short summary.
        if old.get('extraction')=='full-text' and full['extraction']!='full-text':return aid,False
        if all(old.get(k)==full.get(k) for k in ('title','text','published_at','updated_at','announced_at','date_basis','extraction')):return aid,False
        w.json_write(w.ROOT/'data/article-history'/aid/(old['source_sha256']+'.json'),old)
    w.json_write(path,full)
    return aid,True


def validate_config():
    ids=set()
    for src in sources():
        if src['id'] in ids:raise ValueError('Duplicate source ID')
        ids.add(src['id'])
        canonical(src['url'])
        if src['kind'] not in ('feed','web') or src['section'] not in range(len(settings()['sections'])):raise ValueError('Invalid source configuration')
    ZoneInfo(settings()['timezone'])
    return {'status':'success','sources':len(ids),'timezone':settings()['timezone']}


def effective_date(article):
    field={'announced':'announced_at','updated':'updated_at','published':'published_at'}.get(article.get('date_basis'))
    return article.get(field) if field else None


def collect(days=14,limit=60,selected=None):
    if not 1<=days<=90 or not 1<=limit<=500:raise ValueError('days 1–90, limit 1–500')
    validate_config()
    enabled=[s for s in sources() if s.get('enabled',True) and (not selected or s['id'] in selected)]
    if selected and set(selected)-{s['id'] for s in enabled}:raise ValueError('Unknown --source')
    started=now()
    def run(src):
        result={'source_id':src['id'],'name':src['name'],'status':'ok','saved':0,'unchanged':0,'unknown_date':0,'future_date':0,'truncated':0,'needs_fulltext':0}
        try:
            text,raw=fetch(src['url'],src['id'])
            result['raw_path']=raw['raw_path']
            if src['kind']=='web':
                result.update(status='needs-review',reason='Landing page archived; Agent must inspect dated article links',landing_text=html_text(text)[:1000])
                return result
            candidates=[]
            for entry in feed_entries(text):
                date_value=effective_date(entry)
                dt=datetime.fromisoformat(date_value) if date_value else None
                if not dt:result['unknown_date']+=1
                elif dt>started:result['future_date']+=1
                elif dt<started-timedelta(days=days):continue
                candidates.append(entry)
            candidates.sort(key=lambda e:effective_date(e) or '',reverse=True)
            result['truncated']=max(0,len(candidates)-limit)
            result['candidates']=len(candidates)
            for entry in candidates[:limit]:
                try:
                    _,changed=save_article(entry,src,raw)
                    result['saved' if changed else 'unchanged']+=1
                    result['needs_fulltext']+=1
                except ValueError as error:
                    result.setdefault('article_errors',[]).append(str(error))
            if result.get('article_errors'):result['status']='partial'
            # API/feeds may themselves cap listings. This is a source coverage limit.
            result['listing_is_complete']=False
        except Exception as error:
            result.update(status='failed',error=str(error))
        return result
    with ThreadPoolExecutor(max_workers=4) as executor:
        results=list(executor.map(run,enabled))
    rid=started.strftime('%Y%m%dT%H%M%S')+'-'+uuid.uuid4().hex[:8]
    run={'id':rid,'started_at':started.isoformat(),'finished_at':now().isoformat(),'sources':results,'selected_sources':selected or [],'lookback_days':days,'per_source_limit':limit}
    w.json_write(w.ROOT/'data/runs'/(rid+'.json'),run)
    return run


def due_window(report_date=None):
    cfg=settings()
    local=now().astimezone(ZoneInfo(cfg['timezone']))
    if report_date:
        end=datetime.fromisoformat(report_date).replace(hour=cfg['daily_hour'],tzinfo=ZoneInfo(cfg['timezone']))
        if end>local:raise ValueError('Cannot report a window that has not closed')
    else:
        end=local.replace(hour=cfg['daily_hour'],minute=0,second=0,microsecond=0)
        if end>local:end-=timedelta(days=1)
    return {'date':end.date().isoformat(),'timezone':cfg['timezone'],'start':(end-timedelta(days=1)).isoformat(),'end':end.isoformat()}


def load_articles():
    return [json.loads(p.read_text()) for p in sorted((w.ROOT/'data/articles').glob('*.json'))]


def latest_health():
    runs=sorted((w.ROOT/'data/runs').glob('*.json'))
    if not runs:return {'id':None,'sources':[]}
    latest=json.loads(runs[-1].read_text())
    merged={}
    for path in reversed(runs):
        run=json.loads(path.read_text())
        for source in run['sources']:
            merged.setdefault(source['source_id'],dict(source,checked_at=run['finished_at']))
    latest['sources']=list(merged.values())
    return latest


def packet(report_date=None):
    window=due_window(report_date)
    start,end=(datetime.fromisoformat(window[k]) for k in ('start','end'))
    entries=[]
    excluded={'undated':0,'future':0,'out_of_window':0}
    for article in load_articles():
        dtval=effective_date(article)
        if not dtval:excluded['undated']+=1;continue
        dt=datetime.fromisoformat(dtval)
        precision=article.get('date_precision','timestamp')
        if dt>now():excluded['future']+=1;continue
        intersects = (dt < end and dt + timedelta(days=1) > start) if precision=='date-only' else start<=dt<end
        if not intersects:excluded['out_of_window']+=1;continue
        item=dict(article)
        item['text_truncated']=len(item['text'])>16000
        item['text']=item['text'][:16000]
        item['date_boundary_uncertain']=precision=='date-only'
        entries.append(item)
    run=latest_health()
    coverage={'excluded':excluded,'source_health':run['sources'],'run_id':run['id'],'feed_limit_note':'Feeds/API may only expose recent entries; no claim of exhaustive coverage.'}
    evidence_key={'window':window,'articles':[{k:a.get(k) for k in ('id','source_sha256','published_at','updated_at','announced_at','date_basis','date_precision')} for a in entries],
                  'health':[{k:h.get(k) for k in ('source_id','status','truncated','unknown_date','error')} for h in run['sources']]}
    version=hashlib.sha256(json.dumps(evidence_key,sort_keys=True).encode()).hexdigest()
    pkt={'window':window,'coverage':coverage,'articles':entries,'packet_sha256':version,'generated_at':now().isoformat()}
    target=w.ROOT/'data/packets'/window['date']/(version+'.json')
    if not target.exists():w.json_write(target,pkt)
    return pkt,target


def validate_editorial(ed,pkt):
    if ed.get('date')!=pkt['window']['date'] or ed.get('packet_sha256')!=pkt['packet_sha256']:raise ValueError('Editorial date/packet does not match current evidence; regenerate the packet and review')
    if not isinstance(ed.get('overview'),str) or not ed['overview'].strip():raise ValueError('Chinese overview required')
    available={a['id']:a for a in pkt['articles']}
    keys=set()
    if not isinstance(ed.get('items'),list) or len(ed['items'])>settings()['max_items']:raise ValueError('Invalid item list or too many events')
    for item in ed['items']:
        for field in ('event_key','title','analysis'):
            if not isinstance(item.get(field),str) or not item[field].strip():raise ValueError('Each event requires '+field)
        if item['event_key'] in keys:raise ValueError('Duplicate event_key')
        keys.add(item['event_key'])
        if item.get('section') not in range(len(settings()['sections'])):raise ValueError('Invalid section')
        if not item.get('article_ids') or any(x not in available for x in item['article_ids']):raise ValueError('Evidence ID missing or outside the daily window')
        if any(not available[x].get('text', '').strip() for x in item['article_ids']):raise ValueError('Source text is missing; fetch and read the original before including this event')
        if not isinstance(item.get('facts'),list) or not item['facts'] or any(not isinstance(x,str) or not x.strip() for x in item['facts']):raise ValueError('Fact bullets required')
        if item.get('reviewed') is not True:raise ValueError('Agent must mark the event reviewed after reading evidence')
        if not isinstance(item.get('locators'),dict) or any(not item['locators'].get(x) for x in item['article_ids']):raise ValueError('Each supporting article needs a locator')
    # Source checks include search-only company/startup discovery and all web pages.
    if not isinstance(ed.get('source_checks'),list):raise ValueError('source_checks required')
    for check in ed['source_checks']:
        if check.get('status') not in ('checked','failed','not-checked') or not check.get('source_id') or not check.get('note'):raise ValueError('Invalid source coverage check')
    return available


def report(editorial=None,report_date=None):
    pkt,packet_path=packet(report_date)
    date_value=pkt['window']['date']
    folder=w.ROOT/'reports/daily'/date_value
    if editorial:
        ed=json.loads(Path(editorial).read_text())
        available=validate_editorial(ed,pkt)
    else:
        if pkt['articles']:raise ValueError('Candidate evidence exists: Agent editorial review required before report')
        ed={'date':date_value,'packet_sha256':pkt['packet_sha256'],'overview':'当前窗口没有已归档且日期合格的候选；不代表行业没有新闻。','items':[],'source_checks':[]}
        available={}
    content_digest=hashlib.sha256(json.dumps(ed,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    manifest_path=folder/'manifest.json'
    if manifest_path.exists():
        old=json.loads(manifest_path.read_text())
        if old.get('editorial_sha256')==content_digest:
            return dict(old,unchanged=True)
        history=folder/'revisions'/old['editorial_sha256']
        for name in ('report.md','editorial.json','manifest.json'):
            if (folder/name).exists():w.atomic_write(history/name,(folder/name).read_bytes())
    window=pkt['window']
    lines=[f'# AI 产业分析日报（{date_value.replace("-", ".")}）','',f'统计窗口：{window["start"]} 至 {window["end"]}（北京时间，右端不含）。','',ed['overview'],'']
    for section,title in enumerate(settings()['sections']):
        lines += [f'## {section+1}. {title}','']
        selected=[i for i in ed['items'] if i['section']==section]
        if not selected:lines+=['本期未收录经核验的新事件；覆盖情况见文末。','']
        for item in selected:
            lines += ['### '+item['title'],'']
            lines += ['- '+fact for fact in item['facts']]
            lines += ['','**产业判断：** '+item['analysis'],'','**来源与核验范围：**']
            for aid in item['article_ids']:
                a=available[aid]
                label={'updated':'更新时间','announced':'源站公告时间'}.get(a['date_basis'],'发布时间')
                lines += [f'- [{a["source_name"]} · {a["title"]}]({a["url"]})；{label}：{effective_date(a)}；定位：{item["locators"][aid]}；阅读范围：{a["extraction"]}；ID：`{aid}`。']
                if a.get('date_boundary_uncertain'):lines+=['  日期仅精确到天，无法确认 08:00 边界。']
            lines+=['']
    lines+=['## 覆盖与证据说明','','- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。',f'- 候选 {len(pkt["articles"])} 条，精选 {len(ed["items"])} 个事件；未注明日期 {pkt["coverage"]["excluded"]["undated"]} 条不进入日报。','- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。','']
    checks={x['source_id']:x for x in ed['source_checks']}
    for src in sources():
        health=next((x for x in pkt['coverage']['source_health'] if x['source_id']==src['id']),None)
        check=checks.get(src['id'])
        status=check['status'] if check else health.get('status','not-checked') if health else 'not-checked'
        note=check['note'] if check else (health.get('error') or health.get('reason') or '自动来源扫描；正文按选题核对') if health else '本次未检查'
        trunc=health.get('truncated',0) if health else 0
        lines+=[f'- {src["name"]}：{status}；{note}；已知截断 {trunc} 条。']
    discovery=checks.get('startup-discovery',{'status':'not-checked','note':'本次未完成新公司开放检索'})
    lines += [f'- 新公司发现：{discovery["status"]}；{discovery["note"]}。','',f'证据包：`{w.relative(packet_path)}`；采集 run：`{pkt["coverage"]["run_id"]}`。','']
    manifest={'date':date_value,'status':'analyzed' if ed['items'] else 'empty','packet_sha256':pkt['packet_sha256'],'editorial_sha256':content_digest,'report_path':w.relative(folder/'report.md'),'packet_path':w.relative(packet_path),'events':len(ed['items']),'generated_at':now().isoformat(),'timezone':window['timezone']}
    with w.write_lock():
        w.transaction({w.relative(folder/'report.md'):'\n'.join(lines),w.relative(folder/'editorial.json'):json.dumps(ed,ensure_ascii=False,indent=2)+'\n',w.relative(manifest_path):json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'})
    return manifest


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='action',required=True)
    sub.add_parser('validate')
    sub.add_parser('status')
    c=sub.add_parser('collect');c.add_argument('--days',type=int,default=14);c.add_argument('--limit',type=int,default=60);c.add_argument('--source',action='append')
    for name in ('packet','report'):
        sp=sub.add_parser(name);sp.add_argument('--date')
        if name=='report':sp.add_argument('--editorial')
    i=sub.add_parser('import');i.add_argument('file');i.add_argument('--source',required=True)
    f=sub.add_parser('fetch');f.add_argument('url');f.add_argument('--source',required=True)
    a=p.parse_args()
    try:
        if a.action=='validate':result=validate_config()
        elif a.action=='collect':result=collect(a.days,a.limit,a.source)
        elif a.action=='status':result={'health':latest_health(),'articles':len(load_articles()),'due_window':due_window()}
        elif a.action=='packet':
            pkt,path=packet(a.date)
            result={'path':str(path),'window':pkt['window'],'articles':len(pkt['articles']),'packet_sha256':pkt['packet_sha256']}
        elif a.action=='report':result=report(a.editorial,a.date)
        elif a.action=='fetch':
            src=next(s for s in sources() if s['id']==a.source)
            text,raw=fetch(a.url,src['id'])
            result=dict(raw,text=html_text(text))
            path=w.ROOT/'data/extracted'/(raw['sha256']+'.json');w.json_write(path,result)
            result={'path':str(path),'raw_path':raw['raw_path'],'characters':len(result['text'])}
        else:
            src=next(s for s in sources() if s['id']==a.source)
            article=json.loads(Path(a.file).read_text())
            for key in ('published_at','updated_at','announced_at'):
                if article.get(key):
                    parsed=parse_date(article[key])
                    if not parsed:raise ValueError('Invalid '+key)
                    if len(article[key])==10:article['date_precision']='date-only'
                    article[key]=parsed
            if article.get('date_basis') not in ('published','updated','announced','unknown'):raise ValueError('Explicit date_basis required')
            if article['date_basis']=='published' and not article.get('published_at'):raise ValueError('published_at required')
            if article['date_basis']=='updated' and not article.get('updated_at'):raise ValueError('updated_at required')
            if article['date_basis']=='announced' and not article.get('announced_at'):raise ValueError('announced_at required')
            if article.get('raw_path'):
                rawpath=w.local_path(article['raw_path'])
                if not w.relative(rawpath).startswith('raw/'):raise ValueError('Evidence must be an archived raw file')
                raw={'raw_path':w.relative(rawpath),'sha256':hashlib.sha256(rawpath.read_bytes()).hexdigest(),'fetched_at':now().isoformat()}
            else:
                # Browser-extracted source text is archived as such, never called raw HTTP.
                article['retrieval_method']='agent-source-extract'
                raw=w.archive(article['text'].encode(), 'source-extract.txt',article['url'])
            aid,changed=save_article(article,src,raw)
            result={'id':aid,'changed':changed,'raw_path':raw['raw_path']}
        print(json.dumps(w.plain(result),ensure_ascii=False,indent=2))
        return 0
    except (ValueError,KeyError,OSError,StopIteration,ET.ParseError) as error:
        print(json.dumps({'status':'error','error':str(error)},ensure_ascii=False))
        return 1

if __name__=='__main__':raise SystemExit(main())
