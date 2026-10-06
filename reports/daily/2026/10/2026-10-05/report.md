# AI 产业分析日报（2026.10.05）

统计窗口：2026-10-04T18:00:00-07:00 至 2026-10-05T18:00:00-07:00（洛杉矶时间，右端不含）。

实际生成时间：2026-10-05T18:23:15.945992-07:00（America/Los_Angeles；UTC 2026-10-06T01:23:15.945992+00:00）。

本期筛选174条日期合格候选，收录10个事件：ChatGPT广告与文本溯源、Google Cloud迁移Agent、Namespace融资、Reflection Beam预览、vLLM正式版本、两篇PyTorch阶段综述和两篇论文。主要变化是商业化与可信分发机制扩展，Agent供给链延伸到迁移、构建/测试和输入管线；预览、后续计划与正式可用分别标明。新增13个已发布知识页，更新既有页0个，回查默认query/get_page及raw hash均通过。GPU栏目没有达到本期证据标准的精选事件，不代表没有行业变化。

本轮于洛杉矶2026-10-05 18:01开始，实际生成时间见报告头及manifest.generated_at。核实窗口为[10月4日18:00,10月5日18:00)，America/Los_Angeles，当日实际24小时；右端不含，配置一致。本周周报首个到期日为10月9日，本轮未到期。Namespace/Beam及论文公告日期只有日，来源时区/具体时刻未知，边界不确定，并已与前一期事件去重；两篇论文提交日期均为10月2日，不说成当天提交。

覆盖：本轮93个启用来源机器检查，71成功、12失败、10需浏览器；同源补查结果逐项列于下方。Qwen博客、国家数据局、重庆数据局、机器之心文章列表、Artificial Analysis、Bloomberg、MIT Technology Review和虎嗅仍有获取或正文不足。The Verge和IT之家历史采集gap与本窗口重叠，起止保存在research-audit.json；补检索未保证补齐。命令每源保存上限60（配置可更高），未报本地列表上限或源文本截断警报；证据包会裁剪展示文本，原始raw完整保留并用于选题阅读。1条未注明日期材料、1条未来日期材料均排除，绝不以采集日替代发布日期。

未完成范围：大多数未选候选仅初筛标题/feed内容，付费媒体全文、公众号/私域、全部论文分页与全文、技术报告及部署实验未完成。cs.AI本日266条只筛首50条，并检查cs.LG/cs.DC首页；两篇论文仅摘要/版本/公告记录，未采用成绩排名。机器状态的显示时区可能为Asia/Singapore，日报窗口与归档日期始终按America/Los_Angeles。

## 1. MaaS市场与产品形态

### ChatGPT 将测试图像生成广告，并扩展转化与增量测量

- OpenAI 宣布新的视觉广告格式：计划本月稍晚在美国与首批广告主测试，在图像生成场景单独展示并标注广告；不是宣布今天全面可用。
- 新增转化集成和增量测量合作伙伴。相对库内购物助手与工作助手案例，新增的是广告变现及广告主测量体系。
- 已读官网正文，未逐项读合作伙伴外链与案例数据；独立于回答的设计为公司主张，未验证实际执行。

**产业判断：** 判断（derived）：生成式交互逐步成为可销售的广告库存，转化集成与增量实验会影响广告主是否持续投放，测量服务商可能受益。反例是点击和归因增长没有带来真实增量，或广告体验影响用户留存；应观察实际测试覆盖、增量实验结果和广告主续投，而不能从合作名单推断收益。

