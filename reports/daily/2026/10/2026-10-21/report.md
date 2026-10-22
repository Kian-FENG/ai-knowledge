# AI 产业分析日报（2026.10.21）

统计窗口：2026-10-20T18:00:00-07:00 至 2026-10-21T18:00:00-07:00（America/Los_Angeles，右端不含）。

实际生成：2026-10-22T15:15:02.060473-07:00（America/Los_Angeles）；2026-10-22T22:15:02.060473+00:00（UTC）。本次约洛杉矶15点触发，按规则补最近到期21日窗口；22日窗口尚未到期。

本期14个事件显示，AI产业竞争正同时转向采购分发、主动注意力管理与持续交付：OpenAI扩展云与广告渠道，Claude Duet试验后台助手，Blacksmith及Claude Security处理代码增长后的验证负载。Flint和Humming从模型与运行栈降低部署摩擦，DSX POD与供应链预付款则尝试缩短物理交付；这些宣布、预览和产能计划都需要分别验收。正文保留A5X下月GA、场地已准备、Flint上下文口径与摘要级论文等限制，覆盖仍有官方空页、媒体漏采和中国Today AI待核线索。

## 1. MaaS市场与产品形态

### OpenAI模型将进入Google Cloud，云承诺消费成为新的分发渠道

- OpenAI与Google Cloud于10月21日宣布将前沿模型和Codex工作流带入Model Garden，经Google Cloud Marketplace交易，客户可用已有GCP消费承诺购买。相对此前分发渠道，增量是采购与治理接入现有云环境。
- 官方计划未来几周正式可用，Google Antigravity和Gemini Agent中的模型接入也仍为即将推出；未核定完整型号、价格、区域和实际配额。Microsoft仍是OpenAI主要云伙伴，不能把合作公告写成全面上线或伙伴替换。

**产业判断：** 云采购预算与数据治理可降低企业评估和签约摩擦，模型提供商扩大分发，云平台则强化多模型控制层。反例是云上价差、区域或容量限制抵消便利。观察可购买日期、区域、计费与承诺抵扣条款及使用量。

