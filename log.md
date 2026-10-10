# Activity log

## 2026-10-01 — 初始化

参考远端 LLM-Wiki、AI-News 和用户日报样例建立本地 Agent 与每日流程。
未将样例新闻或配置视为已验证知识。

## 2026-10-02 — 首次在线验证

完成首份试运行日报，选6个事件；归档368条机器候选并补读官方原文，首次入库6个来源/论文页与Volantis实体。arXiv公告日与投稿日分离；论文仅摘要级核验。直接HTTP受限的OpenAI文章用网页读取并保留阅读笔记，未伪造全文快照。

## 2026-10-02 — 信息渠道修复

按渠道审计与逐条在线核查修复来源：智谱改为发布记录页，DeepSeek 增加 Change Log、价格页与 Hugging Face，Anthropic 增加 Research 与站点地图，Meta 改为 Newsroom，Qwen/MiniMax 等 JS 或拦截页标记为浏览器核查。新增一手、政府、研究、中英文媒体与 Techmeme 聚合来源，共 94 个（93 个启用）。采集器支持按来源轮询间隔、漏采窗口、网页新链接与页面变化线索、关键词过滤和 robots.txt。Google News RSS 回测效果好但 robots.txt 禁止，改为 Agent 检索清单。首次全量采集 42 ok、38 建立快照、10 需浏览器、3 失败（2 项已修）。未改动已发布知识页。首次采集时 feed 扫描覆盖了 4 条已导入证据（原保护只认 full-text），已修复并从 article-history 恢复。详见 docs/source-remediation-2026-10-02.md。

## 2026-10-04 — 日报截止时间调整

按用户要求将日报改为新加坡时间（Asia/Singapore）每天 06:00 截止，窗口为前一天 06:00 至当天 06:00；周报保留周六 08:00。同步配置、Agent 流程与报告时间标注；历史报告和原始证据保持原窗口。本机未找到已保存的 Codex 自动化配置，实际触发状态尚未确认，定时计划文档已注明。

## 2026-10-04 — 日报与周报改用洛杉矶时间

按最新要求将日报改为洛杉矶时间每天 18:00、周报改为洛杉矶时间每周五 18:00 截止并执行。
两者使用 America/Los_Angeles，按当地日期归档并自动切换夏令时；来源未标注时区的日期仍沿用原配置，历史报告与证据不重写。
新计划首期周报为 2026-10-09，覆盖当地 2026-10-02 18:00 至 2026-10-09 18:00。
46 项离线测试与配置、知识库校验通过，覆盖 23/25 小时日报、167/169 小时周报、窗口衔接与筛选边界。
本机仍未找到已保存的 Codex 自动化配置，此次只更新本地配置和执行流程，实际自动触发尚未确认。

## 2026-10-04 — Ingest 与 Query 的统一 Agent 入口

对照 MacBook-LLM-Wiki 项目历史执行记录中的用户级技能与本地已有契约快照，
在 SKILL.md 和 AGENTS.md 明确 ingest、query、组合任务与报告分流；入库补充
来源版本查重、批次续传、审核发布后的默认检索回查，查询工作流独立放在 prompts/query.md。
保留证据类型与核验分离的现有规则；参考快照及来源/hash 存于 docs/upstream/，
未声称核对了远端当前文件或提交。

query 支持仅按领域/类型/标签/兼容置信度过滤；ingest 的 JSON 标志支持子命令前后。
新增 3 项隔离 CLI 工作流测试，验证归档→审核发布→查询→来源追溯、草稿隔离和查询只读。
全量 49 项离线测试、7 页知识库校验、6 种索引生成、来源配置与技能校验通过；
真实库内公司页可通过纯过滤检索并解析来源关系。测试材料未写入正式知识库。
本次未新增真实知识条目，未提交或推送。

## 2026-10-04 — AI产业日报自动运行（洛杉矶日期）

实际开始2026-10-05 03:09:41 UTC（洛杉矶10月4日20:09:41），补最近到期窗口：10月3日18:00至10月4日18:00 America/Los_Angeles，右端不含。配置核对一致。93个启用来源：75成功、10需浏览器、8获取失败；通过可用网页/浏览器补查，动态空正文、中文feed失败、付费全文与公众号等缺口如实保存。67候选筛选后收录1个媒体归因事件。周报首期10月9日未到期。

新增并审核发布5页：美国AI协调机构媒体披露；Gemini个人模型访问安排（发布日期未知）；RRSI v2摘要与README（9月背景）；Halluminate官方融资来源与公司实体（10月1日背景）。所有页面回查，reported与source-checked不等于独立复现。新增Halluminate跟踪；未更新已有知识页。NASA/IBM、Vertiv–KES、漏洞赏金暂停等旧事件排除，未冒充本期。日报、编辑JSON、两版packet、修订、run及research-audit保留。

用户本次明确授权提交并普通推送origin/main，优先于旧文档的本地保存限制。开始时HEAD为23c4770，已有788个改动/未跟踪路径，保存基线并在提交中排除既有无关内容；Git结果另记于本期sync-state及自动化memory，避免以日志提交自己的hash。

## 2026-10-06 UTC / 日报窗口2026-10-05

