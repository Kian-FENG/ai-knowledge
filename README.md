# ai-knowledge

本地 AI 产业研究 Agent，沿用 LLM-Wiki 的入库与检索流程，参考 AI-News 的
“采集 → 证据包 → Agent 编辑核验 → 报告”流程，每天洛杉矶时间 18:00 生成日报（自动切换夏令时），
每周五洛杉矶时间 18:00 生成周报。定时触发由 Codex 自动化执行
[统一入口](prompts/scheduled.md)：每天 18:00 处理日报，周五同次处理周报，漏跑时补最近到期周期。
启用状态和运行要求见[定时计划](docs/report-schedule.md)。

重点覆盖 OpenAI、Anthropic、DeepSeek、Qwen/阿里、Kimi/月之暗面及新公司；
同时跟踪产品形态、模型能力、SGLang/vLLM/Dynamo、GPU 供应链与相关论文。

在本项目聊天中直接说：

- `ingest <URL 或本地文件>，更新相关公司、模型和趋势页`
- `批量入库这个目录中的资料，跳过重复来源`
- `query OpenAI 和 Anthropic 最近的产品形态有什么变化？`
- `把这篇文章入库，然后比较它与已有模型评测结论的差异`
- `比较 DeepSeek、Qwen、Kimi 的最新模型能力，注明测试口径`
- `分析 SGLang、vLLM、Dynamo 本周进展及推理成本影响`
- `生成今天的 AI 产业分析日报`
- `生成最近一期已到期的 AI 产业分析周报`

Agent 使用同一知识库完成两种工作：ingest 负责原文归档、去重、综合、审核发布，
query 负责检索已发布页、阅读证据并回答。纯查询默认只读；组合请求先入库再回查。
入口为 [SKILL.md](SKILL.md)，共同规则为 [AGENTS.md](AGENTS.md)，具体步骤见
[入库工作流](docs/workflows.md)与[查询工作流](prompts/query.md)。
`.agents/skills/ai-knowledge` 链接到项目根，使用同一份技能入口。

## 运行

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
scripts/python scripts/query.py "AI Infra 推理成本" --json
scripts/python scripts/query.py --type entity --domain companies --json
scripts/ai-news collect --days 14 --limit 60
scripts/ai-news collect --due --summary   # 高频定时任务，只抓到期来源
scripts/ai-news packet --brief
scripts/ai-news packet --period weekly
bash tests/run.sh
```

`collect` 采集和归档，`packet` 组织证据；中文分析由执行 `prompts/daily.md` 的
Agent 完成，`report` 验证并渲染编辑 JSON。单独运行采集命令不会生成可信的分析。
来源分为一手、Infra、研究、政府、媒体和聚合六组，媒体 feed 多数只保留 1–2 天，需要
按[采集说明](docs/ingest-automation.md)安装每 2 小时一次的 `collect --due`。各来源实测
与样例覆盖对照见[来源修复记录](docs/source-remediation-2026-10-02.md)。

知识入口：[index](index.md)。Agent 入口：[SKILL](SKILL.md)。
日报保存到 `reports/daily/YYYY/MM/YYYY-MM-DD/report.md`；周报保存到
`reports/weekly/YYYY/MM/YYYY-MM-DD/report.md`。目录按窗口结束日归类，
历史修订和证据可追溯；从[报告索引](reports/index.md)按类型、年份、月份检索。
周报工作流见 [weekly prompt](prompts/weekly.md)，汇总截至洛杉矶时间周五 18:00 的七天变化。
日报版式来自 `docs/examples/ai-industry-daily-reference.md`，样例中的旧闻不是新证据。

移植来源、兼容范围和差异见 [porting](docs/porting.md)。
