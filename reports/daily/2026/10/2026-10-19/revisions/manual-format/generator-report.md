# AI 产业分析日报（2026.10.19）

统计窗口：2026-10-18T18:00:00-07:00 至 2026-10-19T18:00:00-07:00（洛杉矶时间，右端不含）。

本期11条事件显示，Agent竞争同时落在服务单价、研发工作流、硬件接入与推理运行效率。MiniMax服务已上线而权重仍待交付，OpenAI收购Orchestra延伸研发协调，芯片融资与软件后端扩展仍须验证交付。论文只读摘要，媒体漏采、官网列表空白与付费/私域资料缺口限制覆盖；未将宣布、预发布或模拟估算提升为生产事实。

## 1. MaaS市场与产品形态

### MiniMax M3.1 Flash上线API与订阅，权重仍待发布

- MiniMax 10月19日宣布M3.1 Flash正式上线API、M Plan和MiniMax Code；权重将稍后发布，Pro仍为后续计划。相对此前M3与预览版，增量是正式服务与新的价格表。
- 公告列USD/百万token：输入0.15、输出0.60、缓存输入0.015。速度、综合任务降本和榜单名次是厂商主张，缺完整harness、预算与负载，不据此对模型排名。日期仅到日，窗口边界不确定，前一期未收录。

**产业判断：** 低输出单价可能降低长程Agent的试错预算，应用商受益、其他API面临价格压力；反例是更多重试抵消单价优势。观察固定任务成功率、完整账单和权重实际交付。

