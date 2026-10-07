# AI 产业分析日报（2026.10.06）

统计窗口：2026-10-05T18:00:00-07:00 至 2026-10-06T18:00:00-07:00（洛杉矶时间，右端不含）。

实际生成：2026-10-06T18:23:24.166888-07:00（America/Los_Angeles）；18:00 为开始执行时间。

本期收录14个事件：企业Agent的上下文与资格访问规则进一步具体化，OpenAI新增专用判别API及用量层级调整，Mistral提供大型模型预览而Google发布可获取的多模态嵌入权重。验证产物、集群配置契约和harness研究说明交付与审核体系的重要性，但多数效果仍是厂商或论文作者披露。GPU与供应链没有经完整核验的精选新事件；中国重点对象已实际检查，Qwen等入口及媒体漏采、论文分页仍有覆盖缺口。

## 1. MaaS市场与产品形态

### Atlassian 扩展 OpenAI 合作：企业上下文与 Agent 工作流进一步结合

- OpenAI 与 Atlassian 宣布扩大合作，将 GPT-6 家族模型用于 Atlassian 平台及 Rovo；Teamwork Graph 提供人员、项目、文档和决策的企业上下文。协议扩展 GPT-6 Astra 与 GPT-5.6 系列的模型访问。
- OpenAI 披露 Atlassian 有超过 3,000 名开发者使用 Codex；插件可在适当权限下向 ChatGPT/Codex 提供 Jira、Confluence 等上下文。更深入的 Jira Agent 分派、进度追踪和 DX 效果测量仍在探索，不是今天全部正式可用。
- 相对库内办公与编码 Agent 背景，新增的是合作范围和公司内部采用披露；开发者人数不等于付费席位、收入或效率提升。

**产业判断：** 企业上下文、权限与工作记录的持有者可能掌握 Agent 的分发和反馈闭环，工作系统厂商因此受益。若跨系统权限或执行可靠性不足，模型访问扩展仍可能只提升搜索体验；应观察付费使用、任务完成率与实际开发周期，而非插件连接数。

