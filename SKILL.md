---
name: ai-knowledge
description: 查询（query）或入库（ingest）AI 行业、公司、产品、模型和 AI Infra 资料，支持 URL、本地文件与批量资料的归档、综合、审核发布及来源追溯；也生成中文 AI 产业日报和周报。使用本地 /Users/kian/workspace/ai-knowledge 知识库；低层算子实现和部署实验不属于本技能。
---

# AI Knowledge

在 `/Users/kian/workspace/ai-knowledge` 运行工具。读取该目录的 `AGENTS.md`。

## 选择任务

- **Ingest**：“入库、收录、ingest、更新知识库”。读取 [入库工作流](docs/workflows.md)，
  完成 archive → deduplicate → draft/update → synthesize/link → review → finalize → query。
  用户要求只归档或只起草时按其边界停止；正常 ingest 已授权本地审核发布。
- **Query**：“查询、解释、比较、分析、query”，或“读这篇并回答”。读取
  [查询工作流](prompts/query.md)，执行 retrieve → read → trace → answer，默认只读。
- **Ingest + Query**：“入库后回答/比较”。先完成入库，再用默认检索读取已发布页回答；
  未能发布时说明原因，并区分外部资料与库内知识。纯查询遇到知识缺口不自动入库。
- **报告**：“日报/每天自动报告”用 [daily](prompts/daily.md)；“周报”用
  [weekly](prompts/weekly.md)；定时任务用 [scheduled](prompts/scheduled.md)。

不要求用户使用英文命令。只给链接且用途不明时先阅读，不默认写库。
只加载当前任务需要的工作流；入库查重可直接使用下列工具。

## 工具入口

```bash
scripts/python scripts/query.py "DeepSeek Qwen Kimi 模型能力" -n 8 --json
scripts/python scripts/query.py --type entity --domain companies --json
scripts/python scripts/get_page.py PAGE_ID_OR_PATH --follow-sources --json
scripts/python scripts/grep_wiki.py "精确片段" --json
```

过滤器 `--domain/--type/--tag/--confidence` 可重复，同字段 OR、跨字段 AND。
可以只传过滤器。默认只检索 published；为查重或检查草稿才加 `--include-unpublished`。
`--tfidf` 是词法相似度，`--semantic` 只是兼容别名。`--follow-sources` 列出证据定位，
不代表读过原文。检索分数不代表可信度，source-checked 不代表独立复现。

广泛问题先看 [知识目录](index.md) 和 `queries/by-domain.md`；查询示例见
[examples](docs/retrieval/examples.md)。模型/Infra 比较加载 [研究口径](docs/research-focus.md)，
元数据加载 [schema](docs/retrieval/schema.md)，报告质量加载 [report spec](docs/report-spec.md)。
最新信息先查库再在线核对一手资料，注明 as-of。

新公司从发现队列进入跟踪，经过身份和来源核实后建立 entity 页；不把模型品牌
直接当独立公司（例如 Qwen/通义归属阿里，Kimi 为 Moonshot AI/月之暗面的产品）。
