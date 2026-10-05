---
name: ai-knowledge
description: 研究 AI 行业趋势、产品形态、美国和中国 AI 公司及新创公司的发展，以及模型能力、SGLang/vLLM/Dynamo 等 AI Infra 和相关论文；查询、入库或生成中文 AI 产业分析日报。使用本地 /Users/kian/workspace/ai-knowledge 的可追溯知识库；低层算子实现和部署实验不属于本技能。
---

# AI Knowledge

在 `/Users/kian/workspace/ai-knowledge` 运行工具。读取该目录的 `AGENTS.md`。

## Retrieve → read → trace → answer

1. 用用户语言搜索，例如：
   `scripts/python scripts/query.py "DeepSeek Qwen Kimi 模型能力" -n 8 --json`。
   `--domain/--type/--tag/--confidence` 可重复，同字段 OR，跨字段 AND。
   广泛问题先看 `index.md`、`queries/by-domain.md`。
2. 按返回路径读页：
   `scripts/python scripts/get_page.py PATH --follow-sources --json`。
   evidence/sources 是证据关系，related/specializes 是导航；还需读原始出处。
3. 精确片段用 `grep_wiki.py`；`--expand` 扩展关联；`--tfidf` 是词法相似度。
   `--semantic` 仅是旧别名，不代表 embedding。无结果换同义词，再说明知识缺口。
4. 按“事实与变化 → 判断与依据 → 不确定性和观察指标”回答，附页面与原始来源。
   最新产品、模型、版本、价格和公司动态需在线核验；不能用记忆补“最新”。

默认只检索 published；主动检查未发布页才加 `--include-unpublished`。
检索排名不是可信度，source-checked 不是独立复现。

## Authoring and daily report

- “ingest/收录/入库”：读取 [workflows](docs/workflows.md)，沿用 LLM-Wiki
  的 archive → deduplicate → draft → synthesize/link → review → finalize → validate。
- “日报/每天自动报告”：执行 [daily prompt](prompts/daily.md)；“周报/每周报告”：执行
  [weekly prompt](prompts/weekly.md)。两者遵守
  [report spec](docs/report-spec.md)。日报使用新加坡时间，每天 06:00 截止，事实与分析分开。
- 比较模型或 Infra 时加载 [研究口径](docs/research-focus.md)；理解元数据时读取
  [schema](docs/retrieval/schema.md)。不为简单查询加载所有文档。

新公司从发现队列进入跟踪，经过身份和来源核实后建立 entity 页；不把模型品牌
直接当独立公司（例如 Qwen/通义归属阿里，Kimi 为 Moonshot AI/月之暗面的产品）。
