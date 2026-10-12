# AI 产业分析日报（2026.10.11）

实际生成时间：2026-10-11T18:16:59.523667-07:00（America/Los_Angeles）。

统计窗口：2026-10-10T18:00:00-07:00 至 2026-10-11T18:00:00-07:00（洛杉矶时间，右端不含）。

本期精选2件变化：GPT-6.1 Sol默认工作集扩大的媒体披露，以及Amazon洽谈Decart潜在交易。前者须分开订阅扣量与API计价，后者尚未确认成交；持续Agent与实时模型的价值仍要看可交付能力和完整任务成本。Odyssey-3、Vals多Agent成本评测和Epoch InnovationEval在本期补充入库，但发布日期为10月8/9/7日，不计本期首发。106个既有启用入口已采集，23个需浏览入口逐项核查；存在媒体漏采、Qwen/机器之心正文不足、TODAY入口404和Techmeme快照失败，不能把未精选等同全行业没有新闻。

## 1. MaaS市场与产品形态

### 媒体报道：GPT-6.1 Sol默认上下文扩至500k，订阅扣量另作调整

- IT之家归因于OpenAI的Thibault Sottiaux称，Codex与Work的GPT-6.1 Sol默认上下文从272k提升至500k、约增加80%；最大1M且仍可手动设置。网页与RSS发布时间为北京时间10月12日08:23:08，即洛杉矶10月11日17:23:08，落本窗口；原公告具体事件时刻未取得。
- 相对已存Ultrafast服务和输入框预测，新信息是会话默认工作集和订阅使用量政策。媒体称从订阅中扣量时不收长上下文费用；未核实API、购买credits、全部套餐/地区资格，也未测试账户，不延伸为API长上下文免费。
- 已读完整RSS正文和浏览器网页主文，但嵌入社交帖未恢复，尚未读原公告或看到本期正式release note确认；保留reported媒体归因，未独立验证实际交付/效果。

**产业判断：** 判断（derived）：更大默认工作集可能减少压缩、降低长任务重新取上下文的协调开销，持续编码/办公Agent和会话缓存服务可能受益；若长上下文质量下降、工具等待或重试主导，容量增加未必改善交付。订阅扣量变化可改变用户尝试长任务的意愿，却不能推出提供商实际推理成本下降；观察原公告/资格、压缩次数、正确完成任务率、尾延迟和订阅/API各自完整账单。