**来源与核验范围：**
- [OpenAI News · Atlassian and OpenAI expand partnership to turn enterprise knowledge into action](https://openai.com/index/atlassian-partnership)；发布时间：2026-10-06T16:00:00+00:00；定位：主文及 Connecting OpenAI models with enterprise knowledge / Building toward the next generation of AI-powered teamwork；未审阅全部插件文档、客户数据及 DX 方法；合作计划和公司采用数字均为当事方披露；阅读范围：full-text；ID：`2896758265cec81d9589`。

### Anthropic 扩展 CVP：网络安全模型访问按资格和用途分层

- Anthropic 将 Glasswing 与 Cyber Verification Program 合并为分层访问体系：Defense Access、Red Team Access、Specialized Access；不同层级对应资格审核、允许用途与不同保护措施。
- 公告列出 Opus 5.5、Sonnet 5.5、Mythos 5.1 等模型，涉及 Claude、Vertex AI、Microsoft Foundry；Bedrock 路径受 EFS 资格约束。数据保留用于监控；特定既有 Fable/Mythos 零保留客户存在例外，未来 EFS 安排尚未完成。
- 增量是模型能力的交付与治理规则；不是所有模型对所有个人开放。正文只有 10 月 6 日日期，时区与窗口边界不确定，已对照前期去重。

**产业判断：** 实际可用能力由模型与访问层级共同决定，合规组织可能获得更适合授权测试的工具，平台采购和数据保留政策会影响采用。厂商演示不能证明普遍安全或效果；观察审核等待时间、可用平台、授权范围和真实误报率。

**来源与核验范围：**
- [Anthropic Newsroom · Expanding the Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program)；发布时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：Introducing the expanded Cyber Verification Program；访问层级、平台与 data retention / safeguards 说明；已读正文与访问/保留规则；未复现 CyScenarioBench，不用不同保护设置的结果作模型普遍能力或安全性排名；阅读范围：full-text；ID：`2bd8707fdab8226a9f67`。
  日期仅精确到天，无法确认 18:00 边界。

### OpenAI 发布 Decisions API beta：为分类与路由提供专用计费接口

- OpenAI 在10月6日changelog宣布 Decisions API 公开 beta，当前仅支持 gpt-6-luna；对文本/图像返回条件概率、固定选项或rubric分数，正式可用仍计划未来数周。
- 当前文档报价为 USD0.10/百万输入token，仅收输入费，不收cache读写或输出token费；区域处理溢价和长上下文输入乘数仍适用。这不是所有 gpt-6-luna 接口的统一价格。
- 新增产品形态是专用判别与路由接口，非自由生成或任意JSON工具调用；“约快10倍”为厂商主张，未提供本项目可复核的负载/基线，不视为实测。日期仅到日，边界不确定。

**产业判断：** 对固定分类和路由任务，仅输入计费可让高频判别组件更容易预算，应用编排与实时交互可能受益。若概率未校准或任务需要复杂工具调用，低延迟判别不能替代完整Agent；观察相同输入下准确率、尾时延和总账单。

**来源与核验范围：**
- [OpenAI API Changelog · OpenAI API October 6 updates: Decisions public beta and usage tiers](https://developers.openai.com/api/docs/changelog)；发布时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：Changelog October 6两条；Decisions How decisions work / Choose a question type / Pricing and availability；Rate limits Usage tiers / Spend limits；已读10月6日两项changelog、Decisions文档概述/问题类型/计费与可用性、rate-limits用量层级小节。文档是无日期的当前背景，不当作新发布；未调用API/测试速度，日期仅到日、时区未知；阅读范围：full-text；ID：`49e8d0577a5e1f9d20fd`。
- 补充官方文档：[Decisions计费与范围](https://developers.openai.com/api/docs/guides/decisions)、[Usage tiers门槛与月度上限](https://developers.openai.com/api/docs/guides/rate-limits)；当前文档无发布日期，作为changelog的背景说明。
  日期仅精确到天，无法确认 18:00 边界。

### OpenAI API 付费用量层级简化为 Build、Launch、Grow

- OpenAI 10月6日将付费用量层级从五档简化为 Build、Launch、Grow；按组织累计购买credit自动升级，仍保留 Free 层。
- 当前文档累计credit购买门槛为 USD5/100/500，对应月度用量上限 USD500/5,000/200,000；用量层级、模型速率限制和自行设置的spend cap是不同概念，不推导每个模型吞吐必然提升。
- 新增的是采购与扩容规则，既非模型token统一降价，也非月费套餐或ARR；日期仅到日、源站时区未知，已对照前期去重。

**产业判断：** 更少层级和明确credit门槛可能降低从试验转向规模使用的采购摩擦，应用创业团队可能受益。实际吞吐还受模型限流与组织配置约束；观察扩容等待、限流和资金占用，不能把较高月度上限当成已实现收入。

**来源与核验范围：**
- [OpenAI API Changelog · OpenAI API October 6 updates: Decisions public beta and usage tiers](https://developers.openai.com/api/docs/changelog)；发布时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：Changelog October 6两条；Decisions How decisions work / Choose a question type / Pricing and availability；Rate limits Usage tiers / Spend limits；已读10月6日两项changelog、Decisions文档概述/问题类型/计费与可用性、rate-limits用量层级小节。文档是无日期的当前背景，不当作新发布；未调用API/测试速度，日期仅到日、时区未知；阅读范围：full-text；ID：`49e8d0577a5e1f9d20fd`。
- 补充官方文档：[Decisions计费与范围](https://developers.openai.com/api/docs/guides/decisions)、[Usage tiers门槛与月度上限](https://developers.openai.com/api/docs/guides/rate-limits)；当前文档无发布日期，作为changelog的背景说明。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Jump Trading 披露长时研究 Agent 用法，人工检查仍在流程中

- OpenAI 客户案例介绍 Jump Trading 使用 ChatGPT 和 GPT-6 Astra 支持研究、编码及长时任务；由公司 LLM R&D 负责人描述递归改进和多数据研究过程。
- 案例仍保留定期人工检查、结果审阅和受控执行；研究信号可能错误，需接入现有评估流程。相对一般助手案例，新增的是高专业度研究团队的工作方式。
- 文章没有披露交易收益、收入、可复核的效率实验或客户总体采用率；不能从客户引述推出投资回报。

**产业判断：** 专业场景的商业价值可能来自长任务执行与既有研究评估系统的结合，工具集成和可观察性服务商可能受益。若人类复核成本抵消产出增量，自动化不会改善单位经济；应跟踪有效研究产出、复核负担和错误流入执行的比例。

**来源与核验范围：**
- [OpenAI News · How Jump Trading is scaling quant research with ChatGPT](https://openai.com/index/jump-trading)；发布时间：2026-10-06T12:00:00+00:00；定位：Jump Trading 主文：Lucas Baker 引述、长时研究任务及 regular check-ins / controlled execution；已读官方客户案例主文；未独立核实客户生产使用、收益或安全措施；阅读范围：full-text；ID：`ebb413cc5359756bf923`。

### Vinci 披露 2.5 亿美元 B 轮，扩展物理仿真与硬件设计平台

- Vinci CEO Hardik Kabaria 于 10 月 6 日披露完成 USD 250 million B 轮，估值 USD 1.5 billion；公司新闻稿称 Advent、Temasek、Xora 共同领投，AMD Ventures 等参与。融资额与估值分别记录，不作收入或 ARR。
- 官网将产品称为 Continuous Physics Reasoning，组合设计理解、Agent 编排、物理基础模型与 GPU 原生物理内核；公司称已在半导体工程项目商业化热、热机械和对流流体分析。
- 新增跟踪对象为 Vinci（官网页脚使用 Vinci4d 名称），不是同名大型基础设施集团。资金将用于扩大物理覆盖、工作流集成、人才和计算设施；拓展车辆/航空等仍是路线图。日期只有到日，边界不确定。

**产业判断：** 若物理分析能在设计修改尚便宜时反馈，可能降低后期返工并扩大可探索设计空间，先进封装与工程软件环节受益。若求解精度、数据准备或集成开销限制交付，融资不能直接转化为采用；观察客户续约、与签核求解器的一致性及完整流程耗时。

**来源与核验范围：**
- [Vinci Official Blog · Why Physics Needs to Move at the Pace of Design](https://www.getvinci.ai/blog/why-physics-needs-to-move-at-the-pace-of-design/)；发布时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：CEO正文 What waiting for physics costs / Physics inside the design process / What we are building toward；所链接公司 BusinessWire 新闻稿融资段与 About Vinci；公司新闻稿和 CEO 文章属于同一披露主体，不构成独立证实；未审阅客户数据、求解器基线或可比较硬件实验，不采用营销加速倍数；阅读范围：full-text；ID：`0af72b6a4f9fa603ef58`。
- 补充原始出处：[Vinci公司融资新闻稿](https://www.businesswire.com/news/home/20261006307372/en/Vinci-Raises-%24250M-Series-B-at-%241.5B-Valuation-to-Build-the-Intelligence-Infrastructure-for-a-New-Era-of-Hardware-Engineering)；与CEO文章同一披露主体。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### OpenAI 与 Ironclad 用合同工作任务评估计算机操作能力

- Ironclad 成为 OpenAI 软件研究合作伙伴，为研究模型的计算机操作训练与评估提供合同管理环境；研究包含 11 项法律、采购等任务，每项有 8–50 条判据。
- 训练使用来自公开 SEC EDGAR 合同的合成任务并过滤个人信息；公告明确不使用 Ironclad 私有客户或内部合同。评分属于研究任务层面，不代表端到端企业工作流成功率。
- 厂商报告 Astra Max 与 GPT-5.6 Sol High 的不同设置结果；预算不一致，不直接排名。文中的完成时间基于假定处理/生成速度估计，不能当作客户实测节省时间。

**产业判断：** 垂直软件可提供任务环境和可检查结果，帮助通用模型跨越操作界面与业务规则之间的差距，领域系统厂商因数据结构和评估入口受益。11 项研究任务仍可能偏离真实异常处理；观察新客户工作流覆盖、人工复核率和生产错误率。

**来源与核验范围：**
- [OpenAI News · Advancing computer use with Ironclad](https://openai.com/index/advancing-computer-use-with-ironclad)；发布时间：2026-10-06T10:00:00+00:00；定位：主文、Training and evaluation、11任务rubric、模型设置表及估计时间脚注；已读主文和脚注；未运行环境或复现评分。内部研究模型未发布，不写成可购买模型；阅读范围：full-text；ID：`f57eff9c23a4454b476b`。

### OpenAI 发布数学手稿与部分 Lean 证明，结果仍有不同核验阶段

- OpenAI 发布内部未公开模型产生的数学研究材料、部分 Lean 形式化证明及 10 个推理摘要；不是宣布该内部模型正式可用。
- openai/math README 当前版本列出 722 份手稿、372 个结果家族及约 4,000 个尝试问题；家族内可能包含主结果、配套论证或替代证明，722 不能等同于独立解决 722 个开放问题。
- 仓库明确并非所有结果都有 Lean 证明，未形式化材料可能存在问题。本次只读公告和固定 commit 的 README，未审阅手稿、证明对应关系或编译 Lean；平均思考计算量不是硬件成本或实际小时报价。

**产业判断：** 可下载证明材料把能力评价从单一分数推进到可审查产物，形式化工具和研究审核可能受益。形式化的命题是否准确映射原始开放问题、引用是否完整仍需专家检查；观察修订记录、独立核验与学术接受，而非手稿数量。

**来源与核验范围：**
- [OpenAI News · Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics)；发布时间：2026-10-06T12:00:00+00:00；定位：OpenAI公告主文；openai/math README Navigating the collection / How the results were produced / verification caveats；读取范围仅官方公告及 README；未验证数学正确性或解决开放问题主张；阅读范围：full-text；ID：`00427e47df5ef3064509`。
- 补充原始证据：[openai/math README固定版本](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/README.md)；仅读README，未核验手稿或Lean证明。

### Mistral Large 4 进入 API 公开预览，权重仍待月底交付

- Mistral Large 4 已在 Mistral Studio 提供 API 公开预览；官方计划月底发布权重，当前不能据此称为已开放权重或已确认最终许可。预览期间强化学习仍继续。
- 公司披露模型总参数约 1T、激活约 49B，原生多模态，训练使用自有欧洲数据中心的 3,800 个 NVIDIA Grace Blackwell GPU；这属于公司披露，不是本项目实测供给或成本。
- 官方介绍可组合强化学习环境、工具与奖励接口。相对前期 Beam 预览，新增一个独立模型供给选择；两者的评测、计算预算和交付状态不能混成统一排名。

**产业判断：** 预览 API 可先验证需求，后续权重交付才可能扩大自部署和区域主权选择，对封闭 API 厂商构成潜在竞争。若权重延迟或部署成本过高，API 预览并不改善私有化供给；观察实际权重、许可、量化支持与相同任务的总成本。

**来源与核验范围：**
- [Mistral AI · Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/)；发布时间：2026-10-06T12:00:27+00:00；定位：官方主文公开预览/月底权重说明；模型参数与欧洲训练基础设施；RL environment 小节；真实浏览器和 HTTP 正文均已读取；未核实最终权重、模型卡许可、第三方全部评测 harness 或硬件利用率。不采用跨口径领先排名；阅读范围：full-text；ID：`1ef243007176e85cc8c6`。

### EmbeddingGemma 2 发布多模态开放嵌入模型，支持端侧检索

- Google 发布 740M 参数的 EmbeddingGemma 2，支持文本、代码、图像、视频和音频嵌入；官方称使用 Apache 2.0 许可，Hugging Face 和 Kaggle 权重已可获取，Model Garden 支持仍是后续计划。
- 模型基于 Gemma 4，模块分为 270M 文本、170M 视觉、300M 音频；支持 8K 输入和 768 维嵌入，通过 Matryoshka Representation Learning 可截为 512/256/128 维。
- 相对文字嵌入，新增多模态统一检索与可裁剪模块。公告 Pixel 设备的量化权重内存数字不等于全流程峰值内存；本次不据此比较端侧时延或耗电。

**产业判断：** 本地多模态索引有机会让个人助手检索私有媒体并减少上传需求，端侧设备与本地检索应用受益。下游生成若仍走云端，嵌入在本地并不保证整个流程数据不出设备；观察量化后召回质量、功耗、峰值内存与产品权限。

**来源与核验范围：**
- [Google DeepMind · EmbeddingGemma 2: an open, lightweight multimodal embedding model](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)；发布时间：2026-10-06T19:57:04+00:00；定位：主文多模态/模块参数、Matryoshka和端侧说明、许可与获取渠道；已读公告正文；模型卡、全部框架支持和实际端侧性能未逐项核验，所有数字保留厂商归因；阅读范围：full-text；ID：`c11a83f73b42d7563944`。

## 4. AI Infra社区与工程趋势

### NVIDIA 介绍 AICR v1.0：固定集群配置契约与可追溯验证

- NVIDIA 介绍 AI Cluster Runtime v1.0 的稳定 CLI、REST、Go SDK 和制品 schema；snapshot 记录观测状态，recipe 固定期望依赖，bundle 渲染部署制品，validation 记录实际集群证据。
- recipe 本身不负责持续协调集群，部署由 Helm、Argo CD、Flux 等执行；安装成功与性能符合要求分开，验证结果可形成带签名证据。
- 新增的是稳定接口与配置/验证边界，不能把签名当成独立复现，也不把兼容契约当成任意硬件的性能保证。

**产业判断：** 固定版本与可追踪验证有助于减少集群升级和交付中的兼容风险，集成与运维厂商可能受益。若配方未覆盖实际网络、驱动或负载，稳定接口仍不能防止运行退化；观察第三方集成、配方覆盖与重放验证差异。

**来源与核验范围：**
- [NVIDIA Technical Blog · AICR v1.0: Open, stable, and verifiable GPU cluster configuration](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration/)；发布时间：2026-10-06T16:13:47+00:00；定位：AICR v1.0 compatibility contract；snapshot/recipe/bundle/validation；What recipes do not do；已读 NVIDIA 技术博客全部正文；未独立安装、运行或核查每个 release/tag，不把博客中的集成披露视为生产采用证明；阅读范围：full-text；ID：`f9524fd6a641f04a61eb`。

### PyTorch 介绍 FBTriton：稀疏嵌入路径转向可配置的 Python/Triton

- PyTorch 官方博客介绍 FBTriton，将 Table Batched Embeddings 前后向稀疏路径从 CUDA 模板转为普通 Python/Triton，并通过配置选择硬件特性与执行路径。
- 文章实验为 GB200、FP16 权重、exact row-wise Adagrad，307 个分片配置、283 种不同形状；部分短 run 仍慢于 CUDA，长 run 只达到相当表现。完整软件版本与所有输入形状未逐项核对，因此不把结果推广为 Triton 普遍更快。
- 相对库内 PyTorch 硬件接入综述，新增具体推荐系统稀疏路径的工程案例。正文的未来融合空间属于路线图，本项目不执行算子移植或跑分。

**产业判断：** 可配置实现可缩短优化与硬件接入迭代时间，推荐系统工程团队及替代硬件生态可能受益；特定指令和调参也可能维持硬件差异。观察不同芯片上的完整训练耗时、维护成本和未受益形状，不能用单个局部内核结果推断训练总成本。

**来源与核验范围：**
- [PyTorch Foundation Blog · Modernizing Table Batched Embeddings with FBTriton](https://pytorch.org/blog/modernizing-table-batched-embeddings-with-fbtriton/)；发布时间：2026-10-06T22:57:33+00:00；定位：官方 feed 完整正文 §5 Results and Analysis / Where Triton still loses / §6 Beyond Performance；已读 feed-content 全文（含尾部）；外链代码、图表图片与全部实验配置未检查，未复现；阅读范围：feed-content；ID：`20a052b4dc40d9691eaf`。

## 5. 模型与AI Infra论文

### HEAR：把 Agent 工作流意图与推理引擎状态连接起来

- HEAR 提议双向 Harness–Engine 协议：harness 提供工作流依赖、上下文生命周期和执行需求，引擎返回队列、KV 状态、能力及操作结果；协议语义与优化策略分开。
- 已读 §3 区分意图/控制、偏好/要求、观测/保证、接受/完成；§4 展示缓存协调和角色推理配置，策略收益随负载变化，没有单一策略在所有负载占优。
- v1 于 2026-10-05T16:07:33Z 提交，10 月 6 日进入 cs.AI 公告列表；本期按公告日纳入（仅到日、边界不确定），不称今天首次投稿。已读摘要、协议及实验可见正文，未读附录与代码，不采用加速倍数。

**产业判断：** 当多 Agent 任务争用缓存和队列，跨层信息可能帮助减少重复计算，同时保持依赖和等待约束；编排与服务框架接口可能成为竞争点。若状态过期或反馈开销超过收益，协议未必改善成本；观察时延尾部、信息新鲜度和跨框架适配。

**来源与核验范围：**
- [arXiv model and infra papers · Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving](https://arxiv.org/abs/2610.06597)；源站公告时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：arXiv v1 摘要/提交历史；HTML §3 Protocol / §4 Experiments；cs.AI 10月6日公告第9条；未逐项核对精度、软件版本、全部长度/并发设置及附录，不进行跨系统排名或复现声明；阅读范围：full-text；ID：`0365f0df8dab5c310603`。
- 已读正文：[HEAR HTML v1](https://arxiv.org/html/2610.06597v1)；协议和实验可见正文，未读附录或复现。
  日期仅精确到天，无法确认 18:00 边界。

### HERA：让 harness 与任务环境共同演进，学习何时停止

- HERA 通过受控环境变更，把同一请求构造成可完成与不可完成的配对任务；执行失败诊断同时驱动 harness 调整和新环境生成，基础执行模型保持固定。
- 已读方法包含独立 solver 验证、语义审查和 rescue 检查，以减少把仍可完成的任务错误标成不可完成；评估要求在可行任务行动、不可行任务停止。
- v1 于 2026-10-05T15:49:12Z 提交，10 月 6 日列入 cs.AI 公告第13条。仅读摘要、引言部分与方法 §3，未完整审阅实验/附录；不采用摘要中的收益、跨模型排名或成本数字。公告日仅到日、窗口边界不确定。

**产业判断：** 企业 Agent 的价值还取决于识别缺失前提和停止无效操作，环境构造与失败反馈可能提升可靠性评估的区分度。自动生成的不可行标注仍可能漏掉替代路径，过度停止也会降低完成率；观察人工复核标签、可行任务误停率及跨业务迁移。

**来源与核验范围：**
- [arXiv model and infra papers · HERA: Harness–Environment Co-Evolution for Reliable Agentic Abstention](https://arxiv.org/abs/2610.06563)；源站公告时间：2026-10-06（仅日期；源站时区未知，00:00 为解析占位而非原站时刻）；定位：arXiv v1 摘要/提交历史；HTML §3.1 Construction / §3.2 Co-Evolution；cs.AI 10月6日公告第13条；与既有 RRSI/RSI 的增量在停止决策和环境–任务配对；未执行项目代码或验证作者成本结论；阅读范围：full-text；ID：`ca73ad6631f866e61d8b`。
- 已读正文：[HERA HTML v1](https://arxiv.org/html/2610.06563v1)；方法§3，未完整审阅实验和附录。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

本期未收录经核验的新事件；覆盖情况见文末。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 184 条（其中线索 13 条），精选 14 个事件；未注明日期 1 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- OpenAI News：checked；已读本期4篇官网正文与官方RSS时刻：Atlassian、Ironclad、数学材料、Jump Trading；未逐篇审阅其他历史公告；已知截断 0 条。
- OpenAI API Changelog：checked；已读10月6日Decisions beta及三档paid tier两条，补读Decisions概述/计费、rate-limits用量层级；未调用API。文档无发布时间只作背景；已知截断 0 条。
- Anthropic Newsroom：checked；官网News实际核对10月6日CVP并阅读全文；其余列表最新旧文10月2日/10月1日；日期仅到日；已知截断 0 条。
- Anthropic Research：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Anthropic 站点地图：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- DeepSeek Research & News：checked；官网Research & News列表可见最新9月10日V4.1 Flash；研究列表最新6月24日。已检查的可见列表无本窗口日期，未检查公众号/私域；已知截断 0 条。
- DeepSeek API Change Log：checked；已读官方updates列表及顶部更新，最新9月10日；未把正文日期不变或页面hash变化当新发布；已知截断 0 条。
- DeepSeek 模型与价格：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- DeepSeek · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Alibaba / Qwen Blog：failed；真实浏览器打开qwen.ai/blog并沿官方Latest Advancements到/research#research_latest_advancements，仍只有导航/排序，正文列表不足；不能据此说Qwen没有新闻；已知截断 0 条。
- Qwen · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；机器入口/en/blog和浏览工具/blog均检查，后者跳转kimi.ai/blog；可见最新K3/PerceptionBench为7月16日，无本窗口列示；日期缺失的新链接未当新闻；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Z.ai 发布记录：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 智谱开放平台发布记录：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 智谱 · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- MiniMax News：checked；真实浏览器news列表最新8月26日业绩、8月3日H3等；页脚M3/Music3.0无核实日期，未当本期发布；公众号未覆盖；已知截断 0 条。
- MiniMax · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Mistral AI：checked；机器官方RSS+真实浏览器+HTTP主文核对Large 4公开API预览与未来月底权重；未核验最终权重/许可及全部第三方harness；已知截断 0 条。
- Meta Newsroom：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- AI at Meta Blog：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Google DeepMind：checked；补读EmbeddingGemma 2官网全部正文和可用范围；其余候选仅筛标题/日期，未逐篇核对模型卡；已知截断 0 条。
- Google AI Blog：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Google Cloud Blog：failed；HTTP采集被robots阻断；浏览工具访问同域HTML成功，但本期列表/原始正文未补齐，不能把可到达解释为无新闻；已知截断 0 条。
- Tencent Newsroom：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Tencent · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- ByteDance Seed Blog：checked；真实浏览器/en/research可见Blog最新8月5日/7月31日，论文列表7月6日；已检查可见列表未发现本窗口日期，不代表全部渠道；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Alibaba Cloud Press Room：checked；真实浏览器press-room可见前10项最新9月23日/9月22日，未发现本窗口日期；Qwen品牌独立页面获取失败另列；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- xAI News：checked；浏览工具news列表可见最新9月28日TeamBots、9月21日Grok4.7，未发现列表本窗口日期；非全面渠道核验；已知截断 0 条。
- NVIDIA Newsroom：checked；机器robots失败，浏览工具同官网HTML可读：10月6日电信开源模型/10月5日癌症案例等。仅检查列表，未完整核验这些正文；未发现可选硬件新品，非全面无新闻；已知截断 0 条。
- NVIDIA Blog：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- AMD Press Releases：checked；机器robots失败，浏览工具同官网列表可读；10月6日16:15 EDT为财报发布日期通知，9月28日收购旧文。非本期已公布财报或新硬件；已知截断 0 条。
- About Amazon：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Qualcomm Newsroom：checked；浏览工具官方press列表可见10月5日华为专利许可；只到日、未新增本期产品事实，未当10月6日发布；已知截断 0 条。
- Samsung Newsroom：checked；机器TLS失败，浏览工具同官网列表可读；10月6日为SmartThings/艺术内容，9月29日Helix投资为旧文，未据此推出HBM供给变化；已知截断 0 条。
- SK hynix Newsroom：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- ASML News：failed；官网浏览工具访问失败；限定官网检索只发现旧9月8日材料，未恢复本期入口正文；已知截断 0 条。
- TSMC Newsroom：checked；浏览工具官方latest-news列表最新9月10日收入、9月8日High-NA合作；媒体涨价线索无本期一手原文，不当已发生新事实；已知截断 0 条。
- Volantis（公司新闻稿）：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Reflection AI Blog：checked；官网blog实际补查，Beam预览仍为前期已核实10月5日资料，无新增权重交付一手证据，去重跳过；已知截断 0 条。
- Namespace Blog：checked；官网blog实际补查，Series B及Agent infra披露属于前期，未找到增量证据，去重跳过；已知截断 0 条。
- Vinci Official Blog：checked；新发现公司：已读CEO主文及其所链接公司BusinessWire新闻稿，核对身份、产品归属、USD250M融资/1.5B估值；同主体归因，性能未独立验证；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；已读官方Atom前4个版本元数据，最新v0.5.21更新时间10月2日，未把旧版本更新作本期新release；已知截断 0 条。
- SGLang Blog：checked；官网列表已读：最新9月23日Unified Radix Cache，9月20日RLinf，9月10日V4.1；可见6条无本窗口发布；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；已读官方Atom版本及候选正文：本期v0.31.1rc0是RC；v0.31.0更新时间变化，正式published_at已在前期核验并入库。本期不重复宣称正式新发布；已知截断 0 条。
- vLLM Blog：checked；官网列表可见最新9月29日/9月24日/9月22日，未发现列示本窗口发布；未读所有历史正文；已知截断 0 条。
- NVIDIA Dynamo：checked；已读官方Atom前4个版本元数据，最新1.5.0-motif-3-dev.1为10月2日，正式1.5.0为9月21日；开发版不当正式发布；已知截断 0 条。
- FlashInfer：checked；已读官方Atom最新rc4/rc5/0.7.2rc1日期与简短tag/changelog正文；都是RC且实质说明不足，未当本期正式版本事件；已知截断 0 条。
- Mooncake：checked；已读官方Atom前4项元数据，最新0.3.14-rc1为9月7日；未把候选版作正式release；已知截断 0 条。
- NVIDIA Technical Blog：checked；已补读AICR v1.0全部技术正文。DOCA GPUNetIO/Green Contexts候选只到短feed且web失败，正文不足未采用；没有做部署和性能复现；已知截断 0 条。
- PyTorch Foundation Blog：checked；FBTriton feed全文含尾部已读；保留GB200、FP16、Adagrad和形状限制，不跨硬件排名，外链代码与图片表格未检查；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；配置cs.CL+cs.DC RSS被robots阻断；浏览工具cs.AI recent补看10月6日554项中的首50，全文只选读HEAR和HERA的已列章节。未覆盖其余分页、cs.CL/cs.DC全量或所有论文全文；公告日与提交日分开。日期专用URL429失败；已知截断 0 条。
- METR：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- UK AI Security Institute Blog：checked；机器TLS失败，浏览工具同官网blog列表可读，最新10月1日/9月28日；未阅读全文或扩大到未列示研究；已知截断 0 条。
- Artificial Analysis Articles：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Artificial Analysis Changelog：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- SemiAnalysis：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- NIST News：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- US BIS News & Updates：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 工业和信息化部：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 最高人民法院：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 外交部例行记者会：checked；机器robots失败，同官网例行记者会列表补查10月6日答记者问；只核查列表，没有阅读全文，不据此断言无AI政策事件；已知截断 0 条。
- 中国政府网 政策：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 重庆市大数据应用发展管理局：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 国家数据局：failed；浏览工具同官网只有空正文（0行），无法恢复国家数据局动态；不表述为无政策新闻；已知截断 0 条。

### 媒体直连 feed

- TechCrunch AI：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- The Decoder：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条；可能漏采 2026-10-05T03:11 至 2026-10-06T10:50。
- The Verge AI：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- The Information：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- Bloomberg Technology：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条；可能漏采 2026-10-05T03:11 至 2026-10-06T19:41。
- Financial Times Technology：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- Financial Times AI：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- New York Times Technology：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- SCMP Tech：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- MIT Technology Review：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条；可能漏采 2026-10-05T03:11 至 2026-10-06T10:35。
- Ars Technica AI：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- Tom's Hardware：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- 量子位：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 虎嗅：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- IT之家：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条；可能漏采 2026-10-06T01:03 至 2026-10-06T09:31。
- 36氪：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 钛媒体：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 雷峰网：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- 极客公园：failed；本轮HTTP采集失败；浏览工具同一来源feed/入口兜底仍不可读或超时。未恢复完整正文，不能解释为没有新闻；已知截断 0 条。
- 智东西：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- C114 通信网：checked；机器robots失败，浏览工具同站列表可读，最新可见10月2日/9月30日；未覆盖全部频道；已知截断 0 条。
- 快科技（驱动之家）：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。
- 机器之心：failed；浏览工具页面正文不足，不能恢复可判定日期的新闻列表；不表述为没有报道；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；本轮入口采集ok；仅作为候选与日期筛选，未逐篇阅读全文，不据此断言无新闻；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- bloomberg-ai：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- ft-nyt-wsj-ai：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- china-ai-companies-zh：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- china-ai-policy-zh：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- china-chips-zh：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- embodied-world-models-zh：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- supply-chain-en：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。
- newsroom-fallback：checked；已按 after:2026-10-05 before:2026-10-07 执行该中/英文发现检索；粗日期结果仍须核对准确窗口，搜索摘要仅为线索，未取得一手全文的融资/IPO/订单传闻未选用。

- 新公司发现：checked；已做中英文新公司发现。Vinci回查官网/公司新闻稿并加入跟踪；Ghost主报道10月5日11:07 PDT在本窗口之前，Hark/MirrorParticle/Melius等未读一手正文，中文具身/世界模型检索多为旧文；未核实对象不建公司事实页。

证据包：`data/packets/daily/2026/10/2026-10-06/d1bf88e1e3c25ad229692ce820d0ee91bdba490030c804695fdeb60c80dbe457.json`；采集 run：`20261007T010511-e3e3d943`。

补充覆盖限制：Techmeme 10月5日和6日 h2355 快照获取失败，媒体限定检索不能补回全部已挤出feed条目。无本地截断/采集上限警报不代表上游完整；cs.AI 554项仅筛首50，其余分页及cs.CL/cs.DC全量未完成。未知日期1条仅归档，不作为本期新闻。

知识入库：新建并发布15页（11来源、2论文、1公司、1综合研究），更新0页；重复背景与未核实线索详见 research-audit.json。[[research/synthesis/agent-delivery-and-verification-20261006|Agent交付与验证综合研究]]；[[reference/entities/vinci|新增Vinci跟踪页]]。
