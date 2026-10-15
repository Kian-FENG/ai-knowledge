# AI 产业分析日报（2026.10.14）

统计窗口：2026-10-13T18:00:00-07:00 至 2026-10-14T18:00:00-07:00（洛杉矶时间，右端不含）。

企业Agent的新变化集中在组织身份、场景工具和成本管理：企业微信与WorkBuddy互通、千问办公电商邀测，以及BigQuery词元配额实施说明。语音与端侧安全继续推进，但Grok Voice的效果仍需独立核对，Gemma反诈应用是分阶段推出；Dynamo的GLM支持仍为实验快照。ASML季度兑现与供给预期、NVIDIA芯片工程工具显示上游交付和验证仍影响算力扩张。本期13条事件，包含客户案例/教程的新披露而非全部功能当日首发；中文产品部分只读到媒体原文，论文仅摘要，五段媒体漏采与arXiv652条截断使覆盖不完整。 证据包另排除1条未来日期候选，未作为新闻。

## 1. MaaS市场与产品形态

### 企业微信与WorkBuddy打通账号和授权上下文，向认证企业开放

- 雷峰网10月14日报道，企业微信5.0.12与WorkBuddy 5.8.0双向互通，机器人进入企业联系人列表，WorkBuddy支持企微账号登录，在企业授权范围内调用消息、文档等能力。
- 互通面向企微已认证企业，提供限免体验名额；管理员可分配账号、权限和用量。相对一般连接器，新增统一身份与组织内分发；1400万企微组织并不等于WorkBuddy客户数。官方版本说明未取得，未验证实际账户开通。

**产业判断：** 判断：统一身份和上下文可降低企业部署、授权与培训成本，使协作平台成为Agent分发渠道；集成深度也会提高切换成本。若权限粒度、数据质量或跨组织协作受限，连接未必转为有效完成率。观察认证企业实际开通率、任务成功率及权限审计负担。

