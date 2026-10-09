# AI 产业分析日报（2026.10.08）

统计窗口：2026-10-07T18:00:00-07:00 至 2026-10-08T18:00:00-07:00（洛杉矶时间，右端不含）。

本期收录15个事件。企业Agent开始把云端持续执行、身份权限与任务预算放到同一产品；服务端则按会话管理缓存。GPT-6.1 Sol新增Ultrafast，低延迟伴随显著价格溢价。科研资源承诺与台积电月度营收提供商业观察点，但不能直接推导已兑现算力或AI产能。公司、维护者与作者陈述标reported，产业判断为derived；source-checked只表示有限来源支持关系已核对。日期仅到日的材料存在窗口边界不确定，并已对照前期去重。

## 1. MaaS市场与产品形态

### Google 发布 Gemini 工作 Agent：云端持续执行、任务身份与项目预算结合

- Google 10月8日宣布通用工作 Agent：云端持续运行、跨设备共享上下文，可在 Workspace、Microsoft 365、Slack 等入口使用；临时子 Agent 使用任务身份，协作同事保留各自权限。
- 相对已有 Modernize 云迁移产品组合，本期增量是统一工作入口、Smart Routing、实时项目支出上限及 token/沙箱成本管理；文中称今天可编排 Gemini 与 Claude，其他模型是后续计划。
- 金融服务与法律行业版本为预览，政府、医疗和零售版本尚待推出。未核实全部功能的价格、地区、账户启用与 GA 矩阵。

**产业判断：** 持续任务把成本从单次回答扩展到跨日执行，身份和项目暂停机制可能降低企业采用门槛，云平台和工作流集成商受益。权限配置失误、跨平台能力不齐或预算耗尽会中断任务；观察真实完成率、恢复行为与每项任务账单。

**来源与核验范围：**
- [Google Cloud Blog · Google 发布 Gemini 工作 Agent：云端持续执行、任务身份与项目预算结合](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026/)；发布时间：2026-10-08T12:00:00+00:00；定位：官网完整正文；Gemini agent、multi-agent、security、cost controls、industry specialization段；未实测账户、计费或行业预览。；阅读范围：full-text；ID：`d23b22ea893414096a19`。

### LegalOn 案例把模型分工与预算管理同时纳入编码 Agent 采用

- OpenAI 10月8日客户案例称 LegalOn 相对此前 GPT-5.5 Fast 使用方式，将预计每日费用降低65%，开发速度保持；这是客户披露，非独立对照实验或已审计实际账单。
- Luna 承担明确需求实现，Sol 6.1 处理常规设计分析，Astra 处理复杂架构判断；同时限制默认 Fast 使用并设置部门/个人月额度。
- 相对昨天小模型与缓存报价变化，本期新增组织层面的模型分工和预算治理。按功能发布衡量 ROI 的流程还在建设中，不能视作已验证财务回报。

**产业判断：** 任务分工和额度控制有机会减少高价模型的过度使用，企业开发治理工具受益。任务难度分流失误、反复升级或返工会抵消节省；观察同范围交付质量、实际账单和功能发布收益，而非仅比较 token 价格。

