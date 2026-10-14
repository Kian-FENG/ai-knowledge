# AI 产业分析日报（2026.10.13）

统计窗口：2026-10-12T18:00:00-07:00 至 2026-10-13T18:00:00-07:00（洛杉矶时间，右端不含）。

本期变化集中在付费模型分发、个人助手入口与本地算力软件：Gemini 4 Argon开放API/订阅入口，苹果及中国终端把身份、行动与额度融入产品，Run:ai完整开源把GPU平台竞争延伸到管理与支持。Pluto和GEO营销融资显示AI采用正在带动治理与分发工具需求，但披露和媒体数据不等于独立效果。十条精选；论文栏无核实的新公告，部分正文、会员来源与五段媒体漏采未恢复。

## 1. MaaS市场与产品形态

### 苹果HomeView开放预购，Siri AI进入可识别家庭成员的常驻屏幕

- 苹果10月13日公告7英寸HomeView及Siri AI，最多识别6位用户。个人上下文及跨App行动需配对支持Apple Intelligence的iPhone或iPad；未配对时仍有部分对话和一般知识能力。
- 美国两种机型均为USD299，首批市场即日预购，11月13日起上市；新加坡10月15日开放预购。公告称欧盟因Siri AI当前不可用而不销售，不能外推全球交付。只有日期、窗口边界不确定，已对照前一期未重复。
- 新增是家庭共享硬件入口及身份切换，并非本日首次发布Siri AI。已读官网主文与可用性段；未测试设备或核实隐私隔离效果。

**产业判断：** 判断（derived）：常驻屏幕、家庭身份和手机上下文联动可能提高助手使用频率，苹果设备及家庭服务生态受益；设备配对门槛、地区限制或身份误识别会削弱采用。观察正式交付、跨App完成率、多用户隔离和持续使用。

**来源与核验范围：**
- [Apple Newsroom · Meet Apple HomeView](https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home/)；发布时间：2026-10-13T00:00:00+08:00；定位：Apple主文Personalized Experience、Siri AI、Pricing and Availability；浏览阅读笔记，非实机评测。；阅读范围：full-text；ID：`e8f5bd2da63e49edb020`。
  日期仅精确到天，无法确认 18:00 边界。

### Higgsfield客户案例：创作Agent把教学视频流程延伸到10分钟以上

- OpenAI于10月13日12:00 UTC发布客户案例，Higgsfield CEO称GPT-6 Astra创作Agent通过外部工具和3D任务处理，支持制作超过10分钟的教学视频，此前约1分钟。
- 这是多步骤生产流程的客户自报，不是单次视频模型直接输出10分钟成片；一致性、制作耗时、人工参与、总费用和成功率未独立验证。GPT-Image-2.5与Codex分别用于图像及原型环节。
- 相对既有生成工具，本期增量是长内容工作流采用案例。voice-to-movie/GPT-Live-1处于Looking ahead愿景；未记为正式交付。

**产业判断：** 判断（derived）：规划、工具和后期处理结合可能扩大长内容供给，创作平台与小团队受益；返工、素材一致性和人工审查可能抵消节省。观察每分钟合格内容成本、人工工时、重复生成率和真实付费留存。

