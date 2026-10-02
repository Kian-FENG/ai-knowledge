"""Local, file-backed wiki contract. No network or model calls."""
from __future__ import annotations
import base64
from collections import Counter, defaultdict, deque
from contextlib import contextmanager
from datetime import date, datetime
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile
import uuid
from urllib.parse import unquote, urlparse
from zoneinfo import ZoneInfo
import yaml

ROOT = Path(os.environ.get('AI_KNOWLEDGE_ROOT', Path(__file__).resolve().parent.parent)).resolve()
REVIEW_FIELDS = {'lifecycle', 'reviewed_at', 'reviewed_by', 'reviewed_content_sha256'}
NAV_ROOTS = ('index.md', 'research/KNOWLEDGE-GRAPH.md')
LIST_REFS = ('sources', 'related', 'supersedes', 'applies_to', 'specializes')


def today():
    return datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()


def plain(value):
    return json.loads(json.dumps(value, default=str, ensure_ascii=False))


def config(path):
    return yaml.safe_load((ROOT / path).read_text(encoding='utf-8'))


def local_path(value):
    p = Path(value)
    p = (ROOT / p).resolve() if not p.is_absolute() else p.resolve()
    if p != ROOT and ROOT not in p.parents:
        raise ValueError('Path must stay within the knowledge repository')
    return p


def relative(path):
    return local_path(path).relative_to(ROOT).as_posix()


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = data.encode('utf-8') if isinstance(data, str) else data
    fd, temporary = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def json_write(path, value):
    atomic_write(path, json.dumps(plain(value), ensure_ascii=False, indent=2) + '\n')