**来源与核验范围：**
- [雷峰网 · 腾讯AI办公再进一步，企业微信与WorkBuddy深度联合](https://www.leiphone.com/category/industrynews/7m8YMd1LU7x6aDvM.html)；发布时间：2026-10-14T13:57:00+08:00；定位：已读雷峰网网页主文和完整RSS，定位版本、企业授权、认证企业及限免段；官方公告/实际账户未核。；阅读范围：full-text；ID：`5ff8f27599db0cfaed38`。

### 千问办公电商版开启邀测，将经营工具接入Agent工作流

- 雷峰网10月14日报道千问办公电商版开启邀测，包含跨平台经营看板、趋势及卖点分析、素材批量生成与ROI优化，称已接入生意参谋、有赞、千牛。
- 新增的是商家经营场景，和前一期面向个人的千问Go申请不是同一产品事件。当前为邀测；价格、商家覆盖、授权和实际ROI尚未取得官方条款或独立证据。Qwen/千问属于阿里品牌。

**产业判断：** 判断：经营数据和交易工具结合可让Agent从内容生产进入商家运营，生态接口与可执行权限可能比单轮生成更影响采用。若工具覆盖不足或归因不可靠，批量生成可能增加低效投放。观察获邀商家范围、跨平台读写能力、获客成本和可复核增量收益。

**来源与核验范围：**
- [雷峰网 · 千问办公发布电商版，开启邀测](https://www.leiphone.com/category/industrynews/eg8S5cDorgtGnzPy.html)；发布时间：2026-10-14T14:31:00+08:00；定位：雷峰网完整短讯主文及日期；未读官方原始公告、定价或商家后台。；阅读范围：full-text；ID：`e0049e56d8b5d4b3fef2`。

### BigQuery解释已GA的生成式AI词元配额，预算控制可到项目和用户

- Google Cloud10月14日技术文章解释近期已GA的四类每日配额，分别约束项目/项目内用户的输入及输出词元，跨区域汇总，输出包括thinking；embedding不在这些配额内。
- 配额耗尽后停止新的LLM调用，不同SQL函数可能返回部分结果或失败。AI.COUNT_TOKENS是输入下界估计，不包括函数包装、输出/推理及非文本输入；不能据配额直接保证固定美元账单。新增的是实施细节，不把本教程当GA首次公告。

**产业判断：** 判断：成本约束进入数据执行层，有利于把AI SQL从试验扩展到批量数据工作，治理和数据平台受益。不同模型价格、部分结果及配额执行延迟仍可能削弱预算可预测性。观察单位有效处理行成本、超限行为、失败重试与跨项目治理。

**来源与核验范围：**
- [Google Cloud Blog · Predictable AI spend in BigQuery: Introducing cost management for generative AI functions](https://cloud.google.com/blog/products/data-analytics/using-bigquerys-generative-ai-cost-management-features/)；发布时间：2026-10-14T16:00:00+00:00；定位：已读官方全文RSS和HTTP网页正文；定位Quotas、What's not covered、How enforcement works、AI.COUNT_TOKENS；未运行SQL或单独审核计费文档。；阅读范围：full-text；ID：`00d3d09a2175378871e6`。

### Amp客户案例呈现订阅登录、语音调度与编码外任务的组合

- OpenAI10月14日客户案例称Amp已集成Sign in with ChatGPT，并使用GPT-6 Astra支持写作/设计；Puck用于发起和管理其他Agent，Calling Puck由GPT-Live-1提供实时语音。
- 文章称Amp正在测试Ultrafast。相对纯代码助手，新增观察是身份计费入口、语音与任务协调的组合；这是案例披露日，文章未确认每项功能当日首发，也未列完整套餐、地区、价格或独立效果。

**产业判断：** 判断：订阅可携带性与实时入口可把第三方Agent变成持续使用的工作界面，分发和任务编排层受益。权益限额、平台依赖或语音干扰可能抵消便利。观察实际可用套餐、有效任务总成本和离开桌面后的完成率。

**来源与核验范围：**
- [OpenAI News · Amp puts AI agents to work beyond code with OpenAI models](https://openai.com/index/amp-beyond-coding)；发布时间：2026-10-14T12:00:00+00:00；定位：OpenAI案例主文Lowering the cost、Calling Puck及Ultrafast段；未读Amp完整发布日志和账户权益条款。网页文本快照，非HTTP原始响应。；阅读范围：full-text；ID：`57c3309db5bedcdec4e0`。

## 2. AI公司发展与新公司

### Third Moment披露万Agent长时研究案例，扩展工作流定制推理路线

- OpenAI10月14日客户案例称Third Moment Research使用Codex、GPT-6系列及GPT-6.1 Sol运行1万个并发Agent，研究会话36–48小时；外层harness决定重试、终止或转人工，Daybreak用于环境安全测试。
- 其[官网](https://thirdmomentresearch.com/)（未知发布日期的背景材料）提供按工作流改进的托管推理endpoint：采集轨迹、诊断、用户确认、评测与后训练/harness优化，再发布版本。新纳入跟踪的是既有公司，不宣称今日成立；官网日期未知。规模及效果均客户/供应商披露，无公开可比harness、成本或独立复现。

**产业判断：** 判断：专业工作流的失败轨迹和评测闭环可能形成区别于通用MaaS的服务壁垒，观测、隔离和调度基础设施受益。高token投入和人工确认可能限制单位经济，万Agent规模也不等于万份有效研究。观察付费客户、可复核改进、任务成本与人工复核量。

**来源与核验范围：**
- [OpenAI News · How Third Moment Research runs 10,000 agents for 36+ hours](https://openai.com/index/third-moment-research)；发布时间：2026-10-14T07:00:00+00:00；定位：OpenAI案例主文及Third Moment官网全部可见产品流程；未独立验证并发、收益、融资或法定注册主体。；阅读范围：full-text；ID：`a8b8c31de898145e14c8`。

### Anthropic开设新加坡办公室，与政府签署合作备忘录

- Anthropic10月14日宣布其亚太第五个办公室在新加坡开业，并与新加坡数码发展及新闻部签署MOU，涵盖安全、评测、采用研究及公私部门应用合作。
- 文章称GovTech逾1500名工程与技术人员已采用Claude Code，并提及Bedrock区域内推理。新增是本地组织和合作机制；MOU不等于采购收入，客户采用数字为公司披露。来源仅日期，18:00窗口边界不确定，已对照前一期去重。

**产业判断：** 判断：本地团队、区域推理和政府评测合作可降低受监管客户采购摩擦，区域云和交付服务受益。备忘录若未形成部署和持续采购，商业增量仍有限。观察本地招聘、合作项目交付与实际付费使用。

**来源与核验范围：**
- [Anthropic Newsroom · Anthropic开设新加坡办公室，与政府签署合作备忘录](https://www.anthropic.com/news/singapore-office-opening)；发布时间：2026-10-14T00:00:00+08:00；定位：官方公告全文，定位Supporting responsible AI和How Singapore is working with Claude；未审阅MOU全文、合同或客户审计。；阅读范围：full-text；ID：`241a0eb7150b75c2c4dd`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### Grok Voice 3.0开放API，维持每分钟USD0.08并自动升级latest别名

- SpaceXSI/xAI10月14日宣布Grok Voice 3.0当日通过Voice Agent API提供，每分钟USD0.08，grok-voice-latest已自动切换；相对前代价格不变。
- 低于1秒延迟、Tesla/Starlink对话量及无需人工解决比例均为厂商披露。厂商引述Artificial Analysis 10月13日结果，未核对完整harness、预算和原始评测，故不采用跨模型排名或普遍成本优势。来源仅日期，窗口边界不确定。

**产业判断：** 判断：同价升级和自动别名可降低语音Agent迁移成本，客服集成与工具执行层可能受益。实际语种、电话网络和工具时延可能吞掉模型延迟收益，自动升级也需回归验证。观察端到端完成率、每次解决成本和转人工率。

**来源与核验范围：**
- [xAI News · Grok Voice 3.0开放API，维持每分钟USD0.08并自动升级latest别名](https://x.ai/news/grok-voice-3)；发布时间：2026-10-14T00:00:00+08:00；定位：官方公告全文，定位Pricing and Availability、Used by Millions及评测归因；未读第三方评测全文、未实测延迟。；阅读范围：full-text；ID：`12251940b3b4d2234012`。
  日期仅精确到天，无法确认 18:00 边界。

### DeepMind与新加坡GovTech微调端侧Gemma反诈模型，应用分阶段推出

- DeepMind10月14日披露与GovTech微调Gemma，先以轻量分类器筛查，再由模型分析多轮对话；推理在设备上，应用需用户同意，推出将分阶段进行。
- 训练使用匿名化诈骗报告及情报数据，在GovTech管理的GCP环境内进行。相对通用安全能力，新增本地诈骗语境和端侧两阶段管线；未给出具体Gemma版本、模型大小、误报率、功耗或普遍可用应用清单。

**产业判断：** 判断：先筛查再调用模型可在隐私、功耗与检测深度间取舍，有利于端侧模型和本地数据合作。误报、对话访问权限和机型覆盖可能限制效果。观察实际应用交付、授权率、分语种漏报及电池消耗。

**来源与核验范围：**
- [Google DeepMind · Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)；发布时间：2026-10-14T02:00:14+00:00；定位：官方主文On-device AI、Under the hood和Built on strict governance；未读取底层模型卡、测试集或独立测量。；阅读范围：full-text；ID：`36a7e1c23fbbe3b1fdc0`。

## 4. AI Infra社区与工程趋势

### Dynamo发布GLM-5.3-Flash的SGLang实验快照，保留多模态验证限制

- Dynamo v1.6.0-glm-5.3-flash-dev.1（commit 6beb569）为非QA门禁的实验快照；以SGLang0.5.21/CUDA13、NVFP4权重和FP8 KV提供4张B200/GB200聚合、12张GB200分离配方，后者通过Mooncake/NVLink传KV。
- 聚合配方声明文本/图像/视频，分离配方为文本/图像；发布说明明确端到端多模态生成尚未验证，未附实测性能。新增是部署适配配方，不能当稳定生产支持或智谱模型今日首发。输入输出长度和并发没有性能结论，故不作速度排名。

**产业判断：** 判断：混合注意力模型适配正牵动缓存、处理器和GPU拓扑，框架集成能力影响新模型落地速度。非QA快照和端到端未验说明兼容不等于可运营。观察稳定版合入、视频正确性、生产回归与完整负载成本。

**来源与核验范围：**
- [NVIDIA Dynamo · Dynamo v1.6.0-glm-5.3-flash-dev.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-glm-5.3-flash-dev.1)；更新时间：2026-10-14T04:01:46+00:00；定位：官方Atom完整release正文及GitHub预发布标签，定位Summary、Models、Known Issues；未运行容器或逐个审阅PR。；阅读范围：full-text；ID：`703764fc18cc8a52512f`。

## 5. 模型与AI Infra论文

### AgentWeave提出工作流分解调度，处理长短Agent请求阻塞

- arXiv 10月14日公告的AgentWeave v1提出在聚合部署中把长请求分成细粒度执行单元，以流自适应调度减少长请求阻塞短请求和新请求。v1实际提交为10月10日10:55:44 UTC，并非今日投稿。
- 已读摘要及版本历史；作者在四类Agent应用上报告改善，但硬件、精度、模型、负载长度、并发和详细基线未读，本文不采用加速倍数。公告仅日历锚点，午夜是RSS载体，不代表准确发布时间，窗口边界不确定。

**产业判断：** 判断：Agent服务优化开始覆盖工具与LLM组成的整段工作流，调度平台可能从单模型批处理扩展到任务级服务。分解开销与状态依赖可能抵消收益。观察完整配置、短请求尾时延及同等资源任务吞吐；目前只是论文作者结论。

**来源与核验范围：**
- [arXiv model and infra papers · AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](https://arxiv.org/abs/2610.14804)；源站公告时间：2026-10-14T00:00:00-04:00；定位：arXiv摘要和Submission history；未读全文、图表、代码或独立复现。；阅读范围：abstract；ID：`d4165083d002a4fe5e71`。
  日期仅精确到天，无法确认 18:00 边界。

### SAFE-KV强调非前缀缓存的因果状态约束，保真修复未必省计算

- arXiv10月14日公告的SAFE-KV v1把非前缀KV复用看作相对同一prompt完整prefill的行为保持问题，从选定文档起重编码因果后缀。实际v1提交为10月10日21:19:57 UTC。
- 摘要基于Qwen2.5-7B-Instruct与HotpotQA-500/2Wiki-500，并指出保真修复需重算大部分上下文，在单请求L40S研究中策略对所有负载都选择完整prefill。已读范围不足以声称通用提速；精度/长度/预算未核。公告时间仅日历级，窗口边界不确定。

**产业判断：** 判断：KV节省必须同时核算行为偏差和修复成本，缓存服务可能需要从命中率转向正确性与总成本。多请求共享或其他模型可能出现不同收益，当前结果不能外推为所有缓存复用无效。观察真实并发、任务一致性和端到端成本。

**来源与核验范围：**
- [arXiv model and infra papers · SAFE-KV: Causal Suffix Repair for Behavior-Preserving Non-Prefix KV Cache Reuse in RAG](https://arxiv.org/abs/2610.15186)；源站公告时间：2026-10-14T00:00:00-04:00；定位：arXiv摘要、Comments与Submission history；未读36页全文、33张表或代码。；阅读范围：abstract；ID：`f15c5d5ffeb79e1528aa`。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

### ASML第三季销售EUR116.62亿，预计2027–2028计划供给仍不足

- ASML10月14日披露2026Q3净销售EUR116.62亿、净利润EUR49.60亿，毛利率57.5%；季度期间截至9月27日，按US GAAP、未经审计。全年销售EUR440–450亿为指引。
- 管理层称目前规划的2027/2028供给不能满足客户需求，正研究在此前沟通的2028扩产30%基础上继续增加产能。2029/2030客户下单兴趣不等于已签订单或确认收入。新增是季度兑现和产能预期；来源仅日期，窗口边界不确定。

**产业判断：** 判断：上游光刻产能与升级服务仍可能成为先进算力供给约束，设备和产能提升环节受益，扩产客户面临交付排期压力。需求预期可被取消订单、替代工艺和投资放缓推翻。观察实际订单、设备交付、产能爬坡和收入确认。

**来源与核验范围：**
- [ASML News · ASML第三季销售EUR116.62亿，预计2027–2028计划供给仍不足](https://www.investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026)；发布时间：2026-10-14T00:00:00+08:00；定位：官方季度公告正文、财务表、CEO outlook、脚注2及US GAAP/unaudited说明；未读投资者电话或完整财务附表。；阅读范围：full-text；ID：`a5ab26986e75e2108b82`。
  日期仅精确到天，无法确认 18:00 边界。

### NVIDIA将CUDA-X扩展至芯片工程，cuPotential仍处于early access

- NVIDIA10月14日宣布cuPotential用于原子交互模拟，并披露多家半导体公司的CUDA-X/AI采用。cuPotential为early access；NanoVDB在OpenVDB中开源，NPP通过CUDA Toolkit提供。
- Lam Research的NanoVDB加速SEMulator3D目标是年底发布，尚非已交付。新增是AI与仿真工具进入芯片工程流程；公告的多项倍数缺少统一硬件/精度/负载/基线，此处不作性能比较或推算晶圆产能增幅。

**产业判断：** 判断：模型与物理仿真结合可缩短工艺探索和缺陷诊断周期，EDA、仿真软件与GPU工具链受益。模拟误差、验证周期和物理设备产能仍限制转化。观察正式版本、客户量产采用、可比基准和最终良率改善。

**来源与核验范围：**
- [NVIDIA Newsroom · NVIDIA and Semiconductor Leaders Advance AI Across Chip Design and Manufacturing for AI-Defined Fabs](https://nvidianews.nvidia.com/news/nvidia-and-semiconductor-leaders-advance-ai-across-chip-design-and-manufacturing-for-ai-defined-labs)；发布时间：2026-10-14T16:10:00+00:00；定位：官方HTTP完整公告，定位cuPotential、Semiconductor Leaders及Availability；未逐项读合作方技术报告或复现。；阅读范围：full-text；ID：`e43508c4c22acdd3becf`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 323 条（其中线索 23 条），精选 13 个事件；未注明日期 6 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Stacklok Official：checked；打开官网公司页，核对品牌与ToolHive/Mecatl产品；未发现可核实本期日期的新增声明，不代表全站无新闻。；已知截断 0 条。
- Peppermint Official：checked；打开原融资公告，仍为10月8日背景，已入库去重；未查全部博客。；已知截断 0 条。
- Microsoft Command Line：checked；打开Decision-1旧技术公告；未将旧页面或发现时间视为今日发布。；已知截断 0 条。
- Satya Nadella Public Article：failed；指定X帖子浏览工具返回Internal Error，未取得正文；不能判断是否有新动态。；已知截断 0 条。
- Nous Research Official：checked；打开官网可见文本，产品/博客仅有限入口核查；无足够日期与正文确认本期新增，非完整全站检查。；已知截断 0 条。
- Healthleap Official：checked；打开官网产品页，旧融资背景不重收；未读取所有客户/研究文章。；已知截断 0 条。
- OpenAI News：checked；读取本期Third Moment/Amp原文及官方RSS；其他Block/SentinelOne案例只筛标题，不声称全文覆盖；ChatGPT release notes最新可见为10月9日。；已知截断 0 条。
- OpenAI API Changelog：checked；collect HTTP403，官方浏览工具恢复页面；本期日期检索未见Oct14条目，但页面长且导航占比高，未完成逐条新旧diff；不把页面变化当新事件。；已知截断 0 条。
- Anthropic Newsroom：checked；实际打开news列表，读10月14日新加坡办公室/MOU全文；选举保障文章作政策背景筛查，非本期重点事件。；已知截断 0 条。
- Anthropic Research：checked；采集入口与sitemap已检查；10月12日蒸馏/复制研究沿用已入库背景，不将采集或修改时间当新实验。；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 533 个，最近一次新增 2 个；检查于 10-15 09:04；已知截断 0 条。
- DeepSeek Research & News：checked；官网自动采集成功；浏览器补读API更新日志，最新可见9月10日，未核实本期官方模型发布。私域和团队社交不全。；已知截断 0 条。
- DeepSeek API Change Log：checked；浏览工具首次超时后一次重试恢复，已核对9月10日顶端条目；不是无访问情况下断言无新闻。；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-15 09:04；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-15 09:04；已知截断 0 条。
- Alibaba / Qwen Blog：failed；原生浏览器实际打开博客，仅返回导航/页脚，未取得正文或日期列表；阿里云press-room另行查过不能代替Qwen正文。；已知截断 0 条。
- Qwen · Hugging Face：checked；本次机器抓取HF新仓库入口；新仓库仅线索，不等于正式模型发布；许可和卡片未全读。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；实际打开官方Research页，最新可见Kimi K3/PerceptionBench为7月16日，入口未见可核实本期研究发布；产品渠道不全。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-15 09:04；已知截断 0 条。
- Z.ai 发布记录：ok；页面无变化；检查于 10-15 09:04；已知截断 0 条。
- 智谱开放平台发布记录：ok；最近一次检测到页面变化；检查于 10-15 09:04；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-15 09:04；已知截断 0 条。
- MiniMax News：failed；网页工具和原生浏览器均只取到导航，未获得news正文/日期列表。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-15 09:04；已知截断 0 条。
- Mistral AI：ok；feed 89 条；检查于 10-15 09:04；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 4 条；检查于 10-15 09:04；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-15 09:04；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-15 09:04；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 1 条；检查于 10-15 09:04；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-15 09:04；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-15 09:04；已知截断 0 条。
- ByteDance Seed Blog：checked；打开官方Research入口，仅有限可见文本；未完成全站及中文公众号检查，不能确认本期无动态。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-15 09:04；已知截断 0 条。
- Alibaba Cloud Press Room：checked；原生浏览器恢复press-room列表，顶部10月12日Genting MoU为旧背景；未把千问电商媒体稿当作官网确认。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个，最近一次新增 1 个；检查于 10-15 09:04；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-15 09:04；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-15 09:04；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-15 09:04；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个，最近一次新增 2 个；检查于 10-15 09:04；已知截断 0 条。
- xAI News：checked；实际读取News列表、Grok Voice3原文和release-notes本期入口；独立评测完整harness未读。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-15 09:04；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 8 条；检查于 10-15 09:04；已知截断 0 条。
- Qualcomm Newsroom：checked；打开官方releases及搜索核对news，最新相关AI宽带公告为10月12日背景；10月13日诉讼声明不在本期研究重点。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 19 条；检查于 10-15 09:04；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条。
- ASML News：checked；原官网入口恢复并跳转投资者站；实际读Q3财务公告、CEO展望、脚注与未经审计说明。；已知截断 0 条。
- TSMC Newsroom：checked；打开官方latest-news入口但返回含大量导航的有限文本；未逐条核实所有日期或补读财报，不断言无新闻。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-15 09:04；已知截断 0 条。
- Reflection AI Blog：checked；打开官网blog，仅有限可见列表；已知Beam旧事件不重复采用，未完成全站日期diff。；已知截断 0 条。
- Namespace Blog：checked；官网blog最新可核实融资为10月5日Series B，去重；未查全部文章。；已知截断 0 条。
- Vinci Official Blog：checked；打开官网blog有限列表，未获得可核实本期新事件；旧融资去重，不代表全站无新闻。；已知截断 0 条。
- TODAY Official Blog：failed；指定官网blog浏览工具仍失败，没有本期正文或日期证据。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；打开官网blog有限入口，旧融资与Jev背景去重；完整模型卡/最新动态未逐条补读。；已知截断 0 条。
- GlobalFoundries Official News：checked；打开官方news/events看到10月14日列表项目；未读其原文，无事实结论纳入。；已知截断 0 条。
- Meet Odyssey-3：checked；打开10月8日Odyssey3官方旧文章，背景去重；未逐段重核全部评测。；已知截断 0 条。
- Decart官网：checked；打开官网产品入口，未取得可核实本期交易公告，旧洽谈不升级为已收购。；已知截断 0 条。
- Microsoft Official Blog：checked；打开官方首页，有限可见列表；未全面覆盖研究/Foundry/云产品全部渠道。；已知截断 0 条。
- 模思智能官方新闻：checked；实际打开新闻列表，最新融资10月12日，旧事件去重；无可核实本期新条目。；已知截断 0 条。
- ModCraft产品官网：checked；打开官网产品入口，未知日期内容不作当天新闻；法定主体仍待核。；已知截断 0 条。
- Apple Newsroom：checked；打开官方Newsroom，仅取得首页/订阅文字，日期列表不完整；HomeView前期已入库，本期未完成Apple全站核查。；已知截断 0 条。
- Pluto Security：checked；打开官方blog，顶部融资10月13日已收录，未将转载作为新融资。；已知截断 0 条。
- SemiGraph 半图科技：checked；打开官网，品牌/产品仍可见；公司动态融资为2025年12月旧背景，未将前期媒体新轮报道当作官方证实。；已知截断 0 条。
- Third Moment Research Official：checked；collect后新纳入的官网入口，已实际读全部可见产品流程；未知日期只归档，不冒称起始自动采集覆盖。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方Atom/release入口本次抓取，未见本期新增稳定release；SGLang博客Fish Audio为10月13日日历日期的旧线索，未凭发现时间收录。；已知截断 0 条。
- SGLang Blog：ok；页面链接 7 个；检查于 10-15 09:04；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；本次Atom含v0.32.0rc1和proto-v0.6.0；前者是RC，后者仅短标题，未获得足够实质发布说明，不凑稳定版新闻。；已知截断 0 条。
- vLLM Blog：checked；官方博客入口自动核查，10月12日双向KV背景已入库，无已核实本期新文章。；已知截断 0 条。
- NVIDIA Dynamo：checked；实际读GLM-5.3-Flash预发布全文；另Motif dev.2仅候选，未将dev标签视为生产版。；已知截断 0 条。
- FlashInfer：checked；本次官方Atom入口成功，未见本期新增条目；RC与正式版区别保留。；已知截断 0 条。
- Mooncake：checked；本次官方入口成功，无已核实本期新release；Dynamo配方里的Mooncake使用单独归因。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-15 09:04；已知截断 0 条。
- PyTorch Foundation Blog：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；cs.CL+cs.DC RSS共保存60条，另652条受本地limit截断，完整RSS字节已归档。补查cs.DC官方new列表显示10月14日95条，但未逐条阅读。两篇仅摘要和版本史；不声称论文全覆盖。；已知截断 652 条。
- METR：ok；页面链接 26 个；检查于 10-15 09:04；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 100 个；检查于 10-15 09:04；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 1 个；检查于 10-15 09:04；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-15 09:04；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- Vals AI：checked；打开10月9日多Agent研究旧页，本期无经确认正文修订差异，不重复当新研究。；已知截断 0 条。
- Epoch InnovationEval：checked；打开既有InnovationEval页，旧评测背景去重；未阅读全文/日志的新版本差异。；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-15 09:04；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-15 09:04；已知截断 0 条。
- 工业和信息化部：ok；页面链接 21 个，最近一次新增 4 个；检查于 10-15 09:04；已知截断 0 条。
- 最高人民法院：ok；页面链接 81 个，最近一次新增 4 个；检查于 10-15 09:04；已知截断 0 条。
- 外交部例行记者会：checked；机器超时，浏览工具恢复记者会列表并看到10月14日入口；未阅读全文，不据列表作政策结论。；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个；检查于 10-15 09:04；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 16 个；检查于 10-15 09:04；已知截断 0 条。
- 国家数据局：checked；网页工具正文为空后，原生浏览器恢复官方列表；可见数据要素大赛10月9日等旧条目，部分动态模块为空，未查全部政策。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；打开财联社转载原文入口；10月10日利太智药融资为旧背景，未再作本期事件。；已知截断 0 条。
- TechCrunch AI：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条；可能漏采 2026-10-14T01:03 至 2026-10-14T12:00。
- The Information：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 5 条；检查于 10-15 09:04；已知截断 0 条；可能漏采 2026-10-14T01:03 至 2026-10-14T10:30。
- Financial Times Technology：ok；feed 25 条，关键词过滤 8 条；检查于 10-15 09:04；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-15 09:04；已知截断 0 条。
- New York Times Technology：ok；feed 22 条，关键词过滤 10 条；检查于 10-15 09:04；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 7 条；检查于 10-15 09:04；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 3 条；检查于 10-15 09:04；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 20 条；检查于 10-15 09:04；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-15 09:04；已知截断 0 条；可能漏采 2026-10-14T01:03 至 2026-10-14T02:14。
- 虎嗅：failed；采集robots不可用/禁止，网页工具访问同一RSS超时；本期完整窗口未补回。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 29 条；检查于 10-15 09:04；已知截断 0 条。
- 36氪：ok；feed 30 条，关键词过滤 15 条；检查于 10-15 09:04；已知截断 0 条。
- 钛媒体：ok；feed 14 条，关键词过滤 5 条；检查于 10-15 09:04；已知截断 0 条；可能漏采 2026-10-14T01:03 至 2026-10-14T17:49。
- 雷峰网：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- 极客公园：ok；feed 30 条；检查于 10-15 09:04；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-15 09:04；已知截断 0 条。
- C114 通信网：checked；首次快照needs-review；网页工具超时后原生浏览器恢复10月14日日期列表，已筛芯片/算力标题，正文未逐条读。；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 60 条；检查于 10-15 09:04；已知截断 0 条；可能漏采 2026-10-14T01:03 至 2026-10-14T17:47。
- 机器之心：failed；官方首页仅取得PRO会员导流和摘要，未取得本期文章正文或完整窗口列表。；已知截断 0 条。
- Reuters转述WSJ：checked；打开已知Decart收购洽谈转载，仍为旧报道；未当成交、不重复入本期。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 109 个，最近一次新增 34 个；检查于 10-15 09:04；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；按Oct13–15日期边界实际执行Reuters独家AI检索；搜索结果不足以支持本期新结论，未读付费全文。。
- bloomberg-ai：checked；实际执行窗口附近Bloomberg AI检索，并筛本次RSS；Anthropic营收等原始付费全文未取得，未直接采用融资/收入数字。。
- ft-nyt-wsj-ai：checked；实际执行FT/NYT/WSJ窗口检索并筛feed；未取得多数付费原文，个人刑事指控与未核实财务不入本期。。
- china-ai-companies-zh：checked；执行中国产品/模型/公司检索，补读千问办公、WorkBuddy等媒体原文；官方条款和中文私域不完整。。
- china-ai-policy-zh：checked；执行工信部/数据局/网信等窗口检索；列表与线索未获得足够正文支持，不作新政策结论。。
- china-chips-zh：checked；执行HBM/存储/GPU产能涨价中文检索；多数为媒体或旧背景，未将来源不足的涨价/产能数字收入。。
- embodied-world-models-zh：checked；实际执行具身/世界模型融资发布检索；结果多旧公告或二次聚合，未核实新的公司身份/融资，不据摘要建实体。。
- supply-chain-en：checked；执行HBM/CoWoS/High-NA/出口管制检索；ASML与NVIDIA一手补读，其他观点与旧材料去重。。
- newsroom-fallback：checked；执行Qualcomm/ASML/TSMC及xAI/Qwen/MiniMax站点检索；ASML原公告恢复，Qwen/MiniMax仍仅导航，明确保留失败。。

- 新公司发现：checked；实际开展中英文新公司发现检索。核对Third Moment官网产品与OpenAI客户案例后建立entity；Harmonic融资、高维医药/天序智能等缺一手原文仅保留线索，不能把聚合页当独立确认。。

证据包：`data/packets/daily/2026/10/2026-10-14/fbceab0e0de68281819a4bde1f56f9ed20afa598ac1583072b2fa01589c40cc8.json`；采集 run：`20261015T010317-0d63d952`。
