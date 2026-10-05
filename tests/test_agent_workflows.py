"""Exercise Agent-facing commands against an isolated knowledge repository."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


SOURCE = Path(__file__).resolve().parents[1]


class AgentWorkflows(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='ai-knowledge-workflow-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('data/schemas.yaml', 'data/refresh-cutoff.yaml',
                     'data/retrieval-aliases.yaml', 'tags/domains.yaml'):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, target)
        shutil.copytree(SOURCE / '_templates', self.root / '_templates')
        (self.root / 'reference').mkdir()
        (self.root / 'research').mkdir()
        (self.root / 'index.md').write_text('# Test navigation\n', encoding='utf-8')
        self.env = dict(os.environ, AI_KNOWLEDGE_ROOT=str(self.root))

    def command(self, script, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(SOURCE / 'scripts' / script), *args],
            cwd=self.root, env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def fill(self, path, body, **metadata):
        target = self.root / path
        meta = yaml.safe_load(target.read_text(encoding='utf-8').split('---', 2)[1])
        meta.update(summary='隔离测试：星舟服务的来源与公司页',
                    evidence_kind='reported', **metadata)
        target.write_text('---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False)
                          + '---\n\n' + body, encoding='utf-8')

    def ingest_fixture(self):
        source_text = (
            'Offline fixture only; not a real company or news event.\n'
            'Starboat / 星舟 is a fictional model serving company.\n'
            'Its release describes a planned product, without measured performance.\n')
        incoming = self.root / 'incoming.txt'
        incoming.write_text(source_text, encoding='utf-8')
        archive = self.command('ingest.py', 'archive', str(incoming),
                               '--source-url', 'https://example.org/starboat', '--json')
        self.assertEqual(archive['sha256'], hashlib.sha256(source_text.encode()).hexdigest())
        duplicate = self.command('ingest.py', '--json', 'archive', str(incoming))
        self.assertEqual(archive['raw_path'], duplicate['raw_path'])

        source = self.command('ingest.py', 'draft', '--type', 'source', '--slug', 'starboat-release',
                              '--domain', 'products', '--title', '星舟产品公告', '--json')['path']
        entity = self.command('ingest.py', '--json', 'draft', '--type', 'entity', '--slug', 'starboat',
                              '--domain', 'companies', '--title', '星舟公司')['path']
        version = 'sha256:' + archive['sha256']
        source_body = (
            '# 星舟产品公告\n\n这是隔离测试的虚构材料，不是真实公司动态。'
            '原文只说明计划，没有实测性能，页面不得将计划解释为已完成交付。\n\n'
            '## Evidence\n\n原始来源第 2–3 行，保留来源版本与阅读范围。\n')
        self.fill(source, source_body, url='https://example.org/starboat',
                  raw_path=archive['raw_path'], sha256=archive['sha256'],
                  sources=[archive['raw_path']],
                  evidence=[{'source': archive['raw_path'], 'locator': 'lines 2-3', 'version': version}])
        self.fill(entity, '# 星舟公司\n\n虚构公司用于离线测试，产品仍处于计划阶段。'
                  '本页只复述测试原文，没有独立实验，也不声称测量结果。\n\n## Evidence\n\n'
                  '依据来源公告中的计划描述，不提升核验程度。\n',
                  aliases=['星舟', 'Starboat'], sources=['source-starboat-release'],
                  evidence=[{'source': 'source-starboat-release', 'locator': 'Evidence', 'version': version}])
        with (self.root / 'index.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[[reference/entities/starboat|星舟公司]]\n')

        self.assertEqual(self.command('query.py', 'Starboat', '--json')['status'], 'empty')
        inspected = self.command('query.py', 'Starboat', '--include-unpublished', '--json')
        self.assertIn(entity, [hit['path'] for hit in inspected['results']])
        self.command('ingest.py', 'review', source, entity, '--reviewer', 'Offline test', '--json')
        self.assertEqual(self.command('query.py', 'Starboat', '--json')['status'], 'empty')
        self.command('ingest.py', 'finalize', source, entity, '--json')
        return source, entity, archive

    def test_ingest_then_query_and_trace_without_writes(self):
        source, entity, archive = self.ingest_fixture()
        before = {str(p.relative_to(self.root)): p.read_bytes()
                  for p in self.root.rglob('*') if p.is_file()}
        found = self.command('query.py', 'Starboat', '--json')
        self.assertEqual(found['results'][0]['path'], entity)
        pg = self.command('get_page.py', entity, '--follow-sources', '--json')
        self.assertEqual(pg['metadata']['lifecycle'], 'published')
        self.assertEqual(pg['metadata']['verification'], 'unchecked')
        self.assertNotIn('last_verified', pg['metadata'])
        self.assertTrue(any(r['resolution'].get('path') == source for r in pg['references']))
        original = self.command('get_page.py', source, '--follow-sources', '--json')
        self.assertTrue(any(r['resolution']['status'] == 'raw' and
                            r['resolution']['path'] == archive['raw_path']
                            for r in original['references']))
        raw = (self.root / archive['raw_path']).read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), archive['sha256'])
        self.assertEqual(self.command('grep_wiki.py', '虚构', '--json')['status'], 'success')
        self.assertEqual(self.command('validate.py', '--require-migrated', 'reference',
                                      '--require-migrated', 'research', '--json')['errors'], [])
        after = {str(p.relative_to(self.root)): p.read_bytes()
                 for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after, 'Query and source tracing must not write to the knowledge repository')
        self.assertEqual(len(list((self.root / 'queries').glob('*.md'))), 6)

    def test_filter_only_query_and_lifecycle_boundaries(self):
        source, entity, _ = self.ingest_fixture()
        selected = self.command('query.py', '--type', 'entity', '--domain', 'companies', '--json')
        self.assertEqual([h['path'] for h in selected['results']], [entity])
        union = self.command('query.py', '--type', 'entity', '--type', 'source', '--tfidf', '--json')
        self.assertEqual([h['path'] for h in union['results']], sorted([source, entity]))
        self.assertTrue(all(h['score'] == 0 for h in union['results']))
        limited = self.command('query.py', '--type', 'entity', '--type', 'source', '-n', '1', '--json')
        self.assertEqual(len(limited['results']), 1)
        self.assertEqual(self.command('query.py', '--type', 'entity', '--domain', 'infra',
                                      '--json')['status'], 'empty')
        self.command('ingest.py', 'draft', '--type', 'entity', '--slug', 'pending',
                     '--domain', 'companies', '--title', '未发布公司', '--json')
        visible = self.command('query.py', '--type', 'entity', '--json')['results']
        self.assertEqual([h['path'] for h in visible], [entity])
        all_states = self.command('query.py', '--type', 'entity', '--include-unpublished', '--json')
        self.assertEqual(len(all_states['results']), 2)

    def test_invalid_query_does_not_silently_list_everything(self):
        for args in [[], ['   '], ['!!!'], ['--type', 'unknown'],
                     ['--domain', 'unknown'], ['--type', 'entity', '-n', '0']]:
            with self.subTest(args=args):
                self.assertEqual(self.command('query.py', *args, '--json', expected=2)['status'],
                                 'invalid-input')


if __name__ == '__main__':
    unittest.main()
