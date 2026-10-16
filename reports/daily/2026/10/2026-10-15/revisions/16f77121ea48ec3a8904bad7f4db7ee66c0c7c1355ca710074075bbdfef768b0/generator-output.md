# AI 产业分析日报（2026.10.15）

统计窗口：2026-10-14T18:00:00-07:00 至 2026-10-15T18:00:00-07:00（洛杉矶时间，右端不含）。

本期16个事件显示，模型供给向开放权重、专用时序与多模态Agent扩展，消费端分发则连接语音、实验室席位和个人记忆。许可、API连续性、实时SLO与评估访问决定这些供给能否转成可靠服务；这属于本报告研究判断。先查已发布知识，再核对原文；Visko为新增跟踪，合作和demo发生于更早日期。覆盖受Qwen/MiniMax正文不可得、付费/私域、三段媒体漏采及arXiv254条本地截断限制；实际编辑于2026-10-15T18:17:24.088309-07:00（America/Los_Angeles），来源日期仍沿用Asia/Singapore默认解析，只有日期时明确边界不确定。

## 1. MaaS市场与产品形态

### OpenAI向美国大学实验室开放Rosalind学术计划申请，最多30席免费12个月

- OpenAI于10月15日宣布：符合资格的美国大学实验室可申请最多30个Business Standard席位，最长12个月免费；GPT-Rosalind仍须trusted-access审核，当前不含API。有既有Enterprise协议的学校走校内流程。
- 相对已有模型与科研资源计划，新增的是面向实验室的申请和补贴分发路径；申请开放不代表所有实验室即时获批，案例演示也不是生物科研结果验证。

**产业判断：** 以团队席位降低试用成本，可能帮助生命科学工具进入实验室协作流程，受益环节包括工具编排和数据接入。反例是审批或实验验证成为主要瓶颈；观察获批实验室、实际使用和补贴结束后的留存。

