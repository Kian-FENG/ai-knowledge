# AI 产业分析日报（2026.10.10）

统计窗口：2026-10-09T18:00:00-07:00 至 2026-10-10T18:00:00-07:00（洛杉矶时间，右端不含）。

实际生成时间：2026-10-10 18:12:14 PDT（America/Los_Angeles；UTC 2026-10-11 01:12:14）。

本期精选4个事件：模型分发增加试用入口，AI多肽融资提供研发线索，Agent治理强调模型之外的执行授权，服务器内存供给则仍处路线预期。未把媒体重发、仅日期未能归属本期的背景、厂商效率主张或未来量产写成当天已实现的变化。公司/作者披露为reported，产业判断为derived，未独立复现。

America/Los_Angeles当地前日18:00至当日18:00，右端不含；核对配置一致。本次采集实际开始2026-10-10 18:00:06 PDT；实际生成时间见下方及manifest。日期仅到日的午夜是工具解析占位，展示仅保留日期；来源日期沿用原Asia/Singapore解析配置，不伪造发布小时。

## 1. MaaS市场与产品形态

本期未收录经核验的新事件；覆盖情况见文末。

## 2. AI公司发展与新公司

### 利太智药近人民币5000万元种子轮：媒体披露 AI 多肽研发资金用途

- 财联社/科创板日报10月10日22:37（北京时间）报道，利太智药近日完成近人民币5000万元种子轮；投资方包括讯飞创投、L2F光源创业者基金及产业方。报道日期在窗口内，具体交割日未知；公司和投资方原始公告未取得。
- 报道将资金用途列为算力租用、管线研发、专利、人才和运营。金额是融资额，估值、收入与ARR未知；相对现有库，这是新增的AI多肽研发融资线索。
- HIT-to-lead管线及2027年初候选化合物属于报道转述的进展/计划，不证明临床有效、获批药物或商业收入；未采用亲和力和闭环速度为实测结果。

**产业判断：** 融资若落实，可把算力与湿实验验证连接起来，云算力和实验服务有潜在需求；研发价值仍取决于可复核的候选与后续实验，资本投入不能替代成药性。反例是数据/实验不泛化导致管线停滞。观察投资方公告、具名候选、实验协议和分阶段验证，不用融资额排名技术能力。