**来源与核验范围：**
- [OpenAI News · Building advertising for the way people use AI](https://openai.com/index/new-chatgpt-ads-format-and-measurement)；发布时间：2026-10-05T10:00:00+00:00；定位：正文 New ad formats / Improving measurement / 品牌安全与隐私说明；本月稍晚测试范围。；阅读范围：web-rendered-text；ID：`2d8e70fb45cef7470a5b`。

### OpenAI 推出文本水印选择，欧盟 ChatGPT 与 Codex 将分批覆盖

- OpenAI 称即日起为部分 API 模型提供全球可选文本水印，默认关闭；欧盟符合条件的 ChatGPT/Codex 输出将在未来数周逐步加水印。
- 检测器只向获准研究机构等有限开放；短文本、受限格式和编辑会影响检测。相对已有知识新增文本溯源的产品推出范围，不能据此确认文字真伪、所有权或作者身份。
- 已读官方产品政策正文，技术报告及检测实验未读；厂商报告不等于独立测量。

**产业判断：** 判断（derived）：溯源能力开始进入产品分发和企业采购条件，模型供应商与内容验证服务需要处理不同地区的输出策略。反例是短文本和编辑削弱检测，不能将水印当作完整审计。观察实际模型覆盖、多语言误报/漏报与研究检测器开放范围；本项不推断已满足某项法律要求。

**来源与核验范围：**
- [OpenAI News · Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance)；发布时间：2026-10-05T15:00:00+00:00；定位：正文 Rollout / How textGrain works / Detection limitations / 适用范围与FAQ。；阅读范围：web-rendered-text；ID：`d2b5b29b4c8155256199`。

### Google Cloud Modernize 将云评估和应用迁移组织成 Agent 产品组合

- Google 发布 Modernize 产品组合与控制台 Modernization Hub，整合基础设施评估、Java/.NET 和大型机应用现代化。Agentic Quick Estimator 标为 GA，EKS→GKE Migration Agent 标为 Public Preview，并有人工审批与 GitOps 约束。
- 相对库内办公与对话助手，新增面向云迁移决策和执行的企业 Agent 形态。公告中的客户案例及节省幅度是厂商引用，不代表本次产品的独立效果。
- 网页正文已读，控制台、产品文档、客户效果与所有外链未实测。

**产业判断：** 判断（derived）：云厂商可以把 Agent 放进迁移评估和代码改造流程，降低获客与迁移服务门槛，并争夺存量云工作负载。反例是遗留系统的许可、权限和业务等价验证限制自动化收益。观察正式完成的跨云迁移、回滚/等价测试通过率与总成本，不能从预览工具推断已生产采用。

**来源与核验范围：**
- [Google Cloud Blog · Introducing Google Cloud Modernize, transforming for (and with) AI](https://cloud.google.com/blog/products/infrastructure-modernization/google-cloud-modernize-accelerate-transformation-with-ai/)；发布时间：2026-10-05T16:00:00+00:00；定位：Agentic infrastructure assessment；Automated container transitions to GKE；Application modernization with Modernization Hub。；阅读范围：full-text；ID：`84ef5a781e78045af14f`。

## 2. AI公司发展与新公司

### Namespace 披露 4,200 万美元 B 轮，扩展编码 Agent 的构建与测试设施

- Namespace 官网披露近期完成 4,200 万美元 B 轮，Scale Venture Partners 领投；累计融资 6,500 万美元。币种为美元，融资额不是收入、ARR 或估值，交易完成的具体日期未公布。
- 资金计划用于产品及数据中心扩展，包括 Mac 机群；Devboxes 与 GitHub Actions runners 面向跨 Mac/Windows/Linux 的编码、构建和测试。新增跟踪实体 Namespace Labs, Inc.，不是将融资日期当作成立日期。
- 官网日期仅到2026-10-05、时区未知，窗口边界不确定；与前期去重无同事件。仅核实公司披露，交易到账/客户成效未独立核实。

**产业判断：** 判断（derived）：编码 Agent 生成更多候选修改，会增加编译、测试及隔离环境需求，使 CPU 与 Mac 实体基础设施也成为供应环节。反例是无效提交增多而实际交付不增，环境收入未必与生成量等比例增长。观察付费留存、利用率、单次有效交付成本与资本开支；厂商收入增长主张没有绝对基数，不推算 ARR。

**来源与核验范围：**
- [Namespace Blog · Announcing our $42M Series B](https://namespace.so/blog/series-b)；发布日期：2026-10-05（仅日期；时区与时刻未知）；定位：融资开篇；The next 100 billion commits；Investing in Mac at any scale；公司页脚。；阅读范围：web-rendered-text；ID：`7be89e5e058e4fabe4ca`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### Reflection 预览 Beam：501B MoE，权重与 Apache 2.0 许可仍待本月发布

- Reflection 公布 Beam 文本模型预览，披露 MoE 总参数 501B、激活参数 23B；当前向少数早期用户开放并提供等待名单，权重、技术文档和 Apache 2.0 发布是本月后续计划。
- 相对已有模型跟踪新增 Reflection/Beam；官网的推理计算优势按近似 FLOPs 口径估算，排除部分上下文与服务开销，不能直接换算实际价格、延迟或跨模型排名。
- 日期仅到2026-10-05、时区未知，边界不确定，前期无重复；已读官网文本，未读完整技术报告、模型卡或评测harness。不把open-weight标题当作当前权重可下载。

**产业判断：** 判断（derived）：若权重与部署材料按计划交付，企业自部署和托管 MaaS 会多一个模型选择，开源工具链可能受益。反例是大 MoE 总权重仍带来显存、分发和预填充成本，激活参数少不等于整机成本低。观察真正发布的权重/许可、完整评测预算，以及同硬件和负载下的服务质量与成本。

**来源与核验范围：**
- [Reflection AI Blog · Introducing Beam: Reflection’s 501B open-weight model](https://reflection.ai/blog/introducing-beam)；发布日期：2026-10-05（仅日期；时区与时刻未知）；定位：模型结构与 inference compute 解释；The Path Ahead。；阅读范围：web-rendered-text；ID：`917ba46d3f15f0c5b9b7`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### vLLM v0.31.0 正式发布：GPU 权重驻留重启与缓存隔离改进

- GitHub Releases API 标明 v0.31.0 正式 published_at 为10月5日06:44:55 UTC、prerelease=false；10月2日是 created_at，Atom updated_at 是10月5日06:45:40 UTC。三种时间已分开。
- 发布说明包括 GPU 权重 preload daemon、实验性 TP=1 CRIU 已初始化引擎快照、LoRA/cache_salt 前缀缓存隔离，以及多模态请求参数需显式信任的兼容性变化。相对旧候选只有提交署名，本次补全正式发布说明。
- 阅读发布重点与相关条目，未逐项审阅PR或生产验证；正式发布不等于实际生产采用。

**产业判断：** 判断（derived）：服务重启、缓存隔离和兼容性治理逐步与吞吐优化并重，可能减少模型运维中断和多租户风险。反例是常驻权重增加显存占用，CRIU 范围仅实验性 TP=1，不代表分布式生产恢复成熟。观察冷启动时间、资源占用、缓存正确性和升级失败率；未开展跑分，不宣称性能增幅。

**来源与核验范围：**
- [vLLM Releases · v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0)；发布时间：2026-10-05T06:44:55+00:00；定位：Highlights；preload / CRIU；prefix cache LoRA/cache_salt；Breaking Changes；GitHub Releases API日期字段。；阅读范围：full-text；ID：`9668af85ed2e1acf35b7`。

### PyTorch 总结硬件接入体系：跨仓 CI 与参考后端降低集成摩擦

- PyTorch 10月5日文章总结工作组在2026年上半年的硬件接入进展：跨仓库 CI、设备无关测试迁移，以及 PrivateUse1/OpenReg 和 OCCL 参考实现。
- OpenReg 是最小 CPU 参考后端，OCCL 为分布式后端接入参考；这是一篇阶段综述，不将所述能力全部当作10月5日首次上线，也不将接入示例当作生产性能证明。
- 全文文字已读；没有运行参考实现或核对每个外链PR，未进行后端性能测量。

**产业判断：** 判断（derived）：框架与芯片后端的联合 CI 和稳定接入契约可以降低新硬件的维护成本，有利于下游推理框架和硬件供应商。反例是接口可接入仍无法保证算子覆盖、编译和分布式效率。观察新增后端的 CI 覆盖、修复周期和端到端软件可用性，不能从参考实现推断与 CUDA 性能等价。

**来源与核验范围：**
- [PyTorch Foundation Blog · PyTorch Hardware Enablement: Updates from the Accelerator Integration Working Group](https://pytorch.org/blog/pytorch-hardware-enablement-updates-from-the-acceleration-integration-working-group/)；发布时间：2026-10-05T13:12:59+00:00；定位：Cross-Repository CI；Device-Agnostic Testing；PrivateUse1/OpenReg；OCCL及结尾路线。；阅读范围：full-text；ID：`537645ae693322a4a431`。

### PyTorch 说明媒体处理分工：TorchCodec 集中 I/O，Vision/Audio 聚焦变换

- PyTorch 文章回顾过去两年的媒体处理调整：TorchCodec 承接图像、音频与视频 I/O；TorchVision/TorchAudio 聚焦各自变换，旧 I/O API 逐步弃用，部分音频接口按反馈保留。
- 这是10月5日发表的架构说明，不是全部 API 当日新发布。相对库内模型推理研究，新增的是多模态数据管线维护和包兼容性的工程脉络。
- 网页正文已读；旧API文档、版本矩阵与实际迁移未逐项验证。

**产业判断：** 判断（derived）：统一媒体 I/O 有助于集中二进制依赖、解码和硬件支持维护，可能降低多模态应用集成成本。反例是旧项目迁移和版本组合带来额外成本，稳定 ABI 主张不保证所有场景立即兼容。观察生态迁移、依赖冲突及真实输入管线瓶颈；未按同负载测量，不宣称吞吐增幅。

**来源与核验范围：**
- [PyTorch Foundation Blog · Evolution of the PyTorch Media Processing Landscape](https://pytorch.org/blog/evolution-of-the-pytorch-media-processing-landscape/)；发布时间：2026-10-05T20:45:50+00:00；定位：Main media-processing分工；TorchCodec；API保留与弃用；ABI与独立发布安排。；阅读范围：full-text；ID：`7c477c1278221668b434`。

## 5. 模型与AI Infra论文

### JIL：输出长度预测可能成为请求调度的攻击面

- arXiv v1 于10月2日15:12:43 UTC 提交，出现在10月5日 cs.AI 近期公告组；本条按公告日纳入，具体公告时刻未知，窗口边界不确定，前一期无同事件。
- 摘要提出对抗后缀使 TRAIL 的长度探针低估请求，从而取得排队优先级；作者称在两数据集、四模型下测试，并讨论粗分档防御与回答质量权衡。仅摘要阅读，不采用加速数字。
- 只读摘要、提交历史和公告列表；未读24页全文、六幅图或实验配置，作者结果 reported，未复现。

**产业判断：** 判断（derived）：服务调度如果把可被提示词影响的预测信号用于资源分配，就需要同时考虑吞吐与公平性，多租户服务可能受影响。反例是其他调度器、预测模型和防御配置未必存在相同效果。后续阅读具体模型/硬件/负载/harness，并验证分档的效率代价；不能推断所有 vLLM 或生产服务存在漏洞。

**来源与核验范围：**
- [arXiv model and infra papers · Jumping the Line: Exploiting Length Predictions in LLM Scheduling](https://arxiv.org/abs/2610.03430)；源站公告日期：2026-10-05（仅日期；时区与时刻未知）；定位：arXiv:2610.03430v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第17条。；阅读范围：abstract；ID：`3f62bd6aacfa7e7c8b5f`。
  日期仅精确到天，无法确认 18:00 边界。

### 任务与 harness 共同演进：推理数据合成的自我改进研究

- arXiv v1 于10月2日16:30:15 UTC 提交，出现在10月5日 cs.AI 公告组；按公告日纳入，具体时刻未知，边界不确定，与前期去重无同事件。
- 摘要提出任务与构造 harness 共同演进：在线从解题失败提炼技能，批次后更新技能、提示与工作流；模型权重和验证标准固定，以有效任务难度提升及有限成本增长筛选修订。
- 只读摘要、提交历史和公告列表；模型版本、APEX版本、mean-16预算与全文实验未核实，不采用成绩排名。

**产业判断：** 判断（derived）：推理数据价值可能来自可改进的生成流程，而不仅是模型规模，数据供应商和训练团队有机会积累工作流资产。反例是难度增长可能只是针对固定求解器，训练收益未必跨基准迁移。观察验证防泄漏、迭代预算、独立测试集和下游迁移效果；摘要成绩缺完整harness，故不作模型排名，也不与既有 RRSI 混为同一论文。

**来源与核验范围：**
- [arXiv model and infra papers · Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis](https://arxiv.org/abs/2610.03548)；源站公告日期：2026-10-05（仅日期；时区与时刻未知）；定位：arXiv:2610.03548v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第12条。；阅读范围：abstract；ID：`723bcd73ff7c849de2f7`。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

本期未收录经核验的新事件；覆盖情况见文末。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 174 条（其中线索 18 条），精选 10 个事件；未注明日期 1 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- OpenAI News：checked；已读两篇本期官网正文：图像广告及文本溯源；HTTP抓取失败后通过网页工具取得正文并归档。帮助中心最新可见10月2日，未见本期release notes。仅覆盖公开渠道。；已知截断 0 条。
- OpenAI API Changelog：checked；采集并读10月5日差异：部分组织管理员可在设置接受标准BAA/启用HIPAA支持。只作为低优先级候选，未推断法律合规或所有账号可用。；已知截断 0 条。
- Anthropic Newsroom：checked；读取官方Newsroom近期日期列表，最新可见10月2日培训公告；本期未核实新的可精选事件。；已知截断 0 条。
- Anthropic Research：checked；机器检查公开Research页面，结合官网入口筛选，未核实本窗口新研究；未逐篇重读既有文章。；已知截断 0 条。
- Anthropic 站点地图：checked；官方站点地图采集成功，新链接仅为发现线索，未逐项读取所有外链。；已知截断 0 条。
- DeepSeek Research & News：checked；采集SSL失败后网页工具成功读取同一官方News页面；未核实本窗口新公告，故障与补查分开保留。；已知截断 0 条。
- DeepSeek API Change Log：checked；采集SSL失败后网页工具读取官方更新页，最新可见9月10日V4.1 Flash；未见本窗口条目。；已知截断 0 条。
- DeepSeek 模型与价格：checked；机器快照价格页无变化；没有定位到本期的新调价证据，未覆盖私域通知或实际账单。；已知截断 0 条。
- DeepSeek · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Alibaba / Qwen Blog：failed；网页工具与真实浏览器实际加载博客，仅得到导航和页脚；没有可读日期列表。官方HF及中英文域名补检索已查，不能据此断言千问无变化。；已知截断 0 条。
- Qwen · Hugging Face：checked；官方HF近期列表扫描未形成本期合格发布证据；仓库元数据发现不等于正式模型发布。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；读取Kimi官方博客，最新可见K3/PerceptionBench为7月16日；公开列表未见本窗口新文，私域/灰度覆盖不足。；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；官方HF公开列表已扫描，未核实本期可精选正式发布。；已知截断 0 条。
- Z.ai 发布记录：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 智谱开放平台发布记录：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 智谱 · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- MiniMax News：checked；真实浏览器读取官方News完整可见列表，最新可见8月26日财务披露和8月3日H3；未见本窗口条目。；已知截断 0 条。
- MiniMax · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Mistral AI：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Meta Newsroom：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- AI at Meta Blog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Google DeepMind：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Google AI Blog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Google Cloud Blog：checked；Modernize官方正文已读并归档，明确Quick Estimator GA与EKS→GKE Public Preview；客户节省数字未当独立测量。；已知截断 0 条。
- Tencent Newsroom：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Tencent · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- ByteDance Seed Blog：checked；旧/en/blog返回404；从官网导航进入/en/research读取Research/Blog列表，最新可见8月5日博客，未见本期条目。来源配置和跟踪入口已修复。；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Alibaba Cloud Press Room：checked；网页工具未给出完整列表后真实浏览器读Press Room，最新可见9月23日、9月22日；未见本期合格条目。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- xAI News：checked；网页工具读官方News，最新可见9月28日Team Bots；未见本窗口条目。；已知截断 0 条。
- NVIDIA Newsroom：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- NVIDIA Blog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- AMD Press Releases：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- About Amazon：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Qualcomm Newsroom：checked；读取官方新闻入口，10月5日华为许可公告未列入AI日报，尚无明确AI能力/部署成本增量证据；没有逐篇读所有地区新闻。；已知截断 0 条。
- Samsung Newsroom：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- SK hynix Newsroom：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- ASML News：checked；同一官方入口跳转投资者新闻，实际读取日期列表，最新可见9月8日公告，无本窗口条目。；已知截断 0 条。
- TSMC Newsroom：checked；实际读取官方Latest News日期列表，最新可见9月10日营收，无本窗口条目。；已知截断 0 条。
- Volantis（公司新闻稿）：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Reflection AI Blog：checked；已读官网Beam文本全文（搜索工具返回正文），有限预览与未来权重发布分开；未读完整技术报告或评测harness。；已知截断 0 条。
- Namespace Blog：checked；已读官网融资正文与主体页脚，核实4,200万美元B轮/累计6,500万美元及开发基础设施产品；没有推算ARR。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；SSL采集失败后读官方GitHub release列表；未核实本窗口新正式版本。浏览可见列表与Atom更新时间并非统一发布口径，未推导性能变化。；已知截断 0 条。
- SGLang Blog：checked；机器列表检查成功且页面未变；近期9月23日Unified Radix Cache不作为本期新闻。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；正式v0.31.0选题已读发布重点及API时间字段；确认10月5日published_at、prerelease=false，10月2日created_at不当作发布时间。未逐项读PR或跑分。；已知截断 0 条。
- vLLM Blog：checked；robots采集失败后通过网页工具读取官方博客，最近可见9月29日文章；本期未核实新文章，采集失败仍保留。；已知截断 0 条。
- NVIDIA Dynamo：checked；官方release Atom采集成功，未形成本窗口正式新版本证据；开发预览保持原身份，不将更新时间当首次发布。；已知截断 0 条。
- FlashInfer：checked；SSL采集失败后读官方release列表；本期没有核实新正式版本，rc保持预发布身份。列表可能为缓存，不据其推断全部发布完整性。；已知截断 0 条。
- Mooncake：checked；官方release Atom采集成功，本窗口没有日期合格候选；不据此声称社区无开发变化。；已知截断 0 条。
- NVIDIA Technical Blog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- PyTorch Foundation Blog：checked；本期两篇正文已完整阅读，分别为硬件接入阶段综述和媒体架构分工；没有把历史进展当作当日全新能力。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；机器RSS robots失败；网页补查cs.AI/cs.LG/cs.DC近期列表与两篇v1摘要/历史。cs.AI只筛本日266条中的首50条；两篇按10月5日公告日而非10月2日提交日纳入，具体时刻未知。全文、其余分页/学科未完成。；已知截断 0 条。
- METR：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- UK AI Security Institute Blog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Artificial Analysis Articles：failed；SSL采集失败后网页工具仅得到简短页面壳，没有足够带日期文章正文；未采用评测数值。；已知截断 0 条。
- Artificial Analysis Changelog：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- SemiAnalysis：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- NIST News：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- US BIS News & Updates：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 工业和信息化部：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 最高人民法院：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 外交部例行记者会：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 中国政府网 政策：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 重庆市大数据应用发展管理局：failed；robots/采集失败后网页工具访问同一官方来源仍超时；不能写成无新闻。；已知截断 0 条。
- 国家数据局：failed；采集需浏览器；网页工具实际访问同一官网返回空正文，无法核查本期动态。；已知截断 0 条。

### 媒体直连 feed

- TechCrunch AI：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- The Decoder：checked；采集握手超时后网页工具读取主页并筛选已有feed候选，单篇阅读全文覆盖有限；没有采用其摘要冒充一手证据。；已知截断 0 条。
- The Verge AI：checked；本次feed恢复采集但历史gap与窗口重叠；Techmeme快照补查未取得可读内容，未弥补全部漏采。；已知截断 0 条；可能漏采 2026-10-05T03:11 至 2026-10-05T09:09。
- The Information：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Bloomberg Technology：failed；robots采集失败；网页工具得到数月前缓存页面，不能支持本期覆盖。付费全文未取得。；已知截断 0 条。
- Financial Times Technology：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Financial Times AI：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- New York Times Technology：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- SCMP Tech：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- MIT Technology Review：failed；机器超时后网页工具访问同一站点仍失败，已停止重试。；已知截断 0 条。
- Ars Technica AI：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- Tom's Hardware：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 量子位：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 虎嗅：failed；机器超时后网页工具访问同一来源仍失败；本期获取失败。；已知截断 0 条。
- IT之家：checked；本次feed恢复采集但历史gap与窗口重叠；不能把成功采集理解为完整覆盖。起止见research-audit.json。；已知截断 0 条；可能漏采 2026-10-02T03:11 至 2026-10-05T09:56。
- 36氪：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 钛媒体：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 雷峰网：checked；本次feed采集成功并初筛；网页全文补查超时，未逐篇读全文。；已知截断 0 条。
- 极客公园：checked；本次feed采集成功并初筛；网页全文补查超时，未逐篇读全文。；已知截断 0 条。
- 智东西：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- C114 通信网：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 快科技（驱动之家）：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。
- 机器之心：failed；网页工具读取首页只有PRO/介绍/导航，未取得可审阅的本期文章列表；公众号覆盖不足。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；机器采集近期公开条目并初筛标题/已有feed正文；未逐篇阅读全文，未核实可精选新事件。；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；执行10月4–5日路透域名AI/芯片/公司检索，未取得可精选的本期一手新证据，不代表路透无报道。。
- bloomberg-ai：checked；执行本期Bloomberg发现检索；付费全文及当前主页获取不足，未采用其融资摘要作为确认事实。。
- ft-nyt-wsj-ai：checked；执行本期FT/NYT/WSJ检索；NYT robots与付费正文限制，原始融资/供给细节未充分核实。。
- china-ai-companies-zh：checked；已执行中英文OpenAI/Anthropic/DeepSeek/Qwen/Kimi及中文新公司检索，结果含大量旧索引；私域、公众号与灰度渠道未完成。。
- china-ai-policy-zh：checked；按本期执行中国AI政策域名检索；国家数据局/重庆数据局部分入口失败，没有足够新原文支撑精选。。
- china-chips-zh：checked；执行本期GPU/HBM/产能中文检索；媒体供给数量与交易规模未回查到足够一手资料，未作为事实。。
- embodied-world-models-zh：checked；执行本期世界模型/具身融资检索；Reactor投资加入线索与旧轮次关系未核实，Mistlabs页面日期冲突，未采用。。
- supply-chain-en：checked；按本期执行HBM/CoWoS/GPU英文检索；Tencent/Oracle及Anthropic/Broadcom媒体线索原始合同/披露未取得，不列确证新闻。。
- newsroom-fallback：checked；实际打开xAI/高通/ASML/TSMC官方入口，并用真实浏览器补阿里云/MiniMax/Seed/Qwen；Qwen仍无可读日期列表。。

- 新公司发现：checked；执行中英文10月4–5日AI新公司/融资发现检索，Namespace和Reflection取得官网主体/产品与日期支持并加入跟踪。Reactor/聚合融资页只作为候选，不把媒体数量当独立证实。。

证据包：`data/packets/daily/2026/10/2026-10-05/c16ba4641e5e9e4f219d4fa61b5efde9a621b30486b9972d7fc3bd04858d1262.json`；采集 run：`20261006T010220-a72dfdef`。
