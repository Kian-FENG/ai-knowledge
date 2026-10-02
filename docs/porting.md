# 移植来源与兼容边界

参考项目为 WorkingMacMini（remote-control）的 `/Users/kian/workspace/llm-wiki`
和 `/Users/kian/workspace/ai-news`。2026-10-01 从现有 Codex 聊天的文件读取结果取得
契约、SKILL、流程、schema 和日报/周报编辑规范；快照保存在 `docs/upstream/`。
这是一份基于已读取契约的本地实现，并非远端完整代码/知识库的逐字复制。

LLM-Wiki 参考聊天：`Print AGENTS.md`（01a0fa0f-7386-7860-9375-0c48bc2a3fcc）、
`Ingest WeChat article`（01a0ec59-7637-73a2-b08a-8d425c7cb6a8）。
AI-News 参考聊天：`AI 每日采集与每周产业分析`
（01a0f9e9-3e24-7413-bb78-8b619c5fe07a、01a0f4c4-2fe9-7371-a0c4-d56fa42d8a38）。

| 流程 | 本地保持 | 面向本需求的调整 |
|---|---|---|
| ingest | 原文不可覆盖、查重、八类模板、综合关联、审核指纹、发布、校验 | 产业/公司/产品/模型/Infra 领域和口径 |
| query | search/read/trace/answer、同名 CLI、过滤、中文检索、仅 published | 公司别名、模型和社区关系、最新信息在线核对 |
| evidence | 类型和核验分离、定位与版本、失效审核重做 | 事件时间、商业指标、模型评测和 Infra 配置 |
| daily | validate/collect/status/packet/editorial/report、原始档案与健康记录 | 从每周报告改成每日北京时间 08:00，六个栏目 |

本地实现不含远端实验环境、历史知识页、SQLite 多仓库 discovery route promotion、
Git hooks 或远端自动化配置。日报候选通过本地文件索引和 Agent 核验后按标准 ingest
入库；不声称复用了远端全部内部 CLI 参数。两个远端项目保持原样。

Agent 的项目入口采用 [OpenAI 官方 AGENTS.md 约定](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。