**来源与核验范围：**
- [财联社正文（东方财富转载） · 利太智药完成近5000万元种子轮融资 讯飞创投出手](https://finance.eastmoney.com/a/202610103892000121.html)；发布时间：2026-10-10T22:37:00+08:00；定位：完整转载主文的融资、用途、HIT-to-lead与2027计划段；已读正文后有限摘录，原发财联社与一手公告缺失。；阅读范围：full-text；ID：`b0fa1e8be714fdff1fb1`。

## 3. 模型能力与技术演进

### Nous 公告 MISSINGNO 限时免费入口，能力与正式可用范围仍待核实

- Nous官网10月10日公告将MISSINGNO描述为编码与Agent推理模型，宣布可限时免费通过Nous Portal搭配Hermes Agent使用。日期只有日精度，未标时区，窗口边界不确定；前期日报没有此事件。
- 新增变化是模型分发入口声明；“token efficient”仍为厂商主张，缺模型卡、评测任务/harness/预算、开发主体、权重许可和免费结束时间。
- 原X公告获取失败；公开Portal概览未显示MISSINGNO名称，未登录测试或发起推理，无法确认账号/地区范围及实际服务可用性。

**产业判断：** 限时免费可降低开放harness用户尝试另一模型的门槛，分发渠道可能通过跨模型选择争取使用量；持久成本优势要看质量相当的完整任务token与后续收费。反例是免费结束、资格限制或失败重试抵消单次token节省。观察模型卡、正式端点、完整任务成功率和账单。

**来源与核验范围：**
- [Nous Research Official · Nous announces limited-time MISSINGNO access on Portal](https://nousresearch.com/)；发布日期：2026-10-10（仅日期；解析占位不是发布时刻）；定位：官方首页Announcements Oct10 MISSINGNO条目；有限事实摘录，非HTTP全文；另读公开Portal概览。；阅读范围：full-text；ID：`0304daca2f1d8fb29989`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### 纳德拉提出 Agent 外部控制原则：权限、审计与人为中止独立于模型

- 已读纳德拉10月10日完整公开文章，主张将模型、编排harness和动作空间分开，权限执行与保障机制放在模型之外；重要动作应留可审计证据，授权人能在任务中途暂停或关闭。
- 相对现有库的缓存/任务预算研究，新增的是执行授权和独立审计的工程要求。文章也指出CoT透明本身不能保证输出忠实；它是建议，不是微软产品上线、统一标准或安全评测成绩。
- 网页显示7:43但未标时区，归档仅保留10月10日日期，窗口边界不确定；web403后原生浏览器已恢复全文。

**产业判断：** 这将企业采用的瓶颈从模型回答延伸到权限覆盖、审计和运行时停止，身份、工具网关及观测服务可能受益。但声明不证明所有子进程/远程工具都能被中止，额外模型审查也可能复制同一盲点。观察独立策略执行、故障注入和停止后的残余动作，不能把治理理念算为已实现的生产安全。

**来源与核验范围：**
- [Satya Nadella Public Article · Models as Insider Risks in the Super Intelligence Era](https://x.com/satyanadella/status/2108931348857827686)；发布日期：2026-10-10（仅日期；解析占位不是发布时刻）；定位：公开X Article的模型/harness/action-space分离段、7项principles及CoT限制；完整主文已读，归档有限摘录。；阅读范围：full-text；ID：`eeeced9a0bbd73898899`。
  日期仅精确到天，无法确认 18:00 边界。

## 5. 模型与AI Infra论文

本期未收录经核验的新事件；覆盖情况见文末。

## 6. GPU与供应链

### 长鑫 DDR5 RDIMM 年底计划获媒体披露，服务器供给变化尚待交付

- IT之家10月10日完整RSS正文转述长鑫总裁演讲：4F² DRAM及混合键合研发取得进展，预计2026年底推出结合相关技术的DDR5 RDIMM。相对库中已有GPU/FD-SOI路线，新增服务器内存路线线索。
- 本期采用的是媒体披露的未来计划，演讲确切日期、一手讲稿、模块规格、量产和服务器认证未核实；不能表述成已出货、HBM供给增加或已降价。

**产业判断：** 若通过服务器验证并规模交付，可能增加系统内存采购选择，影响CPU/Agent宿主侧的容量与成本；DDR5路线不直接解决GPU HBM瓶颈。反例是良率、兼容性或交付延期限制采用。观察容量/频率、OEM认证、实物出货和可采购价格，暂不估算成本降幅。

**来源与核验范围：**
- [IT之家 · 长鑫技术新突破，融合 4F² 架构等先进技术的 DDR5 RDIMM 产品预计年底亮相](https://www.ithome.com/1/011/494.htm)；发布时间：2026-10-10T11:25:20+00:00；定位：原始RSS完整item：总裁演讲、年底计划及规格未公布段；网页获取失败，一手讲稿未取得。；阅读范围：feed-content；ID：`c88cfc2141319fa4253e`。

## 本次知识入库

新建11页（8 source、2 company entity、1 synthesis note），更新Nous公司页1页；12页均已审核发布、默认query命中目标ID、get_page --follow-sources可见且raw hash一致。

Stacklok和Peppermint为新增跟踪的既有公司；Composer预测与Decision-1为10月9日背景，Peppermint融资为10月8日背景，均不计本期事件。利太智药公司一手身份未核实，暂只发布带归因来源页。

- [[reference/sources/codex-composer-predictions-20261009|Codex 输入框预测进入 beta：下一条提示仍由用户提交]]
- [[reference/sources/nous-missingno-portal-20261010|Nous 宣布 MISSINGNO 编码模型限时免费入口]]
- [[reference/sources/ligit-seed-media-20261010|财联社报道利太智药近人民币5000万元种子轮]]
- [[reference/sources/stacklok-agent-architecture-20261010|Stacklok 身份与 ToolHive/Mecatl 架构：新增跟踪背景]]
- [[reference/sources/peppermint-seed-20261008|Peppermint 临床试验账单产品与 USD470万种子轮背景]]
- [[reference/sources/microsoft-decision-1-20261009|Microsoft Decision-1 将预定义选项评分做成低价 API]]
- [[reference/sources/nadella-agent-containment-20261010|纳德拉建议将 Agent 权限和审计控制置于模型之外]]
- [[reference/sources/cxmt-4f-rdimm-plan-20261010|媒体披露长鑫 4F² DDR5 RDIMM 年底计划，尚非量产供给]]
- [[reference/entities/stacklok|Stacklok：MCP 治理与云原生 Agent 执行平台]]
- [[reference/entities/peppermint|Peppermint：AI 与人工结合的临床试验账单平台]]
- [[reference/entities/nous-research|Nous Research：Hermes Agent与开放模型研究]]
- [[research/synthesis/agent-decisions-and-authority-20261010|Agent 决策 API 与执行权限开始分层，低价评分不能替代独立控制]]

去重跳过：既存Anthropic事故回顾、Qwen图像模型、Dynamo开发快照、TypeSafe/Namespace等融资；腾讯元器和Vidu的媒体重发亦不当本期首发。未完成核验与覆盖缺口见[pending-evidence.md](pending-evidence.md)。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 189 条（其中线索 26 条），精选 4 个事件；未注明日期 2 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Stacklok Official：checked；官方公司页和首页实际读取，核对创始人与ToolHive/Mecatl归属并新增跟踪；unknown publication date只作背景。USD17.5M融资线索为2023年旧事。；已知截断 0 条。
- Peppermint Official：checked；官方融资全文已读：Oct8 USD4.7M种子轮及AI+human billers，明确窗口外背景新增跟踪；排除同名成人俱乐部。；已知截断 0 条。
- Microsoft Command Line：checked；官方完整正文/附录已读，Oct9日期与更新时刻未知，当前Foundry/OpenRouter入口与价格仅作背景；检索缓存和当前runner-up/可用性不同，保留版本边界。；已知截断 0 条。
- Satya Nadella Public Article：checked；原X文章web403后，原生浏览器成功读完整主文；日期Oct10，7:43未标时区，按日精度；工程原则而非产品交付。；已知截断 0 条。
- Nous Research Official：checked；实际读官网Oct10 MISSINGNO公告并归档有限摘录；原X公告读取失败，公开Portal目录未显示名称，未测试账号/推理，实际资格和期限未知。Oct9 Step5线索仍待模型卡。；已知截断 0 条。
- Healthleap Official：checked；官方首页产品及既存USD38M融资说明已读，与前期重复；未审临床效果或新客户。；已知截断 0 条。
- OpenAI News：checked；实际读取news列表、帮助中心10月9日Composer预测详情和release-note日期；输入框预测仅作背景入库，源站缺小时/时区，未把采集时间作发布。news列表本入口未见10月10日新条目；不代表所有渠道无新闻。；已知截断 0 条。
- OpenAI API Changelog：checked；原始HTTP正文与变化行已读；本次差异为导航顺序/栏目，不当API功能发布。；已知截断 0 条。
- Anthropic Newsroom：checked；官网news索引已读，最新10月7/8日公告为前期；未发现本入口合格新增。；已知截断 0 条。
- Anthropic Research：checked；官网research索引已读；10月9日unintended actions与前期重复，已回读前期来源及raw暂停联网段。；已知截断 0 条。
- Anthropic 站点地图：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- DeepSeek Research & News：checked；实际读取官网新闻与API更新列表，最新可见V4.1 Flash为9月10日；HF列表亦自动核查，无新链接。媒体harness/Bug主张未回查到完整研究，保留候选。；已知截断 0 条。
- DeepSeek API Change Log：checked；官网更新列表已读且HTTP正文未变；未见本入口新增。；已知截断 0 条。
- DeepSeek 模型与价格：checked；本次官方HTTP快照采集成功、正文未变；web工具失败仍保留HTTP结果，未实测账单。；已知截断 0 条。
- DeepSeek · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Alibaba / Qwen Blog：failed；web返回零正文，原生浏览器博客也只读到导航，未取得文章列表；HF列表成功且无新链接，只覆盖部分渠道，不能称Qwen没有新闻。；已知截断 0 条。
- Qwen · Hugging Face：checked；本期官方HF列表无新链接；前期Qwen-Image2.1-Turbo原API/raw回读，revision日期仍10月9日，LICENSE缺口未解决。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；官方英文blog列表实际读到，最新可见K3/PerceptionBench为7月背景；HF入口亦检查，未见本入口合格新增。；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Z.ai 发布记录：checked；原HTTP变化正文实际读，移除旧条目且保留最新8月26日；属于文档整理，无当前模型首发证据。；已知截断 0 条。
- 智谱开放平台发布记录：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 智谱 · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- MiniMax News：checked；web只返回导航后，用原生浏览器成功读dated news列表，最新可见8月26日财报和8月3日H3；M3/H3页标不构成当前发布日期。；已知截断 0 条。
- MiniMax · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Mistral AI：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Meta Newsroom：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- AI at Meta Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Google DeepMind：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Google AI Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Google Cloud Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Tencent Newsroom：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Tencent · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- ByteDance Seed Blog：checked；官方research列表实际阅读，部分入口无日期；已知7月文章为背景；HF列表自动检查。未定时的Seed-Realtime不作本期新闻。；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Alibaba Cloud Press Room：checked；web未给新闻正文，原生浏览器恢复正式press-room列表，最新可见9月23日；导航中的Qwen-Image3.0名称无日期，不列新品。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- xAI News：checked；官方news列表已读，最新可见9月28日TeamBots，未核实本入口新增。；已知截断 0 条。
- NVIDIA Newsroom：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- NVIDIA Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- AMD Press Releases：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- About Amazon：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Qualcomm Newsroom：checked；web正文不足后，原生浏览器成功读取dated release列表，最新10月4日华为许可协议；未见本入口10月10日新公告。；已知截断 0 条。
- Samsung Newsroom：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- SK hynix Newsroom：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- ASML News：checked；官方页面跳转投资者news，实际读取列表，最新可见9月8日；涨价媒体主张未取得一手支持，不列确认事实。；已知截断 0 条。
- TSMC Newsroom：checked；官方新闻列表已读，最新月度收入10月8日是已入库背景；未推导AI产能或分业务收入。；已知截断 0 条。
- Volantis（公司新闻稿）：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Reflection AI Blog：checked；官方blog已读，Beam既存背景；NVIDIA交易谈判只有媒体线索，本期不写已收购或已融资。；已知截断 0 条。
- Namespace Blog：checked；官方blog列表已读，最新Oct5 USD42M Series B为前期重复。；已知截断 0 条。
- Vinci Official Blog：checked；官方blog融资入口已读，Oct6 USD250M Series B为既存背景，无本期合格增量。；已知截断 0 条。
- TODAY Official Blog：failed；配置的官网blog路径web获取失败，原生浏览器返回404；不称公司无动态。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；官网blog及Jev归属入口已读，USD870M/7.5B既存融资为前期重复；未解客户占比口径冲突。；已知截断 0 条。
- GlobalFoundries Official News：checked；官方newsroom列表已读，Oct9 FD-SOI路线已存；Oct8中介层协议为周报背景，Dresden条目无经读本期交集证据未收录。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方GitHub release列表实际核查，最新v0.5.21日期Oct2；没有把PR合并或列表检索当正式新发布。；已知截断 0 条。
- SGLang Blog：checked；打开官方blog只取得短入口页，未读文章全文；未宣称本期没有技术文章。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；官方release列表实际核查，v0.31.0是已存发布；未执行部署或性能实验。；已知截断 0 条。
- vLLM Blog：checked；本次原HTTP正文列表已读，新发现Rubin preview文章仅标Oct9；未读完整11分钟正文、图表/harness，不采用7.8x或供应可用性结论；留后续背景。；已知截断 0 条。
- NVIDIA Dynamo：checked；官方release列表实际核查，最新MiniMax M3 dev.1为Oct9T20:54Z，前期已收录；不是生产版，本期去重。；已知截断 0 条。
- FlashInfer：checked；正式release列表与v0.7.0 highlights实际读；v0.7.1已于前期收录。RSS v0.7.0时间与GitHub页面9月22日发布日期不同，版本旧、发布时间冲突，留待核验，不当本期新发布/能力排名。；已知截断 0 条。
- Mooncake：checked；官方release列表已读，最新v0.3.14rc1为9月7日，稳定0.3.13post1为8月31日；未将rc等同稳定生产发布。；已知截断 0 条。
- NVIDIA Technical Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- PyTorch Foundation Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；本次官方RSS返回0条；另按Oct10/模型/Agent/推理与GPU-serving执行一手论文发现检索，没有确认本窗口新公告。聚合器的Oct10日报不能作论文日期，媒体cues论文投稿日10月5日属背景。未覆盖全部分类/更新版本，不等同本期无论文。；已知截断 0 条。
- METR：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- UK AI Security Institute Blog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Artificial Analysis Articles：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Artificial Analysis Changelog：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- SemiAnalysis：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- NIST News：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- US BIS News & Updates：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 工业和信息化部：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 最高人民法院：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 外交部例行记者会：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 中国政府网 政策：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 重庆市大数据应用发展管理局：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 国家数据局：checked；web零正文后原生浏览器从官方根页成功恢复；业务频道最新可见10月9日数据要素赛事通知，非本期AI产业增量。错误子路径404已排除，不代表整个站点失败。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；原生浏览器完整阅读财联社转载的利太智药融资正文和发布时间；公司/投资方一手公告未找到，融资交割日未知，不建立公司entity。；已知截断 0 条。
- TechCrunch AI：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- The Decoder：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- The Verge AI：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- The Information：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Bloomberg Technology：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Financial Times Technology：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Financial Times AI：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- New York Times Technology：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- SCMP Tech：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- MIT Technology Review：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Ars Technica AI：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- Tom's Hardware：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 量子位：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 虎嗅：failed；HTTP RSS读取超时；同站浏览器兜底首页导航超时，未取得正文；本次停止重试，不以故障代替无新闻。；已知截断 0 条。
- IT之家：checked；完整RSS精选阅读：长鑫DDR5 RDIMM为未来计划转述；腾讯元器媒体日期Oct10但公告Oct8，Vidu媒体Oct10但官方分发新闻Oct7，均不作本期发布。原网页获取失败；媒体条数上限和漏采窗口保留。；已知截断 0 条；可能漏采 2026-10-10T01:03 至 2026-10-10T01:28。
- 36氪：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 钛媒体：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条；可能漏采 2026-10-10T01:03 至 2026-10-10T17:57。
- 雷峰网：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条；可能漏采 2026-10-10T01:03 至 2026-10-10T09:38。
- 极客公园：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 智东西：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- C114 通信网：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 快科技（驱动之家）：checked；自动采集已检查此入口；列表/候选不代表逐篇阅读全文，未精选者未作事实支持；上限、unknown_date、needs_fulltext与缺口见证据包。；已知截断 0 条。
- 机器之心：failed；实际打开仅得到服务导航/数据服务页，没有本期文章正文；公众号内容未检索全覆盖。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；自动river新链接仅作为线索；Oct9/Oct10 h2355快照通过web工具访问失败，未恢复媒体漏采窗口。旧聚合条目未重复收录，未声称覆盖完整。；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- bloomberg-ai：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- ft-nyt-wsj-ai：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- china-ai-companies-zh：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- china-ai-policy-zh：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- china-chips-zh：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- embodied-world-models-zh：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- supply-chain-en：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。
- newsroom-fallback：checked；按本期Oct10或after:Oct9/before:Oct11日期条件执行中英文/域名检索；摘要仅作线索。检索无可采用结果不代表渠道无事件，未完整阅读所有命中；实际采用与未完成项见pending-evidence.md。。

- 新公司发现：checked；已执行英文AI startup融资及中文AI新公司/融资检索，回读Stacklok、Peppermint官网，作为既有公司背景新增跟踪；利太智药媒体披露的一手身份未验证，Hone等融资线索仍待官方证据。。

证据包：`data/packets/daily/2026/10/2026-10-10/bd0171389f219fb7e40b84575d64bac1d21de4ffb45cb110f3ba022f4b7a0ed8.json`；采集 run：`20261011T010006-7fc95a81`。