新增13个知识页（8个source、2个paper、2个entity、1个note），更新0页。原始版本与hash保留，全部审核发布并经默认query→get_page→raw哈希回查。新增跟踪Namespace与Reflection，修复Seed Research浏览器入口。阶段综述、预览/计划与正式版本分开；论文仅摘要，不采用性能排名。页面入口见 [[research/KNOWLEDGE-GRAPH|知识图谱]]；候选跳过和覆盖缺口见 reports/daily/2026/10/2026-10-05/research-audit.json。本次授权提交/推送，结果将写sync-state.json。

### 2026-10-07 UTC / 洛杉矶2026-10-06日报入库批次

新起草14页：10 source、2 paper、1 entity、1 note。相对前期新增企业上下文/访问分层/数学验证制品、Mistral预览、EmbeddingGemma多模态检索、AICR稳定契约及Vinci融资；论文仅所读章节，不采用摘要加速/成本数字。导航已连接，待审核发布回查；旧raw版本保留。重复背景Beam、Namespace、vLLM v0.31.0未重建页。

2026-10-07 UTC批次完成：补读API changelog和Decisions/usage tier文档后最终发布15页（11source、2paper、1entity、1note），新增Vinci跟踪；默认检索可见与原始hash/证据链回查通过。40页校验、97来源配置及49项离线测试通过；日报14事件，date-only展示已修正并保留原生成版本。

## 2026-10-08T01:20:19.743998+00:00 — 2026-10-07日报与知识入库

完成洛杉矶前一日18:00至当日18:00窗口，精选12事件；新建并审核发布14页（9来源/2论文/2公司/1综合），更新0；默认标题query→get_page回查14页及raw hash均通过。去重Vinci/Namespace/Reflection、旧学习功能；未核实融资/模型卡/论文全文保留候选。54页结构校验与49离线测试通过，source-checked仅有限陈述核对，不作独立复现。报告/证据/覆盖详见reports/daily/2026/10/2026-10-07。

## 2026-10-09T01:11:43.480038+00:00 — 2026-10-08 日报知识批次

起草以下有增量且可追溯页面；公司/维护者为reported、综合为derived，source-checked仅有限来源支持关系。

- [[reference/sources/google-gemini-work-agent-20261008|Google 发布 Gemini 工作 Agent：云端持续执行、任务身份与项目预算结合]]
- [[reference/sources/legalon-codex-budget-routing-20261008|LegalOn 案例把模型分工与预算管理同时纳入编码 Agent 采用]]
- [[reference/sources/codex-faster-steering-20261008|Codex 桌面端开始推送更快的任务中途引导]]
- [[reference/sources/anthropic-usage-policy-20261008|Anthropic 公布使用政策修订，11月12日才生效]]
- [[reference/sources/anthropic-cyber-mission-20261008|Anthropic 扩展关键基础设施防御，并推出自愿加入的开源扫描服务]]
- [[reference/sources/today-seed-20261008|新增公司 TODAY：为金融保险顾问工作流融资 EUR 280万]]
- [[reference/sources/anthropic-genesis-commitment-20261008|Anthropic 承诺三年提供 USD 1.5亿科研资源]]
- [[reference/sources/openai-sol-ultrafast-20261008|GPT-6.1 Sol 新增 Ultrafast：以更高单价购买低延迟服务]]
- [[reference/sources/dynamo-session-aware-20261008|Dynamo 按 Agent 会话管理缓存和准入，部分接口仍是提案]]
- [[reference/sources/pytorch-spyre-native-device-20261008|IBM 说明 Spyre 原生 PyTorch 设备集成及其运行时边界]]
- [[reference/sources/dynamo-kimi-k3-snapshot-20261008|Dynamo 发布 Kimi-K3 实验快照，明确不适合生产]]
- [[reference/papers/vllm-omni-2610-09307|vLLM-Omni 技术报告：把多模态生成组织为多阶段运行时]]
- [[reference/papers/comoe-2610-09424|CoMoE：为缺少 GPU P2P 的普通多卡系统设计 MoE 数据路径]]
- [[reference/sources/nvidia-science-commitment-20261008|NVIDIA 承诺五年投入价值 USD 10亿的美国科研支持]]
- [[reference/sources/tsmc-september-revenue-20261008|台积电9月合并营收同比增54.6%，不能直接推导 AI 产能]]
- [[reference/entities/today|TODAY：金融保险顾问的工作流 Agent]]
- [[research/synthesis/persistent-agents-session-budget-20261008|持续Agent的竞争开始连接身份、会话缓存与任务预算]]

- 2026-10-08批次发布与回查完成：17新页；默认标题检索可见、raw证据hash一致。

## 2026-10-10T01:14:19.146664+00:00 — 2026-10-09 日报及到期周报

新建9 source、2 paper、1 entity；更新既有持续Agent综合1页。原文/限定浏览摘录已归档；新公司TypeSafe身份与产品归属核对，采用口径冲突保留。GF中介层为10月8日补充周报；Dynamo v1.5.0旧发布说明更新时间去重。论文只读摘要，不收录未对齐提速/评分。等待审核发布与默认回查。

- 完成审核发布与13页默认回查，83页结构校验及49测试通过；日报/周报日期及口径审阅完成。TypeSafe事件日来自已读投资方公告，论文RSS日期证据补充，未升measured/replicated。准备按运行基线选择性提交并普通推送origin/main。
