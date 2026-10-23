# AI 产业分析日报（2026.10.22）

统计窗口：2026-10-21T18:00:00-07:00 至 2026-10-22T18:00:00-07:00（洛杉矶时间，右端不含）。

本期11个事件把Agent规模化的竞争推进到专用判别、云采购、企业推广、执行与缓存成本以及限定安全保证。Decisions API与Anthropic管理的Google Cloud接入已GA，Google Agent Compute Engine仍是预告；Nirva融资和设备交付、Skills治理计划与实际采用分别保留状态。GPU部分关注Minerva如何提高既有集群有效产出，论文仅摘要级；官方空页、媒体漏采、中国融资与模型材料未核等缺口单列。

## 1. MaaS市场与产品形态

### Decisions API正式可用，缓存与400问请求扩展实时判别能力

- OpenAI于10月22日将GPT-6 Luna支持的Decisions API从公开beta转为正式可用；相对库内10月6日beta和15日语音委派，新增正式供给、缓存与更大请求容量。
- 接口对文本、图像、原生JSON返回概率、固定选项或评分；单次上限从200增至400问，新增US/EU推理驻留。公告报价为USD0.10/百万输入token、缓存读取USD0.01/百万token，无输出token费；缓存写入与区域处理的完整条款未核，不能据此估算完整账单。
- 厂商及客户的速度倍数缺少本项目可比较的完整负载，不采作实测；新缓存规则也意味着10月6日历史版本的“无缓存读写费”不能继续视为当前报价。

**产业判断：** 把重复分类、路由和动作评分抽成专用接口，可以减少复杂Agent每一步的等待和重复上下文费用，编排和实时交互受益。反例是概率校准不足或调用次数增长抵消单次节省。观察相同任务准确率、P95、缓存命中及含写入和区域费用的完整账单。

