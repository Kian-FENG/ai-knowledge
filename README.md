# ai-knowledge

本地 AI 产业研究 Agent，沿用 LLM-Wiki 的入库与检索流程，参考 AI-News 的
“采集 → 证据包 → Agent 编辑核验 → 报告”流程，每天北京时间 08:00 生成日报，
每周六北京时间 08:00 生成周报。定时触发由 Codex 自动化执行
[统一入口](prompts/scheduled.md)：每天处理日报，周六同次处理周报，漏跑时补最近到期周期。
启用状态和运行要求见[定时计划](docs/report-schedule.md)。

重点覆盖 OpenAI、Anthropic、DeepSeek、Qwen/阿里、Kimi/月之暗面及新公司；
同时跟踪产品形态、模型能力、SGLang/vLLM/Dynamo、GPU 供应链与相关论文。

在本项目聊天中直接说：

- `ingest <URL 或本地文件>，更新相关公司、模型和趋势页`
- `query OpenAI 和 Anthropic 最近的产品形态有什么变化？`
- `比较 DeepSeek、Qwen、Kimi 的最新模型能力，注明测试口径`
- `分析 SGLang、vLLM、Dynamo 本周进展及推理成本影响`
- `生成今天的 AI 产业分析日报`
- `生成最近一期已到期的 AI 产业分析周报`

## 运行

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
scripts/python scripts/query.py "AI Infra 推理成本" --json
scripts/ai-news collect --days 14 --limit 60
scripts/ai-news packet
scripts/ai-news packet --period weekly
bash tests/run.sh
```

`collect` 采集和归档，`packet` 组织证据；中文分析由执行 `prompts/daily.md` 的
Agent 完成，`report` 验证并渲染编辑 JSON。单独运行采集命令不会生成可信的分析。

知识入口：[index](index.md)。Agent 入口：[SKILL](SKILL.md)。
日报保存到 `reports/daily/YYYY/MM/YYYY-MM-DD/report.md`；周报保存到
`reports/weekly/YYYY/MM/YYYY-MM-DD/report.md`。目录按窗口结束日归类，
历史修订和证据可追溯；从[报告索引](reports/index.md)按类型、年份、月份检索。
周报工作流见 [weekly prompt](prompts/weekly.md)，汇总截至周六 08:00 的七天变化。
日报版式来自 `docs/examples/ai-industry-daily-reference.md`，样例中的旧闻不是新证据。

移植来源、兼容范围和差异见 [porting](docs/porting.md)。
