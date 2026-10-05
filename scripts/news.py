"""Auditable collection → packet → reviewed editorial → daily/weekly Markdown.
The agent supplies analysis. Collection never fabricates an editorial report.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import difflib
from email.utils import parsedate_to_datetime
import fcntl
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
from urllib.parse import urljoin, urlsplit, urlunsplit, parse_qsl, urlencode
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import uuid
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
import wiki_core as w

# Report coverage is grouped in this order. Aggregator results are discovery leads only.
GROUPS = {'official':'公司与产品一手来源','infra':'AI Infra 社区与工程','research':'论文、评测与研究机构',
          'government':'政府、监管与司法','media':'媒体直连 feed','aggregator':'聚合发现（仅作线索）'}
KINDS = ('feed','web','sitemap','hf-models')
STATE = 'data/source-state.json'
USER_AGENT = 'AI-Knowledge/1.0 (public source research)'


def now():
    return datetime.now(timezone.utc)


def settings():
    return w.config('data/report-settings.yaml')


def sources():
    return w.config('data/sources.yaml')['sources']


def discovery_searches():
    path=w.ROOT/'data/watchlist.yaml'
    if not path.exists():return []
    return ((w.config('data/watchlist.yaml') or {}).get('discovery') or {}).get('searches') or []


def load_state():
    path=w.ROOT/STATE
    return json.loads(path.read_text()) if path.exists() else {}


@contextmanager
def collect_lock():
    (w.ROOT/'.cache').mkdir(exist_ok=True)
    with (w.ROOT/'.cache/collect.lock').open('a') as handle:
        fcntl.flock(handle,fcntl.LOCK_EX)
        try:yield
        finally:fcntl.flock(handle,fcntl.LOCK_UN)


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
    value=' '.join(value.split())
    # Some Chinese feeds use "YYYY-MM-DD HH:MM:SS +0800" instead of RFC 822.
    m=re.fullmatch(r'(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?) ?([+-]\d{2}):?(\d{2})',value)
    if m:value=f'{m.group(1)}T{m.group(2)}{m.group(3)}:{m.group(4)}'
    try:
        dt = datetime.fromisoformat(value.replace('Z','+00:00'))
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


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.href=None
        self.label=[]
        self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style','noscript','svg'):self.skip+=1
        if tag=='a':
            self.href=dict(attrs).get('href') or ''
            self.label=[]
    def handle_data(self,data):
        if self.href is not None and not self.skip:self.label.append(data)
    def handle_endtag(self,tag):
        if tag in ('script','style','noscript','svg') and self.skip:self.skip-=1
        if tag=='a' and self.href is not None:
            self.links.append((self.href,' '.join(''.join(self.label).split())))
            self.href=None


def page_links(text,base,pattern):
    parser=LinkExtractor()
    parser.feed(text)
    found={}
    for href,label in parser.links:
        if not href.strip() or href.startswith(('#','mailto:','javascript:','tel:')):continue
        try:url=canonical(urljoin(base,unescape(href.strip())))
        except ValueError:continue
        if re.search(pattern,url) and (url not in found or (label and not found[url])):found[url]=label[:200]
    return [{'url':url,'title':label} for url,label in found.items()]


def sitemap_links(text,pattern):
    root=ET.fromstring(text)
    if root.tag.endswith('sitemapindex'):raise ValueError('Sitemap index is not supported; configure a child sitemap URL')
    found=[]
    for node in root:
        loc=next((c.text for c in node if c.tag.endswith('loc') and c.text),None)
        if not loc:continue
        url=canonical(loc.strip())
        if re.search(pattern,url):
            found.append({'url':url,'title':'','hint':next((c.text.strip() for c in node if c.tag.endswith('lastmod') and c.text),'')})
    return sorted(found,key=lambda x:x['hint'],reverse=True)


def hf_links(text,pattern):
    # createdAt is repository creation time; a repo can be private long before release.
    rows=[m for m in json.loads(text) if isinstance(m,dict) and m.get('id')]
    return [{'url':'https://huggingface.co/'+m['id'],'title':m['id'],'hint':m.get('createdAt','')} for m in rows if re.search(pattern,'https://huggingface.co/'+m['id'])]


def listing(src,text,base):
    pattern=src.get('link_pattern','.')
    if src['kind']=='sitemap':return sitemap_links(text,pattern)
    if src['kind']=='hf-models':return hf_links(text,pattern)
    return page_links(text,base,pattern)


def keyword_filter(words):
    if not words:return None
    # ASCII keywords need word boundaries ("AI" must not match "said"); CJK cannot use them.
    parts=[r'(?<![A-Za-z0-9])'+re.escape(x)+r'(?![A-Za-z0-9])' if x.isascii() else re.escape(x) for x in words]
    return re.compile('|'.join(parts),re.I)


def decode(body,headers=None):
    ctype=next((v for k,v in (headers or {}).items() if k.lower()=='content-type'),'')
    m=re.search(r'charset=["\']?([\w-]+)',ctype,re.I)
    name=m.group(1) if m else None
    if not name:
        m=re.search(rb'^\s*<\?xml[^>]+encoding=["\']([\w-]+)',body[:300]) or re.search(rb'<meta[^>]+charset=["\']?([\w-]+)',body[:4096],re.I)
        name=m.group(1).decode('ascii') if m else 'utf-8'
    name=name.lower()
    if name in ('gb2312','gbk','x-gbk','gb_2312-80'):name='gb18030'
    try:return body.decode(name,errors='replace'),name
    except LookupError:return body.decode('utf-8',errors='replace'),'utf-8'


def fetch(url,source_id,timeout=None):
    url=canonical(url)
    maximum=settings()['max_response_bytes']
    req=Request(url,headers={'User-Agent':USER_AGENT,'Accept-Encoding':'gzip','Accept':'application/atom+xml, application/rss+xml, text/html, */*'})
    status=200
    headers={}
    fetched=now().isoformat()
    try:
        with urlopen(req,timeout=timeout or settings()['timeout_seconds']) as response:
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
    try:
        if status>=400:
            raise ValueError(f'HTTP {status}; raw={record["raw_path"]}')
        if clipped:
            raise ValueError(f'Response exceeds {maximum} bytes; truncated raw preserved')
        if body.startswith(b'\x1f\x8b'):
            with gzip.GzipFile(fileobj=io.BytesIO(body)) as z:
                decoded=z.read(maximum+1)
            if len(decoded)>maximum:raise ValueError('Decompressed response exceeds size limit')
            body=decoded
        text,record['charset']=decode(body,headers)
        return text,record
    finally:
        w.json_write(w.ROOT/'data/fetches'/(uuid.uuid4().hex+'.json'),record)


def robots_allows(url,cache):
    """RFC 9309 for scheduled polling: 4xx robots.txt allows, unreachable disallows."""
    p=urlsplit(url)
    key=p.scheme+'://'+p.netloc
    if key not in cache:
        rules=RobotFileParser()
        try:
            with urlopen(Request(key+'/robots.txt',headers={'User-Agent':USER_AGENT}),timeout=settings()['timeout_seconds']) as response:
                rules.parse(response.read(512000).decode('utf-8',errors='replace').splitlines())
        except HTTPError as error:
            if 400<=error.code<500:rules.parse([])
            else:rules.disallow_all=True
        except Exception:
            rules.disallow_all=True
        cache[key]=rules
    return cache[key].can_fetch(USER_AGENT,url)


def snapshot(previous):
    """Text of the last successful response for this source, re-read from its raw archive."""
    if not previous.get('raw_path'):return None
    try:body=w.local_path(previous['raw_path']).read_bytes()
    except (OSError,ValueError):return None
    if body.startswith(b'\x1f\x8b'):body=gzip.decompress(body)
    return decode(body,{'Content-Type':'charset='+previous.get('charset','utf-8')})[0]


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


SCAN_EXTRACTIONS = ('feed-content','abstract','metadata-only')


def save_article(article,src,raw,scan=False):
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
        # A later feed scan must not replace full evidence with a short summary, nor any
        # record the Agent imported (read notes, abstract pages with submission history).
        if old.get('extraction')=='full-text' and full['extraction']!='full-text':return aid,False
        if scan and (old.get('imported') or old.get('retrieval_method') or old.get('extraction') not in SCAN_EXTRACTIONS):return aid,False
        # Two feeds can carry the same URL (e.g. NVIDIA newsroom and blog); keep the richer text.
        if scan and old.get('source_id')!=src['id'] and len(full['text'])<=len(old.get('text','')):return aid,False
        if all(old.get(k)==full.get(k) for k in ('title','text','published_at','updated_at','announced_at','date_basis','extraction')):return aid,False
        w.json_write(w.ROOT/'data/article-history'/aid/(old['source_sha256']+'.json'),old)
    w.json_write(path,full)
    return aid,True


def save_lead(lead,src,raw,key=None):
    """A discovered link or page change: a candidate to open, never report evidence."""
    url=canonical(lead['url'])
    aid=hashlib.sha256((key or url).encode()).hexdigest()[:20]
    path=w.ROOT/'data/articles'/(aid+'.json')
    # Keep the first sighting; an Agent import of the same URL later replaces the lead.
    if path.exists():return aid,False
    full=dict(lead,id=aid,url=url,title=lead.get('title') or url,text='',extraction='metadata-only',lead=True,
              source_id=src['id'],source_name=src['name'],section=src['section'],raw_path=raw['raw_path'],
              source_sha256=raw['sha256'],fetched_at=raw['fetched_at'],date_basis='discovered',
              discovered_at=raw['fetched_at'],date_precision='timestamp')
    full.setdefault('published_at',None)
    w.json_write(path,full)
    return aid,True


def validate_config():
    ids=set()
    for src in sources():
        sid=src.get('id')
        if sid in ids:raise ValueError('Duplicate source ID')
        ids.add(sid)
        canonical(src['url'])
        if src['kind'] not in KINDS or src['section'] not in range(len(settings()['sections'])):raise ValueError('Invalid source configuration: '+str(sid))
        if src.get('group') not in GROUPS:raise ValueError('Source group must be one of '+', '.join(GROUPS)+': '+str(sid))
        if src.get('fetch','http') not in ('http','browser'):raise ValueError('fetch must be http or browser: '+str(sid))
        for key,low,high in (('poll_hours',1,168),('timeout',1,120),('limit',1,500),('listing_cap',1,1000)):
            if key in src and (not isinstance(src[key],int) or isinstance(src[key],bool) or not low<=src[key]<=high):raise ValueError(f'Invalid {key}: {sid}')
        if 'include' in src and (not isinstance(src['include'],list) or not src['include'] or not all(isinstance(x,str) and x.strip() for x in src['include'])):raise ValueError('include must be a non-empty keyword list: '+str(sid))
        if 'link_pattern' in src:
            try:re.compile(src['link_pattern'])
            except re.error as error:raise ValueError(f'Invalid link_pattern for {sid}: {error}')
        if src['kind']=='hf-models' and not src['url'].startswith('https://huggingface.co/api/models?'):raise ValueError('hf-models needs a Hugging Face models API URL: '+str(sid))
    ZoneInfo(settings()['timezone'])
    for key in ('daily_hour','weekly_hour'):
        if not isinstance(settings().get(key),int) or not 0<=settings()[key]<=23:raise ValueError('Invalid '+key)
    if not isinstance(settings().get('weekly_weekday'),int) or not 0<=settings()['weekly_weekday']<=6:raise ValueError('Invalid weekly_weekday')
    return {'status':'success','sources':len(ids),'timezone':settings()['timezone']}


def effective_date(article):
    field={'announced':'announced_at','updated':'updated_at','published':'published_at','discovered':'discovered_at'}.get(article.get('date_basis'))
    return article.get(field) if field else None


def article_id(url):
    try:return hashlib.sha256(canonical(url).encode()).hexdigest()[:20]
    except ValueError:return None


def collect_feed(src,text,raw,previous,started,days,limit,known,result):
    entries=feed_entries(text)
    dated=sorted(datetime.fromisoformat(d) for d in (effective_date(e) for e in entries) if d)
    result['entries']=len(entries)
    if dated:result['oldest_entry_at']=dated[0].isoformat()
    if src.get('listing_cap') and len(entries)>=src['listing_cap']:result['listing_cap_reached']=True
    # A sliding-window feed whose oldest item is newer than our last successful read has
    # dropped whatever was published in between; that window cannot be recovered later.
    if dated and src.get('gap_check',True):
        if previous.get('last_ok_at'):
            if dated[0]>datetime.fromisoformat(previous['last_ok_at']):
                result['gap']={'from':previous['last_ok_at'],'to':dated[0].isoformat(),'detected_at':raw['fetched_at']}
        else:result['coverage_from']=dated[0].isoformat()
    keywords=keyword_filter(src.get('include'))
    candidates=[]
    for entry in entries:
        if keywords and not keywords.search(entry['title']+'\n'+entry['text'][:4000]):
            result['filtered']=result.get('filtered',0)+1
            continue
        date_value=effective_date(entry)
        dt=datetime.fromisoformat(date_value) if date_value else None
        if not dt:result['unknown_date']+=1
        elif dt>started:result['future_date']+=1
        elif dt<started-timedelta(days=days):continue
        candidates.append(entry)
    candidates.sort(key=lambda e:effective_date(e) or '',reverse=True)
    cap=max(limit,src.get('limit',0))
    # Only entries never archived count as truncated; earlier frequent runs may hold them.
    result['truncated']=sum(1 for e in candidates[cap:] if article_id(e['url']) not in known)
    result['candidates']=len(candidates)
    lead=src['group']=='aggregator'
    for entry in candidates[:cap]:
        try:
            if lead:entry=dict(entry,summary=entry['text'][:600],text='',lead=True)
            _,changed=save_article(entry,src,raw,scan=True)
            result['saved' if changed else 'unchanged']+=1
            if not lead:result['needs_fulltext']+=1
        except ValueError as error:
            result.setdefault('article_errors',[]).append(str(error))
    if result.get('article_errors'):result['status']='partial'
    # API/feeds may themselves cap listings. This is a source coverage limit.
    result['listing_is_complete']=False


def collect_listing(src,text,raw,previous,result):
    items=listing(src,text,raw['final_url'])
    result['links']=len(items)
    old=snapshot(previous)
    try:seen={x['url'] for x in listing(src,old,previous.get('final_url') or src['url'])} if old is not None else set()
    except (ValueError,ET.ParseError):seen=set()
    if not items:
        result.update(status='failed',error='没有匹配链接；页面结构、渲染或访问方式可能已变化')
        return
    if not seen:
        result.update(status='needs-review',baseline=True,top_links=items[:10],
                      reason='首次快照，尚无法区分新链接；需核查页面前列链接')
        return
    new=[x for x in items if x['url'] not in seen]
    result['new_links']=len(new)
    if len(new)>max(20,int(len(items)*0.8)):
        result.update(status='needs-review',top_links=items[:10],reason='大部分链接同时变化，疑似改版；未保存线索，需人工核查')
        return
    keywords=keyword_filter(src.get('include'))
    if keywords:
        kept=[x for x in new if keywords.search(x.get('title','')+' '+x['url'])]
        result['filtered']=len(new)-len(kept)
        new=kept
    for item in new:
        lead={'url':item['url'],'title':item.get('title') or item['url'],'link_text':item.get('title','')}
        if item.get('hint'):lead['listing_hint']=item['hint']
        _,changed=save_lead(lead,src,raw)
        result['leads']=result.get('leads',0)+changed


def collect_page(src,text,raw,previous,result):
    current=html_text(text)
    result['text_chars']=len(current)
    if len(current)<200:
        result.update(status='failed',error='可读正文不足 200 字；需浏览器渲染或检查访问限制')
        return
    old=snapshot(previous)
    if old is None:
        result.update(status='needs-review',baseline=True,landing_text=current[:1000],reason='首次快照；需阅读一次当前页面')
        return
    rows=[x for x in difflib.unified_diff(html_text(old).splitlines(),current.splitlines(),lineterm='',n=0) if x[:1] in '+-' and not x.startswith(('+++','---'))]
    result['changed']=bool(rows)
    if rows:
        result.update(diff_lines=len(rows),diff=rows[:40])
        digest=hashlib.sha256(current.encode()).hexdigest()
        _,changed=save_lead({'url':src['url'],'title':src['name']+'：页面内容变化','summary':'\n'.join(rows[:40])},src,raw,key='change:'+src['id']+':'+digest)
        result['leads']=int(changed)


def collect_source(src,previous,started,days,limit,known,robots):
    result={'source_id':src['id'],'name':src['name'],'group':src['group'],'status':'ok','saved':0,'unchanged':0,'unknown_date':0,'future_date':0,'truncated':0,'needs_fulltext':0}
    state=dict(previous,last_attempt_at=started.isoformat())
    if src.get('fetch','http')=='browser':
        # Not fetched: JS-only or blocked for our crawler. The Agent checks it in a browser.
        result.update(status='needs-browser',reason=src.get('note') or 'HTTP 采集不可用；需用浏览器核查')
        state['last_status']=result['status']
        return result,state
    try:
        url=canonical(src['url'])
        if not robots_allows(url,robots):
            result.update(status='failed',error='robots.txt 不允许本采集器抓取，或无法读取 robots.txt')
            state['last_status']=result['status']
            return result,state
        text,raw=fetch(url,src['id'],src.get('timeout'))
        result['raw_path']=raw['raw_path']
        if src['kind']=='feed':collect_feed(src,text,raw,previous,started,days,limit,known,result)
        elif src['kind']=='web' and not src.get('link_pattern'):collect_page(src,text,raw,previous,result)
        else:collect_listing(src,text,raw,previous,result)
        if result['status']!='failed':
            state.update(last_ok_at=raw['fetched_at'],raw_path=raw['raw_path'],charset=raw.get('charset','utf-8'),final_url=raw['final_url'])
            for key in ('entries','oldest_entry_at','links','text_chars'):
                if key in result:state[key]=result[key]
            if result.get('gap'):state['gaps']=(previous.get('gaps',[])+[result['gap']])[-30:]
    except Exception as error:
        result.update(status='failed',error=str(error))
    state['last_status']=result['status']
    return result,state


def is_due(src,previous,at):
    last=previous.get('last_attempt_at')
    return not last or at-datetime.fromisoformat(last)>=timedelta(hours=src.get('poll_hours',24))*0.9


def collect(days=14,limit=60,selected=None,due=False):
    if not 1<=days<=90 or not 1<=limit<=500:raise ValueError('days 1–90, limit 1–500')
    validate_config()
    enabled=[s for s in sources() if s.get('enabled',True) and (not selected or s['id'] in selected)]
    if selected and set(selected)-{s['id'] for s in enabled}:raise ValueError('Unknown --source')
    with collect_lock():
        state=load_state()
        started=now()
        if due:
            enabled=[s for s in enabled if is_due(s,state.get(s['id'],{}),started)]
            # Frequent scheduled checks with nothing due leave no empty run records.
            if not enabled:return {'id':None,'started_at':started.isoformat(),'finished_at':started.isoformat(),'sources':[],'due_only':True}
        known={p.stem for p in (w.ROOT/'data/articles').glob('*.json')}
        robots={}
        # One worker per host: requests to the same site run one after another.
        hosts=defaultdict(list)
        for src in enabled:hosts[urlsplit(src['url']).hostname].append(src)
        def run_host(group):
            return [(src,)+collect_source(src,state.get(src['id'],{}),started,days,limit,known,robots) for src in group]
        with ThreadPoolExecutor(max_workers=6) as executor:
            outputs=[row for rows in executor.map(run_host,hosts.values()) for row in rows]
        order={s['id']:i for i,s in enumerate(enabled)}
        outputs.sort(key=lambda row:order[row[0]['id']])
        for src,_,new_state in outputs:state[src['id']]=new_state
        w.json_write(w.ROOT/STATE,state)
        rid=started.strftime('%Y%m%dT%H%M%S')+'-'+uuid.uuid4().hex[:8]
        run={'id':rid,'started_at':started.isoformat(),'finished_at':now().isoformat(),'sources':[r for _,r,_ in outputs],'selected_sources':selected or [],'due_only':due,'lookback_days':days,'per_source_limit':limit}
        w.json_write(w.ROOT/'data/runs'/(rid+'.json'),run)
    return run


def due_sources(at=None):
    state=load_state();at=at or now()
    return [s['id'] for s in sources() if s.get('enabled',True) and is_due(s,state.get(s['id'],{}),at)]


def window_gaps(start,end):
    rows=[]
    for sid,entry in sorted(load_state().items()):
        for gap in entry.get('gaps',[]):
            if datetime.fromisoformat(gap['to'])>start and datetime.fromisoformat(gap['from'])<end:rows.append(dict(gap,source_id=sid))
    return rows


def due_window(report_date=None,period='daily'):
    if period not in ('daily','weekly'):raise ValueError('Invalid report period')
    cfg=settings()
    local=now().astimezone(ZoneInfo(cfg['timezone']))
    span=7 if period=='weekly' else 1
    hour=cfg[period+'_hour']
    if report_date:
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',report_date):raise ValueError('Report date must be YYYY-MM-DD')
        end=datetime.fromisoformat(report_date).replace(hour=hour,tzinfo=ZoneInfo(cfg['timezone']))
        if period=='weekly' and end.weekday()!=cfg['weekly_weekday']:raise ValueError('Weekly report date must be the configured weekday (Saturday)')
        if end>local:raise ValueError('Cannot report a window that has not closed')
    else:
        end=local.replace(hour=hour,minute=0,second=0,microsecond=0)
        if period=='weekly':end-=timedelta(days=(end.weekday()-cfg['weekly_weekday'])%7)
        if end>local:end-=timedelta(days=span)
    return {'period':period,'date':end.date().isoformat(),'timezone':cfg['timezone'],'start':(end-timedelta(days=span)).isoformat(),'end':end.isoformat()}


def report_folder(period,date_value):
    if period not in ('daily','weekly') or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',date_value):raise ValueError('Invalid report location')
    datetime.fromisoformat(date_value)
    return w.ROOT/'reports'/period/date_value[:4]/date_value[5:7]/date_value


def report_indices():
    """Called under the workspace write lock after report publication/migration."""
    root=w.ROOT/'reports'
    overview=['# AI 产业报告索引','','报告日期按各自统计窗口的时区计算，并按窗口结束日所属年份、月份归档；历史窗口见各期报告。','']
    for period,label in (('daily','日报'),('weekly','周报')):
        lines=['# '+label+'索引','']
        manifests=[]
        for path in sorted((root/period).glob('*/*/*/manifest.json'),reverse=True):
            manifest=json.loads(path.read_text())
            manifests.append((path,manifest))
        bucket=None
        for path,manifest in manifests:
            date_value=manifest['date']
            if bucket!=date_value[:7]:
                bucket=date_value[:7];lines+=['## '+bucket,'']
            relative_path=(path.parent/'report.md').relative_to(root/period).as_posix()
            lines+=[f'- [{date_value}]({relative_path}) · {manifest["events"]} 个事件 · {manifest["status"]}']
        if not manifests:lines+=['尚无已生成报告。','']
        w.atomic_write(root/period/'index.md','\n'.join(lines).rstrip()+'\n')
        overview+=[f'- [{label}]({period}/index.md) · {len(manifests)} 份']
    w.atomic_write(root/'index.md','\n'.join(overview)+'\n')


def migrate_reports():
    """Move legacy flat report folders without rewriting report text/evidence."""
    plans=[]
    with w.write_lock():
        for period in ('daily','weekly'):
            for folder in sorted((w.ROOT/'reports'/period).glob('????-??-??')):
                if not folder.is_dir():continue
                target=report_folder(period,folder.name)
                if target.exists():raise ValueError('Migration target already exists: '+w.relative(target))
                updates=[]
                for path in folder.rglob('manifest.json'):
                    manifest=json.loads(path.read_text())
                    old=w.relative(folder)+'/'
                    value=manifest.get('report_path','')
                    if value.startswith(old):manifest['report_path']=w.relative(target)+'/'+value[len(old):]
                    manifest.setdefault('period',period)
                    updates.append((path.relative_to(folder),manifest))
                plans.append((folder,target,updates))
        for folder,target,updates in plans:
            target.parent.mkdir(parents=True,exist_ok=True)
            folder.rename(target)
            for relative_path,manifest in updates:w.json_write(target/relative_path,manifest)
        local=now().astimezone(ZoneInfo(settings()['timezone']))
        for period in ('daily','weekly'):
            month=w.ROOT/'reports'/period/local.strftime('%Y')/local.strftime('%m')
            month.mkdir(parents=True,exist_ok=True)
            if not any(month.iterdir()):w.atomic_write(month/'.gitkeep','')
        report_indices()
    return {'moved':[w.relative(target) for _,target,_ in plans],'index':'reports/index.md'}


def load_articles():
    return [json.loads(p.read_text()) for p in sorted((w.ROOT/'data/articles').glob('*.json'))]


def health_note(health):
    if health.get('error'):return health['error']
    parts=[health['reason']] if health.get('reason') else []
    if 'entries' in health:parts.append(f'feed {health["entries"]} 条'+(f'，关键词过滤 {health["filtered"]} 条' if health.get('filtered') else ''))
    if 'links' in health:parts.append(f'页面链接 {health["links"]} 个'+(f'，最近一次新增 {health["new_links"]} 个' if health.get('new_links') else ''))
    if 'changed' in health:parts.append('最近一次检测到页面变化' if health['changed'] else '页面无变化')
    if health.get('coverage_from'):parts.append('首次采集，覆盖起点 '+health['coverage_from'][:16])
    if health.get('checked_at'):parts.append('检查于 '+datetime.fromisoformat(health['checked_at']).astimezone(ZoneInfo(settings()['timezone'])).strftime('%m-%d %H:%M'))
    return '；'.join(parts) or '自动来源扫描；正文按选题核对'


def latest_health():
    runs=sorted((w.ROOT/'data/runs').glob('*.json'))
    if not runs:return {'id':None,'sources':[]}
    latest=json.loads(runs[-1].read_text())
    merged={}
    wanted={s['id'] for s in sources() if s.get('enabled',True)}
    for path in reversed(runs):
        run=json.loads(path.read_text())
        for source in run['sources']:
            merged.setdefault(source['source_id'],dict(source,checked_at=run['finished_at']))
        # Frequent partial (--due) runs accumulate; stop once every configured source is seen.
        if wanted<=set(merged):break
    latest['sources']=list(merged.values())
    return latest


def packet(report_date=None,period='daily'):
    window=due_window(report_date,period)
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
        # A discovered link was published at most once between two snapshots; hour unknown.
        item['date_boundary_uncertain']=precision=='date-only' or article.get('date_basis')=='discovered'
        entries.append(item)
    run=latest_health()
    gaps=window_gaps(start,end)
    coverage={'excluded':excluded,'source_health':run['sources'],'run_id':run['id'],'gaps':gaps,'leads':sum(1 for a in entries if a.get('lead')),
              'feed_limit_note':'Feeds/API may only expose recent entries; no claim of exhaustive coverage. Leads are discovery-only, not evidence.'}
    # Optional keys are added only when present so hashes of older evidence stay stable.
    evidence_key={'window':window,'articles':[dict({k:a.get(k) for k in ('id','source_sha256','published_at','updated_at','announced_at','date_basis','date_precision')},**({'discovered_at':a['discovered_at']} if a.get('discovered_at') else {})) for a in entries],
                  'health':[{k:h.get(k) for k in ('source_id','status','truncated','unknown_date','error')} for h in run['sources']]}
    if gaps:evidence_key['gaps']=gaps
    version=hashlib.sha256(json.dumps(evidence_key,sort_keys=True).encode()).hexdigest()
    pkt={'window':window,'coverage':coverage,'articles':entries,'packet_sha256':version,'generated_at':now().isoformat()}
    date_value=window['date']
    target=w.ROOT/'data/packets'/period/date_value[:4]/date_value[5:7]/date_value/(version+'.json')
    if not target.exists():w.json_write(target,pkt)
    return pkt,target


def validate_editorial(ed,pkt):
    if ed.get('period','daily')!=pkt['window']['period']:raise ValueError('Editorial period does not match evidence')
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
    if pkt['window']['period']=='weekly' and ed['items']:
        if not isinstance(ed.get('outlook'),list) or not ed['outlook'] or any(not isinstance(x,str) or not x.strip() for x in ed['outlook']):raise ValueError('Weekly report requires outlook observations')
    return available


def report(editorial=None,report_date=None,period='daily'):
    pkt,packet_path=packet(report_date,period)
    date_value=pkt['window']['date']
    folder=report_folder(period,date_value)
    if editorial:
        ed=json.loads(Path(editorial).read_text())
        available=validate_editorial(ed,pkt)
    else:
        if pkt['articles']:raise ValueError('Candidate evidence exists: Agent editorial review required before report')
        ed={'period':period,'date':date_value,'packet_sha256':pkt['packet_sha256'],'overview':'当前窗口没有已归档且日期合格的候选；不代表行业没有新闻。','items':[],'source_checks':[]}
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
    label='周报' if period=='weekly' else '日报'
    zone_label={'Asia/Singapore':'新加坡时间','Asia/Shanghai':'北京时间'}.get(window['timezone'],window['timezone'])
    cutoff=datetime.fromisoformat(window['end']).strftime('%H:%M')
    lines=[f'# AI 产业分析{label}（{date_value.replace("-", ".")}）','',f'统计窗口：{window["start"]} 至 {window["end"]}（{zone_label}，右端不含）。','',ed['overview'],'']
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
                if a.get('date_boundary_uncertain'):lines+=[f'  日期仅精确到天，无法确认 {cutoff} 边界。']
            lines+=['']
    if period=='weekly':
        lines+=['## 下周观察','']+['- '+x for x in ed.get('outlook',[])]+['']
        if not ed.get('outlook'):lines+=['本期证据不足，暂不形成观察判断。','']
    coverage=pkt['coverage']
    lines+=['## 覆盖与证据说明','','- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。',
            f'- 候选 {len(pkt["articles"])} 条（其中线索 {coverage.get("leads",0)} 条），精选 {len(ed["items"])} 个事件；未注明日期 {coverage["excluded"]["undated"]} 条不进入本期报告。',
            '- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。','']
    checks={x['source_id']:x for x in ed['source_checks']}
    for group,label in GROUPS.items():
        members=[s for s in sources() if s.get('group')==group]
        if not members:continue
        lines+=['### '+label,'']
        for src in members:
            if not src.get('enabled',True):
                lines+=[f'- {src["name"]}：disabled；{src.get("note") or "已停用"}。']
                continue
            health=next((x for x in coverage['source_health'] if x['source_id']==src['id']),None)
            check=checks.get(src['id'])
            status=check['status'] if check else health.get('status','not-checked') if health else 'not-checked'
            note=check['note'] if check else health_note(health) if health else '本次未检查'
            trunc=health.get('truncated',0) if health else 0
            gaps=''.join(f'；可能漏采 {g["from"][:16]} 至 {g["to"][:16]}' for g in coverage.get('gaps',[]) if g['source_id']==src['id'])
            capped='；列表达到条数上限，可能不完整' if health and health.get('listing_cap_reached') else ''
            lines+=[f'- {src["name"]}：{status}；{note}；已知截断 {trunc} 条{gaps}{capped}。']
        lines+=['']
    searches=discovery_searches()
    if searches:
        # Agent-run searches (robots.txt keeps them out of collect) still need a recorded result.
        lines+=['### Agent 检索清单','']
        for item in searches:
            check=checks.get(item['id'],{'status':'not-checked','note':'本次未执行'})
            lines+=[f'- {item["id"]}：{check["status"]}；{check["note"]}。']
        lines+=['']
    discovery=checks.get('startup-discovery',{'status':'not-checked','note':'本次未完成新公司开放检索'})
    lines += [f'- 新公司发现：{discovery["status"]}；{discovery["note"]}。','',f'证据包：`{w.relative(packet_path)}`；采集 run：`{pkt["coverage"]["run_id"]}`。','']
    manifest={'period':period,'date':date_value,'window':window,'status':'analyzed' if ed['items'] else 'empty','packet_sha256':pkt['packet_sha256'],'editorial_sha256':content_digest,'report_path':w.relative(folder/'report.md'),'packet_path':w.relative(packet_path),'events':len(ed['items']),'generated_at':now().isoformat(),'timezone':window['timezone']}
    with w.write_lock():
        w.transaction({w.relative(folder/'report.md'):'\n'.join(lines),w.relative(folder/'editorial.json'):json.dumps(ed,ensure_ascii=False,indent=2)+'\n',w.relative(manifest_path):json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'})
        report_indices()
    return manifest


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='action',required=True)
    sub.add_parser('validate')
    sub.add_parser('status')
    sub.add_parser('migrate-reports')
    c=sub.add_parser('collect');c.add_argument('--days',type=int,default=14);c.add_argument('--limit',type=int,default=60);c.add_argument('--source',action='append')
    c.add_argument('--due',action='store_true',help='only sources whose poll_hours interval has elapsed')
    c.add_argument('--summary',action='store_true',help='print run id, status counts, failures and gaps only')
    for name in ('packet','report'):
        sp=sub.add_parser(name);sp.add_argument('--date');sp.add_argument('--period',choices=('daily','weekly'),default='daily')
        if name=='report':sp.add_argument('--editorial')
        else:sp.add_argument('--brief',action='store_true',help='also list candidate ids, dates and titles');sp.add_argument('--group',choices=tuple(GROUPS))
    i=sub.add_parser('import');i.add_argument('file');i.add_argument('--source',required=True)
    f=sub.add_parser('fetch');f.add_argument('url');f.add_argument('--source',required=True)
    a=p.parse_args()
    try:
        if a.action=='validate':result=validate_config()
        elif a.action=='collect':
            result=collect(a.days,a.limit,a.source,a.due)
            if a.summary:
                rows=result['sources']
                result={'id':result['id'],'finished_at':result['finished_at'],'sources':len(rows),
                        'status':{k:sum(1 for r in rows if r['status']==k) for k in sorted({r['status'] for r in rows})},
                        'failed':{r['source_id']:r.get('error','') for r in rows if r['status']=='failed'},
                        'saved':sum(r.get('saved',0) for r in rows),'leads':sum(r.get('leads',0) for r in rows),
                        'gaps':[dict(r['gap'],source_id=r['source_id']) for r in rows if r.get('gap')]}
        elif a.action=='status':
            at=now()
            result={'health':latest_health(),'articles':len(load_articles()),'due_window':due_window(),'weekly_due_window':due_window(period='weekly'),
                    'due_sources':due_sources(at),'recent_gaps':window_gaps(at-timedelta(days=2),at)}
        elif a.action=='migrate-reports':result=migrate_reports()
        elif a.action=='packet':
            pkt,path=packet(a.date,a.period)
            result={'path':str(path),'window':pkt['window'],'articles':len(pkt['articles']),'leads':pkt['coverage']['leads'],'gaps':pkt['coverage']['gaps'],'packet_sha256':pkt['packet_sha256']}
            if a.brief:
                group={s['id']:s.get('group') for s in sources()}
                rows=[x for x in pkt['articles'] if not a.group or group.get(x['source_id'])==a.group]
                result['candidates']=[[x['id'],(effective_date(x) or '')[:16],x['source_id'],'lead' if x.get('lead') else x['extraction'],x['title'][:120]] for x in sorted(rows,key=lambda x:(group.get(x['source_id']) or '',x['source_id'],effective_date(x) or ''))]
        elif a.action=='report':result=report(a.editorial,a.date,a.period)
        elif a.action=='fetch':
            src=next(s for s in sources() if s['id']==a.source)
            text,raw=fetch(a.url,src['id'],src.get('timeout'))
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
            article['imported']=True
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
