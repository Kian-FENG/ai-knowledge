"""Compatible command surfaces for the local wiki."""
import argparse
import json
import re
import sys
from pathlib import Path
import wiki_core as w


def output(value, as_json=False):
    if as_json:
        print(json.dumps(w.plain(value), ensure_ascii=False, indent=2))
    elif isinstance(value, str):
        print(value)
    else:
        print(json.dumps(w.plain(value), ensure_ascii=False, indent=2))


def main(command=None):
    command = command or Path(sys.argv[0]).stem
    p = argparse.ArgumentParser(prog=command)
    if command == 'query':
        p.add_argument('query')
        for flag in ('domain','type','tag','confidence'):
            p.add_argument('--'+flag, action='append', default=[])
        p.add_argument('-n', type=int, default=5)
        p.add_argument('--tfidf', '--semantic', action='store_true', dest='tfidf')
        p.add_argument('--expand', action='store_true')
    elif command == 'get_page':
        p.add_argument('page')
        p.add_argument('--follow-sources', action='store_true')
        p.add_argument('--as-of')
    elif command == 'grep_wiki':
        p.add_argument('pattern')
        p.add_argument('--regex', action='store_true')
        p.add_argument('--ignore-case', '-i', action='store_true')
    elif command == 'ingest':
        sub = p.add_subparsers(dest='action', required=True)
        d = sub.add_parser('draft')
        d.add_argument('--type', required=True)
        d.add_argument('--slug', required=True)
        d.add_argument('--domain', action='append', required=True)
        d.add_argument('--title')
        d.add_argument('--to')
        r = sub.add_parser('review')
        r.add_argument('pages', nargs='+')
        r.add_argument('--reviewer', required=True)
        for name in ('finalize','commit'):
            s = sub.add_parser(name)
            s.add_argument('pages', nargs='+' if name=='finalize' else '*')
        t = sub.add_parser('touch')
        t.add_argument('page')
        t.add_argument('--verification-note', required=True)
        t.add_argument('--verification', choices=['source-checked','replicated'], default='source-checked')
        t.add_argument('--as-of')
        a = sub.add_parser('archive')
        a.add_argument('file')
        a.add_argument('--source-url')
    elif command == 'validate':
        p.add_argument('--require-migrated', action='append', default=[])
    elif command in ('staleness_report','reliability_report','orphan_report','capability_report'):
        p.add_argument('--as-of')
    p.add_argument('--json', action='store_true')
    p.add_argument('--paths-only', action='store_true')
    p.add_argument('--include-unpublished', action='store_true')
    a = p.parse_args()
    try:
        if command == 'query':
            domains = w.config('tags/domains.yaml')['domains']
            types = w.config('data/schemas.yaml')['types']
            if any(x not in domains for x in a.domain) or any(x not in types for x in a.type):
                raise ValueError('Unknown domain/type filter')
            result = w.search(a.query, {'domain':a.domain,'type':a.type,'tags':a.tag,'confidence':a.confidence}, a.n, a.include_unpublished, a.tfidf, a.expand)
        elif command == 'get_page':
            result = w.get_page(a.page, a.include_unpublished, a.follow_sources, a.as_of)
        elif command == 'grep_wiki':
            flags = re.I if a.ignore_case else 0
            rx = re.compile(a.pattern if a.regex else re.escape(a.pattern), flags)
            hits = []
            for path, pg in w.pages().items():
                if not a.include_unpublished and pg['metadata'].get('lifecycle') != 'published':
                    continue
                for n, line in enumerate(pg['body'].splitlines(), 1):
                    if rx.search(line):
                        hits.append({'path':path,'body_line':n,'text':line})
            result = {'status':'success' if hits else 'empty','results':hits}
        elif command == 'ingest':
            if a.action == 'draft':
                result = {'path':w.draft(a.type,a.slug,a.domain,a.title,a.to)}
            elif a.action == 'review':
                result = {'reviewed':w.review(a.pages,a.reviewer)}
            elif a.action in ('commit','finalize'):
                result = w.finalize(a.pages)
            elif a.action == 'touch':
                result = {'path':w.touch(a.page,a.verification_note,a.verification,a.as_of)}
            else:
                src = Path(a.file).expanduser()
                result = w.archive(src.read_bytes(),src.name,a.source_url)
        elif command == 'validate':
            for folder in a.require_migrated:
                if not w.local_path(folder).is_dir():
                    raise ValueError('Missing required directory '+folder)
            errors = w.validate()
            result = {'status':'invalid' if errors else 'success','errors':errors,'pages':len(w.pages())}
            output(result,a.json)
            return int(bool(errors))
        elif command == 'generate-indices':
            result = w.finalize([])
        else:
            corpus = w.pages()
            visible = {k:v for k,v in corpus.items() if a.include_unpublished or v['metadata'].get('lifecycle')=='published'}
            if command == 'orphan_report':
                result = {'unreachable':w.navigation(corpus),'unresolved':[{'path':k,**ref} for k,pg in visible.items() for ref in w.references(pg) if w.resolve(ref['target'],corpus)['status'] in ('unresolved','ambiguous')]}
            elif command == 'staleness_report':
                result = [{'path':k,**w.freshness(pg['metadata'],a.as_of)} for k,pg in visible.items()]
            elif command == 'reliability_report':
                result = [{'path':k,'evidence_kind':pg['metadata']['evidence_kind'],'verification':pg['metadata']['verification']} for k,pg in visible.items()]
            else:
                result = {'pages':len(corpus),'published':len(visible),'types':sorted(w.config('data/schemas.yaml')['types']),'domains':list(w.config('tags/domains.yaml')['domains']),'validation_errors':w.validate()}
        if a.paths_only:
            seen = set()
            for hit in result.get('results', [result]):
                if 'path' in hit and hit['path'] not in seen:
                    print(hit['path'])
                    seen.add(hit['path'])
        else:
            output(result,a.json)
        return 1 if isinstance(result,dict) and result.get('status')=='not-found' else 0
    except (ValueError, KeyError, OSError, TypeError, re.error) as error:
        output({'status':'invalid-input','error':str(error)},a.json)
        return 2

if __name__ == '__main__':
    sys.exit(main())