**来源与核验范围：**
- [MiniMax News · MiniMax M3.1 Flash: Redefining Agent Performance and Cost](https://www.minimax.io/blog/minimax-m31f)；发布时间：2026-10-19T00:00:00+08:00；定位：官方正文2026-10-19、Pricing、可用渠道与weights later；主文已读，图表像素/评测harness未审。；阅读范围：full-text；ID：`b984a5c544e6313764dd`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### OpenAI确认收购Orchestra Bio，将研发协调平台接入Rosalind

- OpenAI正文明确has acquired Orchestra Bio，Orchestra官网也确认加入OpenAI；团队和技术将与Rosalind结合，覆盖药物研发项目的研究、决策和进度依赖。交易金额及交割文件未披露。
- 新增是从模型/科学工具延伸到项目协调平台；未证明已缩短临床研发周期。网页标10月20日，官方RSS为10月20日00:00 UTC＝洛杉矶19日17:00，属于本期；日期证据不靠采集时间。

**产业判断：** 将实验分析与跨部门协调结合，有机会提高工作流切换成本并扩展企业产品边界；反例是数据集成、责任划分和审批拖慢采用。观察客户实际开放范围、系统集成与项目周期证据。

**来源与核验范围：**
- [OpenAI News · OpenAI acquires Orchestra Bio](https://openai.com/index/openai-to-acquire-orchestra-bio/)；发布时间：2026-10-20T00:00:00+00:00；定位：OpenAI主文Bringing Rosalind and Orchestra together/Designed for the way biopharma teams work；另核Orchestra官网声明与官方RSS时间，未审交易文件。；阅读范围：full-text；ID：`cc198d0786d8a93aed80`。

### 铭芯启睿披露超4亿元A轮与CEO变动，第一代LPU仍在研发

- 极客公园10月19日正文转述铭芯启睿MemSilicon宣布超4亿元A轮，博原资本领投；前Graphcore总裁卢涛出任CEO兼联合创始人。原文“亿元”未单列币种，不换算、不推估值或收入。
- 公司路线从RRAM产品化扩展到第一代大模型推理LPU研发。新增是资金、组织和产品方向；未取得官网/法定主体核对、到账或样片验收，性能愿景不作量产事实，暂不建立实体页。

**产业判断：** 存储、互联与计算协同可能争取低延迟推理需求，但芯片融资到可用供给还隔着流片、软件和客户验收。观察样片时间、完整模型质量、量产良率与同负载成本；不把多个转载当独立证实。

**来源与核验范围：**
- [极客公园 · MemSilicon完成超 4 亿元 A 轮融资，宣布战略升级](http://www.geekpark.net/news/372545)；发布时间：2026-10-19T12:00:32+08:00；定位：极客公园官方RSS正文首段融资、卢涛身份、第一代LPU研发及关于铭芯启睿；未核所有引述、图表和工商资料。；阅读范围：feed-content；ID：`ca77df14e0ee6b1b013f`。

## 3. 模型能力与技术演进

### OpenAI公布低资源编程评测，将COBOL迁移的行为一致性纳入验证

- OpenAI 10月19日发布MultiLangBench与COBOL迁移评测：前者跨20种语言构建SQLite兼容引擎，后者要求迁移后可观察输出逐字节一致。文章涉及GPT-6 Astra、GPT-6 Luna、GPT-6.1 Sol及GPT-5.6 Sol基线。
- 新增是评测设计和厂商结果披露，并非本期发布这些模型。本文未审完整仓库、harness版本、任务预算与隐藏测试，不转载跨模型成本排名；生产迁移仍须检查业务规则、依赖和专家验收。

**产业判断：** 老系统现代化的价值取决于保留业务行为，受益环节可能是银行IT、迁移服务和测试工具；反例是隐藏依赖未被评测覆盖。观察真实代码库迁移、缺陷逃逸率和人工审阅成本。

**来源与核验范围：**
- [OpenAI News · Advancing coding in low-resource programming languages](https://openai.com/index/low-resource-programming-languages)；发布时间：2026-10-19T12:00:00+00:00；定位：官方主文两项评测设计、模型结果和生产限制已读；GitHub测试套件/预算/全部图表未审，数字不作外部验证。；阅读范围：full-text；ID：`1dbe22633003a2af4fdd`。

## 4. AI Infra社区与工程趋势

### SGLang 0.5.22正式发布，扩展推测解码并改变升级要求

- GitHub API确认v0.5.22于10月19日02:55:19 UTC发布，prerelease=false；created_at是15日23:39:11 UTC，updated_at是19日05:55:53 UTC，不混用。相对0.5.21，这是本期正式版本。
- Highlights包含HiSparse的EAGLE/MTP、Apple Silicon标准PyTorch路径及混合线性模型状态恢复修复。需Python3.11+，attention DP参数及host-receive阈值语义变化。框架新增适配不等于对应模型本期首发；性能百分比缺完整口径，不采用。

**产业判断：** 推理栈同时改善模型覆盖、缓存与正确性，但升级依赖与参数变化可能抬高部署成本。观察相同模型负载的正确性、尾延迟和回滚率，不能将零散PR加速相乘。

**来源与核验范围：**
- [SGLang Releases · v0.5.22](https://github.com/sgl-project/sglang/releases/tag/v0.5.22)；发布时间：2026-10-19T02:55:19+00:00；定位：v0.5.22 Highlights/To upgrade/Security/Dependencies/Breaking Changes；API日期和预发布标记；未逐PR、运行升级或复现实验。；阅读范围：full-text；ID：`6d0f4e95afe7efb24ef4`。

### vLLM用异步准备与NIXL EP减少扩缩容停顿，容量就绪仍需时间

- vLLM 10月19日技术文章把拓扑准备放到后台，并复用保留worker的CUDA图；增量是减少Elastic EP重配置期间的服务中断。官方称功能在最新vLLM/NIXL可用，但正文未固定精确版本号，未自行认定所有部署均支持。
- 案例为DeepSeek V4 Pro、GB200、TP1与DP/EP16↔20、预下载权重和暖编译缓存。停顿与完整扩容时间分开计量；精度、输入输出分布和精确软件版本未全部确认，本期不采用秒数作通用性能结论。Dynamo Snapshot和编排器接入仍是后续工作。

**产业判断：** 缩短停顿可减少扩容时丢失的服务价值，推理平台受益；反例是后台准备仍占资源、突发流量快于容量就绪。观察完整扩容耗时、p95 TTFT、失败率及闲置GPU成本。

**来源与核验范围：**
- [vLLM Blog · Achieving near-zero-downtime scaling in Elastic Expert Parallelism](https://vllm.ai/blog/2026-10-19-elastic-ep-near-zero-downtime)；发布时间：2026-10-19T00:00:00+08:00；定位：官方主文准备/commit、图复用、Performance、Try Elastic EP与What comes next已读；未运行测试、逐PR或验证生产。日期仅到日，边界不确定。；阅读范围：full-text；ID：`59dd48e60c6b9abf716e`。
  日期仅精确到天，无法确认 18:00 边界。

### 微软将内部Agent纳入持续风险控制，Guardian方案仍须验证

- 微软10月19日官方文章提出按身份、权限、数据、端点、网络、云与运行时管理内部Agent，利用Project Perception的信号、动态上下文和Guardian Agents监督行动。增量是将既有安全栈的适用对象扩展到内部Agent。
- 这是厂商架构与治理路线陈述，未公布统一SKU、价格、完整可用范围或对照实验；“持续监督每一步”不视为已覆盖所有生产场景。来源只有日期，窗口边界不确定。

**产业判断：** 执行前控制可能扩大身份与安全平台在Agent预算中的占比；反例是额外延迟、误拦截以及监督Agent自身失效。观察策略覆盖率、绕过率、误报和关键路径延迟。

**来源与核验范围：**
- [Microsoft Official Blog · Securing the agentic insider](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/)；发布时间：2026-10-19T00:00:00+08:00；定位：官方主文agentic insiders、Project Perception三层控制与model transparency；主文已读，链接产品资格/实测未核。；阅读范围：full-text；ID：`3917e17d2e227fd7bd99`。
  日期仅精确到天，无法确认 18:00 边界。

## 5. 模型与AI Infra论文

### KV驻留论文提示：Agent的显存成本还取决于空闲留存与部署位置

- arXiv 2610.22863v1于10月16日03:09:13 UTC投稿，RSS公告为19日00:00（-04:00）；本期按公告收录，不能称19日首次投稿。摘要研究M365四类生产工作流、逾1.21亿模型调用。
- 方法包括轨迹驱动回放、空闲上限、多分辨率KV留存和跨部署复用分析；用Llama-2-70B布局替代保密模型的容量估算不是生产集群实测HBM。只读摘要与版本史，未审全文表图、代码及量化误差，不推广其数值收益。

**产业判断：** 推导：缓存策略与路由可能共同决定长程Agent成本，内存分层和会话编排受益；反例是量化质量损失、迁移网络代价或不同业务闲置分布。观察真实业务留存时间、重算率与端到端质量。

**来源与核验范围：**
- [arXiv model and infra papers · Understanding KV Residency in Production-Scale Agentic LLM Workloads](https://arxiv.org/abs/2610.22863)；源站公告时间：2026-10-19T00:00:00-04:00；定位：arXiv摘要与Submission history v1；HTML全文404，未审PDF、完整实验、代码或独立复现。；阅读范围：abstract；ID：`66191c8d5be18f094fb7`。

### Self-HPO交替优化harness与策略模型，避免把系统改进全归因于模型

- arXiv 2610.22791v1于10月16日01:07:52 UTC投稿，RSS公告为19日00:00（-04:00）；本期是公告增量。Self-HPO让当前策略分析失败、提议harness，再在选定harness下做RL，难题进入下一轮搜索。
- 摘要报告Qwen3.5-35B-A3B在三项编码基准上受益，但本轮仅审摘要与版本史；未读完整实验、预算、harness配置与泄漏控制，虽然HTML可获取，也未称全文审核。故不引用分数作跨系统排名。

**产业判断：** 推导：模型与harness的共同演进可能提高任务效率，也会增加评测归因难度；反例是过拟合搜索集或训练成本高于推理收益。观察固定预算的未见仓库、单组件消融和数据污染控制。

**来源与核验范围：**
- [arXiv model and infra papers · Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791)；源站公告时间：2026-10-19T00:00:00-04:00；定位：arXiv摘要与v1版本史；全文HTML已定位但未完成审阅，未检查代码/训练与评测预算。；阅读范围：abstract；ID：`aa4ccde86d8a3d2eaf50`。

## 6. GPU与供应链

### Tenstorrent宣布15亿美元E轮，62亿美元是投后估值

- Tenstorrent 10月19日官网宣布完成USD1.5B E轮、USD6.2B投后估值，Trace Capital与Innovation X领投；资金用于Galaxy规模部署、全球商业扩展与AI/CPU IP。金额是融资与估值，不能作收入或已交付算力。
- 官网核对Jim Keller、Galaxy和TT-Ascalon/Tensix产品归属。相对既有卡/服务器/IP路线，本期增加融资与规模化计划；未审交割文件、量产交付和性能负载。日期仅到日，边界不确定。

**产业判断：** 资本可支持制造与软件生态扩张，开放权重推理客户可能获得更多供给选择；反例是资金未转化为可靠模型覆盖或交付。观察付费部署、量产节奏、客户迁移工时和同负载总成本。

**来源与核验范围：**
- [Tenstorrent Official Newsroom · Tenstorrent Announces a $1.5B Series E at a $6.2B valuation](https://tenstorrent.com/newsroom/tenstorrent-announces-series-e)；发布时间：2026-10-19T00:00:00+08:00；定位：官方Series E公告全文主文/用途/About Tenstorrent；官网首页产品归属；未审融资文件和独立性能。；阅读范围：full-text；ID：`aa5ca95cb8a0e67d9ecd`。
  日期仅精确到天，无法确认 18:00 边界。

### AWS宣布TorchNeuron原生PyTorch后端，开源安排在次日

- Amazon 10月19日公告TorchNeuron将通过PyTorch标准硬件接入机制支持Trainium2/3，称可用很少配置改动迁移既有代码；Apache2.0开源安排为10月20日PyTorch大会，本期不写成已完成开源。
- 新增是减少后端适配的产品路线及早期采用披露，涉及TorchTitan/FSDP和Hugging Face工具。Cartesia等案例为厂商陈述；没有固定模型/负载/精度、成本和正确性对照，不能认定所有PyTorch代码零迁移。

**产业判断：** 降低软件迁移成本可能扩大Trainium可服务市场，并给其他芯片供应商带来竞争压力；反例是算子覆盖、调试与分布式行为仍需适配。观察次日仓库/许可、真实迁移工时、质量和总账单。

**来源与核验范围：**
- [About Amazon · Amazon opens its AWS Trainium AI chips to every PyTorch developer, no rewrite needed](https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai)；发布时间：2026-10-19T13:00:10+00:00；定位：Amazon主文全部关键小节与What next；官方RSS时间13:00:10 UTC；未审次日仓库、完整算子覆盖或独立客户效果。；阅读范围：full-text；ID：`63cbe58e85a688d893e8`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 273 条（其中线索 26 条），精选 11 个事件；未注明日期 8 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Meta Muse Official Model Card：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Visko Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Stacklok Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Peppermint Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Microsoft Command Line：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Satya Nadella Public Article：failed；配置X链接403。；已知截断 0 条。
- Nous Research Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Healthleap Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- OpenAI News：checked；检查新闻RSS、低资源编程原文、Orchestra收购原文及ChatGPT release notes；HTTP403由浏览工具补读。locked chats页仅标20日，按既定来源默认Asia/Singapore可能与本期部分重叠，实际小时未核；不确定归期，留候选补核。；已知截断 0 条。
- OpenAI API Changelog：ok；最近一次检测到页面变化；检查于 10-21 06:03；已知截断 0 条。
- Anthropic Newsroom：checked；实际打开Newsroom/研究采集入口，公益基金18日事件前一期已收录，本期去重；未核私域渠道。；已知截断 0 条。
- Anthropic Research：ok；页面链接 25 个，最近一次新增 14 个；检查于 10-21 06:03；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 552 个，最近一次新增 52 个；检查于 10-21 06:03；已知截断 0 条。
- DeepSeek Research & News：checked；实际打开官网Research & News与API updates；updates现返回首个API调用页，Flash1017/搜索API属已收录旧事；页面变化无单独日期，不作本期新事件。；已知截断 0 条。
- DeepSeek API Change Log：ok；页面无变化；检查于 10-21 06:03；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-21 06:03；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- Alibaba / Qwen Blog：failed；官方博客返回空正文；兜底检索未取得本期官方新文，不能称无新闻。；已知截断 0 条。
- Qwen · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；实际打开Kimi Research Blog，当前列表最新7月16日；HF入口已采集，未覆盖私域/全部产品渠道。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-21 06:03；已知截断 0 条。
- Z.ai 发布记录：ok；最近一次检测到页面变化；检查于 10-21 06:03；已知截断 0 条。
- 智谱开放平台发布记录：ok；最近一次检测到页面变化；检查于 10-21 06:03；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- MiniMax News：checked；新闻列表仅导航，经官方模型链接读到10月19日M3.1 Flash正文，已归档；全站新闻列表仍不完整。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-21 06:03；已知截断 0 条。
- Mistral AI：ok；feed 91 条；检查于 10-21 06:03；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-21 06:03；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-21 06:03；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-21 06:03；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 1 条；检查于 10-21 06:03；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-21 06:03；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- ByteDance Seed Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- Alibaba Cloud Press Room：failed；Press Room只有空标题/导航，列表未加载；未覆盖公众号与完整公告。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-21 06:03；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-21 06:03；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-21 06:03；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-21 06:03；已知截断 0 条。
- xAI News：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-21 06:03；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 7 条；检查于 10-21 06:03；已知截断 0 条。
- Qualcomm Newsroom：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-21 06:03；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- ASML News：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- TSMC Newsroom：failed；配置最新新闻页超时；搜索兜底未完成全列表核查。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-21 06:03；已知截断 0 条。
- Reflection AI Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Namespace Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Vinci Official Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- TODAY Official Blog：failed；配置博客URL不可访问。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- GlobalFoundries Official News：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Meet Odyssey-3：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Decart官网：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Microsoft Official Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- 模思智能官方新闻：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- ModCraft产品官网：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Apple Newsroom：failed；Newsroom只返回导航，新闻列表未加载。；已知截断 0 条。
- Pluto Security：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- SemiGraph 半图科技：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Third Moment Research Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- HUMXN Official：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Sapiom Official Blog：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Tenstorrent Official Newsroom：checked；本轮实际阅读公司E轮公告及主页，核对融资/投后估值与Galaxy/CPU和AI IP归属；新加入跟踪，未计入起始123入口的机器采集覆盖。；已知截断 0 条。
- Orchestra Bio Official：checked；本轮实际读取官网加入OpenAI声明，并与OpenAI原文交叉核对；公司声明不是独立审计，未计入起始123入口机器采集覆盖。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；GitHub Releases API核对0.5.22正式时间/标记，限定读取Highlights与升级/安全；博客20日新文仅日精度，可能边界重叠，尚未核定本期增量。；已知截断 0 条。
- SGLang Blog：checked；实际读取博客日期列表；本期未确认新文，20日Omni文章无已核小时、可能边界重叠；未完成本期归属核查，留候选。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；API核对最新正式0.32.0为18日去重；19日Elastic EP主文与性能/后续范围已读；20日TorchTPU仅日精度，可能边界重叠，未核定归属。；已知截断 0 条。
- vLLM Blog：checked；实际读取博客与19日Elastic EP主文；20日TorchTPU仅日精度，边界归属未核，留候选。；已知截断 0 条。
- NVIDIA Dynamo：checked；API及Beam dev.1 release正文有限阅读：19日23:39:54Z为预发布、非QA版本；保留线索未纳正式发布事件；20日Muse dev.1窗口外。；已知截断 0 条。
- FlashInfer：checked；API近8版本核查；正式0.7.2为15日已收录；20日04:30rc5晚于截止。；已知截断 0 条。
- Mooncake：checked；GitHub API近8版本核查；最新0.3.14-rc1为9月7日预发布，无本期正式新版本，不代表仓库无提交。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-21 06:03；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- OpenBMB PilotDeck Official Repository：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；本轮500条候选保存60、截断432、列表不完整；20日公告晚于本期，使用已归档19日公告。两篇只审摘要/v1史；未完成其他论文全文核查。；已知截断 432 条。
- METR：ok；页面链接 27 个，最近一次新增 1 个；检查于 10-21 06:03；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-21 06:03；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 1 个；检查于 10-21 06:03；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-21 06:03；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- Vals AI：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- Epoch InnovationEval：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-21 06:03；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-21 06:03；已知截断 0 条。
- 工业和信息化部：ok；页面链接 21 个，最近一次新增 3 个；检查于 10-21 06:03；已知截断 0 条。
- 最高人民法院：ok；页面链接 83 个，最近一次新增 12 个；检查于 10-21 06:03；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-21 06:03；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个，最近一次新增 2 个；检查于 10-21 06:03；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-21 06:03；已知截断 0 条。
- 国家数据局：failed；官方入口返回空正文，未完成政策全文核查。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- The Information：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 10 条；检查于 10-21 06:03；已知截断 0 条；可能漏采 2026-10-18T09:55 至 2026-10-19T08:56；可能漏采 2026-10-19T22:00 至 2026-10-20T07:11。
- Financial Times Technology：ok；feed 25 条，关键词过滤 10 条；检查于 10-21 06:03；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-21 06:03；已知截断 0 条。
- New York Times Technology：ok；feed 20 条，关键词过滤 8 条；检查于 10-21 06:03；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 5 条；检查于 10-21 06:03；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 9 条；检查于 10-21 06:03；已知截断 0 条；可能漏采 2026-10-19T22:00 至 2026-10-20T21:00。
- Ars Technica AI：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 22 条；检查于 10-21 06:03；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-21 06:03；已知截断 0 条。
- 虎嗅：failed；采集器超时，浏览同源首页仍超时；不能推断无新闻。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 38 条；检查于 10-21 06:03；已知截断 0 条；可能漏采 2026-10-18T09:55 至 2026-10-20T05:56。
- 36氪：ok；feed 30 条，关键词过滤 20 条；检查于 10-21 06:03；已知截断 0 条。
- 钛媒体：ok；feed 17 条，关键词过滤 8 条；检查于 10-21 06:03；已知截断 0 条；可能漏采 2026-10-18T09:55 至 2026-10-19T18:36；可能漏采 2026-10-19T22:00 至 2026-10-20T16:07。
- 雷峰网：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-21 06:03；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-21 06:03；已知截断 0 条。
- C114 通信网：ok；页面链接 32 个，最近一次新增 21 个；检查于 10-21 06:03；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 63 条；检查于 10-21 06:03；已知截断 0 条；可能漏采 2026-10-18T09:55 至 2026-10-19T15:57；可能漏采 2026-10-19T22:00 至 2026-10-20T16:00。
- 机器之心：failed；仅会员导航/摘要入口；会员正文与微信公众号未覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；实际打开配置官方入口，仅核对本轮返回的可见主页、标题/日期片段或既有主文；未逐项访问全部外链和客户效果，未确认额外本期增量。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 99 个，最近一次新增 39 个；检查于 10-21 06:03；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- bloomberg-ai：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- ft-nyt-wsj-ai：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- china-ai-companies-zh：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- china-ai-policy-zh：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- china-chips-zh：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- embodied-world-models-zh：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- supply-chain-en：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。
- newsroom-fallback：checked；本轮围绕Oct18–19执行对应中英文、来源或主题检索；返回部分旧/无关结果，搜索不是完整覆盖；拟采用线索才回查原文，付费正文与私域仍有缺口。。

- 新公司发现：checked；执行中英文新创公司检索；回查Tenstorrent官方、Orchestra双方官网并新增跟踪。铭芯启睿只核媒体披露，实体暂缓；Laplace官网空正文，TechCrunch文内发布日期与活动时间有冲突，留候选。。

证据包：`data/packets/daily/2026/10/2026-10-19/3ace4cb9dae21f7de05710f87b712acd0eff33e047321f6aca9b4e385010874a.json`；采集 run：`20261020T220215-9601b4c9`。