**来源与核验范围：**
- [OpenAI News · Higgsfield takes AI video from 1 minute to over 10](https://openai.com/index/higgsfield-longer-videos-voice)；发布时间：2026-10-13T12:00:00+00:00；定位：OpenAI客户案例四节主文；HTTP403后浏览工具恢复；未观看视频或测试产品。；阅读范围：full-text；ID：`8d45898e533e591d4241`。

### 雷峰网：千问Go开放体验申请，个人办事Agent仍分批准入

- 雷峰网10月13日12:11北京时间正文转述千问官方公众号：千问Go内嵌千问App，已上线体验申请，逐步开放资格。未直接取得公众号原文或验证账户可用性，保留媒体归因。
- 报道列举理赔、预约、订餐及购物等任务；记者/用户演示不等于稳定完成率和全面支持。增量是申请入口及个人事务产品形态，不把申请开放写成全量正式可用。
- 价格、地区、具体权限和责任边界尚未核实。Qwen/千问属于阿里旗下品牌，未新建独立公司。

**产业判断：** 判断（derived）：消费平台服务接入可能让助手从回答扩展到履约，阿里分发和本地服务商受益；授权中断、外部客服失败或纠纷会放大交付成本。观察获准比例、可办任务范围、成功率、人工接管和收费。

**来源与核验范围：**
- [雷峰网 · 千问确认将推出「千问Go!」，已开放体验申请](https://www.leiphone.com/category/industrynews/GalDeSPl8orEfNoI.html)；发布时间：2026-10-13T12:11:00+08:00；定位：雷峰网完整RSS正文，申请入口/逐步开放/体验例子；公众号原文未取得。；阅读范围：feed-content；ID：`82db01910c5afa419a42`。

### 快科技：STEPX Neo先行版预售，硬件、模型额度与开发工具合并定价

- 快科技10月13日20:35:11北京时间报道STEPX Neo先行版16GB+256GB定价CNY3999，整合Step模型、Step AOS及Step Studio；当晚21:00预售、10月16日10:13正式开售，未当作已经大规模交付。
- 报道转述购买权益为连续12个月、每月100亿token额度；折算是100亿而非100万。具体适用模型、速率、费用与公平使用条款未核实，不能将额度当实测用量或免费无限推理。
- 端侧简单操作与云端规划、双域记忆及原子能力开放为厂商描述；本期新增系统产品与定价组合。已读完整媒体正文，未取得完整官方条款、设备或端到端评测。

**产业判断：** 判断（derived）：硬件、推理与开发入口捆绑可能降低开发者开始创作的摩擦，终端和应用生态受益；补贴额度、工具兼容和权限失败可能增加长期成本。观察开售交付、额度条款、活跃开发者、任务可靠性和续费。

**来源与核验范围：**
- [快科技（驱动之家） · 首款大模型原生智能体手机！阶跃STEPX Neo先行版发布：3999元](https://news.mydrivers.com/1/1157/1157185.htm)；发布时间：2026-10-13T20:35:11+08:00；定位：快科技完整RSS正文：软硬模全栈价、Token Plan、端云分工、Step Studio及预售时间。；阅读范围：feed-content；ID：`e6995110d45fdf8a40e0`。

## 2. AI公司发展与新公司

### Pluto Security结束隐身状态，披露4200万美元融资

- Pluto官网10月13日公告结束隐身状态并披露USD42M funding，未拆分轮次、估值或交割日；不能直接将媒体所述单轮金额加总替代官网口径。日期仅到天、窗口边界不确定，前一期未收录。
- 官方产品覆盖AI工具、MCP/插件供应链、生成产物和运行时行动的可见性与控制；公司称服务超过150万endpoint、ARR达数百万美元，均为未审计自报，ARR不是同期收入。
- 官网与About已核对品牌和产品归属；团队位于以色列与美国。新纳入跟踪不等于今天成立，法定主体与注册时间未核实。

**产业判断：** 判断（derived）：员工自行使用AI使权限和运行时控制成为独立采购需求，安全厂商受益；误拦截、安装负担或与现有终端安全重复会阻碍采用。观察独立客户验证、误报率、覆盖工具、续约及同口径ARR。

**来源与核验范围：**
- [Pluto Security · Welcome to Planet Pluto!](https://pluto.security/blog/welcome-to-planet-pluto/)；发布时间：2026-10-13T00:00:00+08:00；定位：Pluto公告完整主文和官网/About；融资/endpoint/ARR均保留公司归因。；阅读范围：full-text；ID：`e1aecba691ddadd92665`。
  日期仅精确到天，无法确认 18:00 边界。

### 36氪：深度云海获千万级天使轮，GEO向结果交付工作台延伸

- 36氪10月13日11:10:57北京时间报道深度云海近日完成CNY千万级天使轮、华工科技领投；精确金额、交割日和估值未披露，未取得投资方或公司原始公告。
- 报道描述GEO RaaS系统和DeepWork桌面工作台，连接可见性诊断、内容生产分发与监测，支持本地部署是公司主张。年收入数千万元及3000多家客户均为报道中的公司自报，期间/会计口径不明，不转写为ARR。
- 新增是融资报道及结果交付路线；排名/引用提升没有独立效果验证。公司一手身份来源尚未回查完成，本次不新建该公司实体；同名产品不合并。

**产业判断：** 判断（derived）：AI搜索推荐改变营销分发，监测与知识整理工具可能受益；平台引用规则变化、归因困难或内容质量下降会使结果付费难履约。观察可审计的增量获客、留存、退款、平台政策和客户实际转化。

**来源与核验范围：**
- [36氪 · 深度云海完成千万级天使轮融资，前百度搜索团队创办｜36氪首发](https://36kr.com/p/4023041152585603?f=rss)；发布时间：2026-10-13T11:10:57+08:00；定位：36氪完整RSS正文：融资首段、GEO系统、DeepWork、商业模式与限制；官网/投资方未核实。；阅读范围：feed-content；ID：`9e45e924f4d81d016cc1`。

## 3. 模型能力与技术演进

### Gemini 4 Argon向付费产品与API开放，百万token由输入输出共用

- Google于10月13日16:00 UTC宣布Argon全球推出：API付费层可在AI Studio/Gemini平台使用，Antigravity面向Ultra，Gemini App和AI Mode面向Ultra/Pro；具体地区和产品实际推送仍以账户为准。
- API提供1M统一输入输出token限额，不等于输入1M外再输出1M。公开模型引入价USD2/百万输入、USD10/百万输出，缓存输入折扣95%；11月30日优惠结束后标准价USD4/20。未核对全部长上下文、缓存存储和工具收费细则。
- 相对较早模型预告，本期新增可用入口和价格；长任务、科学与代码能力为Google/客户披露，未逐项审计模型卡、harness、预算和外链PR，不采用厂商领先排名或加速倍数。

**产业判断：** 判断（derived）：广泛分发与优惠价可能推动企业试用长任务，Google云和开发者工具受益；长输出、重试及后续标准价可能增加每任务成本。观察同harness成功率、实际总费用、续用及优惠结束后的迁移。

**来源与核验范围：**
- [Google AI Blog · Gemini 4 Argon: Built to solve your hardest problems](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)；发布时间：2026-10-13T16:00:00+00:00；定位：官网原始HTML及完整文章关键主文/Get started/价格脚注；Google Cloud完整RSS定价交叉回读；未完整模型卡。；阅读范围：full-text；ID：`74c9e10c02543c499970`。

## 4. AI Infra社区与工程趋势

### NVIDIA开源Run:ai完整平台，GPU调度与组织配额可分模块采用

- NVIDIA 10月13日14:19:40 UTC技术文章称完整Run:ai平台源码公开，包含KAI Scheduler、GPU Fractioning Operator、KAI Resource Management和Workload Map，可整体或分模块采用。相对较早只开源调度器，本期增量是完整平台。
- GPU Fractioning对接CUDA13.4原生显存配额；Workload Map描述工作负载结构，本身不调度、不排队或跨集群传播。文章列8家生态伙伴，不据此推导全部生产部署。
- 源码适用各自许可证；NGC Community Product仍需相应软件条款，不要求付费订阅但不含企业支持。未逐仓审核许可证、安装或测算利用率，因此不把开源直接等同免费运营。

**产业判断：** 判断（derived）：可组合调度、配额和GPU共享可能降低平台开发门槛，云服务商及集成商受益，也使支持和托管成为差异化。驱动版本、隔离要求与运维复杂度会限制节省；观察兼容性、真实利用率、故障恢复和支持成本。

**来源与核验范围：**
- [NVIDIA Technical Blog · NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)；发布时间：2026-10-13T14:19:40+00:00；定位：官方正文How to adopt、四组件与Community Product条款；未执行代码、未独立复核所有仓库许可。；阅读范围：full-text；ID：`b3dd2a0f914f65ea3ebf`。

### IBM以Inductor扩展替代独立编译栈，Spyre适配仍需专用后端

- PyTorch 10月13日12:45:30 UTC文章介绍torch-spyre改用backend=inductor，复用主体编译栈，并围绕128字节数据块、scratchpad和静态核分工增加树外扩展。相对10月8日原生设备语义文章，新增重点是编译器复用与维护。
- 作者用lizard统计排除测试/注释的代码行：原sendnn约273000行，新扩展约38600行；约7倍是扩展代码规模差异，不是推理速度，且新栈复用了Inductor，比较不等价。
- 最后一级仍由专有DeepTools生成硬件指令；关键预调度hook仍在推进正式上游支持。已读概述、架构、Evaluation和结论，未审全部代码/PR，不采用缺完整配置的kernel加速作为端到端效果。

**产业判断：** 判断（derived）：复用主流框架可减少替代加速器的软件维护负担，硬件和平台生态可能受益；专有后端、树外钩子和算子覆盖仍带来迁移成本。观察上游hook落地、升级兼容、应用覆盖和完整任务成本。

**来源与核验范围：**
- [PyTorch Foundation Blog · Extending Inductor for the IBM Spyre Accelerator](https://pytorch.org/blog/extending-inductor-for-the-ibm-spyre-accelerator/)；发布时间：2026-10-13T12:45:30+00:00；定位：PyTorch完整RSS中的TLDR、Overall structure、Evaluation、Wrapping up；中间算法非完整审计，未复现。；阅读范围：feed-content；ID：`7f13355308fbe95bb329`。

## 5. 模型与AI Infra论文

本期未收录经核验的新事件；覆盖情况见文末。

## 6. GPU与供应链

### RTX Spark上市前生态更新：PAIR结束beta，Bolt模型仍待10月15日

- NVIDIA 10月13日生态文章称RTX Spark笔记本计划10月16日上市，本期新增软件准备：PAIR当天退出beta、增加llama.cpp等支持；Broadcast2.3可下载，部分Agent已支持MXC。文章只有日期，边界不确定；前期硬件公告不重复算首发。
- Nemotron3.5 Bolt 74B-A9B的24GB/2bit模型计划10月15日发布；Hermes的部分OpenShell/MXC和路由集成仍为月底计划。不能把即将发布的权重、许可或软件能力写成已经交付。
- 本文只采用最高128GB统一内存的厂商规格描述，不据此估算可运行模型上下文或吞吐。未核对所有模型卡、软件包和实机，拒用通用性能排名。

**产业判断：** 判断（derived）：本地模型、隔离与云路由一起降低使用摩擦，PC硬件及本地Agent开发者受益；内存竞争、应用兼容、云升级费或低利用率会抵消收益。观察10月15/16实际交付、同任务能耗/延迟、软件完整性和总体费用。

**来源与核验范围：**
- [NVIDIA Blog · All Systems Go: Global PC App Ecosystem Ready for NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)；发布时间：2026-10-13T00:00:00+08:00；定位：官方生态主文Local agents、PAIR、Bolt、Broadcast、开发工具；未实测，未来时间均保留计划。；阅读范围：full-text；ID：`8bb1da51925f69396745`。
  日期仅精确到天，无法确认 18:00 边界。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 281 条（其中线索 41 条），精选 10 个事件；未注明日期 6 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Stacklok Official：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Peppermint Official：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Microsoft Command Line：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Satya Nadella Public Article：failed；X原帖本轮浏览工具失败；前期授权治理事件不重复。；已知截断 0 条。
- Nous Research Official：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Healthleap Official：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- OpenAI News：checked；已读本轮RSS、官网新闻列表、Higgsfield主文；API changelog及帮助中心已查看，未把旧条目当新发布。；已知截断 0 条。
- OpenAI API Changelog：ok；最近一次检测到页面变化；检查于 10-14 09:04；已知截断 0 条。
- Anthropic Newsroom：checked；已查官网新闻/研究列表及两篇研究主文、HTML日期；均为背景，修改时间未证明实质新增。；已知截断 0 条。
- Anthropic Research：ok；页面链接 11 个；检查于 10-14 09:04；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 531 个，最近一次新增 1 个；检查于 10-14 09:04；已知截断 0 条。
- DeepSeek Research & News：checked；已读API更新、官网/HF采集；当前可见changelog最新Sep10，无核实的本窗口新模型；Winverse投资传闻未取原文不采用。；已知截断 0 条。
- DeepSeek API Change Log：ok；页面无变化；检查于 10-14 09:04；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-14 09:04；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- Alibaba / Qwen Blog：failed；Web工具与原生浏览器均仅见导航，未取得新闻正文；非无新闻。；已知截断 0 条。
- Qwen · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；已读官方研究列表及HF入口，K3/PerceptionBench为旧日期；未证明本窗口新版本。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-14 09:04；已知截断 0 条。
- Z.ai 发布记录：ok；页面无变化；检查于 10-14 09:04；已知截断 0 条。
- 智谱开放平台发布记录：ok；页面无变化；检查于 10-14 09:04；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- MiniMax News：failed；Web工具与原生浏览器均仅见导航/精选，未恢复日期完整列表。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-14 09:04；已知截断 0 条。
- Mistral AI：ok；feed 89 条；检查于 10-14 09:04；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 2 条；检查于 10-14 09:04；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-14 09:04；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-14 09:04；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 1 条；检查于 10-14 09:04；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-14 09:04；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- ByteDance Seed Blog：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- Alibaba Cloud Press Room：checked；Web提取无正文；原生浏览器恢复列表，最新Genting Oct12为窗口前背景，未纳入。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-14 09:04；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-14 09:04；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-14 09:04；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-14 09:04；已知截断 0 条。
- xAI News：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-14 09:04；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 8 条；检查于 10-14 09:04；已知截断 0 条。
- Qualcomm Newsroom：checked；浏览工具恢复日期列表，见Oct12三条宽带/研究项目，未确认本窗口有模型或算力供给实质变化。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-14 09:04；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。
- ASML News：failed；浏览工具访问失败；未恢复本窗口完整新闻列表。；已知截断 0 条。
- TSMC Newsroom：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-14 09:04；已知截断 0 条。
- Reflection AI Blog：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Namespace Blog：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Vinci Official Blog：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- TODAY Official Blog：failed；官方/blog本轮浏览工具失败，旧融资不重复。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- GlobalFoundries Official News：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Meet Odyssey-3：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Decart官网：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Microsoft Official Blog：checked；已打开官方首页，Maia路线为Oct12已收录，未发现新的可核实正文。；已知截断 0 条。
- 模思智能官方新闻：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- ModCraft产品官网：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Apple Newsroom：checked；实际阅读HomeView官方完整主文及可用性；新增来源在collect之后人工核查。；已知截断 0 条。
- Pluto Security：checked；实际阅读官网、About和Oct13融资主文；新增来源在collect之后人工核查。；已知截断 0 条。
- SemiGraph 半图科技：checked；Web超时后原生浏览器恢复官网身份/角色与旧日期新闻；当前融资仅背景。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；核对GitHub Releases与博客，latest v0.5.21显示Oct2，旧版去重。；已知截断 0 条。
- SGLang Blog：ok；页面链接 7 个，最近一次新增 1 个；检查于 10-14 09:04；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；GitHub/Atom本轮新记录为v0.32.0rc0，updated Oct12T20:49Z在窗口前；没有当稳定release。；已知截断 0 条。
- vLLM Blog：ok；页面链接 147 个；检查于 10-14 09:04；已知截断 0 条。
- NVIDIA Dynamo：checked；核对开发快照和原文，MiniMax dev非QA/非生产；旧release/更新去重。；已知截断 0 条。
- FlashInfer：checked；核对v0.7.2rc3，明确RC而非稳定版；未形成长期价值新事件。；已知截断 0 条。
- Mooncake：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-14 09:04；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；RSS仍Oct12两篇已收录论文；Web实际查看cs.AI/new为Oct12、313条，cs.DC/recent为Oct12；未穷尽所有条目/类别，没有核实Oct13公告。；已知截断 0 条。
- METR：ok；页面链接 26 个；检查于 10-14 09:04；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-14 09:04；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 1 个；检查于 10-14 09:04；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-14 09:04；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- Vals AI：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- Epoch InnovationEval：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-14 09:04；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个，最近一次新增 1 个；检查于 10-14 09:04；已知截断 0 条。
- 工业和信息化部：ok；页面链接 21 个；检查于 10-14 09:04；已知截断 0 条。
- 最高人民法院：ok；页面链接 82 个，最近一次新增 6 个；检查于 10-14 09:04；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-14 09:04；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个；检查于 10-14 09:04；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 17 个；检查于 10-14 09:04；已知截断 0 条。
- 国家数据局：checked；Web为空；原生浏览器恢复官网政策与动态列表，已检查可见范围，不宣称全站完整。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条；可能漏采 2026-10-13T01:04 至 2026-10-13T09:55。
- The Information：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 7 条；检查于 10-14 09:04；已知截断 0 条。
- Financial Times Technology：ok；feed 25 条，关键词过滤 8 条；检查于 10-14 09:04；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-14 09:04；已知截断 0 条。
- New York Times Technology：ok；feed 20 条，关键词过滤 9 条；检查于 10-14 09:04；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 8 条；检查于 10-14 09:04；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 4 条；检查于 10-14 09:04；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 23 条；检查于 10-14 09:04；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-14 09:04；已知截断 0 条；可能漏采 2026-10-13T01:04 至 2026-10-13T04:01。
- 虎嗅：failed；RSS超时，Web兜底仍失败；未恢复全窗口。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 26 条；检查于 10-14 09:04；已知截断 0 条；可能漏采 2026-10-13T01:04 至 2026-10-13T13:02。
- 36氪：ok；feed 30 条，关键词过滤 16 条；检查于 10-14 09:04；已知截断 0 条。
- 钛媒体：ok；feed 17 条，关键词过滤 9 条；检查于 10-14 09:04；已知截断 0 条；可能漏采 2026-10-13T01:04 至 2026-10-13T18:26。
- 雷峰网：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-14 09:04；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-14 09:04；已知截断 0 条。
- C114 通信网：checked；collect被robots限制；浏览工具恢复原生日期列表，未逐条阅读全文。；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 54 条；检查于 10-14 09:04；已知截断 0 条；可能漏采 2026-10-13T01:04 至 2026-10-13T17:14。
- 机器之心：failed；已读首页可见Week41与专题列表，会员/公众号正文未覆盖，正文不足仍记失败覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；已实际打开配置官网/文章入口，核查可见列表或旧资料；没有核实到本窗口实质新增。不代表账户实测或全站完整覆盖。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 94 个，最近一次新增 28 个；检查于 10-14 09:04；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- bloomberg-ai：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- ft-nyt-wsj-ai：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- china-ai-companies-zh：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- china-ai-policy-zh：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- china-chips-zh：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- embodied-world-models-zh：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- supply-chain-en：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。
- newsroom-fallback：checked；本轮实际按2026-10-12至14日期范围执行对应主题检索；搜索结果仅作线索。Reuters/Bloomberg/FT/WSJ付费原文、公众号与未回查交易不作已核实事实。。

- 新公司发现：checked；实际执行英文new AI startup funding launch与中文AI新公司/融资/具身检索；回查Pluto及SemiGraph官网。Winverse金额/估值冲突、Ubitium/Clueso等未读一手，不采用；深度云海仅媒体归因。。

证据包：`data/packets/daily/2026/10/2026-10-13/5a8288e4008e5b9c440e8d78a83a7bc01d17558c94394edf6a092b7416899ee3.json`；采集 run：`20261014T010312-72922c75`。