**来源与核验范围：**
- [OpenAI News · LegalOn 案例把模型分工与预算管理同时纳入编码 Agent 采用](https://openai.com/index/legalon-halves-codex-costs/)；发布时间：2026-10-08T00:00:00+08:00；定位：OpenAI案例正文模型选择、预算治理、estimated daily costs和ROI建设段；HTTP403，使用浏览工具已读段落摘录；未访问客户账单。；阅读范围：full-text；ID：`f3f22c1798a43bc2d07f`。
  日期仅精确到天，无法确认 18:00 边界。

### Codex 桌面端开始推送更快的任务中途引导

- 10月8日帮助中心宣布，在 ChatGPT 桌面应用中推送更快的 Codex steering；用户可在任务进行中纠正方法、补充信息或调整方向。
- 增量是跟进指令更早作用于运行任务；可选择跟进消息引导当前执行还是等待下一次。没有公开延迟数字、完整地区/套餐矩阵或独立实测。

**产业判断：** 中途纠偏可能减少无效执行和返工，提升人协作式编码 Agent 的可控性。频繁改动也可能破坏任务上下文；观察指令生效时延、取消后的剩余计算和回归率。

**来源与核验范围：**
- [OpenAI News · Codex 桌面端开始推送更快的任务中途引导](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；发布时间：2026-10-08T00:00:00+08:00；定位：帮助中心2026-10-08 Faster steering in Codex小节；只核对宣布与推送状态，未实测客户端。；阅读范围：full-text；ID：`3930e8dede7666d8dfd2`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Anthropic 公布使用政策修订，11月12日才生效

- 10月8日公布的政策修订于2026年11月12日生效，不能写成今日已经实施。
- 新增可造成身体伤害的自主硬件要求：合格操作员可观察和停止行为，断连时进入安全状态；对选举、欺骗、支持地区等条款作澄清。
- 医疗、法律和金融领域的合格人员介入与披露义务仍保留。相对昨天模型价格与供给，本期增量是部署及组织访问约束；未逐项解释法律适用。

**产业判断：** 具身系统和高风险垂直应用需要把操作员介入、断连行为纳入产品设计，相关治理工具可能受益。形式上的停止按钮不能证明安全；观察实际停机路径、客户迁移条款与访问限制执行。

**来源与核验范围：**
- [Anthropic Newsroom · Anthropic 公布使用政策修订，11月12日才生效](https://www.anthropic.com/news/2026-usage-policy-update)；发布时间：2026-10-08T00:00:00+08:00；定位：官方2026 usage policy update完整正文；effective date及hardware、supported regions、high-stakes段。未对未来生效政策进行法律意见或生产审计。；阅读范围：full-text；ID：`4e66a7e453a3193bb5cb`。
  日期仅精确到天，无法确认 18:00 边界。

### Anthropic 扩展关键基础设施防御，并推出自愿加入的开源扫描服务

- Cyber Mission 公告将关键基础设施防御项目 CIDP 面向电力、水务、交通等 OT 系统，通过11家合作伙伴结合 Claude、现场工程与威胁研究。
- 免费 OSS Scanner 接受项目主动加入，定期生成模型扫描报告，在可用时附解释、PoC 和修复建议；这些报告没有逐条人工审核，不能等同于原有人工核实披露流程。
- 相对前期 CVP/Glasswing 的访问分层，本期新增行业交付伙伴与两种漏洞报告流程。厂商预期的高真阳性率未当作测得结果，也未核实实际防御效果。

**产业判断：** 模型能力经行业伙伴落地后可能扩大安全服务市场，维护者也可能承受更高的分诊负担。误报、缺少修复资源或 OT 无法停机是反例；观察人工确认比例、修复周期和运行干扰。

**来源与核验范围：**
- [Anthropic Newsroom · Anthropic 扩展关键基础设施防御，并推出自愿加入的开源扫描服务](https://www.anthropic.com/news/anthropic-cyber-mission)；发布时间：2026-10-08T00:00:00+08:00；定位：Anthropic Cyber Mission完整正文；CIDP、伙伴名单、OSS Scanner与人工CVD边界；未读全部关联研究或验证漏洞。；阅读范围：full-text；ID：`c4a1f46e5a98744a7c57`。
  日期仅精确到天，无法确认 18:00 边界。

### 新增公司 TODAY：为金融保险顾问工作流融资 EUR 280万

- TODAY/UseToday ApS 官方披露已完成EUR2.8M种子轮，由 HTGF 与 Insurtech Gateway 共同领投；这是融资额，未披露估值、ARR或期间营收。
- 官网核实公司2024年成立，位于哥本哈根和柏林；Michael Gackstatter任CEO、Artem Demchenkov任CTO。产品覆盖会议转录、后台事务、销售辅导及来电接听，目标为金融保险顾问。
- 这是本次开放发现新增跟踪对象；公司声称DACH地区超过3500名顾问使用，未核实付费口径、留存或效果，不采用营销收益倍数。日期仅到日，窗口边界不确定，前一期未收录。

**产业判断：** 顾问工作前后流程比通用聊天更容易形成垂直分发入口，保险经纪与后台集成商可能受益。录音权限、责任边界和客户付费意愿会制约扩张；观察付费顾问数、机构续约、人工复核和真实合规工作量。

**来源与核验范围：**
- [TODAY Official Blog · 新增公司 TODAY：为金融保险顾问工作流融资 EUR 280万](https://www.usetoday.io/blog/today-secures-2-8m-seed-funding/)；发布时间：2026-10-08T00:00:00+08:00；定位：TODAY官方融资新闻稿全文已读；归档保留融资、身份和产品相关段落摘录。公司自报客户数未独立核验，未阅读全部安全文档。；阅读范围：full-text；ID：`93ab3995ae9af1bf246c`。
  日期仅精确到天，无法确认 18:00 边界。

### Anthropic 承诺三年提供 USD 1.5亿科研资源

- Anthropic 宣布未来三年提供价值USD150M的 Claude、Claude Code 和 API credits，并配套培训与技术支持，面向美国联邦科研项目。
- 公告称覆盖超过15个机构的数百项目；这是未来资源承诺，不是当期现金拨款、已确认收入或已经消耗的算力。
- 相对既有 DOE/Genesis 合作，本期增量为承诺规模与项目接入安排，未核实各项目执行、兑现进度或研究产出。

**产业判断：** 资源与人员支持可降低科研团队接入 Agent 的启动成本，同时可能培育供应商依赖。额度无法覆盖数据治理或科学验证时，采用不会自动转化为成果；观察兑付、可持续预算与可复现科学产出。

**来源与核验范围：**
- [Anthropic Newsroom · Anthropic 承诺三年提供 USD 1.5亿科研资源](https://www.anthropic.com/news/genesis-mission-commitment)；发布时间：2026-10-08T00:00:00+08:00；定位：Genesis mission commitment官方正文；资源种类、三年金额、机构/项目范围，未核实独立预算或已兑付金额。；阅读范围：full-text；ID：`6c062b861d6d205bc313`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### GPT-6.1 Sol 新增 Ultrafast：以更高单价购买低延迟服务

- 10月8日 API Changelog 宣布 Responses API 的 GPT-6.1 Sol 新增 Ultrafast，面向所有API用户但受独立限额约束，支持全球处理以及美国、欧盟数据驻留。新增的是服务档位，不是新模型权重或能力评测。
- 生成时读取的[官方价格表](https://developers.openai.com/api/docs/pricing)USD/百万token：短上下文输入12、缓存读0.60、缓存写15、输出60；对应Standard为2、0.10、2.50、10。长上下文Ultrafast为24、1.20、30、90。区域处理另有10%附加。
- 相对昨日小模型与缓存降价，本期增量是更昂贵的低延迟选项。未测试首token/端到端时延或网络开销，不采用速度倍数。公告仅到日、边界不确定，前期未收录。

**产业判断：** 多工具轮次中的等待可能放大交互时延，因此部分高价值实时任务有支付溢价的动力。工具、网络或人工等待占主导时，计算提速价值有限；观察每项成功任务的总成本、尾时延和限流情况。

**来源与核验范围：**
- [OpenAI API Changelog · GPT-6.1 Sol 新增 Ultrafast：以更高单价购买低延迟服务](https://developers.openai.com/api/docs/changelog)；发布时间：2026-10-08T00:00:00+08:00；定位：HTTP Changelog Oct8小节及官方pricing Standard/Ultrafast表；另已读Ultrafast指南Availability/连接开销。浏览搜索缓存的Changelog未显示该项，采用实际HTTP版本并记录差异；未调用API。；阅读范围：full-text；ID：`49e8d0577a5e1f9d20fd`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### Dynamo 按 Agent 会话管理缓存和准入，部分接口仍是提案

- PyTorch技术文章描述稳定session_id/parent_session_id识别完整Agent轨迹，复用Claude Code、Codex、OpenCode等harness头部，并连接追踪、回放与缓存调度。
- ThunderAgent按会话工作集在工具边界施加背压，避免请求级负载均衡导致KV反复淘汰。相对昨天Dynamo稳定补丁，增量是会话层调度设计。
- shared-pool indexer被明确标为实验性；KvHint的Share/Prefetch/Demote为拟议接口，部分实现尚待合入。未据博客断言全部功能已在稳定版生产可用，也不采用配置不完整的吞吐百分比。

**产业判断：** 长时Agent的效率取决于整段上下文的存活，会话准入可使缓存容量与并发协调，路由和外部KV存储环节可能受益。长会话占用资源或暂停不公平是反例；观察重prefill次数、KV占用、任务完成率和尾时延。

**来源与核验范围：**
- [PyTorch Foundation Blog · Dynamo 按 Agent 会话管理缓存和准入，部分接口仍是提案](https://pytorch.org/blog/session-aware-agentic-inference-with-nvidia-dynamo/)；发布时间：2026-10-08T18:13:46+00:00；定位：技术文章完整正文；session headers、program-aware scheduling、experimental shared-pool和proposed KvHint段；未逐项读PR、运行harness或独立复现。；阅读范围：full-text；ID：`ad8a8b340dbbd2077651`。

### IBM 说明 Spyre 原生 PyTorch 设备集成及其运行时边界

- 文章说明torch-spyre经PrivateUse1建立设备身份、allocator张量驻留、流语义和Inductor编译路径，将Spyre接入PyTorch；这是工程说明，不是新硬件发布。
- 运行时支持传输与计算重叠，但不能据此认为任意计算流并发；compile-backed eager有首次编译开销，不支持的操作可能回退或失败。
- 相对已有GPU框架供给，本期增量是非CUDA设备沿用PyTorch抽象的方式。用户可直接调用的events仍是计划，内部运行时events已使用；实验精度/完整软件版本未核对，不采用速度倍数。

**产业判断：** 原生设备语义可减少迁移应用代码的成本，替代加速器生态可能受益。算子覆盖、编译首次开销和回退比例会限制实际效率；观察应用移植成功率、长尾算子和端到端成本。

**来源与核验范围：**
- [PyTorch Foundation Blog · IBM 说明 Spyre 原生 PyTorch 设备集成及其运行时边界](https://pytorch.org/blog/building-spyre-as-a-native-pytorch-device/)；发布时间：2026-10-08T12:45:49+00:00；定位：官网完整正文；PrivateUse1、allocator、streams/events、compile-backed eager及limitations；未审阅代码/PR或执行移植。；阅读范围：full-text；ID：`b1835280789af2a0e7a3`。

### Dynamo 发布 Kimi-K3 实验快照，明确不适合生产

- v1.5.0-kimi-k3-post.1标为非QA-gated实验快照；底层镜像为Dynamo1.5.1、SGLang0.5.18、CUDA13、Python3.12，不能混作1.5稳定新增能力。
- 官方提供GB300上的聚合与1P1D分离配方：均16张GB300，聚合两worker采用DCP8/TP8，分离配合Mooncake NVLink传KV；模型experts为MXFP4、KV为FP8。
- 相对昨日Dynamo1.5.1补丁，这是新模型部署实验包；未新增Kimi模型发布事件。公布吞吐用了合成接受长度4.05，不是真实DSpark验证；另有长prefill健康检查、logprobs/stop_token_ids和JSON解码限制，不采用性能排名。

**产业判断：** 模型部署生态开始提供明确的缓存、精度和拆分配方，可缩短评估准备时间，GB300与KV传输生态受益。但生产稳定性及真实投机接受率尚是约束；观察真实任务吞吐、错误率、重启和H200等硬件覆盖。

**来源与核验范围：**
- [NVIDIA Dynamo · Dynamo 发布 Kimi-K3 实验快照，明确不适合生产](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0-kimi-k3-post.1)；更新时间：2026-10-08T20:14:58+00:00；定位：GitHub发布正文完整阅读；experimental、versions、recipes、precision及known limitations，tag a0dcfbf6d3aa788e8dba806189f1611d9293a52f；未跑benchmark或读全部PR。；阅读范围：full-text；ID：`76f09c0a1e436734492b`。

## 5. 模型与AI Infra论文

### vLLM-Omni 技术报告：把多模态生成组织为多阶段运行时

- 2610.09307v1摘要提出统一orchestrator、可横向复制的stage engines、连接器和会话控制，覆盖文本、音频、视频等跨阶段生成；这是技术报告，不等于今日新稳定版本。
- v1提交于10月7日02:04:28Z；官方cs.DC在10月8日公告，按公告日纳入，边界不确定，前一期未收录。相对vLLM0.31请求服务变化，增量是多模态阶段和会话组织。
- 仅阅读摘要、提交历史及官方公告列表，未完整阅读34页实验/附录、评测harness或代码，故不采用性能优势数字。

**产业判断：** 音视频生成阶段具有不同资源需求，统一编排可能减少阶段间集成成本，多模态服务平台受益。阶段间搬运与同步也会增加时延；观察流式响应、异构阶段资源占用和相同工作负载下的可靠性。

**来源与核验范围：**
- [arXiv model and infra papers · vLLM-Omni 技术报告：把多模态生成组织为多阶段运行时](https://arxiv.org/abs/2610.09307)；源站公告时间：2026-10-08T00:00:00+08:00；定位：arXiv2610.09307v1摘要及submission history；官方RSS和cs.DC Thu8Oct列表第10条。只读摘要/历史/列表，未读全文实验或复现。；阅读范围：abstract；ID：`e5d4288115ce109a9b27`。
  日期仅精确到天，无法确认 18:00 边界。

### CoMoE：为缺少 GPU P2P 的普通多卡系统设计 MoE 数据路径

- 2610.09424v1摘要提出host-centric token路由、host-backed multicast与细粒度聚合buffer，减少全局同步，面向没有GPU P2P的普通PCIe多卡系统。
- v1提交于10月7日04:24:45Z；官方cs.DC在10月8日公告，按公告日纳入，边界不确定，前一期未收录。新增的是对低成本互连条件的推理系统设计，不是模型质量改进。
- 仅阅读摘要、提交历史和公告列表。作者报告RTX5090/A800结果，但卡数、精度、模型、并发、软件版本与成本价格点尚未审阅，不采用其速度/成本倍数或跨硬件排名。

**产业判断：** 以主机协调通信可能扩大消费卡运行MoE的部署空间，低预算推理服务商受益。PCIe带宽、主机内存和路由不均衡可能成为瓶颈；观察完整任务时延、主机资源成本及与成熟基线的同口径比较。

**来源与核验范围：**
- [arXiv model and infra papers · CoMoE：为缺少 GPU P2P 的普通多卡系统设计 MoE 数据路径](https://arxiv.org/abs/2610.09424)；源站公告时间：2026-10-08T00:00:00+08:00；定位：arXiv2610.09424v1摘要及submission history；官方RSS和cs.DC Thu8Oct列表第9条。未读完整方法/实验/代码或复现。；阅读范围：abstract；ID：`a2eec7563900758af19e`。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

### NVIDIA 承诺五年投入价值 USD 10亿的美国科研支持

- NVIDIA 公告未来五年提供价值USD1B承诺，覆盖高等院校科研、量子领域与支撑政府任务的云服务商，并参与Genesis第二阶段项目。
- 相对既有国家实验室合作，本期增量是新的金额和五年资源安排；这是未来承诺，不是当期现金支出、GPU订单或已经交付的系统，不能与Anthropic三年额度直接相加比较供给。

**产业判断：** 科研支持可培育长期算力与软件生态需求，学术机构和合作云可能受益。承诺兑现、采购渠道与具体配额尚不明，不能推导短期GPU紧缺缓解；观察项目资金结构、实际交付和开放资源条件。

**来源与核验范围：**
- [NVIDIA Newsroom · NVIDIA 承诺五年投入价值 USD 10亿的美国科研支持](https://nvidianews.nvidia.com/news/nvidia-commits-1-billion-to-advance-us-science-over-the-next-five-years)；发布时间：2026-10-08T14:31:00+00:00；定位：NVIDIA新闻稿正文和前瞻声明；five-year commitment/fields/phase2，不核实项目交付或已支付款。；阅读范围：full-text；ID：`867a207ed4448ee0482b`。

### 台积电9月合并营收同比增54.6%，不能直接推导 AI 产能

- 台积电10月8日披露2026年9月合并净营收约NTD511.86B，环比下降0.6%、同比增长54.6%；1—9月NTD3898.73B，同比增长41.1%。币种为新台币，期间不同须分列。
- 本期新增已披露月度营收，不是融资/ARR。数据覆盖公司整体，未拆分AI收入、GPU出货或CoWoS产能，亦不提供客户交付时点。日期仅到日、边界不确定，前一期未收录。

**产业判断：** 合并营收是制造需求的观察点，可帮助跟踪供应链商业规模；产品组合、价格与季节变化也可能解释增长。AI供给判断仍需封装产能、利用率和交付数据，不能以总营收替代。

**来源与核验范围：**
- [TSMC Newsroom · 台积电9月合并营收同比增54.6%，不能直接推导 AI 产能](https://pr.tsmc.com/english/news/3343)；发布时间：2026-10-08T00:00:00+08:00；定位：台积电官方新闻稿Issued on和合并净营收正文；网页表格图片未读取，采用正文数字；未核实分部或客户订单。；阅读范围：full-text；ID：`2e461f2ac6e5c44a50c2`。
  日期仅精确到天，无法确认 18:00 边界。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 325 条（其中线索 23 条），精选 15 个事件；未注明日期 1 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Nous Research Official：checked；已读官网日期列表：10月8日Microsoft Store/ASUS分发线索，未读商店条款或实测，留待核实；昨日融资重复排除。；已知截断 0 条。
- Healthleap Official：checked；已读官网产品页，未发现可核实本期事件；昨日融资重复排除；未覆盖全部临床证据。；已知截断 0 条。
- OpenAI News：checked；已读News列表、LegalOn案例、帮助中心10月8日steering；False fronts安全研究只发现标题，正文未读不收录；前期Intelligent UI分发计划未实测，重复排除。；已知截断 0 条。
- OpenAI API Changelog：checked；已读实际HTTP Changelog Oct8、Standard/Ultrafast价格表及官方指南；网络搜索缓存版本未显示Oct8项，保留实际版本。API变更非独立性能测试。；已知截断 0 条。
- Anthropic Newsroom：checked；已读官方News列表及三篇本期公告全文；条款11月12日生效，资源承诺未当作已兑付。；已知截断 0 条。
- Anthropic Research：checked；研究列表采集成功；opt-in漏洞服务关联研究和missing-map-of-sky未完整读取，仅以已读Cyber Mission支持有限结论。；已知截断 0 条。
- Anthropic 站点地图：ok；页面链接 527 个，最近一次新增 5 个；检查于 10-09 09:00；已知截断 0 条。
- DeepSeek Research & News：checked；已读官网News且采集API变更/价格/HF近期列表；列表最新9月10日V4.1，未见本期正式模型公告；融资/IPO/私测报道未核实。；已知截断 0 条。
- DeepSeek API Change Log：ok；页面无变化；检查于 10-09 09:00；已知截断 0 条。
- DeepSeek 模型与价格：ok；页面无变化；检查于 10-09 09:00；已知截断 0 条。
- DeepSeek · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- Alibaba / Qwen Blog：failed；浏览器只返回导航，无法读取文章列表；HF近期50链接无新增仅为补充，官网获取不足不能说没有新闻。；已知截断 0 条。
- Qwen · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；已读官网Blog及HF近期列表，最新可见7月16日K3；未见本期正式模型发布，Dynamo快照另列工程事件。；已知截断 0 条。
- Moonshot AI · Hugging Face：ok；页面链接 19 个；检查于 10-09 09:00；已知截断 0 条。
- Z.ai 发布记录：ok；页面无变化；检查于 10-09 09:00；已知截断 0 条。
- 智谱开放平台发布记录：ok；页面无变化；检查于 10-09 09:00；已知截断 0 条。
- 智谱 · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- MiniMax News：checked；浏览器读取News列表，最新可见日期8月26日；未发现列表内本期合格公告，不覆盖所有产品/社交渠道。；已知截断 0 条。
- MiniMax · Hugging Face：ok；页面链接 21 个；检查于 10-09 09:00；已知截断 0 条。
- Mistral AI：ok；feed 89 条；检查于 10-09 09:00；已知截断 0 条。
- Meta Newsroom：ok；feed 10 条，关键词过滤 2 条；检查于 10-09 09:00；已知截断 0 条。
- AI at Meta Blog：ok；页面链接 10 个；检查于 10-09 09:00；已知截断 0 条。
- Google DeepMind：ok；feed 100 条；检查于 10-09 09:00；已知截断 0 条。
- Google AI Blog：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- Google Cloud Blog：ok；feed 20 条，关键词过滤 3 条；检查于 10-09 09:00；已知截断 0 条。
- Tencent Newsroom：ok；页面链接 21 个；检查于 10-09 09:00；已知截断 0 条。
- Tencent · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- ByteDance Seed Blog：checked；浏览器读取Research列表，最新可见8月5日，Publication可见7月6日；未见本期合格条目，不覆盖全部公众号。；已知截断 0 条。
- ByteDance Seed · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- Alibaba Cloud Press Room：checked；浏览器读取Press Room，最新可见9月23日；本期列表未见合格事件，Qwen仍归属阿里。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：ok；页面链接 31 个；检查于 10-09 09:00；已知截断 0 条。
- 京东 jdopensource · Hugging Face：ok；页面链接 23 个；检查于 10-09 09:00；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：ok；页面链接 30 个；检查于 10-09 09:00；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：ok；页面链接 50 个；检查于 10-09 09:00；已知截断 0 条。
- xAI News：checked；已读官网News，最新可见9月28日；未见列表内本期事件，不等于公司无新变化。；已知截断 0 条。
- NVIDIA Newsroom：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- NVIDIA Blog：ok；feed 18 条；检查于 10-09 09:00；已知截断 0 条。
- AMD Press Releases：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- About Amazon：ok；feed 10 条，关键词过滤 7 条；检查于 10-09 09:00；已知截断 0 条。
- Qualcomm Newsroom：checked；已读官方release列表，最新可见10月5日；本期未见合格条目。；已知截断 0 条。
- Samsung Newsroom：ok；feed 50 条，关键词过滤 18 条；检查于 10-09 09:00；已知截断 0 条。
- SK hynix Newsroom：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- ASML News：checked；官网跳转investor.asml.com可读，最新列表9月8日；上次获取失败已恢复，本期列表未见合格事件。；已知截断 0 条。
- TSMC Newsroom：checked；已读官方10月8日月度营收正文；图片表未读，未核实AI分部/产能。；已知截断 0 条。
- Volantis（公司新闻稿）：ok；页面链接 1 个；检查于 10-09 09:00；已知截断 0 条。
- Reflection AI Blog：checked；已读官方Blog列表，Beam为前期预览；未核实计划权重下载或许可，因此不把计划当已兑现。；已知截断 0 条。
- Namespace Blog：checked；已读官方Blog日期列表，10月5日融资重复，未发现本期合格条目。；已知截断 0 条。
- Vinci Official Blog：checked；已读官网Blog列表，最新10月6日融资重复排除，未独立验证物理仿真性能。；已知截断 0 条。
- TODAY Official Blog：checked；开放检索发现并完整阅读官方融资/身份新闻稿，长期跟踪新增，客户数和效果为自报。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方Releases可见稳定0.5.21为10月2日；列表检查与采集完成，未逐项阅读全部提交/博客。；已知截断 0 条。
- SGLang Blog：ok；页面链接 6 个；检查于 10-09 09:00；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；官方Releases稳定0.31为10月5日，前期已收录；本期未见新正式稳定版。；已知截断 0 条。
- vLLM Blog：checked；采集发现10月7日DeepSeek V4.1 Flash文章，正文未读且日期边界不确定，暂留候选。；已知截断 0 条。
- NVIDIA Dynamo：checked；已读Kimi-K3快照完整发布说明；其他DeepSeek/MiniMax实验构建仅检查列表未读全部正文，不当作稳定发布或模型首发。；已知截断 0 条。
- FlashInfer：checked；采集版本列表含0.7.2rc2，只是RC；未核实生产使用，不作为正式版收录。；已知截断 0 条。
- Mooncake：checked；官方仓库采集成功，近期列表未产生新发布候选；不声称审阅全部提交/议题。；已知截断 0 条。
- NVIDIA Technical Blog：ok；feed 100 条；检查于 10-09 09:00；已知截断 0 条。
- PyTorch Foundation Blog：checked；已读Spyre与Dynamo Session-Aware两篇正文；未运行代码或复现，实验/提案和当前实现分开。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；217候选，保存60且155条未归档；标题筛选后仅2篇阅读摘要/提交历史和公告列表，论文全文/实验未审阅。RSS公告占位午夜不当作精确时间。；已知截断 155 条。
- METR：ok；页面链接 26 个；检查于 10-09 09:00；已知截断 0 条。
- UK AI Security Institute Blog：ok；页面链接 99 个；检查于 10-09 09:00；已知截断 0 条。
- Artificial Analysis Articles：ok；页面链接 12 个，最近一次新增 3 个；检查于 10-09 09:00；已知截断 0 条。
- Artificial Analysis Changelog：ok；最近一次检测到页面变化；检查于 10-09 09:00；已知截断 0 条。
- SemiAnalysis：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。

### 政府、监管与司法

- CISA News：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- NIST News：ok；feed 40 条，关键词过滤 32 条；检查于 10-09 09:00；已知截断 0 条。
- US BIS News & Updates：ok；页面链接 31 个；检查于 10-09 09:00；已知截断 0 条。
- 工业和信息化部：ok；页面链接 21 个，最近一次新增 1 个；检查于 10-09 09:00；已知截断 0 条。
- 最高人民法院：ok；页面链接 82 个，最近一次新增 9 个；检查于 10-09 09:00；已知截断 0 条。
- 外交部例行记者会：ok；页面链接 35 个，最近一次新增 1 个；检查于 10-09 09:00；已知截断 0 条。
- 中国政府网 政策：ok；页面链接 14 个，最近一次新增 1 个；检查于 10-09 09:00；已知截断 0 条。
- 重庆市大数据应用发展管理局：ok；页面链接 17 个；检查于 10-09 09:00；已知截断 0 条。
- 国家数据局：failed；HTTP异常后浏览同一官网返回空正文，日期/事件无法核实。；已知截断 0 条。

### 媒体直连 feed

- TechCrunch AI：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- The Decoder：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- The Verge AI：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- The Information：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- Bloomberg Technology：ok；feed 20 条，关键词过滤 10 条；检查于 10-09 09:00；已知截断 0 条；可能漏采 2026-10-08T01:05 至 2026-10-08T10:20。
- Financial Times Technology：ok；feed 25 条，关键词过滤 12 条；检查于 10-09 09:00；已知截断 0 条。
- Financial Times AI：ok；feed 25 条；检查于 10-09 09:00；已知截断 0 条。
- New York Times Technology：ok；feed 20 条，关键词过滤 9 条；检查于 10-09 09:00；已知截断 0 条。
- SCMP Tech：ok；feed 50 条，关键词过滤 10 条；检查于 10-09 09:00；已知截断 0 条。
- MIT Technology Review：ok；feed 10 条，关键词过滤 2 条；检查于 10-09 09:00；已知截断 0 条。
- Ars Technica AI：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- Tom's Hardware：ok；feed 50 条，关键词过滤 29 条；检查于 10-09 09:00；已知截断 0 条。
- 量子位：ok；feed 10 条；检查于 10-09 09:00；已知截断 0 条。
- 虎嗅：failed；HTTP超时后浏览同一官网仍超时；未无限重试，不视作没有新闻。；已知截断 0 条。
- IT之家：ok；feed 60 条，关键词过滤 37 条；检查于 10-09 09:00；已知截断 0 条；可能漏采 2026-10-08T01:05 至 2026-10-08T13:43。
- 36氪：ok；feed 30 条，关键词过滤 17 条；检查于 10-09 09:00；已知截断 0 条。
- 钛媒体：ok；feed 18 条，关键词过滤 10 条；检查于 10-09 09:00；已知截断 0 条；可能漏采 2026-10-08T01:05 至 2026-10-08T19:36。
- 雷峰网：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条；可能漏采 2026-10-08T01:05 至 2026-10-08T10:46。
- 极客公园：failed；HTTP超时后浏览同一官网仍超时；未得到正文。；已知截断 0 条。
- 智东西：ok；feed 20 条；检查于 10-09 09:00；已知截断 0 条。
- C114 通信网：ok；页面链接 32 个，最近一次新增 17 个；检查于 10-09 09:00；已知截断 0 条。
- 快科技（驱动之家）：ok；feed 100 条，关键词过滤 64 条；检查于 10-09 09:00；已知截断 0 条；可能漏采 2026-10-08T01:05 至 2026-10-08T17:36。
- 机器之心：failed；浏览器首页为服务/Pro入口，无法得到当前完整日期新闻列表。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：ok；页面链接 107 个，最近一次新增 36 个；检查于 10-09 09:00；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；执行窗口限定检索，结果无可读且已核实的本期原发独家；检索不能证明完整覆盖。。
- bloomberg-ai：checked；执行窗口限定检索，未补齐Bloomberg订阅正文及漏采时段；保留覆盖缺口。。
- ft-nyt-wsj-ai：checked；执行窗口限定检索；NYT访问受限，FT/WSJ本期付费原文未完整读取。。
- china-ai-companies-zh：checked；执行中文公司变化检索，发现融资/IPO/Haiku转载等；融资缺已读一手，Haiku为前期重复。。
- china-ai-policy-zh：checked；执行中文政策检索，未发现可核实本期且已读的合格公告；国家数据局获取失败。。
- china-chips-zh：checked；执行中文供给检索；Biren拟配售仅媒体线索，未读港交所文件，保留候选不当作融资完成。。
- embodied-world-models-zh：checked；执行中文具身/世界模型检索，聚合线索未找到本期已读一手支持；未收录。。
- supply-chain-en：checked；执行HBM/CoWoS/export等英文检索；旧闻与无一手支持线索排除，未补齐全部价格/订单变化。。
- newsroom-fallback：checked；逐个补查xAI、Qwen、MiniMax、Alibaba Cloud、Seed、Qualcomm、ASML和TSMC；Qwen不足、ASML恢复、TSMC营收已读。。

- 新公司发现：checked；中英文开放检索已执行；TODAY官网核实后入库。Manus/Arena/Turba/Helm.ai/Upscale等缺已读一手或完整口径，留待核实，固定名单并非穷尽。。

证据包：`data/packets/daily/2026/10/2026-10-08/6eb2dfb2efb5a5d91074a0999d44fbf5f6f71f5c5fe29c462d64f7263bfd3d9b.json`；采集 run：`20261009T005952-3d3cdd9e`。