**来源与核验范围：**
- [OpenAI News · OpenAI models are coming to Google Cloud](https://openai.com/index/openai-models-google-cloud/)；发布时间：2026-10-21T12:00:00+00:00；定位：OpenAI公告主文全文已读；机器HTTP403后浏览工具读取；未实测购买和访问。时间来自官方RSS，网页只标日期。；阅读范围：full-text；ID：`5c777dc5eda38b6a8e06`。

### Claude Duet开放美国Pro/Max候补研究预览，把主动跟进纳入个人助手

- Anthropic于10月21日开放Claude Duet候补名单：美国Pro和Max用户研究预览，使用Opus 5.5，共享Claude套餐额度；iOS、Android独立应用和claude.ai可访问。不是全体用户正式可用。
- 相对等待提问的会话，Duet继承记忆、技能与连接器，在自己的云端电脑持续处理任务、发送晨报，每隔数小时检查已连接应用；后台检查和大任务消耗套餐额度。
- 发送消息、支付、签署或删除前展示具体动作并等待批准；当前可能误判紧急性，尚不能展示自己的浏览器，个人订票等场景也较弱。官网客户案例与安全效果均为厂商披露，未独立验证。仅日精度，18:00边界不确定，前一期未收录。

**产业判断：** 助手竞争从回答质量扩展到何时打扰、如何完成并交接任务，连接器、记忆和后台运行共同决定留存。反例是误提醒、遗漏或后台额度耗尽增加管理负担。观察预览准入、提醒准确率、单位验收任务成本和持续使用率。

**来源与核验范围：**
- [Claude Product Announcements · Introducing Claude Duet](https://claude.com/resources/articles/claude-duet)；发布时间：2026-10-21（原文仅日期）；定位：官方公告主文、How Claude Duet works及预览限制完整阅读，产品FAQ旁证；未实测，未审外链安全研究和客户数据。；阅读范围：full-text；ID：`f5220dab8f55b741ff6e`。
  日期仅精确到天，无法确认 18:00 边界。

### ChatGPT广告新增26国，OpenAI披露累计超过10万广告主

- OpenAI于10月21日宣布ChatGPT Ads新增26个国家，覆盖总数达到89国，并披露上线八个多月以来超过100,000个广告主投放过活动。该数是累计参与广告主，不是活跃付费客户、收入或转化率。
- 相对9月区域扩张，新增更多拉美及欧洲、中东、非洲、亚洲市场，广告主可经技术伙伴或Ads Manager接入；广告仅在Free和Go，Plus、Pro及Enterprise保持无广告。回答独立与不向广告主出售数据是公司的原则披露，未审计实现。

**产业判断：** 会话中的比较与决策环节逐渐形成广告分发渠道，可支持低价用户覆盖，也会争夺传统搜索预算。反例是可衡量转化不足或信任受损。观察复投率、广告负载、归因质量、地区单位收入及自然答案体验。

**来源与核验范围：**
- [OpenAI News · ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform](https://openai.com/index/chatgpt-ads-expands-26-new-countries/)；发布时间：2026-10-21T13:00:00+00:00；定位：官方公告全部主文已读；HTTP403后浏览读取。未审核广告后台、地区完整清单、隐私实现或转化原始数据。；阅读范围：full-text；ID：`7e3febf760080930f6fd`。

### Claude Security将一次扫描扩展为持续监测、修复追踪与API工作流

- Anthropic于10月21日更新Claude Security，面向Claude Enterprise客户提供公共beta：连接代码库、先做基线扫描，再按变更的风险与复杂度持续扫描；同一项目可跨多个仓库。相对4月beta，增量是持续跟踪和团队环境上下文。
- 系统可对照代码变更关闭已修复问题、再次出现时重新打开；团队可编辑知识库和威胁模型。新增API、webhook、MCP连接器和角色访问控制，把发现接入既有修复流程。
- 官方称由包含Mythos在内的模型家族提供能力，无需CVP资格；此处是受控产品可用性，不代表模型任意访问或安全效果已获独立验证。只标日期，窗口边界不确定。

**产业判断：** 安全产品的价值可从发现数量转向修复闭环与可达风险排序，代码平台和安全运维集成商可能受益。反例是自动闭环误判或威胁模型遗漏造成假安全感。观察经人工确认的有效发现、误报率、修复时间及复发识别。

**来源与核验范围：**
- [Claude Product Announcements · Claude Security now scans continuously and tracks fixes](https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes)；发布时间：2026-10-21（原文仅日期）；定位：官方主文Continuous monitoring至Getting started及客户引言已读；未实测、未审核促销完整条款或客户漏洞原始记录。；阅读范围：full-text；ID：`9c2e899d121755363e2a`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Blacksmith披露10亿美元估值C轮，Agent代码增长推高CI需求

- Blacksmith联合创始人兼CEO Aditya Jayaprakash于10月21日宣布Sequoia领投C轮，估值USD1B，累计融资USD125M。官方未在该文披露本轮金额，累计融资不能当作本轮金额，也未说明估值的投前/投后口径。
- 公司称自2026年1月以来每周CI任务由500万增至逾9000万、ARR增至17倍；没有披露ARR绝对金额，这不是同期确认收入。现有计算设施功率规模不到10MW、2027年扩大5倍是公司披露和计划。相对库内Scion对验证负载的观察，本期增加独立CI供应商的商业信号。仅日精度，边界不确定。

**产业判断：** 代码生成加速可把瓶颈推向构建、测试和合并，弹性CI及缓存服务获得新增需求。反例是生成代码缺少商业价值，或客户自建与云价格竞争压低利润。观察付费任务留存、算力利用率、失败重跑、毛利及ARR绝对值。

**来源与核验范围：**
- [Blacksmith Official Blog · Building the CI cloud: our Series C](https://www.blacksmith.sh/blog/series-c)；发布时间：2026-10-21（原文仅日期）；定位：CEO署名官方公告全文及官网页尾Blacksmith Software Inc已读；未审法定注册、融资到账、客户账单和ARR原始报表。；阅读范围：full-text；ID：`164952f9102b56af1ece`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### Recursive发布Flint开放权重，本地编码与自动化研发共同优化

- Recursive官方更新列表将Flint发布日期标为10月21日：40B总参数、每token激活约2.5B的MoE编码模型，官方与链接模型卡标为Apache-2.0权重。Eureka Machine参与数据、训练和推理优化是公司披露，不等于已证明开放式递归自我改进。
- 官网称最高512K上下文、建议编码在256K以内；同日vLLM文章写262K，两者口径未消解，部署应以检查点及具体实现核对。vLLM提供专用flint镜像，文章仍称支持正在合并，不能写成已进入正式release。NVFP4检查点在该路径实际按W4A16运行，激活和KV为BF16。
- 评测为厂商自测：Terminal-Bench 2.1用Terminus 2 XML并联网但检索命中解答计失败，SWE-Bench Pro v2/Verified用mini-swe-agent且不联网；温度1、top-p0.95、top-k20，Agent最长5小时、至少5次取pass@1均值。未审图表原始分数、完整模型revision及速度负载，不转述领先排名或速度倍数。日精度边界不确定。

**产业判断：** 小激活MoE与模型专用运行栈有机会把部分编码任务留在本地，硬件和本地工具生态受益；能力与效率也更依赖整套交付。反例是长任务失败、内存容量或后端限制抵消API节省。观察固定任务质量、内存、长上下文延迟及上游正式支持。

**来源与核验范围：**
- [Recursive Superintelligence Official · Introducing Flint](https://recursive.com/updates/introducing-recursive-flint)；发布时间：2026-10-21（原文仅日期）；定位：Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。；阅读范围：full-text；ID：`f3f48867a1e22b1634ae`。
  日期仅精确到天，无法确认 18:00 边界。
- [vLLM Blog · Day-0 Support for Flint on vLLM](https://vllm.ai/blog/2026-10-21-flint)；发布时间：2026-10-21（原文仅日期）；定位：Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。；阅读范围：full-text；ID：`3b031f6c198ac9415336`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### 蚂蚁与vLLM介绍Humming，以统一量化描述降低多硬件部署维护成本

- Ant Group与vLLM社区10月21日发布Humming技术文章，介绍量化推理库：统一权重、激活、缩放和布局描述，再按设备与负载选择执行配置并即时编译。覆盖dense/MoE、NVIDIA Turing及以后架构和CUDA兼容的真武810E，是官方支持披露。
- 正文称vLLM从0.29.0起已包含Humming依赖；本期增量是系统设计与结果披露，不把文章日期当成首次代码集成。更广Rubin能力、真武M890和autotune等列在未来计划，不能当作已交付。
- 端到端示例为DeepSeek-V4.1-Flash、8×H20、TP=8、并发1–64：模型MXFP4权重不变，但Marlin W4A16/BF16激活切为Humming W4A8/tokenwise FP8激活。缺完整输入输出长度与全部软件revision，微基准和实际服务也不同，因此不采泛化倍数或据此排名。

**产业判断：** 量化格式与硬件配置的组合增多，统一表示和适配层可降低每增加一种模型的维护成本，使旧GPU和兼容设备更有部署空间。反例是JIT、精度损失或通信瓶颈吞掉局部收益。观察固定质量/SLO下成本、编译冷启动、后端覆盖及生产回归。

**来源与核验范围：**
- [vLLM Blog · Announcing Humming: Fast, Flexible Kernels for Quantized Inference](https://vllm.ai/blog/2026-10-21-humming)；发布时间：2026-10-21（原文仅日期）；定位：官方技术文章主文、端到端表格、Usage与Future Plans已读；未审全部图像标注、外链源码与许可或复现，未核完整I/O长度和软件版本。；阅读范围：full-text；ID：`3e7599c6661c19f5d674`。
  日期仅精确到天，无法确认 18:00 边界。

### OpenAI披露PHP漏洞协调响应，AI发现能力推动修复流程扩容

- OpenAI于10月21日披露过去两个月围绕PHP关键漏洞的协调响应：Calif使用GPT-5.6 Sol发现关键问题，Wiz也独立发现并报告漏洞；PHP维护者负责修复和发布，研究与基础设施伙伴协助。今天是披露日，不能写成漏洞当天首次发现。
- 增量是将发现延伸到上游确认、下游保护准备、政府协调、更新分发和部署验收的拟议流程；AI可提高发现速度，而保护仍依赖维护者与运营者实施。文章中的普遍推广与未来发现量为主张/预期，未复核技术报告、补丁或在野利用数据。

**产业判断：** 发现吞吐提高可能让维护者响应与补丁部署成为稀缺资源，安全服务、软件供应链运维及自动验证工具受益。反例是低质量报告挤占维护资源或提前披露放大攻击。观察有效漏洞比例、维护成本、修复落地时间和覆盖率。

**来源与核验范围：**
- [OpenAI News · Patch the Planet: global response coordination as agents uncover critical vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)；发布时间：2026-10-21T07:00:00+00:00；定位：官方主文及拟议五阶段流程已读；未审外链PHP/Wiz/CISA技术文档、利用代码或复现。仅产业研究，不提供漏洞操作指南。；阅读范围：full-text；ID：`203093066e1251d7c55c`。

## 5. 模型与AI Infra论文

### OpenAI等披露数千Agent解释细胞数据，结果仍是待实验检验的线索

- OpenAI于10月21日介绍与PerturbAI、Scripps的distributed biological reasoning：把鼠脑CRISPR数据按基因扰动分派给GPT-Rosalind Agent，连接细胞响应与文献，汇成推理图谱。相对单条问答，增量是对复杂实验数据并行探索与文献整合。
- 官方称数千Agent在32分钟分析数百万鼠脑细胞的数据，并报告盲评偏好；这里记录为研究团队披露。本文只读官方介绍，未读链接论文、原始样本及评审记录，模型快照、总预算、硬件与可复现harness未核，不以此量化普遍科学生产率。所得机制假说和疾病线索仍需后续实验，不是药物或临床疗效。

**产业判断：** 科学Agent可把大规模数据整理为可追问的实验候选，实验平台、文献与证据管理服务可能受益。反例是相关性叙事或重复引用增加无效实验。观察盲评设计、实验验证率、每条有效线索成本及跨数据集复现。

**来源与核验范围：**
- [OpenAI News · Using thousands of AI agents to uncover new leads in biological data](https://openai.com/index/scaling-ai-research-for-complex-biological-data/)；发布时间：2026-10-21T04:50:00+00:00；定位：官方研究介绍主文、Big experiments/Divide the work/Finding the next experiment已读；论文、图谱代码、数据、完整统计及生物学结论未独立核查。；阅读范围：full-text；ID：`75125cf5ab0826b20b08`。

### DStill以轨迹蒸馏改善单步扩散草稿的一致性

- arXiv 2610.27379v1于10月19日23:05:16 UTC投稿，10月21日官方RSS公告属于本期；公告日不是初次投稿日。只读摘要与v1提交历史。
- 论文针对块扩散推测解码的单步位置独立预测问题：先训练条件草稿补全部分揭示的块，再把多步细化轨迹蒸馏到一次预测，逐步转向全掩码输入。作者报告跨三模型家族的接受长度和加速改善；未读全文、模型名单、硬件、精度、并行、I/O长度、并发、完整DFlash基线版本或代码，故不采倍数收益。

**产业判断：** 把推理时多步改进迁移到训练阶段可能减少在线草稿开销，推测解码栈受益。反例是蒸馏训练成本或负载迁移后接受率下降。观察完整成本、不同目标模型与负载下的质量和端到端收益。

**来源与核验范围：**
- [arXiv model and infra papers · DStill: Trajectory Consistency Distillation for Accelerated One-Step Drafting in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2610.27379)；源站公告时间：2026-10-21T00:00:00-04:00；定位：arXiv摘要/v1历史与官方RSS公告字段已读；未读PDF、表格、代码或复现。；阅读范围：abstract；ID：`382f3439a08b28d60570`。

### 上下文压缩论文提醒：当前问题表现不能代替后续任务的证据保留

- arXiv 2610.27301v1于10月19日21:15:56 UTC投稿，10月21日RSS公告纳入本期；仅阅读摘要和v1历史，不把公告日当投稿日。
- 作者用四个有证据标注的语料及Agent轨迹，将压缩方法与同token预算随机删除比较。摘要称MultiRC在25%预算下针对当前问题选句可改善当前题，却未显示对后续题优于随机删句；LLMLingua-2、Evidence Inference和需精确标识符的τ-bench结果各异，FEVER还暴露标签正确但保留证据不支持的风险。模型提到gpt-6-luna/Decisions API，具体快照、harness和统计原表未审，不作跨系统排名。

**产业判断：** 持久Agent的记忆预算应按未来任务、证据与精确标识符验收，而不能只测摘要是否回答当前问题。反例是任务分布很窄，定向压缩反而足够。观察后续任务成功率、可追溯证据保留、标识符丢失及累计成本。

**来源与核验范围：**
- [arXiv model and infra papers · Evaluating Context Compaction on the Questions That Come Later](https://arxiv.org/abs/2610.27301)；源站公告时间：2026-10-21T00:00:00-04:00；定位：arXiv摘要、投稿历史及RSS公告已读；未读全文、附表/代码、置信区间和独立复现。；阅读范围：abstract；ID：`a175a3ab6c22f02f9061`。

## 6. GPU与供应链

### NVIDIA发布DSX POD参考设计，14天部署以场地已准备为前提

- NVIDIA于10月21日发布DSX POD参考设计，把Vera Rubin计算、网络、供电与液冷集成和验证前移到伙伴工厂，以模块化集装箱交付。相对传统现场集成，增量是可重复的预制交付与验收流程。
- 官方“从六个月缩到最快14天”限定在电力、冷却、网络等已准备好的场地，不是14天完成选址、供电审批和整座数据中心；全球伙伴交付计划在2027年初，当前不能计作已建成可用产能。时间和经济收益为厂商主张，未审项目实绩。

**产业判断：** 预制可降低现场劳动力、调试与接口不确定性，系统集成、冷却及模块制造商受益；供电和许可约束仍会决定总工期。反例是运输、场地差异或维护使标准化失效。观察从下单到验收的全周期、现场准备耗时及利用率。

**来源与核验范围：**
- [NVIDIA Newsroom · NVIDIA Introduces DSX POD AI Factories to Accelerate Europe’s Infrastructure Deployment](https://nvidianews.nvidia.com/news/nvidia-introduces-dsx-pod-ai-factories-to-accelerate-europes-infrastructure-deployment)；发布时间：2026-10-21T09:34:00+00:00；定位：官方新闻稿全部主文、可用性及前瞻声明已读；未审伙伴合同、项目工期/成本实绩或独立运行数据。；阅读范围：full-text；ID：`283a10a734a97f3fd2cf`。

### NVIDIA以产能预付款扩展基板、封装、测试与光引擎供应

- NVIDIA于10月21日披露与Amkor、IBIDEN、KYEC、三星电机、SPIL及欣兴扩产安排：基板产能目标三年增至2.5倍，Amkor目标2028年底interposer wafer产能增长逾300%；这些是针对所述产线/协议的计划，不是当期GPU交付量。
- KYEC获USD1.1B产能预订预付款支持美国测试设施，目标2027年4月量产；新加坡扩产目标2027年2月量产。公司预计测试总产能2026至2027年翻倍；SPIL CPO光引擎目标2027年中达到当前15倍、2028年底再翻倍。预付款不是股权收购，产能目标不等于收入或已经建成供给。

**产业判断：** 瓶颈从晶圆延伸到基板、测试、先进封装与光学，预付款可将需求风险转移并帮助供应商融资扩产。反例是需求下修、良率或电力延迟使预订产能不能兑现。观察各设施投产、良率、客户分配、现金流与实际系统交付。

**来源与核验范围：**
- [NVIDIA Newsroom · NVIDIA and Supply Chain Partners Expand Capacity to Accelerate AI Infrastructure Buildout](https://nvidianews.nvidia.com/news/nvidia-and-supply-chain-partners-expand-capacity-to-accelerate-ai-infrastructure-buildout)；发布时间：2026-10-21T10:33:00+00:00；定位：官方公告主文、各产能口径及前瞻声明已读；供应商法定披露、合同、现金到账、产能基数和良率未独立核实。；阅读范围：full-text；ID：`9ba8426e373d1daa7f5a`。

### Google Cloud公布A5X扩展，正文明确Rubin实例下月才正式可用

- Google Cloud与NVIDIA于10月21日介绍基于Vera Rubin NVL72的A5X、Virgo网络和分层KV缓存。NVIDIA标题使用“宣布正式可用”，但两方正文均限定实例GA在下月；本报告按正文保留为计划，不能写成本期全面开放。
- 单站80,000、多站最高960,000 Rubin GPU是拟支持的扩展规模，不是已安装、已售或可预订配额。NVIDIA披露Ineffable已先行访问，属于客户案例；与同文中Confidential G4及GDC B300各自GA的状态不能混用。未核A5X实际区域、价目、配额与集群规模。

**产业判断：** 平台把训练、体验生成和长期Agent上下文放入统一系统，可让网络、存储与治理成为GPU之外的差异。反例是规模计划被设施和采购限制拖延。观察下月可用范围、承诺配额、固定负载SLO和全栈账单。

**来源与核验范围：**
- [Google Cloud Blog · Google Cloud and NVIDIA expand co-engineering collaboration to scale infrastructure for the agentic era](https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026/)；发布时间：2026-10-21T11:30:00+00:00；定位：Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。；阅读范围：full-text；ID：`b73d95b43e98dc86c574`。
- [NVIDIA Blog · Google Cloud and NVIDIA Announce General Availability of NVIDIA Vera Rubin Infrastructure](https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/)；发布时间：2026-10-21T10:45:17+00:00；定位：Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。；阅读范围：full-text；ID：`12c1cb38a75e4a7b39f0`。

## 知识入库与待核

本次新建17个标准页：12个source、2篇paper、2个entity与1篇综合note；更新既有标准页0。均已审核发布，并以默认query/get_page回查和raw SHA-256确认；235页结构、132来源配置与49项离线测试已分别通过。

- [[reference/entities/recursive|Recursive实体]]、[[reference/entities/blacksmith|Blacksmith实体]]。
- [[research/synthesis/agent-distribution-attention-and-delivery-20261021|综合：采购分发、注意力与交付]]。
- 去重复用：20日DeepInfer、TorchTPU、llm-d、Arda/Firefly，19日MiniMax与SGLang等；Flint模型与vLLM支持合为同一事件。

- 中国Today AI融资仅搜索可见，36氪原文/todayai.cn失败；today.ai旧创始人文8月3日/9月15日更新仅背景，主体、成立/上线日期与二级目录冲突未解；不同于丹麦UseToday ApS。
- HCLTech合作、Meta/SpaceX/Tesla财报与股本计划、NVIDIA OpenShell/Isaac、Google G4、PyTorch FlyDSL/TitanRL等候选未完整完成原始材料审核，不以遗漏表述为无新闻。
- Mercury3官方文章日期10月19日，21日媒体转述不作新发布；DeepInfer20日开源、TorchTPU、llm-d1.0等前期事件去重。
- 两篇arXiv仅摘要，生物学介绍未读biorxiv论文；性能、预算、评测版本与原始统计范围有限。
- 媒体feed多次运行间存在gap，不能恢复全部被挤出条目；取原始from/to/detected时区，不假称完整覆盖。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 374 条（其中线索 33 条），精选 14 个事件；未注明日期 9 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。
- 本轮collect运行`20261022T220010-e0c7fd06`检查128个启用入口：80成功、45需浏览核查、3失败；45个浏览入口和3个失败端点均实际尝试。另新增并检查Claude产品、Recursive、Blacksmith三个入口，不回算原采集分母。
- 以下“检查于”按采集器默认Asia/Singapore显示；日精度的午夜是标准化占位，正文只显示源站日期，不是假定发布时间。raw归档日与洛杉矶统计日分别保留。
- arXiv本轮保存60条、184条因上限未保存；未完成所有候选与全文阅读。仅摘要、网页片段、截断、空正文和媒体付费摘要均不会自动升级为全文证据。
- Techmeme补漏快照`261021/h2355`已打开但不可访问；中英文新公司与9类discovery检索已执行，论文定向检索也已执行，均为有限范围。
- 调度偏差仍未解决：主机America/New_York，本轮约LA15点启动；项目报告配置America/Los_Angeles 18点正确，窗口未迁就触发时间更改。


### 公司与产品一手来源

- Meta Muse Official Model Card：checked；仅打开模型卡标题、元数据和部分文本；本期版本变化未核，不把下载/发现时间当发布日。；已知截断 0 条。
- Visko Official：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Stacklok Official：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Peppermint Official：checked；10月8日融资旧闻去重。；已知截断 0 条。
- Microsoft Command Line：checked；10月9日Decision文章旧闻去重。；已知截断 0 条。
- Satya Nadella Public Article：failed；X帖子403。；已知截断 0 条。
- Nous Research Official：checked；官网嵌入动态含21日Hermes演示及Krea接入，未读对应原帖和产品版本，只作线索。；已知截断 0 条。
- Healthleap Official：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- OpenAI News：checked；官网/RSS与本期四篇主文实际核对；HTTP403后浏览正文成功，帮助中心最新可见20日锁定聊天旧闻。22日网页标注的Uber与窗口内RSS时间不一致，暂不收录。；已知截断 0 条。
- OpenAI API Changelog：checked；机器页面差异为线索，未将未核日期变更当新API发布；22日Decisions API暂不纳21日。；已知截断 0 条。
- Anthropic Newsroom：checked；anthropic.com新闻页打开，21日信托任命非本期优先；主动补查claude.com产品入口并阅读Duet/Security原文，已添加长期入口；HCLTech仅候选，不宣称完成全文审核。；已知截断 0 条。
- Anthropic Research：ok；页面链接 22 个，最近一次新增 1 个；检查于 10-23 06:01；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 547 个，最近一次新增 3 个；检查于 10-23 06:01；已知截断 0 条。
- DeepSeek Research & News：checked；API updates当前重定向到入门文档，读取Flash-1017别名说明，配合collect的API/价格/HF和既有DeepInfer来源核对；不将20日开源重发算21日新发布，未逐commit审本期更改。；已知截断 0 条。
- DeepSeek API Change Log：checked；实际打开updates文档，当前不是按日期排列的完整发布日志；无日期接口说明不作当日新闻。；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-23 06:01；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-23 06:01；已知截断 0 条。
- Alibaba / Qwen Blog：failed；博客空正文；HF列表50条仅有限辅助，不能据此判断全品牌无新事件。；已知截断 0 条。
- Qwen · Hugging Face：checked；机器检查HF最新50条仓库入口；这不是Qwen博客和阿里全渠道的替代，主页失败保留。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；官方研究列表实际打开，最新可见7月16日K3/PerceptionBench；collect同步核对HF。限研究入口，不声称产品/用户群全部覆盖。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-23 06:01；已知截断 0 条。
- Z.ai 发布记录：ok；最近一次检测到页面变化；检查于 10-23 06:01；已知截断 0 条。
- 智谱开放平台发布记录：ok；最近一次检测到页面变化；检查于 10-23 06:01；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-23 06:01；已知截断 0 条。
- MiniMax News：failed；新闻入口仅导航，未取得完整文章列表；19日M3.1 Flash既有页去重。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-23 06:01；已知截断 0 条。
- Mistral AI：ok；feed 92 条；检查于 10-23 06:01；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-23 06:01；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-23 06:01；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-23 06:01；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 1 条；检查于 10-23 06:01；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-23 06:01；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-23 06:01；已知截断 0 条。
- ByteDance Seed Blog：checked；研究列表当前可见最新定日为9月28日；限列表，未遍历全部公众号与产品。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-23 06:01；已知截断 0 条。
- Alibaba Cloud Press Room：failed；页面已打开但未取得可核定日期的新闻列表；不等于无新闻。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个，最近一次新增 1 个；检查于 10-23 06:01；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-23 06:01；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-23 06:01；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-23 06:01；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-23 06:01；已知截断 0 条。
- xAI News：checked；官网列表20日Grok工单文章已在前期收录，22日伙伴网络不提前纳入；限列表。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-23 06:01；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 8 条；检查于 10-23 06:01；已知截断 0 条。
- Qualcomm Newsroom：checked；官网新闻列表可见21日条目，未完整审阅所有正文；不声称无新闻。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-23 06:01；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条。
- ASML News：checked；本轮浏览恢复到投资者公告列表，最新可见14日；此前401状态不沿用，限可见列表。；已知截断 0 条。
- TSMC Newsroom：checked；官网列表已打开，限可见新闻，不覆盖所有事故、产能或订单线索。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-23 06:01；已知截断 0 条。
- Reflection AI Blog：checked；列表旧Beam文章复用既有页，不因重复报道作新发布。；已知截断 0 条。
- Namespace Blog：checked；博客可见最新14日；限列表。；已知截断 0 条。
- Vinci Official Blog：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- TODAY Official Blog：failed；usetoday.io博客不可访问；与中国todayai.cn/Today AI不混同。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- GlobalFoundries Official News：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Meet Odyssey-3：checked；10月8日研究预览旧闻去重。；已知截断 0 条。
- Decart官网：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Microsoft Official Blog：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- 模思智能官方新闻：checked；新闻列表最新10月12日融资，旧闻去重。；已知截断 0 条。
- ModCraft产品官网：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Apple Newsroom：failed；只取得导航，未覆盖正文列表。；已知截断 0 条。
- Pluto Security：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- SemiGraph 半图科技：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- Third Moment Research Official：checked；本轮实际打开官网，阅读范围仅页面标题/部分可见列表或产品简介；未逐一审全文，未发现足够证据可采用的新条目不等于没有新闻。；已知截断 0 条。
- HUMXN Official：checked；10月6日数据服务换取计划旧闻去重。；已知截断 0 条。
- Sapiom Official Blog：checked；列表最新9月15日，8月融资为既有背景。；已知截断 0 条。
- Tenstorrent Official Newsroom：checked；本轮列表恢复，可见21日PFN/NEDO xPU项目与22日OCA；21日原文未审，22日不纳本期。；已知截断 0 条。
- Orchestra Bio Official：checked；官网产品/收购背景，19日事件已入库。；已知截断 0 条。
- Arda Official and Investor Announcements：checked；官网产品与团队背景核对，无日期不作新新闻。；已知截断 0 条。
- Firefly Physical Safety AI：checked；20日融资公告旧闻去重。；已知截断 0 条。
- Claude Product Announcements：checked；新增入口实际打开，Duet/Security已全文阅读；美国Pro/Max候补research preview与Enterprise public beta分别记录，22日云平台公告不提前纳入。；已知截断 0 条。
- Recursive Superintelligence Official：checked；新公司发现后核对官网/发布页/更新日/链接HF身份，40B/2.5B与Apache标签；法定注册、融资与自动化研发效果未审计。；已知截断 0 条。
- Blacksmith Official Blog：checked；新公司发现后读CEO融资公告/产品和页尾；USD1B估值、USD125M累计融资、ARR17倍分别记录，单轮金额官方正文未披露。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方API近8个release核对：最新0.5.22为19日；本窗口无所检正式release，不等于无代码提交。；已知截断 0 条。
- SGLang Blog：checked；官网列表实际打开；20日Omni已收录，22日Unified Memory不提前纳入；19日HiCache是窗口前背景。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；API近8个release最新0.32.0为18日；Flint是专用镜像与合并中支持披露，不改称正式release。；已知截断 0 条。
- vLLM Blog：checked；Humming和Flint同日主文已读；Humming通用设计不等于21日才首次集成，Flint支持并入同一模型事件。；已知截断 0 条。
- NVIDIA Dynamo：checked；API近8版最新Muse dev.1为20日02:09:56Z、窗口前且实验预发，未发现本窗口新正式版；只审release不代表全仓无变化。；已知截断 0 条。
- FlashInfer：checked；API近8版0.7.2rc6为22日07:58:40Z，已超本窗口；0.7.2正式版15日去重。；已知截断 0 条。
- Mooncake：checked；API近8版最新0.3.14-rc1为9月7日，所检列表无本期release，未遍历提交。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-23 06:01；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条。
- OpenBMB PilotDeck Official Repository：checked；仓库README入口打开；15日2.0发布既有页复用，未完整审全部提交。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；本轮列表统计以run为准，保存60且184条截断；21日候选来自上一轮官方RSS档案。两篇只读摘要/v1历史，21日公告与19日投稿分开；未完成全部论文发现与全文审查。；已知截断 184 条。
- METR：ok；页面链接 28 个，最近一次新增 1 个；检查于 10-23 06:01；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-23 06:01；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 1 个；检查于 10-23 06:01；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-23 06:01；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- Vals AI：checked；10月9日多Agent评测旧闻去重。；已知截断 0 条。
- Epoch InnovationEval：checked；10月7日评测旧闻去重。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-23 06:01；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-23 06:01；已知截断 0 条。
- 工业和信息化部：ok；页面链接 19 个，最近一次新增 3 个；检查于 10-23 06:01；已知截断 0 条。
- 最高人民法院：ok；页面链接 84 个，最近一次新增 9 个；检查于 10-23 06:01；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-23 06:01；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个，最近一次新增 2 个；检查于 10-23 06:01；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-23 06:01；已知截断 0 条。
- 国家数据局：failed；页面零行；无法核对本期原始政策。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；10月10日利太智药旧闻去重。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条；可能漏采 2026-10-20T22:02:36.960633+00:00 至 2026-10-21T08:32:54+00:00（检出：2026-10-21T22:05:37.783601+00:00）。
- The Verge AI：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条；可能漏采 2026-10-21T22:05:37.118184+00:00 至 2026-10-22T11:50:30-04:00（检出：2026-10-22T22:00:31.257206+00:00）。
- The Information：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 8 条；检查于 10-23 06:01；已知截断 0 条；可能漏采 2026-10-21T22:05:39.574448+00:00 至 2026-10-22T10:43:15+00:00（检出：2026-10-22T22:00:34.307106+00:00）。
- Financial Times Technology：ok；feed 25 条，关键词过滤 13 条；检查于 10-23 06:01；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-23 06:01；已知截断 0 条。
- New York Times Technology：ok；feed 23 条，关键词过滤 11 条；检查于 10-23 06:01；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 5 条；检查于 10-23 06:01；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 2 条；检查于 10-23 06:01；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 19 条；检查于 10-23 06:01；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-23 06:01；已知截断 0 条。
- 虎嗅：failed；机器超时，浏览访问相同RSS仍超时。；已知截断 0 条。
- IT之家：failed；机器连接被关闭，浏览同一RSS亦失败；可用的是此前已归档条目。；已知截断 0 条；可能漏采 2026-10-20T22:02:42.362961+00:00 至 2026-10-21T06:07:23+00:00（检出：2026-10-21T22:05:41.649018+00:00）。
- 36氪：ok；feed 30 条，关键词过滤 16 条；检查于 10-23 06:01；已知截断 0 条。
- 钛媒体：ok；feed 17 条，关键词过滤 5 条；检查于 10-23 06:01；已知截断 0 条；可能漏采 2026-10-20T22:02:43.163832+00:00 至 2026-10-21T17:29:36+08:00（检出：2026-10-21T22:05:43.542354+00:00）；可能漏采 2026-10-21T22:05:43.542354+00:00 至 2026-10-22T16:03:44+08:00（检出：2026-10-22T22:00:39.138081+00:00）。
- 雷峰网：failed；机器XML解析失败，浏览相同feed不可访问；保留已有档案。；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-23 06:01；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-23 06:01；已知截断 0 条。
- C114 通信网：ok；页面链接 37 个，最近一次新增 18 个；检查于 10-23 06:01；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 53 条；检查于 10-23 06:01；已知截断 0 条；可能漏采 2026-10-20T22:02:48.089688+00:00 至 2026-10-21T15:44:04+08:00（检出：2026-10-21T22:05:47.277608+00:00）；可能漏采 2026-10-21T22:05:47.277608+00:00 至 2026-10-22T15:37:08+08:00（检出：2026-10-22T22:00:48.253488+00:00）。
- 机器之心：failed；仅导航/会员入口，公众号与正文覆盖未完成。；已知截断 0 条。
- Reuters转述WSJ：checked；Decart约70亿美元谈判转载为既有背景，不升级成完成收购。；已知截断 0 条。
- Reuters Licensed Syndication：checked；打开MarketScreener主页仅作入口检查，未全量检索所有Reuters转载；20日RTX订单旧闻去重。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 133 个，最近一次新增 36 个；检查于 10-23 06:01；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；按after:2026-10-20 before:2026-10-23及October21查询，结果时间仍需逐条过滤；未获得本期拟采用报道的原始全文，不能声称完整覆盖独家。
- bloomberg-ai：checked；窗口定向搜索与feed；可见Nscale谈判更新为20日、窗口前，旧口径不作当期确认。付费正文未读，仅摘要线索。
- ft-nyt-wsj-ai：checked；按窗口检索FT/NYT/WSJ；NYT访问受robots限制，付费正文与Meta/SpaceX财报原始文件未完整审阅，保留候选。
- china-ai-companies-zh：checked；执行21日公司/模型/Agent检索；Today累计融资、GLM-5.5预测等仍需原始材料与身份/版本核实，未作已发生新模型。
- china-ai-policy-zh：checked；执行21日政策/算力/芯片检索，结果含旧发布会与二级转载；原始DeepSeek禁令、统计口径、最新政策正文未全部核定。
- china-chips-zh：checked；执行21日HBM/GPU/光刻机/订单检索；三星/海力士中国工厂升级、美光罢工等未回查一手正文，不作确认供给变化。
- embodied-world-models-zh：checked；执行21日具身/世界模型/融资检索，墨甲、宇树与南京活动为线索；未完整核对版本与商业可用范围，未凑事件。
- supply-chain-en：checked；执行21日HBM/CoWoS/export controls/memory prices检索，采用NVIDIA两篇一手扩产/交付公告；未完成所有上游供应商法定披露。
- newsroom-fallback：checked；按官方域名检索并实际打开Qualcomm/ASML/TSMC/xAI/Qwen/MiniMax等入口；ASML和Tenstorrent本轮列表恢复，空页仍单独记失败。

- 新公司发现：checked；已执行英文AI startup launch/funding与中文新公司/融资/智能体检索；Recursive、Blacksmith核实后入库。发现中国Today AI，但36氪原文和todayai.cn直接访问失败，搜索可见材料不当全文；today.ai创始人旧文与主体/上线日期冲突留待核，不混同既有丹麦TODAY。

证据包：`data/packets/daily/2026/10/2026-10-21/feb23ab42c65595a3461e64fe9b88b96cfd25bbc238f2daae0cf131d74555937.json`；采集 run：`20261022T220010-e0c7fd06`。

### 无日期材料清单（仅归档，不作本期新闻）

- [模思智能公司身份与产品研究方向](https://www.mosi.cn/about)；来源`mosi`。
- [ModCraft产品身份](https://www.modcraft.games/)；来源`modcraft`。
- [Orchestra Bio is joining OpenAI](https://orchestra.bio/)；来源`orchestra-bio`。
- [Arda Industries — AI for Manufacturing](https://arda.ai/)；来源`arda`。
- [SemiGraph：AI互动角色与3D行为产品背景](https://www.semigraph.com/)；来源`semigraph`。
- [Changes to Gemini model access and limits](https://support.google.com/gemini/answer/17004136)；来源`google-ai-blog`。
- [Stacklok company identity and open agent architecture](https://stacklok.com/company/)；来源`stacklok`。
- [Visko official product identity — undated](https://www.visko.ai/)；来源`visko`。
- [Decart官网：DOS、Lucy与Oasis归属](https://decart.ai/)；来源`decart`。
