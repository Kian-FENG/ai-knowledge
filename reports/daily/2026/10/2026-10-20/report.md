# AI 产业分析日报（2026.10.20）

统计窗口：2026-10-19T18:00:00-07:00 至 2026-10-20T18:00:00-07:00（America/Los_Angeles，右端不含）。

实际生成：2026-10-21T15:13:38.726200-07:00（America/Los_Angeles）；2026-10-21T22:13:38.726200+00:00（UTC）。本次触发早于洛杉矶18:00，按规则补最近到期20日窗口。

本期11条事件显示，Agent竞争同时进入可审阅的工作流、持续会话状态和跨硬件服务栈：ChatGPT增加会话锁，Arda与Firefly面向制造/实体安全，DeepInfer、TorchTPU和llm-d各自降低不同层次的工程摩擦。订单需求、可运行代码和生产可用系统之间仍有明显距离；模型栏目本期没有核定新发布。覆盖存在官方空列表、媒体漏采、论文只读摘要及Anthropic草稿等重大待核线索，不能把未收录理解为没有新闻。

## 1. MaaS市场与产品形态

### ChatGPT开始逐步推送锁定聊天，以账户PIN或设备认证隐藏会话

- OpenAI 10月20日更新说明：锁定会话保留在账户中，但从普通历史、置顶与搜索隐藏，打开时用4位账户PIN或支持的设备认证。
- Free、Go、Plus、Pro在网页、iOS、Android及macOS/Windows新桌面端逐步推送；保留期限和模型改进设置不变。相对此前普通历史管理，增量是会话级访问控制，不应据此推断新增加密或企业合规承诺。
- 官方仅标日期，无首次发布小时；与前一期对照未收录，窗口边界不确定。

**产业判断：** 更细的会话访问控制可能降低共享设备或旁观场景的使用顾虑，支持个人助手积累长期上下文；实际采用仍取决于恢复流程与用户对保留规则的理解。反例是PIN被共用或账户本身失陷。观察推送完成范围、恢复体验与用户使用数据。

