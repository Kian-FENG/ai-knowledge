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
| daily / weekly | validate/collect/status/packet/editorial/report、原始档案与健康记录 | 本地周期与截止时间以 data/report-settings.yaml 及报告 prompt 为准 |

本地实现不含远端实验环境、历史知识页、SQLite 多仓库 discovery route promotion、
Git hooks 或远端自动化配置。日报候选通过本地文件索引和 Agent 核验后按标准 ingest
入库；不声称复用了远端全部内部 CLI 参数。两个远端项目保持原样。

Agent 的项目入口采用 [OpenAI 官方 AGENTS.md 约定](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。

## 2026-10-04：对照 MacBook-LLM-Wiki

本次参考的是 WorkingMacBook 的 `MacBook-LLM-Wiki` 项目
（`/Users/kian/workspace/llm-wiki`），与上面的早期 WorkingMacMini 快照分开记录。
通过项目聊天「查找 Anthropic 类似 GPT Workspace 的功能」
（`01a0ff79-e9d9-7661-ae02-1ef80bf8829e`）的历史命令输出读取它实际使用的
`/Users/kian/.codex/skills/llm-wiki/SKILL.md`；保存为
[技能快照](upstream/macbook-llm-wiki-skill-2026-10-04.md)，
[来源记录](upstream/macbook-llm-wiki-skill-2026-10-04.json)包含时间、路径和 SHA-256。
这是历史执行记录，不是实时远端文件读取；未核对远端当前提交，用户级技能也可能与
仓库 SKILL.md 不同。既有 `llm-wiki-agents-contract.md` 与工作流快照仍保留原版本。

可复用的结构是契约、技能入口、按需工作流、确定性工具、知识页与索引的分层：

| 层 | ai-knowledge 的职责与入口 |
|---|---|
| 共同契约 | AGENTS.md：存储、证据、发布、授权边界 |
| 任务分流 | SKILL.md：ingest、query、组合任务、日报与周报 |
| 入库工作流 | docs/workflows.md：读取、归档、查重、综合、审核发布、回查与续传 |
| 查询工作流 | prompts/query.md：检索、正文阅读、证据追溯、回答与缺口说明 |
| 工具 | ingest.py、query.py、get_page.py、grep_wiki.py；wiki_core.py 共用解析与发布规则 |
| 结构化记忆 | raw、reference、research、index.md、知识图谱及自动生成的 queries |
| 验证 | tests/run.sh，含临时目录中的 CLI 入库→查询→溯源及只读检查 |

`.agents/skills/ai-knowledge` 继续链接到项目根，避免另存一份失同步的技能。
同一 Agent 按用户意图选择流程，不需要常驻多 Agent 或新增外部服务。

补齐了上游示例中的纯过滤查询（无关键词时可按 type/domain/tag/confidence 浏览），
ingest 的 `--json` 同时支持放在子命令前后。没有全量复制上游命令选项。
历史 MacBook 技能仍包含置信度排序、固定刷新阈值等旧规则；本地沿用
evidence_kind 与 verification 独立、逐类型时效阈值和仅 published 默认可见的契约。
SQLite 多仓库路由、跨库发布和 Git hooks 仍不在本次范围内。