**来源与核验范围：**
- [IT之家 · OpenAI 宣布 GPT-6.1 Sol 默认上下文长度从 272k 提升至 500k，增加约 80%](https://www.ithome.com/1/011/736.htm)；发布时间：2026-10-12T00:23:08+00:00；定位：完整RSS text＋网页主文上下文/手动设置/订阅扣量段及发布时间；原社交帖未读。；阅读范围：feed-content；ID：`ccc97f1cd80e4239d292`。

## 2. AI公司发展与新公司

### Reuters转述WSJ：亚马逊洽谈约70亿美元收购Decart，交易尚未确认

- CNA所载Reuters于10月11日转述WSJ知情人士称，Amazon正在洽谈收购Decart，潜在交易约USD7 billion。Reuters未能立即独立核实，双方未回应；谈判可能失败或出现另一买家，不能记为已完成收购。
- Reuters正文只有Oct11日期、时区/精确发布时间未知，窗口边界不确定；Bloomberg RSS同一WSJ报道时间为10月11日20:46:52 UTC（洛杉矶13:46:52），落本窗口，前一期未收录。多家转述同一WSJ消息不构成独立确认；未读WSJ或Bloomberg付费全文。
- 相对库内已有芯片供给/Agent应用研究，增量是潜在整合交易进入跟踪。USD7B为谈判中的可能交易金额，非确认估值、融资、收入或ARR。另读Decart官网核对DOS、Lucy、Oasis归属与公司兼容主张；官网日期未知，只作产品背景，未取得官方收购确认。

**产业判断：** 判断（derived）：若交易签署，云平台可能同时获得优化栈与实时视频/交互模型资产，影响跨芯片工具中立性和低延迟模型分发；这是基于产品组合的推断，买方动机尚无确认。独立软件与其他云客户可能承压，也可能在保持开放后受益；谈判破裂或整合困难会削弱该机制。观察双方正式公告、签署/审批、IP和人才归属、DOS跨芯片支持、API价格与原客户续用，而不是用报道金额推算业务收入。

**来源与核验范围：**
- [Reuters转述WSJ · Reuters转述WSJ：Amazon洽谈约USD7B收购Decart，尚未达成](https://www.channelnewsasia.com/business/amazon-in-talks-buy-ai-startup-decart-around-7-billion-wsj-reports-6451486)；发布时间：2026-10-11（仅日期，来源时区未标明；内部日期解析沿用Asia/Singapore）；定位：CNA所载Reuters完整短文303–323：金额/谈判/无法核实/未回应/可能失败；正文只有日期。；阅读范围：full-text；ID：`15409fd519ad5a7bf4e6`。
  日期仅精确到天，无法确认 18:00 边界。
- [Bloomberg Technology · Amazon Is in Talks to Buy AI Startup Decart, WSJ Reports](https://www.bloomberg.com/news/articles/2026-10-11/amazon-is-in-talks-to-buy-ai-startup-decart-wsj-reports)；发布时间：2026-10-11T20:46:52+00:00；定位：仅RSS摘要一句及pubDate，支持同一WSJ谈判归因/金额及报道时间；非付费全文。；阅读范围：feed-content；ID：`64d4ebe3e21c361f4d73`。

## 3. 模型能力与技术演进

本期未收录经核验的新事件；覆盖情况见文末。

## 4. AI Infra社区与工程趋势

本期未收录经核验的新事件；覆盖情况见文末。

## 5. 模型与AI Infra论文

本期未收录经核验的新事件；覆盖情况见文末。

## 6. GPU与供应链

本期未收录经核验的新事件；覆盖情况见文末。

## 本次知识入库与待证

新建6个来源页、2个公司实体，更新1个既有研究页；9页已完成审核发布、默认query/get_page回查与raw hash核对。Odyssey-3、Vals和Epoch分别是10月8/9/7日背景；不是本期首发。

- [[reference/entities/decart|Decart：DOS、Lucy与Oasis，谈判未确认]]
- [[reference/entities/odyssey|Odyssey与Odyssey-3研究预览]]
- [[reference/sources/vals-multi-agent-cost-20261009|Vals：多Agent成本与评测局限]]
- [[reference/sources/epoch-innovationeval-20261007|Epoch：规则约束下的研究改进]]
- [[research/synthesis/persistent-agents-session-budget-20261008|持续Agent任务预算研究更新]]

原公告、交易确认、新公司缺证线索及未覆盖范围详见同目录pending-evidence.json和research-audit.json。媒体与公司所述为reported，综合判断为derived；未标measured/replicated。

采集实际为82个ok、23个needs-browser、1个failed，单源保存上限60，lookback14天；本次采集已知truncated/unknown_date/future_date均为0，正文待读候选仍存在。物理feed/listing本身上限不保证全窗口；报告132候选包含18线索，3个未定日期材料排除。四个媒体本期漏采段及历史未补齐记录见证据包；Techmeme Oct10快照失败，未补全缺口。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 132 条（其中线索 18 条），精选 2 个事件；未注明日期 3 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Stacklok Official：checked；官方Company实际读，2023团队/融资为背景，未核实本期新事件。；已知截断 0 条。
- Peppermint Official：checked；官方种子轮正文实际读，Oct8背景已在前一期核对，不重复计本期融资。；已知截断 0 条。
- Microsoft Command Line：checked；实际阅读配置中的Microsoft Command Line正文，Oct9旧公告；更新benchmark文字时刻未知，不作本期再发布。；已知截断 0 条。
- Satya Nadella Public Article：checked；原生浏览器恢复完整公开文章，显示Oct10、7:43但时区未标；已存同文去重，非产品交付。；已知截断 0 条。
- Nous Research Official：checked；实际读官网公告列表，Oct11 Hermes Agent is yours仅短标题，未取得实质交付增量；Oct10 MISSINGNO已有，未再计新闻。；已知截断 0 条。
- Healthleap Official：checked；官网实际读取，USD38M旧背景/未定日期；未取得本期新增公告。；已知截断 0 条。
- OpenAI News：checked；已读官方News、帮助release notes与API changelog；最新相关Oct8 Ultrafast、Oct9输入框预测属已存背景。GPT6.1默认500k仅取得IT之家媒体归因，未取得原社交公告，未测试账户/费用。；已知截断 0 条。
- OpenAI API Changelog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Anthropic Newsroom：checked；实际打开官方news/research列表；可见Oct8新闻及Oct9已有unintended-actions研究；媒体重新转述不是再次发生。本期未逐篇审计内部日志。；已知截断 0 条。
- Anthropic Research：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Anthropic 站点地图：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- DeepSeek Research & News：checked；官方API changelog实际读，最新Sep10 V4.1 Flash；模型card/harness遗留待证不因采集改变。；已知截断 0 条。
- DeepSeek API Change Log：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- DeepSeek 模型与价格：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- DeepSeek · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Alibaba / Qwen Blog：failed；官方博客web无正文，原生浏览器仅导航而无文章列表，未恢复本期动态；HF列表检查不等价完整博客覆盖。Qwen属于阿里。；已知截断 0 条。
- Qwen · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；官方blog实际读，最新可见July16 K3；HF列表检查。媒体K3.1/K4参数或计划没有官方版本卡支持，不写正式发布。Kimi属于月之暗面。；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Z.ai 发布记录：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 智谱开放平台发布记录：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 智谱 · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- MiniMax News：checked；web导航不足后原生浏览器恢复列表；可见H3/Aug3、财报Aug26等旧项，未确认M3正式可用及模型卡。；已知截断 0 条。
- MiniMax · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Mistral AI：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Meta Newsroom：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- AI at Meta Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Google DeepMind：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Google AI Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Google Cloud Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Tencent Newsroom：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Tencent · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- ByteDance Seed Blog：checked；官方research列表实际读，最新可见July旧项；Seed-Realtime日期未知，不列当期首发。；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Alibaba Cloud Press Room：checked；原生浏览器恢复Press Room列表，最新可见Sep23；导航产品名称不能作新版本/开源许可公告。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- xAI News：checked；实际打开官方news列表；列表检查范围有限，未取得本窗口可纳入的 dated 新事件。；已知截断 0 条。
- NVIDIA Newsroom：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- NVIDIA Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- AMD Press Releases：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- About Amazon：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Qualcomm Newsroom：checked；官方dated新闻列表实际读；最新可见Oct5许可相关旧项，未将检索结果当本期公告。；已知截断 0 条。
- Samsung Newsroom：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- SK hynix Newsroom：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- ASML News：checked；官方news跳转投资者列表，最新可见Sep8；涨价传闻无一手支持，本期未采用。；已知截断 0 条。
- TSMC Newsroom：checked；官方新闻列表实际读，Oct8月度收入为已入库背景，不推导AI业务/产能。；已知截断 0 条。
- Volantis（公司新闻稿）：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Reflection AI Blog：checked；官方blog实际读，Beam为旧预览，谈判媒体线索无正式交付/权重许可增量。；已知截断 0 条。
- Namespace Blog：checked；实际读官方blog列表，Oct5 USD42M SeriesB已有去重。；已知截断 0 条。
- Vinci Official Blog：checked；实际读配置入口getvinci.ai/blog，最新明确日期Oct6 SeriesB为背景，其他文章部分无日期；未取得本期正式版本时间。；已知截断 0 条。
- TODAY Official Blog：failed；web失败后原生浏览器确认配置blog入口404；不能据此说公司无新闻。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；官方首页完整产品和blog入口实际读；网页Clock Tool的当前日不是发布日期；Jev未定日期陈述不当本期新品，旧融资已存。；已知截断 0 条。
- GlobalFoundries Official News：checked；实际读配置news-and-events入口；最新Oct9德累斯顿/FD-SOI，Oct8中介层旧背景，无本期已核实新公告。；已知截断 0 条。
- Meet Odyssey-3：checked；官方主文/方法/评分与限制已读，Oct8背景入库，不计当日首发。；已知截断 0 条。
- Decart官网：checked；官网及About实际读，产品归属核对；无发布时间/没有取得收购确认，不计新品或完成交易。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方release列表实际读并与采集Atom核对；最新可见v0.5.21旧项，合并/提案不算正式新发布。；已知截断 0 条。
- SGLang Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；实际读官方release列表，v0.31.0已有；RSS修改不当新版本，未复现实验。；已知截断 0 条。
- vLLM Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- NVIDIA Dynamo：checked；实际读官方release列表，MiniMax M3 dev.1和v1.5.0均旧项；开发快照不是生产稳定版。；已知截断 0 条。
- FlashInfer：checked；本次官方release Atom已检查，v0.7.1已有；v0.7.0日期差异待证，未将feed更新时间当首发。；已知截断 0 条。
- Mooncake：checked；实际读官方release列表，v0.3.14rc1/v0.3.13post1为旧项，rc不当生产版。；已知截断 0 条。
- NVIDIA Technical Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- PyTorch Foundation Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；官方RSS本次返回0候选；另按窗口对Agent/推理/MoE/inference执行arxiv发现检索，无日期明确的本期精选。Epoch Oct7和Vals Oct9为研究背景，未覆盖所有分类与论文更新版，不能推断本期无论文。；已知截断 0 条。
- METR：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- UK AI Security Institute Blog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Artificial Analysis Articles：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Artificial Analysis Changelog：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- SemiAnalysis：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Vals AI：checked；官网完整评测和费用/统计说明已读，Oct9背景，单次运行、harness/长上下文费用限制保留。；已知截断 0 条。
- Epoch InnovationEval：checked；官方主文方法/结果/scoring已读，Oct7背景；附录提示和GPU原始日志未完整读。；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- NIST News：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- US BIS News & Updates：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 工业和信息化部：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 最高人民法院：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 外交部例行记者会：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 中国政府网 政策：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 重庆市大数据应用发展管理局：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 国家数据局：checked；web无正文后原生浏览器恢复官方频道，最新可见Oct9通知；未取得本期AI产业事件。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；实际阅读财联社转载完整正文，Oct10已有融资线索去重；不将媒体披露变为独立公司验证。；已知截断 0 条。
- TechCrunch AI：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- The Decoder：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- The Verge AI：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- The Information：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Bloomberg Technology：checked；RSS Decart短摘要已读，只支持WSJ谈判/金额归因；未读付费全文。另读CNA载Reuters完整短文，但同源转述不是独立证实；存在漏采时段。；已知截断 0 条；可能漏采 2026-10-11T01:00 至 2026-10-11T02:38。
- Financial Times Technology：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Financial Times AI：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- New York Times Technology：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- SCMP Tech：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- MIT Technology Review：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Ars Technica AI：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- Tom's Hardware：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 量子位：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 虎嗅：checked；RSS读取超时，web获取不足；原生浏览器恢复首页及前沿科技列表。只看标题/相对时间，没有补回完整RSS窗口或审阅全部正文，不能视为完整覆盖。；已知截断 0 条。
- IT之家：checked；完整RSS和原生浏览器精选GPT6.1主文/发布时间已读；嵌入社交帖未恢复。存在漏采窗口，未精选全部中文条目。；已知截断 0 条；可能漏采 2026-10-11T01:00 至 2026-10-11T11:02。
- 36氪：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 钛媒体：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条；可能漏采 2026-10-11T01:00 至 2026-10-11T12:22。
- 雷峰网：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 极客公园：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 智东西：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- C114 通信网：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条。
- 快科技（驱动之家）：checked；本次自动采集入口成功；候选/列表检查不代表逐篇阅读全文，未精选正文不用于事实结论；限额、正文待办与缺口见证据包。；已知截断 0 条；可能漏采 2026-10-11T01:01 至 2026-10-11T11:35。
- 机器之心：failed；实际打开仅取得Week41标题、PRO/服务导航；无法取得日期明确的完整新闻正文/列表，公众号未覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；CNA所载Reuters完整短文已读；Oct11仅日期，边界不确定，未读WSJ原全文/未获双方确认。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；自动river链接仅线索；浏览river发现Decart，原报道回查。Oct10 h2355快照获取失败，不能补全遗漏；Oct11 h2355尚晚于运行时，不作为已完成窗口快照。；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；按after:2026-10-10 before:2026-10-12执行配置检索，结果未给明确本窗口独家；额外Decart经CNA载Reuters全文，注明WSJ归因。。
- bloomberg-ai：checked；按窗口执行检索；RSS Decart摘要与CNA全文回查，未获取Bloomberg付费全文，新闻不计独立双源。。
- ft-nyt-wsj-ai：checked；按窗口执行三媒体检索；NYT受robots限制，WSJ Decart原全文未取得；这些缺口仍保留。。
- china-ai-companies-zh：checked；按窗口中文重点公司发现检索，多为旧主页/转载；Kimi路线和参数、未来源融资不当已发生事实。。
- china-ai-policy-zh：checked；按窗口中文政策检索并读国家数据局列表，命中多旧政策；没有本期精选，不等于全部政策已覆盖。。
- china-chips-zh：checked；按窗口芯片/存储中文检索，推测、社区线索缺一手证据，未采用；未覆盖所有厂商公告。。
- embodied-world-models-zh：checked；按窗口世界模型/具身融资检索，旧小鹏融资和Odyssey重复报道回查；Odyssey官网Oct8为背景。。
- supply-chain-en：checked；按窗口HBM/High-NA/CoWoS/export/memory检索，旧分析和预测未写成新供给事实。。
- newsroom-fallback：checked；按窗口官方域名兜底，回查Qwen/阿里、MiniMax、xAI、高通、ASML、TSMC；Qwen博客未恢复，其余列表不能保证全部文章覆盖。。

- 新公司发现：checked；实际开展中英文新创公司发布/融资/模型/Agent/Infra开放检索；Aurora/DiffuSpace线索身份、原公告/日期不足，留待证；旧Nous融资聚合日期错误未纳入。官网核实Decart/Odyssey产品归属后新增跟踪，属既有公司，不当新成立。。

证据包：`data/packets/daily/2026/10/2026-10-11/3afcd30afbed4ecbbffbe685fb4049eec06e0f20324c43867eaebefc7a1041b1.json`；采集 run：`20261012T010111-d1ba7083`。