def parse_text(text):
    match = re.match(r'\A---\s*\n(.*?)\n---\s*\n?', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    meta = yaml.safe_load(match.group(1))
    if not isinstance(meta, dict):
        raise ValueError('Frontmatter must be a mapping')
    return plain(meta), text[match.end():].lstrip('\n')


def serialize(meta, body):
    return '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n' + body.rstrip() + '\n'


def page(path, text=None):
    path = local_path(path)
    meta, body = parse_text(text if text is not None else path.read_text(encoding='utf-8'))
    return {'path': relative(path), 'metadata': meta, 'body': body}


def pages(overrides=None):
    found = {}
    for folder in ('reference', 'research'):
        for p in sorted((ROOT / folder).rglob('*.md')):
            if relative(p) in NAV_ROOTS:
                continue
            found[relative(p)] = page(p, (overrides or {}).get(relative(p)))
    for p, text in (overrides or {}).items():
        if p not in found:
            found[p] = page(p, text)
    return found


def fingerprint(meta, body):
    cleaned = {k: v for k, v in meta.items() if k not in REVIEW_FIELDS}
    content = json.dumps(plain(cleaned), sort_keys=True, ensure_ascii=False) + '\n' + body.rstrip()
    return hashlib.sha256(content.encode()).hexdigest()


def references(p):
    m, body = p['metadata'], p['body']
    refs = []
    for field in LIST_REFS:
        for target in m.get(field, []) or []:
            refs.append({'kind': 'evidence' if field == 'sources' else 'navigation', 'field': field, 'target': target})
    for field in ('source', 'url'):
        if m.get(field):
            refs.append({'kind': 'evidence', 'field': field, 'target': m[field]})
    for record in m.get('evidence', []) or []:
        if isinstance(record, dict):
            refs.append({'kind': 'evidence', 'field': 'evidence', 'target': record.get('source', ''),
                         'locator': record.get('locator'), 'version': record.get('version')})
    section = ''
    for line in body.splitlines():
        if line.startswith('## '):
            section = line[3:].strip().lower()
        kind = 'evidence' if section in ('evidence', 'sources', '来源', '证据') else 'navigation'
        for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', line):
            refs.append({'kind': kind, 'field': 'body', 'target': target})
        if kind == 'evidence':
            for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', line):
                refs.append({'kind': kind, 'field': 'body', 'target': target})
    return refs


def resolve(target, corpus):
    if not isinstance(target, str) or not target.strip():
        return {'status': 'unresolved', 'target': target}
    target = target.strip()
    if target.startswith('[[') and target.endswith(']]'):
        target = target[2:-2].split('|')[0]
    if urlparse(target).scheme in ('http', 'https'):
        return {'status': 'external', 'target': target}
    target = unquote(target.split('#')[0])
    if '/' in target or target.endswith('.md'):
        try:
            path = local_path(target)
            if path.suffix != '.md' and not path.exists():
                path = path.with_suffix('.md')
            key = relative(path)
            if key in corpus:
                return {'status': 'resolved', 'path': key, 'target': target}
            if path.is_file() and key.startswith(('raw/', '.raw/')):
                return {'status': 'raw', 'path': key, 'target': target}
        except ValueError:
            pass
        return {'status': 'unresolved', 'target': target}
    exact = [k for k, p in corpus.items() if p['metadata'].get('id') == target]
    matches = exact or [k for k, p in corpus.items() if target.casefold() in
                       [str(v).casefold() for v in [Path(k).stem, p['metadata'].get('title', '')] + (p['metadata'].get('aliases') or [])]]
    if len(matches) == 1:
        return {'status': 'resolved', 'path': matches[0], 'target': target}
    return {'status': 'ambiguous' if matches else 'unresolved', 'target': target, 'matches': matches}


def validate(corpus=None, complete_paths=None):
    corpus = pages() if corpus is None else corpus
    schema, domains = config('data/schemas.yaml'), config('tags/domains.yaml')['domains']
    errors, ids = [], {}
    for path, p in corpus.items():
        m, body = p['metadata'], p['body']
        local = []
        typ = m.get('type')
        if typ not in schema['types']:
            errors.append(f'{path}: unknown page type {typ}')
            continue
        for key in schema['types'][typ]['required']:
            if key not in m or m[key] is None:
                local.append('missing ' + key)
        for key in ('title', 'id'):
            if not isinstance(m.get(key), str) or not m[key].strip():
                local.append('empty/invalid ' + key)
        pid = m.get('id', '')
        if not isinstance(pid, str) or not re.fullmatch(re.escape(typ) + r'-[a-z0-9]+(?:-[a-z0-9]+)*', pid):
            local.append('invalid type-prefixed ID')
        elif pid in ids:
            local.append('duplicate ID with ' + ids[pid])
        else:
            ids[pid] = path
        for key in ('lifecycle', 'evidence_kind', 'verification'):
            if m.get(key) not in schema[key]:
                local.append('invalid ' + key)
        ds = m.get('domain')
        if not isinstance(ds, list) or not 1 <= len(ds) <= 2 or any(x not in domains for x in ds):
            local.append('domain must contain 1–2 known values')
        for key in ('tags', 'aliases') + LIST_REFS:
            if key in m and (not isinstance(m[key], list) or any(not isinstance(v, str) for v in m[key])):
                local.append(key + ' must be a list of strings')
        for key in ('created', 'updated', 'last_verified', 'reviewed_at'):
            if m.get(key):
                try:
                    if date.fromisoformat(str(m[key])) > date.fromisoformat(today()):
                        local.append(key + ' is in the future')
                except ValueError:
                    local.append('invalid ' + key)
        if m.get('entity_kind') and m['entity_kind'] not in schema['entity_kind']:
            local.append('invalid entity_kind')
        if m.get('source_category') and m['source_category'] not in schema['source_category']:
            local.append('invalid source_category')
        complete = path in (complete_paths or set()) or m.get('lifecycle') in ('reviewed', 'published')
        if complete:
            if re.search(r'\bTODO\b|\{\{.*?\}\}', body + str(m)):
                local.append('unfinished scaffold')
            if not m.get('summary') or len(body.strip()) < 40:
                local.append('missing summary or substantive body')
        evidence = m.get('evidence', [])
        if not isinstance(evidence, list) or any(not isinstance(e, dict) for e in evidence):
            local.append('evidence must be a list of records')
            evidence = []
        checked = m.get('verification') in ('source-checked', 'replicated')
        if checked and (not m.get('last_verified') or not m.get('verification_note') or not evidence):
            local.append('checked claims require verification date, note and evidence')
        for e in evidence:
            if any(not isinstance(e.get(k), str) or not e[k].strip() for k in ('source', 'locator', 'version')):
                local.append('evidence requires source, locator and version')
        if m.get('evidence_kind') == 'measured' or m.get('confidence') == 'experimental':
            ev = re.search(r'^## Evidence\s*\n(.+?)(?=^## |\Z)', body, re.S | re.M)
            if not ev or len(ev.group(1).strip()) < 30:
                local.append('measured claims require substantive ## Evidence')
        # Avoid cascading exceptions after malformed fields.
        if not any('list' in e for e in local):
            for ref in references(p):
                res = resolve(ref['target'], corpus)
                if complete and res['status'] in ('unresolved', 'ambiguous'):
                    local.append(f"{res['status']} reference: {ref['target']}")
                if ref['field'] == 'specializes' and (res['status'] != 'resolved' or
                    corpus[res['path']]['metadata'].get('id') != ref['target'] or
                    corpus[res['path']]['metadata'].get('type') != 'concept'):
                    local.append('specializes requires a concept ID')
        if 'specialized_by' in m:
            local.append('specialized_by is derived; remove stored reverse links')
        if m.get('lifecycle') in ('reviewed', 'published'):
            if not m.get('reviewed_by') or not m.get('reviewed_at') or m.get('reviewed_content_sha256') != fingerprint(m, body):
                local.append('missing or stale review fingerprint')
        errors.extend(path + ': ' + x for x in local)
    return errors


def navigation(corpus):
    visible = {k: p for k, p in corpus.items() if p['metadata'].get('lifecycle') == 'published'}
    edges = defaultdict(set)
    for path, p in visible.items():
        for ref in references(p):
            res = resolve(ref['target'], visible)
            if res['status'] == 'resolved':
                edges[path].add(res['path'])
    start = set()
    for nav in NAV_ROOTS:
        if (ROOT / nav).exists():
            text = (ROOT / nav).read_text()
            targets = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', text)
            for dest in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
                dest_path = (Path(nav).parent / dest).as_posix() if nav != 'index.md' else dest
                targets.append(dest_path)
            for target in targets:
                res = resolve(target, visible)
                if res['status'] == 'resolved':
                    start.add(res['path'])
    reached, queue = set(start), deque(start)
    while queue:
        for nxt in edges[queue.popleft()] - reached:
            reached.add(nxt)
            queue.append(nxt)
    return sorted(set(visible) - reached)


def indices(corpus):
    visible = {k: p for k, p in corpus.items() if p['metadata'].get('lifecycle') == 'published'}
    groups = {name: defaultdict(list) for name in ('by-domain', 'by-type', 'by-source', 'by-tag', 'by-entity', 'recent')}
    for path, p in sorted(visible.items()):
        m = p['metadata']
        link = f"- `{m['type']}` [[{path[:-3]}|{m['title']}]]"
        for key, vals in [('by-domain', m['domain']), ('by-type', [m['type']]), ('by-tag', m.get('tags', [])),
                          ('recent', [m.get('updated', 'undated')])]:
            for value in vals:
                groups[key][str(value)].append(link)
        if m['type'] in ('source', 'paper'):
            groups['by-source'][m.get('source_category', m['type'])].append(link)
        if m['type'] == 'entity':
            groups['by-entity'][m.get('entity_kind', 'organization')].append(link)
    output = {}
    for name, buckets in groups.items():
        text = '# ' + name + '\n\nGenerated; published pages only. Do not hand-edit.\n'
        for key in sorted(buckets, reverse=name == 'recent'):
            text += '\n## ' + key + '\n\n' + '\n'.join(buckets[key]) + '\n'
        output['queries/' + name + '.md'] = text
    return output


def _rollback(journal):
    for path, old in journal['before'].items():
        target = local_path(path)
        if old is None:
            target.unlink(missing_ok=True)
        else:
            atomic_write(target, base64.b64decode(old))


@contextmanager
def write_lock():
    (ROOT / '.cache').mkdir(exist_ok=True)
    with (ROOT / '.cache/wiki.lock').open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        journal = ROOT / '.cache/publication.json'
        if journal.exists():
            _rollback(json.loads(journal.read_text()))
            journal.unlink()
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def transaction(changes):
    journal_path = ROOT / '.cache/publication.json'
    journal = {'before': {p: base64.b64encode(local_path(p).read_bytes()).decode() if local_path(p).exists() else None for p in changes}}
    json_write(journal_path, journal)
    try:
        for path, value in changes.items():
            atomic_write(local_path(path), value)
    except BaseException:
        _rollback(journal)
        journal_path.unlink()
        raise
    journal_path.unlink()


def draft(typ, slug, domains, title, to=None):
    schema = config('data/schemas.yaml')
    if typ not in schema['types'] or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Invalid type or kebab-case slug')
    if not domains or not 1 <= len(domains) <= 2 or any(x not in config('tags/domains.yaml')['domains'] for x in domains):
        raise ValueError('Specify 1–2 known --domain values')
    folder = {'note': 'research/' + domains[0], 'comparison': 'research/synthesis', 'entity': 'reference/entities'}.get(typ, 'reference/' + typ + 's')
    target = local_path(Path(to or folder) / (slug + '.md'))
    if not relative(target).startswith(('reference/', 'research/')) or relative(target) in NAV_ROOTS:
        raise ValueError('Drafts belong in reference/ or research/')
    with write_lock():
        if target.exists() or any(p['metadata'].get('id') == typ + '-' + slug for p in pages().values()):
            raise ValueError('Page already exists; update the existing page')
        m, body = parse_text((ROOT / '_templates' / (typ + '.md')).read_text())
        m.update(id=typ + '-' + slug, title=title or slug, domain=domains, created=today(), updated=today())
        atomic_write(target, serialize(m, body.replace('{{title}}', m['title'])))
    return relative(target)


def review(paths, reviewer):
    if not reviewer.strip():
        raise ValueError('Reviewer name required')
    with write_lock():
        corpus = pages()
        changes = {}
        for path in paths:
            key = relative(path)
            p = corpus[key]
            m = dict(p['metadata'])
            m.update(lifecycle='reviewed', reviewed_by=reviewer, reviewed_at=today())
            m['reviewed_content_sha256'] = fingerprint(m, p['body'])
            changes[key] = serialize(m, p['body'])
            corpus[key] = page(key, changes[key])
        errors = validate(corpus, set(changes))
        # Drafts outside this batch can be incomplete, but not malformed.
        if errors:
            raise ValueError('\n'.join(errors))
        transaction(changes)
    return list(changes)


def finalize(paths):
    with write_lock():
        corpus, changes = pages(), {}
        for path in paths:
            key = relative(path)
            p = corpus[key]
            m = dict(p['metadata'])
            if m.get('lifecycle') not in ('reviewed', 'published'):
                raise ValueError(key + ': review required before publication')
            if m.get('reviewed_content_sha256') != fingerprint(m, p['body']):
                raise ValueError(key + ': content changed after review')
            m['lifecycle'] = 'published'
            changes[key] = serialize(m, p['body'])
            corpus[key] = page(key, changes[key])
        errors = validate(corpus)
        unreachable = navigation(corpus)
        if errors or unreachable:
            raise ValueError('\n'.join(errors + ['Unreachable: ' + p for p in unreachable]))
        changes.update(indices(corpus))
        transaction(changes)
    return {'published': [relative(p) for p in paths], 'indices': 6}


def touch(path, note, verification='source-checked', verified=None):
    if not note.strip():
        raise ValueError('Verification note required')
    with write_lock():
        p = page(path)
        m = dict(p['metadata'])
        m.update(verification=verification, verification_note=note, last_verified=verified or today(), updated=today(), lifecycle='draft')
        for field in REVIEW_FIELDS - {'lifecycle'}:
            m.pop(field, None)
        text = serialize(m, p['body'])
        corpus = pages({p['path']: text})
        errors = validate(corpus)
        if errors:
            raise ValueError('\n'.join(errors))
        atomic_write(local_path(path), text)
    return p['path']


def archive(data, name, url=None):
    digest = hashlib.sha256(data).hexdigest()
    suffix = Path(name).suffix or '.bin'
    target = ROOT / 'raw' / today() / (digest + suffix)
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        with target.open('xb') as f:
            f.write(data)
    except FileExistsError:
        if target.read_bytes() != data:
            raise ValueError('Raw hash collision or corrupt archive')
    record = {'raw_path': relative(target), 'sha256': digest, 'source_url': url, 'original_name': Path(name).name,
              'fetched_at': datetime.now(ZoneInfo('UTC')).isoformat()}
    json_write(ROOT / 'data/archive-records' / (uuid.uuid4().hex + '.json'), record)
    return record


def freshness(m, as_of=None):
    cutoff = config('data/refresh-cutoff.yaml')['days'].get(m.get('type'), 30)
    if not m.get('last_verified'):
        return {'status': 'undated', 'days': None, 'threshold_days': cutoff}
    try:
        age = (date.fromisoformat(as_of or today()) - date.fromisoformat(str(m['last_verified']))).days
        return {'status': 'invalid' if age < 0 else 'stale' if age > cutoff else 'fresh', 'days': age, 'threshold_days': cutoff}
    except ValueError:
        return {'status': 'invalid', 'days': None, 'threshold_days': cutoff}


def tokens(text):
    text = text.casefold()
    result = re.findall(r'[a-z0-9][a-z0-9_.+-]*', text)
    for span in re.findall(r'[\u3400-\u9fff]+', text):
        result += [span] if len(span) == 1 else [span[i:i+2] for i in range(len(span)-1)]
    return result


def search(query, filters=None, n=5, include=False, tfidf=False, expand=False):
    if not query.strip() or n < 1:
        raise ValueError('Nonempty query and positive -n required')
    corpus = pages()
    candidates = {k: p for k, p in corpus.items() if include or p['metadata'].get('lifecycle') == 'published'}
    for key, values in (filters or {}).items():
        if values:
            candidates = {k: p for k, p in candidates.items() if set(values) & set(p['metadata'].get(key, []) if isinstance(p['metadata'].get(key), list) else [p['metadata'].get(key)])}
    terms = set(tokens(query))
    expanded_query = query.casefold()
    for group in config('data/retrieval-aliases.yaml')['groups']:
        if any(v.casefold() in expanded_query for v in group):
            for v in group:
                terms.update(tokens(v))
    documents = {}
    for path, p in candidates.items():
        m = p['metadata']
        heading = ' '.join([m['title'], m.get('summary', ''), ' '.join(m.get('aliases', [])), ' '.join(m.get('tags', []))])
        documents[path] = Counter(tokens(heading + '\n' + p['body']))
    df = Counter(t for counts in documents.values() for t in counts)
    qvec = {t: math.log((len(documents) + 1) / (df[t] + 1)) + 1 for t in terms}
    ranked = []
    for path, counts in documents.items():
        p, m = candidates[path], candidates[path]['metadata']
        overlap = terms & set(counts)
        if not overlap:
            continue
        if tfidf:
            vec = {t: (1 + math.log(c)) * (math.log((len(documents) + 1) / (df[t] + 1)) + 1) for t, c in counts.items()}
            score = sum(vec[t] * qvec[t] for t in overlap) / (math.sqrt(sum(v*v for v in vec.values())) * math.sqrt(sum(v*v for v in qvec.values())))
        else:
            heading_terms = set(tokens(m['title'] + ' ' + m.get('summary', '') + ' ' + ' '.join(m.get('aliases', []))))
            score = sum(min(counts[t], 4) + (6 if t in heading_terms else 0) for t in overlap)
        ranked.append({'score': round(score, 6), 'id': m['id'], 'path': path, 'title': m['title'], 'domain': m['domain'], 'lifecycle': m['lifecycle'], 'expanded': False})
    ranked.sort(key=lambda x: (-x['score'], x['path']))
    selected = ranked[:n]
    if expand:
        seen = {x['path'] for x in selected}
        extra = []
        for hit in selected:
            for ref in references(candidates[hit['path']]):
                res = resolve(ref['target'], candidates)
                if res['status'] == 'resolved' and res['path'] not in seen:
                    m = candidates[res['path']]['metadata']
                    extra.append({'score': 0, 'id': m['id'], 'path': res['path'], 'title': m['title'], 'domain': m['domain'], 'lifecycle': m['lifecycle'], 'expanded': True})
                    seen.add(res['path'])
        selected += extra[:n]
    return {'status': 'success' if selected else 'empty', 'results': selected}


def get_page(target, include=False, follow=False, as_of=None):
    corpus = pages()
    res = resolve(target, corpus)
    if res['status'] != 'resolved':
        return {'status': 'not-found', 'resolution': res}
    p = corpus[res['path']]
    if not include and p['metadata'].get('lifecycle') != 'published':
        return {'status': 'not-found'}
    out = dict(p, status='success', freshness=freshness(p['metadata'], as_of))
    out['specialized_by'] = [x['metadata']['id'] for x in corpus.values() if p['metadata']['id'] in x['metadata'].get('specializes', []) and (include or x['metadata'].get('lifecycle') == 'published')]
    if follow:
        out['references'] = [dict(ref, resolution=resolve(ref['target'], corpus)) for ref in references(p)]
    return out