**来源与核验范围：**
- [OpenAI News · ChatGPT release notes — Introducing locked chats](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；发布时间：2026-10-20（原文仅日期）；定位：仅完整阅读release notes的October 20 / Introducing locked chats小节及帮助文档入口；未实测各端或审核安全实现。；阅读范围：仅本期小节全文，归档有限摘录；ID：`3930e8dede7666d8dfd2`。
  日期仅精确到天，无法确认 18:00 边界。

### Grok Bot披露工单监测与经人工批准的批量处置工作流

- SpaceXSI 10月20日披露内部IncidentWatch与IncidentSweep：前者按固定节奏检查相似工单，后者筛选受影响工单，先展示具体批次和消息再由工程师批准。
- 执行后记录动作，批准后不再增加工单，失败即停；这是内部运营案例披露，相对旧Support Bot新增事件监测和收尾流程，并非宣布独立新品全面可用。9月18日处理案例是背景，效果未独立验证。

**产业判断：** 价值来自将重复处置变成有边界、可审阅的工作，而不只缩短单次回答；客服集成和审计工具可能受益。反例是相似工单误归因造成错误批量回复。观察误分类率、人工复核时间、失败恢复和跨客户复现。

**来源与核验范围：**
- [xAI News · Using Grok Bot to detect and respond to incidents](https://x.ai/news/incident-sweep)；发布时间：2026-10-20（原文仅日期）；定位：主文Detecting incidents / Clearing the incident backlog / Give Bots jobs已读；未运行产品，未验证案例数字；页面下载链接指向其他域名，未用于身份或交付范围推断。；阅读范围：full-text；ID：`0de9428d3548b15fe7f4`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Arda公开亮相，Accel披露累计融资2.30亿美元

- Accel 10月20日宣布Arda结束隐身，创始人为前OpenAI研究负责人Bob McGrew；投资方称累计融资USD230M，并参与种子及A轮。该数是累计融资披露，不等于本轮金额、估值或收入。
- 官网将CAD、PDF及PLM信息映射为制造流程、工位和作业说明，并由制造工程师审核。Accel称技术用于Anduril ArsenalOS；客户效果为利益相关方披露。新增跟踪不等于本期成立；机器人执行仍是扩展方向。
- [SiliconANGLE](https://siliconangle.com/2026/10/20/arda-industries-raises-232m-to-make-production-lines-more-adaptable/)可见摘要称USD232M，[Quartz](https://qz.com/arda-ai-manufacturing-startup-230-million-funding-102026)可见摘要称USD230M单轮/USD1.5B估值；两篇未完成全文审阅，与一手累计口径不同；本条保留Accel原口径，不合并数字。仅日期，边界不确定。

**产业判断：** 若设计变更能持续映射到已审核的产线知识，制造软件可从文档工具进入生产变更流程，CAD/PLM与现场集成商可能受益。反例是数据质量或工厂差异使定制成本超过节约。观察跨工厂部署周期、工程错误率和付费续约。

**来源与核验范围：**
- [Arda Official and Investor Announcements · Our Investment in Arda](https://www.accel.com/news/our-investment-in-arda)；发布时间：2026-10-20（原文仅日期）；补充身份/产品来源：[Arda官网](https://arda.ai/)（无日期）；定位：Accel投资公告全文及Arda官网Translate/Plan/Adapt与团队段落已读；官网无日期，仅支持身份与产品背景；注册文件、到账与收入未审。；阅读范围：full-text；ID：`bc9e0209cf577bf2e636`。
  日期仅精确到天，无法确认 18:00 边界。

### Firefly披露2000万美元A轮，将安全摄像头、对讲机与传感器接入同一平台

- Firefly官网10月20日宣布结束隐身并获USD20M A轮，Definition Capital领投、BoxGroup与Susa Ventures参与；公司称2024年由James Batt Buckley及Alex Penn成立。
- 产品结合专用硬件、软件及既有摄像头/对讲机，识别事件并协调安全人员行动；公司称已用于Front Range Community College三校区。新增是本期公开融资与产品披露，客户安全效果未独立核验。
- 该公司是firefly.co对应的实体安全平台，不与同名航天或云管理公司混同；仅日期，边界不确定。

**产业判断：** 复用既有设施可降低替换硬件的门槛，集成与响应流程可能成为竞争壁垒；但误报、跨设备兼容和现场运维会增加交付成本。观察每站点部署成本、误报率、响应时间和后续客户续约。

**来源与核验范围：**
- [Firefly Physical Safety AI · Firefly Raises $20M Series A to Build a New Standard for Safety](https://firefly.co/insights/firefly-series-a)；发布时间：2026-10-20（原文仅日期）；定位：官方融资公告全文、创始人/客户/用途段落已读；浏览工具同源不可访问，项目fetch成功取得完整正文；无财务审计或客户独立证词。；阅读范围：full-text；ID：`51b319f6681d33fcf194`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

本期未收录经核验的新事件；覆盖情况见文末。

## 4. AI Infra社区与工程趋势

### DeepSeek公开DeepInfer代码，离线引擎与完整在线服务仍有明确边界

- 核对DeepInfer截止窗口内提交774ce244（10月20日11:03:13 UTC）的README：支持DeepSeek-V4.1-Flash，默认检查点Flash-1017；列NVIDIA SM100与华为Ascend 950、异步调度、推测解码、结构化输出及Apache-2.0许可。
- DeepSeek称其框架用于自身生产服务，但本次公开版提供离线推理；完整服务仍缺KV缓存系统、VE/Prefill/Decode分离配套和DP副本间负载均衡。增量是模型团队公开引擎代码，不能等同通用API服务可直接替换。
- 提交史最早条目为10月20日04:09:42 UTC；代码提交时间不等于精确公开时刻。当前main含21日更新，本条固定截止内版本。厂商曲线只见4卡prefill/64卡decode SM100说明，精度/负载/基线未完整核对，不转载性能或收益排名。

**产业判断：** 专用模型与引擎共同开放可降低架构复用成本，并给CUDA与昇腾生态提供共同参考；实际部署优势仍受外部服务组件和运维投入约束。反例是模型或硬件适配范围过窄。观察完整服务配套、跨框架正确性、可复现端到端成本。

**来源与核验范围：**
- [DeepSeek Research & News · DeepInfer README at 774ce244](https://github.com/deepseek-ai/DeepInfer/blob/774ce244b87cc0eb8d4b94ab9f5de2ab22049f01/README.md)；更新时间：2026-10-20T11:03:13+00:00；定位：固定774ce244 README全文与GitHub commits API已读；未逐算子、性能图像素、eval harness或完整LICENSE文本审计，未部署复测。；阅读范围：full-text；ID：`4e715cc238d6b9a2ad8f`。

### SGLang Omni将持续交互纳入图与会话运行时，保留不同语音架构的取舍

- 官方博客列表标10月20日；主文以图组合模型、工具和交互控制，用持续会话协调状态、取消与客户端播放进度，覆盖原生全双工、轮次模型及级联方案。相对此前Stage–Process–GPU布局，新增是跨模型与跨轮次交互协调。
- 文章用MiniCPM-o 4.5、Qwen3-Omni和Qwen3-ASR-1.7B→Qwen3.8-27B（关闭thinking）→Qwen3-TTS CustomVoice，在每方案单H200、同Omni revision下比较Full-Duplex-Bench v1.5/v1.0；每v1.5类25对、v1.0子集10样本，并做128会话/并发级别的服务测试。
- 原生方案的打断语义、级联方案的音色连续性和轮次方案的误打断各有代价；16并发是级联配置的准入上限，GPU尚未饱和。没有一种方案全面占优，不能把单次容量直接推成架构上限或普遍成本排名。仅日期，前期未收录，边界不确定。

**产业判断：** 语音助手的优化目标正扩展到用户实际听到的内容、打断后上下文一致性和持续会话成本；可替换组件让开源ASR/LLM/TTS更容易竞争。反例是协调开销抵消组件升级收益。观察误打断、播放历史一致性、长会话状态及同质量总成本。

**来源与核验范围：**
- [SGLang Blog · Unified Runtime for Full-Duplex Interactive Intelligence with SGLang Omni](https://www.sglang.io/blog/omni-interactive-runtime)；发布时间：2026-10-20（原文仅日期）；定位：官方主文、Evaluation Results表格、样本与准入限制、Known Issues及工程附录已读；未复核外链代码revision、评分模型版本、完整精度或独立复现。主文HTTP读取成功；浏览工具不可达不记作没有新闻。；阅读范围：full-text；ID：`bbde6410b22755c4db30`。
  日期仅精确到天，无法确认 18:00 边界。

### TorchTPU开放原生PyTorch后端，vLLM插件明确区分推荐与实验硬件

- Google 10月20日宣布TorchTPU已在GitHub开放，与Meta/PyTorch合作支持eager、torch.compile及分布式接口，并对接vLLM、SGLang和训练生态；这是后端与集成发布，不是新TPU芯片发布。
- Inferact/Google同日发布out-of-tree vllm-torchtpu插件，复用上游调度、KV管理与API，提供Pallas算子、主机KV卸载和分离服务；推荐v7x，v6e/v5e/v5p标实验。首次shape编译需时间，未来24小时新模型CI、部分路由与diffusion路径仍在路线图。
- 相对先前合作宣布，增量是开源后端和可安装插件；Google称“minimal code changes”，不意味着迁移后自动获得峰值性能。PyTorch文章采集版带21日更新，本条以20日Google与vLLM正文为事实依据，未纳其后更新；不作跨芯片跑分比较。

**产业判断：** 共用框架/API可降低TPU试用和模型迁移的固定成本，云客户获得更多议价与部署选择；但形状、分片、编译和容量仍约束实际替代。反例是特定模型移植后SLO或成本恶化。观察真实迁移工时、验证矩阵、冷启动及固定负载账单。

**来源与核验范围：**
- [Google Cloud Blog · TorchTPU is now open source: Run native PyTorch on TPUs](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus/)；发布时间：2026-10-20T11:30:00+00:00；定位：Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。；阅读范围：full-text；ID：`a589f9bd51df1b608590`。
- [vLLM Blog · Introducing vLLM TorchTPU](https://vllm.ai/blog/2026-10-20-vllm-torchtpu)；发布时间：2026-10-20（原文仅日期）；定位：Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。；阅读范围：full-text；ID：`970210a4bdb6c925067e`。
  日期仅精确到天，无法确认 18:00 边界。

### llm-d 1.0把会话路由、流量公平与分离升级纳入同一集群服务栈

- Google 10月20日宣布llm-d 1.0，CNCF Sandbox项目连接Kubernetes与vLLM/SGLang，支持在TPU/GPU池间组合部署；新增稳定v1接口、租户优先级与公平控制、路由高可用和DisaggregatedSet升级协调。
- 长前缀/会话感知路由、分层KV缓存与异步队列让后台Agent和交互请求共享容量；不是单引擎吞吐升级。Google披露生产采用及多种基准，但本轮未逐个读取基准配置/客户原始数据，不采用其百分比作为普遍收益。

**产业判断：** 多轮Agent竞争会把缓存命中、排队公平和升级连续性变成平台能力，统一入口可能降低应用侧对硬件的耦合。反例是缓存索引/转移与控制面成本超过复用收益。观察P95/P99、冷缓存流量、后台任务饥饿、升级丢会话率与完整账单。

**来源与核验范围：**
- [Google Cloud Blog · Announcing llm-d 1.0: Open distributed inference for agents on Google Cloud TPUs and GPUs](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference/)；发布时间：2026-10-20T11:30:00+00:00；定位：官方主文What 1.0 provides、under the hood、In production与limitations对应口径已读；外链基准和客户原始日志未审；“production ready”保留为厂商披露，未部署。；阅读范围：full-text；ID：`42d1c725644fec917f0c`。

## 5. 模型与AI Infra论文

### KVCompass提出跨地域前缀缓存发现平面，区分缓存身份与动态位置

- arXiv 10月20日公告2610.24179v1；首次投稿为10月16日19:54:51 UTC，不能称20日首次投稿。问题是同模型跨地域重复prefill，以及缓存持有者随请求/淘汰动态变化。
- 摘要提出可变长度前缀发现索引，将缓存标识与放置解耦，并在负载、复用和网络距离间选择worker；作者列64-worker地理分布模拟与14-worker三洲真机测试。增量是集群之外的发现层，而非证明跨地域搬KV一定划算。
- 仅审摘要与版本史；硬件、精度、模型、输入输出长度、并发、基线版本与完整网络成本未核，不引用摘要的倍数作普遍性能结论。

**产业判断：** 跨区域复用可能减少重复计算，但网络传输、缓存失效和数据地域约束可能抵消收益。云路由与缓存目录服务可能受益；反例是前缀不重叠或跨域链路昂贵。观察真实缓存可复用率、P99、传输成本及失效准确性。

**来源与核验范围：**
- [arXiv model and infra papers · KVCompass: A Discovery Plane for Internet-Scale Prefix Cache Sharing in LLM Serving](https://arxiv.org/abs/2610.24179)；源站公告时间：2026-10-20T00:00:00-04:00；定位：arXiv摘要与v1 Submission history；未阅读全文、图表、代码或独立复现；公告时间来自已归档官方RSS。；阅读范围：abstract；ID：`8f2f3922f8457ad7f593`。

### Koi用语言模型提出集群计划，再由确定性组件约束评分与放置

- arXiv 10月20日公告2610.24355v1；v1投稿10月17日01:03:13 UTC。论文处理异构、多云推理中加速器、并行、引擎配置与副本数等约140变量的联动。
- 摘要将RLM层级用于假设与推理，确定性组件预测服务行为、评分和控制放置，并按实际部署更新有适用范围的因果关系。相对静态逐任务配置，增量是带证据反馈的集群级规划。
- 仅审摘要和版本史；异构集群硬件、精度、模型/负载、SLO、基线及软件版本未核，不把作者摘要的goodput/成本收益推广到其他云或生产集群。

**产业判断：** 硬件选型若能由可校准证据与确定性约束控制，可减少人工调参与资源错配；但计划错误、测量漂移和频繁迁移可能吞掉收益。观察计划可解释性、SLO违约率、校准耗费与全周期成本。

**来源与核验范围：**
- [arXiv model and infra papers · Koi: Evidence-Guided, Self-Calibrating Planning for Multi-Cloud, Heterogeneous LLM Inference Fleets](https://arxiv.org/abs/2610.24355)；源站公告时间：2026-10-20T00:00:00-04:00；定位：arXiv摘要与v1 Submission history；未阅读全文、代码或独立复现，性能数字留在原始档案。；阅读范围：abstract；ID：`ac3dc5d44172ea544aac`。

## 6. GPU与供应链

### 路透称三家中国平台订购逾350亿美元RTX PRO 5500，订单不等于交付

- 路透10月20日（MarketScreener署名转载）引述匿名人士：字节、阿里与腾讯合计订购逾300万张RTX PRO 5500，按约USD11,400单价计算潜在总值逾USD35B。该数是订单口径，不是英伟达已确认收入或交货金额。
- 报道同时称需求超过计划供应，一位人士称部分客户可能仅获所求数量5%–10%；三家公司未回应，英伟达回应未逐项确认订单。增量是被报道的需求规模与配额约束；2027产量、12月样片及2027Q1交付是消息人士预期。
- 未审原始采购合同、英伟达产品合规文件或文内引用的天阳科技相关法定披露，本条不自行判定出口许可、不推算已实现算力或替代训练能力。

**产业判断：** 若报道属实，合法可购的较弱硬件也可能被推理需求争抢，供给可获得性会比峰值规格更影响部署。国产加速器和替代云供给可能受益；反例是重复下单、政策变化或需求取消。观察实际配额、到货、集群互联与单位已验收任务成本。

**来源与核验范围：**
- [Reuters Licensed Syndication · ByteDance, Alibaba, Tencent place over $35 billion worth of Nvidia chip orders](https://uk.marketscreener.com/news/bytedance-alibaba-tencent-place-over-35-billion-worth-of-nvidia-chip-orders-ce785cdbd08ff024)；发布时间：2026-10-20T10:03:00+01:00；定位：实际阅读MarketScreener转载的Reuters正文与发布时间，归档关键段落及阅读笔记；转载不是第二独立来源。原始合同、监管文件和供应链预测未核。；阅读范围：Reuters正文已读，归档关键段落与阅读笔记；ID：`08598b95b1f9c8829c1f`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 400 条（其中线索 106 条），精选 11 个事件；未注明日期 9 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Meta Muse Official Model Card：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Visko Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Stacklok Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Peppermint Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Microsoft Command Line：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Satya Nadella Public Article：failed；X原帖403，不以无新消息替代故障。；已知截断 0 条。
- Nous Research Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Healthleap Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- OpenAI News：checked；实际阅读ChatGPT 20日locked chats小节，归档有限摘录；20日官网客户案例feed已筛看，未逐客户验效。；已知截断 0 条。
- OpenAI API Changelog：ok；最近一次检测到页面变化；检查于 10-22 06:05；已知截断 0 条。
- Anthropic Newsroom：checked；实际打开News与Research列表，未核定新增本期产品公告；sitemap大量重现旧URL仅线索。IPO草稿/成本与Nscale报道已发现，但原始S-1及完整WSJ正文未读，未写成公司已确认财务事实。；已知截断 0 条。
- Anthropic Research：checked；实际打开研究列表，仅列表级核查；没有逐条阅读所有旧文。；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 544 个，最近一次新增 1 个；检查于 10-22 06:05；已知截断 0 条。
- DeepSeek Research & News：checked；实际打开官网News、API更新与DeepInfer仓库；News仍列9月10日、API17日Flash1017/搜索接口为旧背景，DeepInfer固定20日774ce244 README。；已知截断 0 条。
- DeepSeek API Change Log：checked；实际读取17日更新小节；不是20日新模型发布；不重复转载榜单。；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-22 06:05；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- Alibaba / Qwen Blog：failed；官网博客空正文；已打开QwenLM官方GitHub组织并参考HF机器列表，但未逐仓库/公众号核查，不能判断无新事件。；已知截断 0 条。
- Qwen · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；实际打开官方Research列表和MoonshotAI组织；博客最新可见K3/PerceptionBench为7月16日，未确认20日新模型；未覆盖私域或逐仓库提交。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-22 06:05；已知截断 0 条。
- Z.ai 发布记录：ok；最近一次检测到页面变化；检查于 10-22 06:05；已知截断 0 条。
- 智谱开放平台发布记录：ok；最近一次检测到页面变化；检查于 10-22 06:05；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- MiniMax News：failed；News入口仅导航；已知19日M3.1 Flash去重，未逐个产品页核对20日增量或权重交付。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-22 06:05；已知截断 0 条。
- Mistral AI：ok；feed 92 条；检查于 10-22 06:05；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-22 06:05；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-22 06:05；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-22 06:05；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- Google Cloud Blog：checked；20日TorchTPU及llm-d原文已读；未逐基准外链/所有大会产品公告核查，客户与性能数值不独立确认。；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-22 06:05；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- ByteDance Seed Blog：checked；实际读取官方Research列表，最新可见论文9月28日，未核定额外本期发布；公众号与私域未覆盖。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- Alibaba Cloud Press Room：failed；Press Room仅导航与空条目；未完成官方新闻正文覆盖。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个，最近一次新增 2 个；检查于 10-22 06:05；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-22 06:05；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-22 06:05；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-22 06:05；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-22 06:05；已知截断 0 条。
- xAI News：checked；实际阅读20日incident-sweep主文，内部案例不同于新品GA；未按异常外链推定产品归属。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-22 06:05；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 8 条；检查于 10-22 06:05；已知截断 0 条。
- Qualcomm Newsroom：checked；官方列表20日条目为V2X；未完成裁员媒体线索的一手核查。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-22 06:05；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条。
- ASML News：failed；浏览官方Press Releases返回401；官网兜底检索未获得本期合格正文。；已知截断 0 条。
- TSMC Newsroom：checked；本次官网恢复可读，最新列表为15日三季报；未见列表中的20日新公告，不能覆盖闭门供应链信息。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-22 06:05；已知截断 0 条。
- Reflection AI Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Namespace Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Vinci Official Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- TODAY Official Blog：failed；官方blog浏览不可访问；不重复以旧融资当新事件。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- GlobalFoundries Official News：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Meet Odyssey-3：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Decart官网：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Microsoft Official Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- 模思智能官方新闻：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- ModCraft产品官网：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Apple Newsroom：failed；官网仅导航，新闻列表未返回。；已知截断 0 条。
- Pluto Security：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- SemiGraph 半图科技：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Third Moment Research Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- HUMXN Official：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Sapiom Official Blog：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Tenstorrent Official Newsroom：failed；Newsroom本次仅cookie/导航；前期E轮已去重，未完成全列表覆盖。；已知截断 0 条。
- Orchestra Bio Official：checked；打开官网仅简短品牌/现有收购说明；19日报已收录，不重复列20日新收购。；已知截断 0 条。
- Arda Official and Investor Announcements：checked；官网产品/团队及Accel投资公告实际读取；新建跟踪实体，累计融资口径有媒体差异，使用投资方USD230M累计值。；已知截断 0 条。
- Firefly Physical Safety AI：checked；官方公告项目fetch成功全文；浏览工具同源不可达，已记录获取路径差异；同名公司已区分。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；Releases API近8版本核对，正式0.5.22为19日去重；20日Omni文章是技术文章/运行时进展，不把它当0.5.23正式发版。；已知截断 0 条。
- SGLang Blog：checked；HTTP原文完整取得并阅读Omni主文/评测表/限制与附录；浏览工具不可达。日期依据官方博客列表20日，仅到日。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；Releases API近8版本，正式0.32.0为18日去重；20日TorchTPU是插件发布，未冒充主仓库新版本。；已知截断 0 条。
- vLLM Blog：checked；TorchTPU正文全文，v7x推荐及其他TPU实验状态、编译开销和未来功能已核；未部署。；已知截断 0 条。
- NVIDIA Dynamo：checked；GitHub releases近8版本原始JSON核对，20日02:09:56Z Muse dev.1为experimental/not QA/not production；只列覆盖，不当正式1.6稳定版。；已知截断 0 条。
- FlashInfer：checked；Releases API近8版本：20日04:30:32Z v0.7.2rc5为预发布，正式0.7.2为15日去重；未逐PR核查。；已知截断 0 条。
- Mooncake：checked；Releases API近8版本最新0.3.14-rc1仍9月7日；无本期正式新版本，不代表仓库无提交。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-22 06:05；已知截断 0 条。
- PyTorch Foundation Blog：checked；TorchTPU引言有限阅读，采集版显示21日更新；报告优先20日Google/vLLM文本。其他大会条目未全部全文核对。；已知截断 0 条。
- OpenBMB PilotDeck Official Repository：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；本轮266候选保存60/截断201，列表不完整，21日公告不冒充20日；本期两篇取已归档20日官方RSS，补读摘要与v1史。全文、图表和代码未审。；已知截断 201 条。
- METR：ok；页面链接 27 个；检查于 10-22 06:05；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-22 06:05；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个；检查于 10-22 06:05；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-22 06:05；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- Vals AI：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Epoch InnovationEval：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-22 06:05；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-22 06:05；已知截断 0 条。
- 工业和信息化部：ok；页面链接 19 个，最近一次新增 5 个；检查于 10-22 06:05；已知截断 0 条。
- 最高人民法院：ok；页面链接 84 个，最近一次新增 11 个；检查于 10-22 06:05；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-22 06:05；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个，最近一次新增 2 个；检查于 10-22 06:05；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-22 06:05；已知截断 0 条。
- 国家数据局：failed；官网首页返回空正文；政策搜索仅发现旧资料，未完成20日政策正文覆盖。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-20T22:02 至 2026-10-21T08:32。
- The Verge AI：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条。
- The Information：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 6 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-19T22:00 至 2026-10-20T07:11。
- Financial Times Technology：ok；feed 25 条，关键词过滤 15 条；检查于 10-22 06:05；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-22 06:05；已知截断 0 条。
- New York Times Technology：ok；feed 22 条，关键词过滤 9 条；检查于 10-22 06:05；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 4 条；检查于 10-22 06:05；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 7 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-19T22:00 至 2026-10-20T21:00。
- Ars Technica AI：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 18 条；检查于 10-22 06:05；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-22 06:05；已知截断 0 条。
- 虎嗅：failed；采集器robots读取/许可失败；浏览同源已尝试，未完成可用正文核对；不能断言无新闻。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 33 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-18T09:55 至 2026-10-20T05:56；可能漏采 2026-10-20T22:02 至 2026-10-21T06:07。
- 36氪：ok；feed 30 条，关键词过滤 12 条；检查于 10-22 06:05；已知截断 0 条。
- 钛媒体：ok；feed 15 条，关键词过滤 5 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-19T22:00 至 2026-10-20T16:07；可能漏采 2026-10-20T22:02 至 2026-10-21T17:29。
- 雷峰网：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-22 06:05；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-22 06:05；已知截断 0 条。
- C114 通信网：ok；页面链接 35 个，最近一次新增 17 个；检查于 10-22 06:05；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 65 条；检查于 10-22 06:05；已知截断 0 条；可能漏采 2026-10-19T22:00 至 2026-10-20T16:00；可能漏采 2026-10-20T22:02 至 2026-10-21T15:44。
- 机器之心：failed；可见会员导航与简介；会员正文、公众号未覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。
- Reuters Licensed Syndication：checked；实际打开配置入口；仅核查本次返回的可见主页、标题或列表片段，未逐外链核对所有文章与交付；未核定额外本期增量，不等于全站无新闻。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 107 个，最近一次新增 28 个；检查于 10-22 06:05；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；围绕Oct20执行Reuters与DeepSeek/NVIDIA/Anthropic检索，回查Reuters署名RTX订单全文；其他独家线索未全覆盖。。
- bloomberg-ai：checked；执行Oct20 Bloomberg/AI检索并筛feed线索，Anthropic草稿/Pigment等未完成一手核查；不根据摘要写成确认事件。。
- ft-nyt-wsj-ai：checked；执行FT/NYT/WSJ与Oct20 AI检索；NYT robots受限，WSJ草稿全文未取得，搜索返回旧或无关结果。。
- china-ai-companies-zh：checked；执行20日中文AI公司与新公司检索，睿质20日专访与11日融资报道对照，暂不列新融资；官网身份未核不建实体。。
- china-ai-policy-zh：checked；执行20日工信部/国家数据局/算力检索；2592EFLOPS媒体引述找到，原始发布会口径未读，未将数字用于跨国比较。。
- china-chips-zh：checked；执行20日HBM/GPU/产能检索，回查Reuters署名订单文；NVHBM、国产供应线索未全部一手核验。。
- embodied-world-models-zh：checked；执行20日具身/世界模型/开源/融资检索，返回多篇18日及旧资料；Arda机器人部分仍扩展目标，未当机器人量产。。
- supply-chain-en：checked；执行Oct20 HBM/CoWoS/memory prices检索；大量媒体、社交/旧文返回，未作价格或产量验证；合格订单文保留匿名归因。。
- newsroom-fallback：checked；执行Qwen/MiniMax/ASML官方域名兜底检索，未取得合格额外本期主文；TSMC和Qualcomm列表可读。。

- 新公司发现：checked；实际执行中英文新创公司发现检索，回查Arda官网+Accel、Firefly官网；新增2个实体。ASI/Pigment及睿质等尚缺本轮一手身份/融资证据，保留候选；名单不代表全行业。。

证据包：`data/packets/daily/2026/10/2026-10-20/fa33d7bbf3a91a6c0911b4a26a2cdee88fc95fd89a8f99b7001d6dfb549bac60.json`；采集 run：`20261021T220514-09b9dc77`。


### 本轮审核、入库与调度说明

- 新建14个标准知识页：9来源、2论文、Arda/Firefly两个实体及1篇综合研究；既有标准知识页更新0。14页已审核发布，默认query、get_page与raw hash回查通过。前期Flash1017/搜索API、M3.1 Flash、Orchestra、SGLang0.5.22、vLLM0.32.0、FlashInfer0.7.2去重，不重复算新事件。
- 本轮采集125个起始启用入口：82 ok、42 needs-browser、1 failed。后新增Arda、Firefly与Reuters署名转载3个浏览入口并单独读取，未混入起始分母。42个原浏览入口均实际打开；其中仅列表/主页片段的范围已明示，不代表全站已核验。
- 本期论文取自已归档20日公告；本轮arXiv21日列表266候选、保存60、截断201，列表不完整。两篇仅摘要/v1史；全文、代码、图表与完整评测预算未审。未知日期9条不当当天新闻，Arda官网仅用于身份与产品背景。
- 未完成范围：Anthropic IPO草稿与算力承诺、Nscale谈判、ASI/Pigment融资、睿质官网身份、工信部2592EFLOPS原发布会口径、DeepSeek政策、腾讯WorkBuddy采用、小米/其他公司与NVHBM等线索仍待一手核实。WSJ付费正文、NYT robots、公众号及私域未覆盖。睿质20日专访已有11日融资报道对照，不能据此再称融资首发。
- 配置America/Los_Angeles、daily_hour=18正确，实际主机时区为America/New_York，自动化本次约纽约18:04/洛杉矶15:04触发，早于目标约3小时；未改日报窗口或伪称按时执行。当前cron仅写当地18点、未显式指定洛杉矶时区，调度时区偏差仍待修正。本轮周报最近到期为16日，已完成且不重做，下一期23日18:00洛杉矶。
- 高频媒体存在漏采，不能声称完整补回。来源覆盖列表时间简写与raw目录沿用项目默认Asia/Singapore，raw/2026-10-22为归档日，本轮实际采集发生在10月21日UTC；不代表事件日期。日精度午夜仅为packet标准化占位，正文已改为日期显示。

### 高频媒体漏采原始区间

- bloomberg-tech：from=2026-10-19T22:00:27.783810+00:00；to=2026-10-20T07:11:11+00:00；detected_at=2026-10-20T22:02:39.255372+00:00。未声称全量补回。
- ithome：from=2026-10-18T09:55:52.071326+00:00；to=2026-10-20T05:56:46+00:00；detected_at=2026-10-20T22:02:42.362961+00:00。未声称全量补回。
- ithome：from=2026-10-20T22:02:42.362961+00:00；to=2026-10-21T06:07:23+00:00；detected_at=2026-10-21T22:05:41.649018+00:00。未声称全量补回。
- mit-tech-review：from=2026-10-19T22:00:29.313252+00:00；to=2026-10-20T21:00:00+00:00；detected_at=2026-10-20T22:02:39.433422+00:00。未声称全量补回。
- mydrivers：from=2026-10-19T22:00:44.426353+00:00；to=2026-10-20T16:00:33+08:00；detected_at=2026-10-20T22:02:48.089688+00:00。未声称全量补回。
- mydrivers：from=2026-10-20T22:02:48.089688+00:00；to=2026-10-21T15:44:04+08:00；detected_at=2026-10-21T22:05:47.277608+00:00。未声称全量补回。
- the-decoder：from=2026-10-20T22:02:36.960633+00:00；to=2026-10-21T08:32:54+00:00；detected_at=2026-10-21T22:05:37.783601+00:00。未声称全量补回。
- tmtpost：from=2026-10-19T22:00:35.739914+00:00；to=2026-10-20T16:07:03+08:00；detected_at=2026-10-20T22:02:43.163832+00:00。未声称全量补回。
- tmtpost：from=2026-10-20T22:02:43.163832+00:00；to=2026-10-21T17:29:36+08:00；detected_at=2026-10-21T22:05:43.542354+00:00。未声称全量补回。