**来源与核验范围：**
- [OpenAI News · Bringing GPT-Rosalind to academic research labs](https://openai.com/index/introducing-the-rosalind-academic-plan/)；发布时间：2026-10-15T19:00:00+00:00；定位：What the plan includes / Apply / Responsible access；公告正文有限摘录，未验证演示。；阅读范围：full-text；ID：`30cfe39b8242ef6e2465`。

### Bee把个人记忆接入Alexa与购物：Frontier现售，Eclipse仍待上市

- Amazon 10月15日宣布，Bee Frontier已在Amazon.com以USD74.99销售；磁吸手机配件Bee Eclipse将随后上市，起价USD99.99。购买设备包含摘要、回顾及14天记忆；Bee Pro为USD11.99/月，新用户30天试用，Alexa+/购物/第三方应用集成等属于Pro权益。
- 新增是硬件形态和记忆向行动、购物分发的连接。音频处理后删除、密钥和可见指示灯为Amazon产品说明，本项目没有做隐私或续航测试；地域可用性未穷尽核对。

**产业判断：** 记忆硬件的持续价值可能来自后续待办和交易，订阅将高价值集成与低价设备分开收费。反例是错误记忆、授权摩擦或用户不愿持续佩戴；观察Pro转化、使用留存、误触发率和可撤销操作。

**来源与核验范围：**
- [About Amazon · Amazon introduces Bee Frontier and Bee Eclipse](https://www.aboutamazon.com/news/devices/amazon-personal-ai-bee-frontier-bee-eclipse)；发布时间：2026-10-15T11:55:24+00:00；定位：官方正文，How Bee works / Privacy / Availability and pricing；未购买测试。；阅读范围：full-text；ID：`3d3f739df8190a2d5fa9`。

### DeepSeek故障后宣布返还七天API消耗赠金，恢复更新落入本期

- 快科技10月15日18:03（中国时间）引述DeepSeek开放平台通知：故障从北京时间08:11开始、13:04恢复；10月8日至14日API消耗金额将以赠金返还，后续先扣赠金，并非现金退款。
- 时区换算：故障开始为洛杉矶10月14日17:11，在本期开始前；恢复为22:04，及后续补偿披露属于本期进展。官网状态主页与history实际打开，但历史事件未渲染，未独立取到原通知或核对所有账户到账；具体根因未知。

**产业判断：** 服务中断把MaaS竞争从单价延伸到连续性、备用路由和重试成本，下游Agent服务更易承压。赠金可补偿费用但不能回补任务延误；观察后续事故报告、尾延迟、可用性与故障切换后的任务一致性。

**来源与核验范围：**
- [快科技（驱动之家） · DeepSeek故障近5小时！官方大方发补偿：所有API用户7天内的消耗金额全返](https://news.mydrivers.com/1/1157/1157790.htm)；发布时间：2026-10-15T18:03:16+08:00；定位：媒体完整feed正文；官方状态/history有限可见，原补偿通知未直接获得。；阅读范围：feed-content；ID：`b5daba44536f7d1dce38`。

### GPT-Live原生接入Decisions，让语音中的判断直接触发应用动作

- OpenAI API 10月15日changelog为gpt-live-1/gpt-6-luna与v1/live/sessions列出原生Decisions集成：Live可直接委派，或根据输入/输出转写增量触发。文档要求应用执行动作后读取真实状态，再回报结果。
- 相对10月6日已入库的Decisions公开beta，新增的是语音会话内的调用通路；不由此宣称Decisions已全面GA或所有语音功能统一降价。日期仅到日，窗口边界不确定；已对照前期去重。

**产业判断：** 省去应用中转的一次往返有望改善交互响应，实时助手和设备控制可受益，但动作正确性仍依赖状态读回与权限。反例是转写抖动导致错误触发；观察端到端尾时延、取消/重复执行率和完整账单。

**来源与核验范围：**
- [OpenAI API Changelog · OpenAI API changelog — native Decisions integration in GPT-Live](https://developers.openai.com/api/docs/changelog)；发布时间：2026-10-15T00:00:00+08:00；定位：10月15日changelog；decisions-voice概述、触发与Run actions；未运行代码。；阅读范围：full-text；ID：`49e8d0577a5e1f9d20fd`。
  日期仅精确到天，无法确认 18:00 边界。

### ChatGPT Voice开始推送GPT-Live-1.1与Quip，新增多语言声音

- OpenAI帮助中心10月15日release notes称，GPT-Live-1.1与mini版本GPT-Live-1.1 Quip正在ChatGPT Voice推送；新增法、德、印地、日、韩、墨西哥西语及英语Bubbie声音，实际选项依地域和账户变化。
- 新增为消费端语音模型与声音分发；更自然口音属于厂商陈述，没有本期可比语音评测或统一账户完成推送证据。日期仅到日，边界不确定。

**产业判断：** 语言和声音选择可能增加语音助手使用频率，交互设计的重要性提高。反例是识别、延迟或地区覆盖仍限制留存；观察分地区可用率、误识别和长对话任务完成率。

**来源与核验范围：**
- [OpenAI News · ChatGPT release notes — October 15, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；发布时间：2026-10-15T00:00:00+08:00；定位：仅October15语音release-note小节；未测试账户或音频。；阅读范围：full-text；ID：`3930e8dede7666d8dfd2`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Anthropic让六名METR评估者获得近似内部风险团队访问

- Anthropic 10月15日披露，六名METR员工已获得公司设备、办公空间及近似内部风险评估团队的工具/系统访问；客户资料、法律保密及部分架构信息受例外限制。
- METR可自行发布评估，Anthropic不能否决发表，但可依预定义敏感类别要求删减，METR可公开评论删减。新增相对既有风险报告外部审阅的访问深度；这不是已公布的新评估结果，也不是所有合作机构均有相同权限。

**产业判断：** 评估供给从外部接口测试延伸到流程和事故证据，模型公司与评估机构的协作成本上升。反例是访问例外或长期合作依赖影响结论；观察公开评估的具体发现、删减争议及建议执行。

**来源与核验范围：**
- [Anthropic Newsroom · An update on independent evaluators](https://www.anthropic.com/news/an-update-on-independent-evaluators)；发布时间：2026-10-15T00:00:00+08:00；定位：全文，employee-like access / three tiers / SecureBio更新脚注；未独立核实内部权限。；阅读范围：full-text；ID：`c3f9aa1e97f35f2465d0`。
  日期仅精确到天，无法确认 18:00 边界。

### 新增跟踪Visko：Orbis实时世界模型披露TPU部署案例

- Visko CEO与Google Cloud工程师10月15日联合介绍Orbis：文本/图像起始、可持续输入提示改变视频流；公开demo为9月1日，TPU合作始于8月，所述30天部署是历史过程，本期新增是技术案例披露。官网核对Orbis/Morphe/Kinesis归属及Visko Platform, Inc.页脚，法定注册与融资未核。
- 案例报告BF16、batch1、单TPU slice，视频1664×936/18fps并配同步音频，通过Ulysses上下文并行及局部JAX改写实现约1.07倍播放速度。TPU代际、切片规格、软件commit和完整负载未给齐；未将5.8倍音频局部加速当全链路收益，也不做GPU/TPU成本排名。

**产业判断：** 持续交互视频把供给瓶颈转为逐块截止时间与长会话稳定性，云端协同优化服务可能受益。反例是约7%余量不足抵抗抖动、多人并发或网络开销；观察长会话卡顿、并发SLO、单位会话成本与真实付费。

**来源与核验范围：**
- [Google Cloud Blog · How Visko streams real-time world models on Google Cloud TPUs](https://cloud.google.com/blog/products/media-entertainment/how-visko-streams-real-time-world-models-on-google-cloud-tpus/)；发布时间：2026-10-15T16:00:00+00:00；定位：Google Cloud案例全文与Visko官网可见产品；厂商联合案例，未复现。；阅读范围：full-text；ID：`74066ea0287245909be9`。

## 3. 模型能力与技术演进

### Meta发布Muse Spark Open权重，MaaS许可设收入门槛

- Meta 10月15日发布Muse Spark Open：816B总参数/42B激活、1M上下文，输入含文本/图像/音频/视频、输出文本，提供BF16及NVFP4。PyTorch团队披露SGLang/vLLM推理和TorchTitan微调支持；未复核厂商“最强”等排名。
- 相对8月Muse Spark及10月Muse Wonder消息，新增是Spark分支的权重交付和部署生态。Muse Model License要求署名及使用政策；经营MaaS的被许可方及关联方，任意连续12个月合计毛收入超过USD20M，须先通知并另签协议，门槛不是仅该模型营收。HF有访问申请门禁；不能称无限制MIT/Apache开源。日期部分仅到日，边界不确定。

**产业判断：** 开放权重增加企业定制和多供应商部署选择，同时许可条款可能改变大规模MaaS的议价与分发成本。反例是总权重驻留、长上下文缓存和协议条件抵消API替代收益；观察许可协议、同任务成本与真实部署。

**来源与核验范围：**
- [PyTorch Foundation Blog · Muse Spark Is Now an Open-Weights Model](https://pytorch.org/blog/muse-spark-open/)；发布时间：2026-10-15T17:55:52+00:00；定位：PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。；阅读范围：feed-content；ID：`71debadc09deb421fd5e`。
- [Meta Muse Official Model Card · Muse Spark Open model card and Muse Model License](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)；发布时间：2026-10-15T00:00:00+08:00；定位：PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。；阅读范围：full-text；ID：`0ca06b6fd0946a717fe7`。
  日期仅精确到天，无法确认 18:00 边界。

### NVIDIA发布Nemotron 3.5 Super VL，强调多模态专用Agent定制

- NVIDIA 10月15日介绍120B总参数/12B激活的多模态MoE，支持文本、图像、文档和视频理解及工具调用；发布基础、后训练、NVFP4检查点，配套数据与训练资源。
- 新增是Super VL模型和定制生态；公司说明NVFP4在Blackwell使用4位权重/激活，其他平台可为4位权重/16位激活。客户成本/延迟倍数、排行榜及未来效果未具备本项目完整可比harness，均未用于排名；已读技术博客，未逐份读取模型卡/许可/技术报告或验证服务商交付。

**产业判断：** 统一视觉与工具调用减少多模型交接，适合组织专用Agent；训练数据、策略和部署支撑仍决定成本。反例是量化误差或工具行为回归；观察同一工作流成功率、后训练投入与完整任务账单。

**来源与核验范围：**
- [NVIDIA Technical Blog · NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)；发布时间：2026-10-15T18:01:00+00:00；定位：官方技术博客全文，Architecture / customization / mixed precision / release；未复现性能。；阅读范围：full-text；ID：`bc3eb8977fc1d5b5926a`。

### Mistral推出Timestral时序模型，最大209M并支持已知未来协变量

- Mistral 10月15日发布首个时序基础模型家族Timestral，参数5M/28M/123M/209M、上下文32768时间步、21分位数预测，支持多变量、过去与已知未来协变量。公告称已发布GitHub仓库，通过Forge提供定制和本地/VPC/隔离部署，许可标为Modified MIT。
- 相对Large4通用模型预览，新增为数值预测专用路线。GIFT-Eval/TIME/fev-bench领先为Mistral自测，基准版本与完整harness未核；CPU延迟缺具体型号/完整软件配置，未采用其数值排名。技术报告仍待发布，完整许可条款未审。

**产业判断：** 小型数值模型可与语言Agent分工，把预测和解释分开，制造、能源和计划系统可能减少GPU依赖。反例是生产分布漂移、数据泄漏或校准不足；观察滚动回测、区间覆盖、域内重训和决策收益。

**来源与核验范围：**
- [Mistral AI · Introducing Timestral](https://mistral.ai/news/timestral/)；发布时间：2026-10-15T12:00:00+00:00；定位：官网完整公告，family / contributions / Forge / specs；无独立复现。；阅读范围：full-text；ID：`51edf4c643816e6fc69a`。

## 4. AI Infra社区与工程趋势

### FlashInfer v0.7.2正式版扩展Rubin与Blackwell的MoE和注意力路径

- FlashInfer正式Release v0.7.2（tag d84335d）扩展Rubin SM107的MoELayer/Frost、MLA和线性注意力等路径，DeepSeek-V4 NVFP4稀疏MLA覆盖B200/B300；区别于同日rc标签。
- 相对已入库v0.7.1，新增硬件/精度后端与自动选择。Frost路径需要PyTorch2.14，SM107需要CUDA13.4及以上相关汇编工具；部分低精度路径为opt-in。只是框架能力发布，不代表每种模型已在所有硬件生产验证，也不推出吞吐排名。

**产业判断：** 模型架构和GPU代际分化促使推理库承担更多后端选择与依赖管理，硬件供应商和服务平台均受影响。反例是升级回归或精度不稳；观察同负载正确性、延迟分位数及依赖升级成本。

**来源与核验范围：**
- [FlashInfer · Release v0.7.2](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.2)；更新时间：2026-10-15T21:09:16+00:00；定位：官方Atom的Highlights、升级说明及GitHub对应部分；完整Atom归档，PR清单未逐项审读，未运行。；阅读范围：feed-content；ID：`a8f42b47e2fb9fd0b155`。

### Dynamo提供Nemotron Super VL实验配方，尚非QA生产版本

- Dynamo v1.6.0-nemotron-3.5-super-vl-dev.1（tip5f601db）加入Nemotron3.5 Super VL的vLLM与TensorRT-LLM实验支持；明确非QA门禁、非生产推荐。配方以NVFP4权重、FP8 KV、MTP、会话亲和及最长1M上下文组织部署。
- 相对昨日GLM/SGLang快照，新增不同模型及后端。vLLM基于cu134 nightly bb87d227，TensorRT-LLM1.3.0rc29/CUDA13.1，后者配方仅覆盖B200。VR200公布结果使用合成MTP接受长度，配方默认自然接受；未把其配置清单当通用实测性能。

**产业判断：** 混合模型落地需要同时处理状态恢复、缓存转移与路由；配方降低初试成本，但成熟度决定运营风险。反例是自然接受率和多模态正确性削弱收益；观察稳定release、真实轨迹与完整并发测试。

**来源与核验范围：**
- [NVIDIA Dynamo · Dynamo v1.6.0-nemotron-3.5-super-vl-dev.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-nemotron-3.5-super-vl-dev.1)；更新时间：2026-10-15T22:09:49+00:00；定位：官方Atom完整release，Summary / versions / recipes / Known Issues；无部署实验。；阅读范围：feed-content；ID：`5cbe67fd966ea05f6f22`。

### ExecuTorch把PyTorch部署链扩展到Cortex-M CPU，混合NPU路径仍有覆盖边界

- PyTorch 10月15日说明Cortex-M后端已在ExecuTorch仓库可用，以CMSIS-NN和INT8量化支持Scalar/DSP/MVE，减少转其他框架的步骤；可与Ethos-U分区协作，不支持的操作仍回退portable kernels。
- 新证据是CPU后端工作流及板卡案例，而非端侧大语言模型全面适配。文中性能是作者在Alif E8单M55/400MHz、INT8、Alif kit harness的自测，不是官方MLPerf提交；本期不比较榜单或宣称所有MCU相同收益。流式唤醒词、更多注意力算子和混合精度扩展仍为后续工作。

**产业判断：** 统一训练到部署栈可能降低传感器、常开视觉的迭代成本，嵌入式团队受益。反例是算子覆盖和板卡适配仍需维护；观察模型行为一致性、工具链/固件版本、内存与实际功耗。

**来源与核验范围：**
- [PyTorch Foundation Blog · Bringing ExecuTorch to Arm Cortex-M CPUs](https://pytorch.org/blog/bringing-executorch-to-arm-cortex-m-cpus/)；发布时间：2026-10-15T14:40:35+00:00；定位：全文，Backend / Ethos-U / benchmark条件 / What is Next；不执行低层移植。；阅读范围：feed-content；ID：`ca958c8cd004e7ceb911`。

## 5. 模型与AI Infra论文

### 论文以SLO和goodput选择并行配置，不把TP或PP当固定最优

- arXiv2610.19405v1实际投稿为10月14日01:53:24UTC，RSS公告日为10月15日；本期收录公告，非当天首次投稿。仅阅读摘要与版本史。
- 作者构建TTFT–ITL可行集合及Pareto边界，以满足SLO的goodput分析TP/PP和长上下文取舍。摘要报告不同负载与约束下最优区域迁移；硬件、模型、精度、并发和完整SLO未从全文核查，因此不外推“PP总比TP好”。

**产业判断：** 部署选择应围绕业务延迟约束而非单一吞吐，服务平台可用满足SLO的请求量衡量资源效率。反例是不同互联或请求分布改变边界；后续核对实验矩阵、代码及真实服务轨迹。

**来源与核验范围：**
- [arXiv model and infra papers · Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off](https://arxiv.org/abs/2610.19405)；源站公告时间：2026-10-15T00:00:00-04:00；定位：arXiv abstract / submission history；15页正文、7图未读，公告仅日精度。；阅读范围：abstract；ID：`4200f796e86a8fac4bbe`。
  日期仅精确到天，无法确认 18:00 边界。

### Interlock用完成图约束长程Agent，区分局部正确与任务完整

- arXiv2610.19686v1实际投稿为10月14日07:09:46UTC，RSS公告10月15日；只读摘要和版本史。
- 作者以typed completion graph连接证据、决策、联合约束和必需效果，编译为可重置工作区/请求/rubric；用agent-as-judge与验证脚本筛轨迹，再训练两个Qwen3.6骨干。摘要报告外部任务指标改善，但具体骨干、预算、harness版本与全文消融未核，不作跨模型排名。

**产业判断：** 训练数据价值可能来自跨产物依赖和最终效果，而非逐步动作正确，企业Agent评测与环境供应商可能受益。反例是judge偏差或合成环境与生产差异；观察人审一致率、未见任务迁移和全部要求完成率。

**来源与核验范围：**
- [arXiv model and infra papers · Interlock: From Local Correctness to Task Completion in Long-Horizon Agents](https://arxiv.org/abs/2610.19686)；源站公告时间：2026-10-15T00:00:00-04:00；定位：摘要与v1版本史；未审全文、代码、训练预算或独立复现。；阅读范围：abstract；ID：`ac8626d0b39c368eabcb`。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

### 台积电Q3营收467.2亿美元，Q4指引仍是未来展望

- 台积电10月15日披露截至9月30日Q3合并TIFRS：营收NT$1,494.24 billion（USD46.72 billion），净利NT$763.06 billion，毛利率66.4%；2nm占晶圆收入8%，7nm及以下79%。季度营收、净利及工艺占比均为公司披露。
- 新增为Q3实绩；Q4营收USD52.3–54.3 billion及毛利率65–67%是管理层指引，假设USD/NTD31.8，不是已实现收入。公告未单列AI收入或可交付GPU数量；不能由总营收推断某类GPU供给。日期仅到日、边界不确定。

**产业判断：** 先进节点需求与2nm爬坡继续影响AI芯片采购、资本投入和交付周期，晶圆供给仍只是封装/存储之前的一环。反例是客户结构或汇率带动收入、封装瓶颈限制出货；观察产能利用率、先进封装、HBM与实际交期。

**来源与核验范围：**
- [TSMC Newsroom · TSMC Reports Third Quarter 2026](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/526b65af7305df2dde6b9ece6812b1fdf1e49f9b/3Q26%20EarningsRelease.pdf)；发布时间：2026-10-15T00:00:00+08:00；定位：官方两页Earnings Release与page1视觉核查；未读电话会/Management Report。；阅读范围：full-text；ID：`c802009aef9ffa1c92dc`。
  日期仅精确到天，无法确认 18:00 边界。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 379 条（其中线索 32 条），精选 16 个事件；未注明日期 7 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Meta Muse Official Model Card：checked；collect后新增浏览入口；已读HF可见模型卡概述、访问门禁和许可1–3条，未登录下载/核完整harness。；已知截断 0 条。
- Visko Official：checked；本轮collect后新增入口；已读官网全部可见产品和联合Google Cloud技术案例，法定注册/融资未核。；已知截断 0 条。
- Stacklok Official：checked；实际打开公司页，核对可见产品身份；没有核实本期带日期新公告，旧融资不重报。；已知截断 0 条。
- Peppermint Official：checked；指定官方融资文章日期10月8日，既有背景去重；未把采集日当融资日。；已知截断 0 条。
- Microsoft Command Line：checked；打开Microsoft-Decision-1既有正文入口；仅有限阅读，10月9日背景不重报。；已知截断 0 条。
- Satya Nadella Public Article：failed；指定X文章浏览工具获取失败；没有正文，不推断无动态。；已知截断 0 条。
- Nous Research Official：checked；实际打开官方首页，可见有限文字；未完成所有公告时间diff与正文重读。；已知截断 0 条。
- Healthleap Official：checked；打开官方产品首页有限文字；此前融资为背景，未复核本期所有新闻。；已知截断 0 条。
- OpenAI News：checked；RSS已采集，实际读Rosalind资格/申请/保障及ChatGPT10月15日release notes；官网HTTP403通过网页工具补读。；已知截断 0 条。
- OpenAI API Changelog：checked；采集器403；网页工具恢复官方changelog，并读10月15日GPT-Live/Decisions与文档相关小节。；已知截断 0 条。
- Anthropic Newsroom：checked；官网news列表和10月15日METR原文全文已读；原文更新脚注保留，未将预期结果当评估完成。；已知截断 0 条。
- Anthropic Research：ok；页面链接 11 个；检查于 10-16 09:03；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 534 个，最近一次新增 1 个；检查于 10-16 09:03；已知截断 0 条。
- DeepSeek Research & News：checked；自动采集官方入口；另打开API更新日志，顶端9月10日；状态主页与history打开但事故内容未渲染，故障补偿只归因媒体。；已知截断 0 条。
- DeepSeek API Change Log：checked；实际读取官网更新日志顶端9月10日V4.1Flash旧公告；未核实本期新模型首发。；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-16 09:03；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- Alibaba / Qwen Blog：failed；网页工具返回空；原生浏览器实际打开仍只有导航和页脚，没有本期日期列表/正文；阿里云press-room不能替代Qwen正文。；已知截断 0 条。
- Qwen · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；实际打开官方Research列表，顶端Kimi K3/PerceptionBench为7月16日；产品渠道与私域未全面覆盖。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-16 09:03；已知截断 0 条。
- Z.ai 发布记录：ok；页面无变化；检查于 10-16 09:03；已知截断 0 条。
- 智谱开放平台发布记录：ok；页面无变化；检查于 10-16 09:03；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- MiniMax News：failed；网页工具与原生浏览器实际打开news仅导航，未获取本期文章。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-16 09:03；已知截断 0 条。
- Mistral AI：ok；feed 90 条；检查于 10-16 09:03；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-16 09:03；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-16 09:03；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-16 09:03；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 1 条；检查于 10-16 09:03；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个，最近一次新增 2 个；检查于 10-16 09:03；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- ByteDance Seed Blog：checked；实际打开官方Research入口，有限文本；未全面读公众号或全部文章。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- Alibaba Cloud Press Room：checked；实际打开阿里云press-room但有限可见内容；千问私域/电商条款没有新增核验。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-16 09:03；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-16 09:03；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-16 09:03；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-16 09:03；已知截断 0 条。
- xAI News：checked；实际看官方News，顶端Grok Voice3为10月14日已收录背景；不重作本期发布。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-16 09:03；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 9 条；检查于 10-16 09:03；已知截断 0 条。
- Qualcomm Newsroom：checked；打开官方releases列表，有限可见文本；未逐条阅读全文，不能确认整站无新闻。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-16 09:03；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。
- ASML News：failed；本轮官方press-releases入口网页工具失败；昨日Q3来源已入库，本轮未重查其IR全文，不当作今日新财报。；已知截断 0 条。
- TSMC Newsroom：checked；官方新闻入口失败后转官方IR Q3页，读Earnings Release两页并检查第1页图像；电话会/Management Report未读。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-16 09:03；已知截断 0 条。
- Reflection AI Blog：checked；打开官方blog，Beam既有线索去重；未完成全站正文/许可更新检查。；已知截断 0 条。
- Namespace Blog：checked；打开blog，顶部10月14日果蝇Doom案例，融资为10月5日旧事；未阅读全文或将其作重大AI新事件。；已知截断 0 条。
- Vinci Official Blog：checked；打开blog，主要带日期融资为10月6日背景；其余条目日期与全文未逐一核对。；已知截断 0 条。
- TODAY Official Blog：failed；指定官网blog网页工具仍不可访问，无本期正文。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；打开官方blog，只读列表可见内容；Jev实验更新缺本期日期核验，未当正式全面交付。；已知截断 0 条。
- GlobalFoundries Official News：checked；打开官方news/events，有限可见列表；未读本期全部项目正文，未采用扩产金额。；已知截断 0 条。
- Meet Odyssey-3：checked；打开10月8日Odyssey3旧原文入口，仅背景去重，未重审完整评测。；已知截断 0 条。
- Decart官网：checked；打开官方产品首页有限内容，未核实本期收购成交公告。；已知截断 0 条。
- Microsoft Official Blog：checked；打开官方blog有限列表；Foundry/Research等全部产品渠道未全面覆盖。；已知截断 0 条。
- 模思智能官方新闻：checked；打开官方新闻页，10月12日融资既有背景去重；未核实本期新融资。；已知截断 0 条。
- ModCraft产品官网：checked；打开产品官网，内容无核实发布日期；不作当天新闻，法定身份仍待核。；已知截断 0 条。
- Apple Newsroom：checked；打开Newsroom只取得有限首页/订阅文字；Apple Intelligence中国发布日期线索未取得充分官方证据。；已知截断 0 条。
- Pluto Security：checked；打开官方blog有限列表，旧融资去重，未重核全部正文。；已知截断 0 条。
- SemiGraph 半图科技：checked；打开官网核对品牌/产品，旧融资与媒体线索不当本期一手新事实。；已知截断 0 条。
- Third Moment Research Official：checked；打开官网产品入口，未知日期作为已入库背景，不冒充本日首发。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；Atom及官方v0.5.22标签baa9bef已检查；只有Release标题，没有足够实质变更说明，不凑版本新闻；博客入口自动采集，未逐篇读全。；已知截断 0 条。
- SGLang Blog：ok；页面链接 8 个，最近一次新增 1 个；检查于 10-16 09:03；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；官方v0.32.0rc2已打开，仍为RC且正文不足；未把候选当稳定版。；已知截断 0 条。
- vLLM Blog：checked；入口自动采集；10月14日push KV与adaptive verification为旧线索，本轮未补读全文与时间边界，未采用。；已知截断 0 条。
- NVIDIA Dynamo：checked；完整Atom读Nemotron3.5实验快照并对照昨日GLM背景；未运行容器。；已知截断 0 条。
- FlashInfer：checked；读v0.7.2 Highlights、升级说明及官方release；完整Atom归档，PR清单未逐项审源码；未采信性能倍数。；已知截断 0 条。
- Mooncake：checked；本轮官方release入口采集成功；未获得足够本期实质新版本内容，未推断生产支持或性能变化。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-16 09:03；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；323 RSS条目，保存60、254本地上限截断，原RSS完整字节保留；选两篇仅摘要+v1版本史，公告10月15日不同于投稿10月14日。未补齐全部CL/DC论文。；已知截断 254 条。
- METR：ok；页面链接 26 个；检查于 10-16 09:03；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-16 09:03；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 2 个；检查于 10-16 09:03；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-16 09:03；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- Vals AI：checked；打开既有多Agent研究页，仅有限可见内容，未确认本期实质修订。；已知截断 0 条。
- Epoch InnovationEval：checked；打开既有InnovationEval研究页，未确认本期新版本，不重复作新研究。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-16 09:03；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-16 09:03；已知截断 0 条。
- 工业和信息化部：ok；页面链接 21 个，最近一次新增 2 个；检查于 10-16 09:03；已知截断 0 条。
- 最高人民法院：ok；页面链接 84 个，最近一次新增 14 个；检查于 10-16 09:03；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 2 个；检查于 10-16 09:03；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个；检查于 10-16 09:03；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-16 09:03；已知截断 0 条。
- 国家数据局：checked；网页工具为空；原生浏览器恢复国家数据局列表，部分动态模块未呈现；未完成本期政策全文核验。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；打开10月10日财联社转载旧页；旧融资去重，不作为本期新融资。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条；可能漏采 2026-10-15T01:03 至 2026-10-15T10:00。
- The Information：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 5 条；检查于 10-16 09:03；已知截断 0 条。
- Financial Times Technology：ok；feed 25 条，关键词过滤 9 条；检查于 10-16 09:03；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-16 09:03；已知截断 0 条。
- New York Times Technology：ok；feed 23 条，关键词过滤 10 条；检查于 10-16 09:03；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 6 条；检查于 10-16 09:03；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 2 条；检查于 10-16 09:03；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 15 条；检查于 10-16 09:03；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-16 09:03；已知截断 0 条。
- 虎嗅：failed；采集超时，网页工具访问同一RSS仍失败；未补回窗口全文。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 25 条；检查于 10-16 09:03；已知截断 0 条。
- 36氪：ok；feed 30 条，关键词过滤 15 条；检查于 10-16 09:03；已知截断 0 条。
- 钛媒体：ok；feed 19 条，关键词过滤 4 条；检查于 10-16 09:03；已知截断 0 条；可能漏采 2026-10-15T01:04 至 2026-10-15T16:32。
- 雷峰网：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-16 09:03；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-16 09:03；已知截断 0 条。
- C114 通信网：checked；采集robots失败；网页工具打开C114首页恢复有限列表，未逐条阅读全文，不声称完整窗口。；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 52 条；检查于 10-16 09:03；已知截断 0 条；可能漏采 2026-10-15T01:04 至 2026-10-15T17:32。
- 机器之心：failed；首页仅会员导流与旧PRO摘要，未取得本期完整列表/正文；微信私域未覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；打开Reuters转WSJ的10月11日Decart收购洽谈转载；仍为旧谈判，不升级为成交。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 133 个，最近一次新增 41 个；检查于 10-16 09:03；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；实际按Oct15日期执行Reuters AI检索；未取得支持本期新增事实的一手正文，付费与独家覆盖有限。。
- bloomberg-ai：checked；实际执行Bloomberg日期检索并筛本期RSS；Anthropic收入/CoreWeave融资风险的付费原文未完整读取，未采用财务数字。。
- ft-nyt-wsj-ai：checked；实际执行FT/NYT/WSJ窗口检索和feed筛选；NYT工具robots受限，多数付费原文未读。。
- china-ai-companies-zh：checked；执行中文公司/产品/融资检索，补查DeepSeek媒体全文和状态入口；NEXFORM官网产品与媒体日期仅作去重/待核。。
- china-ai-policy-zh：checked；执行工信部/数据局/网信等日期检索并补查数据局；正文支持不足，未采用新政策结论。。
- china-chips-zh：checked；执行HBM/GPU/算力产能融资日期检索；多数旧背景或二手线索，未据摘要采信价格和产能。。
- embodied-world-models-zh：checked；执行具身/世界模型发布融资检索，NEXFORM官网确认品牌但融资原始证据/事件日仍不足，未作今日新融资。。
- supply-chain-en：checked；执行HBM/CoWoS/出口管制/存储价格英文检索，补读台积电一手Q3；没有用媒体摘要推算GPU供给。。
- newsroom-fallback：checked；实际多site检索Qualcomm/ASML/TSMC/Qwen/MiniMax，并直接查官方入口；TSMC IR恢复，Qwen/MiniMax仍失败，ASML本轮入口失败。。

- 新公司发现：checked；完成中英文新公司开放检索；Visko官网+Google Cloud联合署名案例核对身份产品后新建entity。NEXFORM融资重复日期、Elevatry/Harmonic等缺充分一手资料只留待核。。

证据包：`data/packets/daily/2026/10/2026-10-15/0d9d1e685ff1b124fb00889aba292181dc06b78897b6defb75f25cdf12492493.json`；采集 run：`20261016T010252-06d4e245`。