**来源与核验范围：**
- [OpenAI News · Build more responsive apps with the Decisions API](https://openai.com/index/decisions-api)；发布时间：2026-10-22T19:00:00+00:00；定位：官方公告产品概述、三种输出类型、语音集成和Build/evaluate报价段已读；RSS确认19:00 UTC。未运行演示/API，未审缓存写入完整条款或客户原始测速。浏览快照为所列主文选段。；阅读范围：full-text；ID：`891b7e0bbf66f86d27b7`。

### Claude新增Anthropic管理的Google Cloud接入，完整平台能力进入云承诺采购

- Anthropic于10月22日宣布Claude Models on Google Cloud（Anthropic managed）GA：复用Google Cloud IAM、统一发票并抵扣已有消费承诺，当前有US和Global端点。增量是原生Claude API功能和beta与本家同日提供。
- Anthropic运营服务并担任数据处理方；原有Google managed方式继续存在，适合需要Google处理数据、严格区域驻留或Google原生集成的客户。Managed Agents等仍为beta，不随接入方式GA自动转正。
- 该接入提供Fable 5.1、Opus 5.5、Sonnet 5.5和Haiku 5.5；Opus 5.5 Fast Mode也GA，公告输入/输出价分别USD8/40每百万token。已有折扣需事前确认，不能追溯应用。仅日精度，18:00边界不确定，前期未收录。

**产业判断：** 云采购和原生功能更新可同时满足，降低企业在新能力与已有预算之间的取舍；云平台和模型商扩大分发。反例是数据处理方、驻留要求或折扣损失限制迁移。观察端点覆盖、折扣、模型配额与beta实际可用性。

**来源与核验范围：**
- [Claude Product Announcements · The full Claude Platform, available on Google Cloud](https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed)；发布时间：2026-10-22T00:00:00+08:00；定位：Anthropic官方公告主文完整阅读，包含两种管理方式、端点、价格和折扣提示；未实测购买、API或审合同。Google对应文章超时，不宣称双边正文均核完。；阅读范围：full-text；ID：`b9843ad88f05a84c240b`。
  日期仅精确到天，无法确认 18:00 边界。

### Uber将ChatGPT Work从千人试点扩展至逾三万员工的全公司推广

- OpenAI于10月22日披露Uber开始全公司推广ChatGPT Work，拟覆盖全球超过30,000名员工，初始试点为1,000人。它是ChatGPT Enterprise中的Agent平台，不能把可用席位写成月活或全员已完成部署。
- 集成Google Drive、Gmail、Calendar和Slack，以GPT-6.1 Sol作为默认能力，配套内部skills库、批准的集成和员工培训；开发团队继续使用Codex。相对产品发布，新增企业从试点转向组织推广的采用证据。
- 双方计划以后披露采用和可衡量效果；本次未给合同金额、活跃使用、节省工时或质量数据。只有日期，窗口边界不确定，前期未收录。

**产业判断：** 企业采用取决于连接器、权限、内部流程和培训，组织部署服务可能获得持续需求。反例是发放席位后使用集中于少数团队。观察活跃比例、重复任务验收率、连接器故障与每项有效交付成本。

**来源与核验范围：**
- [OpenAI News · Uber brings ChatGPT Work to all employees with OpenAI](https://openai.com/index/uber-chatgpt-work-rollout/)；发布时间：2026-10-22T00:00:00+08:00；定位：OpenAI官方公告主文与双方引言已读；仅披露推广开始和覆盖目标，未审Uber后台使用或效果数据。；阅读范围：full-text；ID：`8a40836974acd9507d87`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Anthropic将Agent Skills交由AAIF，跨平台工作流标准进入中立治理

- Anthropic于10月22日宣布把Agent Skills名称、标志、GitHub组织与agentskills.io域名捐赠给Linux Foundation旗下AAIF；使用和贡献不要求加入基金会。
- 工程师以个人身份维护，首席维护者为David Soria Parra与Mahesh Murag；版本化发布、正式提案流程和安全指导仍是建议路线图。相对已开放的格式，本期新增治理和资产归属变化。
- 超过70个平台集成、100万skills发布及近2.8亿次安装均为Anthropic披露，未审计统计方法；不是独立活跃用户。日期仅到日，边界不确定。

**产业判断：** 中立治理可减少企业对单一模型商控制工作流格式的顾虑，技能作者和跨模型工具受益；分发、权限与执行质量仍可能各自绑定。反例是规范分叉或安全治理落后。观察版本兼容、提案参与、签名和权限机制及跨平台实际迁移成本。

**来源与核验范围：**
- [Anthropic Newsroom · Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)；发布时间：2026-10-22T00:00:00+08:00；定位：Anthropic捐赠公告全文已读；未审基金会法律交割文件、安装统计、所有平台实现或外链完整规范。；阅读范围：full-text；ID：`bdc7b775ab8d2106278d`。
  日期仅精确到天，无法确认 18:00 边界。

### Nirva获报道2500万美元新融资，AI首饰押注个人反思而非会议转写

- SiliconANGLE于10月22日13:25 EDT报道Nirva Labs新增USD25M融资，累计USD33M，包含此前USD8M种子轮；报道提及Lightspeed、South Park Commons等支持者。未取得融资原始公告或到账文件，USD33M不能当本轮金额，未披露估值。
- [Nirva官网](https://www.nirva.life/)页尾nirva labs（无发布日期，仅身份背景）及产品介绍支持品牌归属：首款首饰式设备围绕日记、情绪和关系洞察；报道识别Wei Lyu为联合创始人兼CEO，并称主要识别佩戴者声音。未独立核实法定注册、隐私实现或健康效果。
- 报道预计11月开放订单、价格USD249、年末发货；官网当前只有预订信息邮件名单。上述为计划和预期，不是已上市或交付。新增公司跟踪而非把无日期官网当当日发布。

**产业判断：** 可佩戴形态和持续上下文可把个人助手入口延伸到离线生活，硬件设计与长期记忆服务受益。反例是电池、误收音、建议质量和闲置率削弱留存。观察真实发货、退货、30/90天留存、可审计数据删除与订阅经济性。

**来源与核验范围：**
- [SiliconANGLE Company Coverage · Nirva raises $25M to make AI jewelry with perspective](https://siliconangle.com/2026/10/22/nirva-raises-25m-to-make-ai-jewelry-with-perspective-that-listens-and-provides-insights/)；发布时间：2026-10-22T13:25:00-04:00；定位：SiliconANGLE完整新闻主文、Nirva官网首页与About可见文本已读；融资仅媒体归因，图中规格、投资方原始披露、注册和实际设备未核。；阅读范围：full-text；ID：`49197db3d36d5fb3244f`。

## 3. 模型能力与技术演进

### Anthropic与Theorem披露123库形式证明，保证范围仍受规格与机器模型约束

- Anthropic于10月22日披露与Theorem合作：Claude对123个OSS-Fuzz库的239个入口，在修复发现问题后生成Rocq证明。增量是把已有fuzz入口转为针对编译后RISC-V二进制的无崩溃规格，再由独立证明检查器检查。
- 保证限于小于64MB输入、单线程静态RISC-V Linux、固定内存预算及建模的系统响应；未覆盖全部入口、所有ASan漏检或调用方误用，规格和机器语义本身仍需可信。不能写成这些库完全无bug或任意x86/ARM生产部署已安全。
- 能力结果为研究团队披露；小任务对比使用36个任务、每任务3次独立单Agent尝试、每次5M token预算。模型效率比较为Opus 5.5对Opus 5的特定子实验，未转作一般代码能力排名。大规模实验的完整模型配置、总预算与公开证明复核尚缺。

**产业判断：** 当证明生成成本下降，安全验证服务可从抽样测试扩展到可检查的限定保证，规格工程与可信语义成为重要环节。反例是证明了错误规格、修改代码取巧或维护成本过高。观察独立检查通过、补丁功能保真、目标平台覆盖与每个有效保证的全成本。

**来源与核验范围：**
- [Anthropic Research · LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)；发布时间：2026-10-22T00:00:00+08:00；定位：官方Introduction、Turning tests into proofs、Finding/fixing、成本与复用子实验、Limitations及脚注已读；附录、证明仓库和Rocq独立执行未审。不是独立复现。；阅读范围：full-text；ID：`f6a301346a05e615cdbc`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### Google公布Agent Compute Engine，以可暂停microVM承接持续Agent执行

- Google Cloud于10月22日公布已支持Gemini工作任务的Agent Compute Engine，面向客户的预览计划未来数月提供；不因公告使用launch一词就写成已经GA或普遍开放。
- 架构用硬件隔离microVM、写时复制、空闲暂停/恢复、每Agent身份与短期凭据，以及Hyperdisk保留工作区；凭据在microVM外出口注入。相对前期状态连续性研究，新增云级执行和治理产品化。
- 面向Kubernetes的开源Agent Substrate是另一条可定制路径，治理扩展中的跨云、终端、成本路由等多项仍为即将预览。未审源码、实际开放区域/价格和完整性能配置，不采用10倍密度或延迟数字做排名。

**产业判断：** 暂停“思考/等待”期间的执行环境可降低闲置资源成本，持久工作区与统一身份减少长任务恢复摩擦，云平台与运行时服务受益。反例是快照I/O、冷恢复或治理复杂度抵消费用。观察固定SLO下每个验收任务的资源成本、恢复成功率和权限隔离。

**来源与核验范围：**
- [Google Cloud Blog · Introducing Agent Compute Engine and expanded agent governance](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance/)；发布时间：2026-10-22T04:00:00+00:00；定位：官方发布主文全文已读，包含preview、Agent Substrate和governance时态；技术deep dive超时、源码与完整压测配置未审。；阅读范围：full-text；ID：`68737869cfdbcb9ddd67`。

### SGLang详解混合模型统一缓存，淘汰收益依赖大块分配条件

- SGLang于10月22日技术文章解释GPU上统一缓存池：全注意力KV和循环状态共享容量，后续扩展到滑窗KV；这不等同CPU迁移或CUDA统一虚拟内存，CPU/外存缓存由HiCache处理。本期是设计与实验披露，不当作当天新正式release。
- 标题收益比较的两组都已使用Unified Memory，仅改变按可回收共享容量停止淘汰的规则。测试为Qwen3.5-4B、RTX5090 32GB、Triton，28个约390-token前缀、7000-token压力请求、28次重访，6次运行中位数：保留10→19个前缀，重访总时间4.105→2.548秒。
- 压力请求分成4个2048-token块时，两种策略都保留17个前缀；整体吞吐无稳定变化。精度、完整软件revision、并行、输出长度/调度并发未完整核实；只作此实验的报告值，不推导普遍吞吐提升。支持后端与K/V head大小仍有限制。

**产业判断：** 混合架构部署的成本可由缓存容量与分配策略决定，重复前缀负载和显存受限环境可能受益。反例是分块预填充抹平差异或搬移开销主导。观察真实请求分布、分配粒度、命中、P99、碎片与固定质量下显存成本。

**来源与核验范围：**
- [SGLang Blog · Unified Memory in SGLang: allocation-aware eviction for hybrid-model caches](https://www.sglang.io/blog/unified-memory)；发布时间：2026-10-22T00:00:00+08:00；定位：官方可视化文章全部可提取主文、教学示例和Results已读；标题日期由官网博客列表确认，未审PR代码/合并时刻和完整benchmark脚本，未复现。；阅读范围：full-text；ID：`a99c4fb24c70553e3648`。
  日期仅精确到天，无法确认 18:00 边界。

## 5. 模型与AI Infra论文

### 推测解码论文：目标模型重生成基线会缩小草稿训练目标的增益

- arXiv 2610.29013v1初次投稿为10月21日00:26:37 UTC，官方RSS于10月22日00:00 EDT公告，属于本期；公告不等于当天初投。只读摘要及版本史。
- 作者在同一语料四种版本上比较交叉熵、目标token蒸馏及验证存活位置门控；摘要报告目标贪心重生成后，蒸馏增益缩小、门控增益很小或消失，并在额外视觉与文本设置检查。未核模型版本、硬件、完整训练预算和harness，不采速度排名。

**产业判断：** 评估草稿训练方法时，数据重写与训练长度可能解释部分收益，模型供应商和推理框架需要更强基线。反例是其他目标或在线分布仍有增益。观察目标重生成基线、等监督长度、训练成本及端到端收益。

**来源与核验范围：**
- [arXiv model and infra papers · Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding](https://arxiv.org/abs/2610.29013)；源站公告时间：2026-10-22T00:00:00-04:00；定位：arXiv摘要、v1提交历史和已归档官方RSS公告字段已读；未读19页PDF、6图15表、代码或复现。；阅读范围：abstract；ID：`3a279e3d6307111e15c2`。

### 推测解码论文：目标概率何时可复用，取决于完整上下文与计算重叠

- arXiv 2610.29210v1初投为10月21日05:02:50 UTC，10月22日官方RSS公告属本期；只读摘要与版本史。
- 作者分析精确复用目标分布需对应下一轮完整上下文，保留该分布有时牺牲已接受token；在6个目标模型上研究当前上下文额外目标分布的首token重排/先采样。摘要报告仅在额外目标计算与独立草稿重叠的实验中有解码加速；目标名单、版本、精度、硬件、I/O、并发、软件与harness未核。

**产业判断：** 利用目标模型已算出的概率可能提高小树预算利用率，但额外计算和调度时机决定端到端价值，推测解码编排层受益。反例是重叠不足或牺牲接受长度抵消收益。观察完整系统预算、树大小、接受长度、尾时延和质量保持。

**来源与核验范围：**
- [arXiv model and infra papers · Understanding Target Probability Reuse in Speculative Decoding](https://arxiv.org/abs/2610.29210)；源站公告时间：2026-10-22T00:00:00-04:00；定位：arXiv摘要、v1提交历史与官方RSS已读；未读29页PDF、6图29表或代码，未独立验证定理与性能。；阅读范围：abstract；ID：`570efb7c773128d39ffe`。

## 6. GPU与供应链

### NVIDIA发布Minerva，将GPU有效供给的竞争延伸到故障与作业观测

- NVIDIA于10月22日发布Minerva AIOps平台，把GPU、网络、存储、调度器和作业遥测关联成动态知识图谱，定位影响训练/推理作业的部件；原生助手可给出建议，人工执行或通过外部API接自动化。
- 公司称IREN正在使用；Aolani、Bitdeer AI、IBM、Jio、Lambda、Quake AI与Tesla计划部署，Dell、Lenovo、Supermicro将纳入运维产品组合。现有使用、未来部署和渠道计划分别记录。
- 增量在提高现有算力可用产出，而非宣布新增GPU装机或证明token成本下降。官方将GPU小时、goodput、uptime与token产量作为yield指标，但未给独立量化效果、普遍可购买范围或完整价格。

**产业判断：** 集群扩大后，故障关联与修复速度可影响有效算力供给，运营工具和数据整合伙伴受益。反例是跨厂商设备可见性不足、误关联或修复自动化增加事故。观察可用GPU小时、MTTR、固定质量goodput、误报与运维成本。

**来源与核验范围：**
- [NVIDIA Blog · NVIDIA Unveils Minerva to Bring End-to-End Observability for AI Factories](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)；发布时间：2026-10-22T15:00:02+00:00；定位：NVIDIA公告全文主文及伙伴使用/计划段已读；RSS15:00:02 UTC与网页Oct22一致。未审客户运行记录、自动化API安全或独立性能。；阅读范围：full-text；ID：`af6b159eb6ea2f663c90`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 310 条（其中线索 41 条），精选 11 个事件；未注明日期 10 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Meta Muse Official Model Card：checked；已打开官方HF卡入口并核对标题；未检查本期revision、完整评测或下载，不能据此断言无更新。；已知截断 0 条。
- Visko Official：checked；已打开首页，显示Orbis与产品主张；无可核本期发布日期，只作既有跟踪入口。；已知截断 0 条。
- Stacklok Official：checked；公司入口可读，出现Mecatl提示；本期具体发布正文和日期未完成核查，留线索。；已知截断 0 条。
- Peppermint Official：checked；实际打开固定公告，正文日期Oct8，旧融资背景；未当作本期融资。；已知截断 0 条。
- Microsoft Command Line：checked；已打开并核对Oct9，属于已入库背景，不把网页重取当新发布。；已知截断 0 条。
- Satya Nadella Public Article：failed；实际打开登记X原帖返回403，无法复核本期更新。；已知截断 0 条。
- Nous Research Official：checked；官网入口可读，当前可见Hermes与使命；未逐篇检查本期公告，Google本期文章的客户引言不是独立采用验证。；已知截断 0 条。
- Healthleap Official：checked；官网产品及38M融资提示可见；旧跟踪，未核对本期新闻日期或临床数据，不重复收录。；已知截断 0 条。
- OpenAI News：checked；官网、官方RSS和Decisions/Uber正文已核；FDE/NASK未完成深入阅读，Oct23储存/训练安全超窗。；已知截断 0 条。
- OpenAI API Changelog：checked；采集器页面变化为导航小变；Oct22 Decisions GA正文单独核实，旧beta/voice已库内回读，不把导航变化当API新事件。；已知截断 0 条。
- Anthropic Newsroom：checked；官网列表与AgentSkills公告全文已读；Oct18公益承诺属旧背景。；已知截断 0 条。
- Anthropic Research：checked；Oct22形式验证主文与限制已读；附录、仓库与独立证明执行未审。；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 555 个，最近一次新增 9 个；检查于 10-24 06:04；已知截断 0 条。
- DeepSeek Research & News：checked；官网动态、API入口和有限HF50条已实际检查，公开入口本期无新带日期正式发布；融资报道未得一手确认，不推断公司无融资。；已知截断 0 条。
- DeepSeek API Change Log：checked；机器读取及官网API入口核对；V4.1-Flash-1017/搜索API是前期已收录，不重发。；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-24 06:04；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-24 06:04；已知截断 0 条。
- Alibaba / Qwen Blog：failed；已实际打开Qwen博客，0行正文；HF有限50条列表无新链接，不能推断全品牌没有新闻。；已知截断 0 条。
- Qwen · Hugging Face：checked；机器有限50条HF列表无新增链接；只支持该列表，博客仍空正文。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；官网列表本次出现K3.1 Pro Oct24；是窗口后/未来日期，未收录为22日发布；媒体“开测”未核完整原文。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-24 06:04；已知截断 0 条。
- Z.ai 发布记录：ok；最近一次检测到页面变化；检查于 10-24 06:04；已知截断 0 条。
- 智谱开放平台发布记录：ok；最近一次检测到页面变化；检查于 10-24 06:04；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-24 06:04；已知截断 0 条。
- MiniMax News：failed；登记news入口只返回模型/产品导航，无带日期新闻正文；HF/定向检索有限补充。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 22 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- Mistral AI：ok；feed 92 条；检查于 10-24 06:04；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-24 06:04；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-24 06:04；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-24 06:04；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- Google Cloud Blog：checked；本次feed获取robots许可失败，未绕过；同一RSS经浏览工具访问仍超时；同一官方域ACE发布主文经浏览和许可允许的逐文抓取读到。Claude对应文与ACE deep-dive超时，改读Anthropic公告；KnowledgeCatalog新文正文未审。；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个，最近一次新增 3 个；检查于 10-24 06:04；已知截断 0 条。
- ByteDance Seed Blog：checked；官方研究列表实际打开，显示SeedRealtime但未给日期及Jul31等旧发布；未据无日期导航构造当天新闻。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-24 06:04；已知截断 0 条。
- Alibaba Cloud Press Room：failed；实际打开press-room，列表空占位和产品导航，未取得带日期新闻正文。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个；检查于 10-24 06:04；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-24 06:04；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-24 06:04；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-24 06:04；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-24 06:04；已知截断 0 条。
- xAI News：checked；官方列表出现Oct22 SpaceXSI Partner Network，Oct20事件运维旧闻；22日伙伴计划正文未审，保留候选。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- NVIDIA Blog：checked；Minerva主文和伙伴状态已读。DSX Power与Cosmos全文可读但正文Oct21而RSSOct22，日期/事件边界不一致，保守不当本期新事件；KazakhstanRSSOct23 02:00Z超窗且网页失败。；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 8 条；检查于 10-24 06:04；已知截断 0 条。
- Qualcomm Newsroom：checked；官方可见列表Oct22仅财报日程、Oct21股息与Oct20 V2X；未发现可采用的本期AI发布，但仅限返回列表。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 19 条；检查于 10-24 06:04；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- ASML News：checked；实际打开重定向投资者列表，最近显示Oct14 Q3与Sep8公告；该列表未见本期新稿，不外推所有渠道。；已知截断 0 条。
- TSMC Newsroom：checked；实际打开并定位All Categories：Oct15财报与Oct8月营收为最新返回项；列表内无本期新稿。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-24 06:04；已知截断 0 条。
- Reflection AI Blog：checked；已打开blog，当前导航有Beam权重入口；本期权重revision/发布日期/完整许可未核，未据导航宣布新发布。；已知截断 0 条。
- Namespace Blog：checked；列表可读，顶部Oct14旧Doom Devbox和SeriesB背景；本期新公告未见于返回列表。；已知截断 0 条。
- Vinci Official Blog：checked；列表Oct6融资背景可读，其余多数无日期；新文正文和发布时间未核。；已知截断 0 条。
- TODAY Official Blog：failed；登记usetoday.io/blog实际打开不可访问；不同today品牌不合并，前期中国Today融资/身份仍待核。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；列表有Jev1.14.0实验功能但无可见日期；只核入口，未以此列为当日更新；Jev论文摘要线索留候选。；已知截断 0 条。
- GlobalFoundries Official News：checked；news入口已打开但返回以导航为主，本期逐条日期正文未完成核查。；已知截断 0 条。
- Meet Odyssey-3：checked；实际打开固定Odyssey3公告，Oct8旧发布；本期无增量核实，不重发。；已知截断 0 条。
- Decart官网：checked；官网Lucy2.5与合作方入口可见；本期融资/收购状态未核，不把合作方logo当交易证据。；已知截断 0 条。
- Microsoft Official Blog：checked；官方可见列表顶部Oct20主权云、Oct19安全及Oct12 Maia；Oct22媒体Maia300是旧发布重述，未收录。；已知截断 0 条。
- 模思智能官方新闻：checked；官网入口显示MOSS产品和Live敬请期待；可见主文未支持本期GA。；已知截断 0 条。
- ModCraft产品官网：checked；官网产品与备案入口可读；本期发布、融资或注册正文未核。；已知截断 0 条。
- Apple Newsroom：failed；登记入口实际打开只返回导航与通知组件，无新闻列表正文。；已知截断 0 条。
- Pluto Security：checked；列表可见Oct20个人助手安全旧文；本期更新未见于返回列表，未审全部文章。；已知截断 0 条。
- SemiGraph 半图科技：checked；官网角色与多模态产品可读，未取得带日期公告，本期不构造发布。；已知截断 0 条。
- Third Moment Research Official：checked；官网自动改进推理端点说明可读，无可核本期发布日期，只保留既有跟踪。；已知截断 0 条。
- HUMXN Official：checked；已打开固定官方公告，Oct6旧免费家政换训练数据项目；不重发。；已知截断 0 条。
- Sapiom Official Blog：checked；列表仍是Sep15/Aug5旧文，页顶50M提示未给日期；未据页顶提示确认本期融资。；已知截断 0 条。
- Tenstorrent Official Newsroom：checked；本次入口只返回筛选/类别与cookie组件；窗口新闻正文未取得，覆盖不足，非“无新闻”。；已知截断 0 条。
- Orchestra Bio Official：checked；官网joining OpenAI文字可读，无新日期；此前事件去重。；已知截断 0 条。
- Arda Official and Investor Announcements：checked；官网制造软件身份可读，既有跟踪；未核本期新融资/版本。；已知截断 0 条。
- Firefly Physical Safety AI：checked；固定融资公告正文标Oct20，已入库旧事件，不重发。；已知截断 0 条。
- Claude Product Announcements：checked；官方产品列表和Oct22 Anthropic-managed GCP公告主文已读；Oct21 Duet/Security前期去重，Oct23 Cowork/Duet安全超窗。；已知截断 0 条。
- Recursive Superintelligence Official：checked；官方updates可见Oct21 Flint，前期已入库；本期无新增公告见于返回列表。；已知截断 0 条。
- Blacksmith Official Blog：checked；列表顶部Oct21 SeriesC，前期去重；未把当日取回当新融资。；已知截断 0 条。
- Nirva Labs Official：checked；新增入口，首页/About正文与页尾nirva labs已读；无新闻日期，仅身份/产品背景。；已知截断 0 条。
- 星忆智能 AstrAlive Official：checked；新增入口，首页/Blog主文已读，July10 v1.0背景；Oct22融资报道正文失败、投资方原始公告缺失。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方release页面与Atom前5版本核对，最新0.5.22为Oct19旧；本期UnifiedMemory为文章，不虚构正式发布。；已知截断 0 条。
- SGLang Blog：checked；UnifiedMemory全文/Results与官网列表日期已读；HiCache Oct19旧文去重，相关PR合并时刻未核。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；官方release与Atom前5核对，0.32.0/0.32.1rc0在Oct18；未见本期release，非没有commit。；已知截断 0 条。
- vLLM Blog：checked；机器文章列表本期无新增；Oct21 Humming/Flint前期去重，未重复审所有技术文。；已知截断 0 条。
- NVIDIA Dynamo：checked；官方release和Atom核对：1.6.0更新时间Oct23 04:08:42Z晚于本期截止01:00Z，留下一期；Muse dev.1 Oct20旧。未提前收录。；已知截断 0 条。
- FlashInfer：checked；官方rc6页确认Pre-release，发布Oct22 07:58，Atom更新08:10Z；只是rc非新稳定GA，正文仅changelog链接未深审，不为凑数。rc7/post1 Oct23均超窗。；已知截断 0 条。
- Mooncake：checked；官方release页/Atom有限10条核对，最近返回0.3.14-rc1 Sep7；无本期release见于列表，不外推提交活动。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-24 06:04；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- OpenBMB PilotDeck Official Repository：checked；官方仓库入口已打开；本期commit/release逐项未审，不把导航或2.0旧版当新release。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；官方RSS在本期的两篇推测解码摘要、v1历史已读；本轮保存上限60，另142条截断，部分本期摘要来自前轮原档；PDF/代码/全部论文检索不完整。；已知截断 142 条。
- METR：ok；页面链接 28 个；检查于 10-24 06:04；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-24 06:04；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- Vals AI：checked；实际打开固定多Agent评测文章，Oct9背景；不重发，不以其指令进行本任务代理委派。；已知截断 0 条。
- Epoch InnovationEval：checked；固定研究入口已打开，未重新审全文或核本期更新，不能宣称评测全面覆盖。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-24 06:04；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-24 06:04；已知截断 0 条。
- 工业和信息化部：ok；页面链接 19 个，最近一次新增 7 个；检查于 10-24 06:04；已知截断 0 条。
- 最高人民法院：ok；页面链接 84 个，最近一次新增 16 个；检查于 10-24 06:04；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个，最近一次新增 1 个；检查于 10-24 06:04；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-24 06:04；已知截断 0 条。
- 国家数据局：failed；官网实际打开0行，无正文，不能表示无新闻。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；实际打开固定Oct10报道入口，非本期来源；未复读完整融资报道。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-22T11:50。
- The Information：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 8 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-22T10:43。
- Financial Times Technology：ok；feed 25 条，关键词过滤 12 条；检查于 10-24 06:04；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-24 06:04；已知截断 0 条。
- New York Times Technology：ok；feed 23 条，关键词过滤 12 条；检查于 10-24 06:04；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 5 条；检查于 10-24 06:04；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 1 条；检查于 10-24 06:04；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 17 条；检查于 10-24 06:04；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-24 06:04；已知截断 0 条。
- 虎嗅：failed；collect超时后已用浏览工具访问同一RSS仍超时，停止重试，不称无新闻。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 35 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-23T09:42。
- 36氪：ok；feed 30 条，关键词过滤 17 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-22T22:00 至 2026-10-23T09:21。
- 钛媒体：ok；feed 14 条，关键词过滤 4 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-22T16:03；可能漏采 2026-10-22T22:00 至 2026-10-23T18:16。
- 雷峰网：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-22T19:08。
- 极客公园：ok；feed 30 条；检查于 10-24 06:04；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-24 06:04；已知截断 0 条。
- C114 通信网：ok；页面链接 34 个，最近一次新增 25 个；检查于 10-24 06:04；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 61 条；检查于 10-24 06:04；已知截断 0 条；可能漏采 2026-10-21T22:05 至 2026-10-22T15:37；可能漏采 2026-10-22T22:00 至 2026-10-23T15:19。
- 机器之心：checked；首页只返回Week43主题和会员入口，有限线索；公开文章全文和窗口覆盖未完成，不视为完整核查。；已知截断 0 条。
- Reuters转述WSJ：checked；登记固定Decart旧闻URL已打开；不把旧URL访问作为本期收购新进展。；已知截断 0 条。
- Reuters Licensed Syndication：checked；MarketScreener入口已打开，仅有限首页/登录视图，本期Reuters具体原文未完成回查。；已知截断 0 条。
- SiliconANGLE Company Coverage：checked；新增媒体入口，Nirva主文及Oct22 13:25EDT已读；25M本轮/33M累计分列，未获一手融资公告。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 135 个，最近一次新增 17 个；检查于 10-24 06:04；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；按Oct22对Reuters和重点对象检索；未取得可采用的一手融资或独家正文，有限检索不能断言无报道。。
- bloomberg-ai：checked；按Oct22检索并阅读候选标题/摘要；AnthropicIPO、Meta信用/支出等未核原始披露或完整媒体正文，未收录。。
- ft-nyt-wsj-ai：checked；按Oct22执行三域检索；NYT robots禁止，FT/WSJ相关全文未取得，有限线索不构成核实。。
- china-ai-companies-zh：checked；按Oct22检索中美大模型/公司并对照候选；DeepSeek融资、Kimi开测与讯飞X2.6尚缺一手原始材料，未将媒体标题当确认。。
- china-ai-policy-zh：checked；按Oct22工信部/国家数据局/智能体检索；杭州会议公告标Oct23是超窗，产业基础十五五规划正文未审，留候选。。
- china-chips-zh：checked；按Oct22检索HBM/GPU/产能/发布；Micron路线图、iHBM等原始技术材料未取得，NVIDIA21日计划不重发，Maia300是Oct12旧闻。。
- embodied-world-models-zh：checked；按Oct22具身/世界模型/融资检索，星忆官网背景核实；模型/硬件采用与融资报道多未核原始材料，不用汇总日报作为独立证据。。
- supply-chain-en：checked；按Oct22 HBM/CoWoS/出口限制检索，返回多为旧文或不相关；未完整覆盖供应链官方网络研讨会和财报，不能表述为无新闻。。
- newsroom-fallback：checked；按Oct22定向检索Qwen/MiniMax/TSMC并实际打开Qualcomm、ASML等官方入口；空页和超窗单列。。

- 新公司发现：checked；执行中英文新公司/融资发现：Nirva媒体正文+官网支持有限公司跟踪；星忆官网背景已核、36氪融资正文失败；Flapping Airplanes检索显示Oct21 13:57PDT，窗口前，未当本期融资。。

证据包：`data/packets/daily/2026/10/2026-10-22/0a1092338f9fc8769fdfd634d3886b71491fddd51a84ebcee903c16b5305c544.json`；采集 run：`20261023T220306-fab63e54`。
