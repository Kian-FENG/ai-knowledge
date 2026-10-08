# AI 产业分析日报（2026.10.07）

统计窗口：2026-10-06T18:00:00-07:00 至 2026-10-07T18:00:00-07:00（America/Los_Angeles，右端不含；本窗口24小时，按当地日历计算）。

实际生成时间：2026-10-07T18:18:05-07:00（America/Los_Angeles）；18:00为开始执行时间。

本期收录12个事件：ChatGPT把回答推进为可操作界面，Haiku5.5与缓存降价让Agent成本更细分，Nous与Healthleap分别扩展开放Agent和垂直流程供给。Dynamo补丁、上下文折叠及GPU共享研究指向服务可靠性和资源利用，RTX Spark公布本地Windows硬件交付路线。厂商/作者结果保留归因；中国重点对象已检查但官方正文、媒体漏采和论文上限仍限制覆盖，不能把未收录解释为没有新动态。

## 1. MaaS市场与产品形态

### ChatGPT 开始推送 Intelligent UI：回答可直接变成交互工具

- OpenAI 于10月7日开始全球向 Plus、Pro、Business、Enterprise 的 Chat 推送 GPT-6 与 Intelligent UI，回答可组合图表、控件和小工具，并在继续思考或调用工具时先输出部分答案。Free、Go 扩展计划从10月8日开始；Enterprise 受管理员设置约束。
- 付费 Chat 使用 GPT-6 Sol，Free/Go 使用 Luna；帮助中心明确 Instant 至 Extra High 支持，Pro 推理仍用 Astra 且不支持 Intelligent UI。本次不改变 Work、Codex 的模型。增量是交互呈现与交付方式，不能推导基础模型统一升级。
- 公告日期仅到日、源站时区未知，窗口边界不确定；已对照前一期。没有独立测试界面可靠性、实际覆盖率或厂商时延主张。

**产业判断：** 交互控件可减少用户把文本答案转成表格、计算器或决策步骤的成本，助手分发和插件生态可能受益。生成控件若状态错误或无法接续任务，体验优势会减弱；观察操作完成率、误操作、可访问性和插件触达。

**来源与核验范围：**
- [OpenAI News · GPT-6 与 Intelligent UI](https://openai.com/index/gpt-6-for-everyone/)；发布时间：2026-10-07（仅日期，源站时区未知）；补充来源：[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；定位：公告主文 Intelligent UI / rollout；帮助中心 October 7 可用档位与 Pro 例外；已读公告正文及 release notes 顶部，未实际试用。；阅读范围：full-text；ID：`d66b18709c4ba948d6fa`。
  日期仅精确到天，无法确认 18:00 边界。

### OpenAI 宣布 College Planner，首批面向美国10–12年级学生

- 10月7日公告称 College Planner 将很快上线，首批覆盖美国申请四年制大学的10–12年级学生，整合申请要求、截止日期和资助任务；其他地区与两年制院校仍是后续计划，当前不是普遍正式可用。
- 文章同时介绍已有学习工具：帮助中心显示闪卡9月22日已有、iOS多页扫描10月1日已开始推送；这些不计为本期首次发布。相对已有教育功能，本期增量是升学规划产品路线。
- 采用官方RSS发布时刻2026-10-07T12:00:00Z；未独立评估学习成效、升学结果或青少年安全效果。

**产业判断：** 升学规划把一次问答延伸为有截止日期的持续任务，提醒、材料管理和学校服务可能受益。若要求或资助信息过期，执行链会失效；观察正式上线范围、信息刷新、任务完成率与人工核对负担。

**来源与核验范围：**
- [OpenAI News · Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan)；发布时间：2026-10-07T12:00:00+00:00；补充来源：[学习工具历史日期](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；定位：College Planner 主文；官方RSS时间；帮助中心 September 22 flashcards / October 1 Scan 的背景时间线。已读所列正文，不将旧功能重发当新闻。；阅读范围：full-text；ID：`661f64ddb5f472a2675e`。

### Google Playground 实验性上线：对话创建、试玩和分享游戏

- Google 于10月7日在美国向18岁及以上用户推出实验性 Playground，可通过对话创建、试玩、分享游戏，并选择私有、链接或公开图库等分发方式；创作访问按 Google AI 订阅档位提供。
- 官方表示支持部分多人游戏类型，发布游戏经过筛查；Unity Spark 集成仍将进入封闭测试。不是已交付的通用游戏开发平台，正文没有完整价格、版权或发行条款。增量是从生成内容转向可运行、可分享的互动产物。

**产业判断：** 创建与试玩形成更短反馈循环，休闲内容创作者和平台分发可能受益。作品质量、多人稳定性或商业权利若不明确，专业采用仍受限；观察重复使用、成功发布比例和实际付费档位限制。

**来源与核验范围：**
- [Google AI Blog · Introducing Playground: Create and play custom games](https://blog.google/innovation-and-ai/technology/ai/playground-experimental-gaming-platform/)；发布时间：2026-10-07T12:00:00+00:00；定位：官方主文（Oct 7）创建/分享/美国18+与订阅条件，Unity Spark closed beta；已读正文，未运行游戏或核实权利条款。；阅读范围：full-text；ID：`b6aec8c05cfc3e2f0fe3`。

### Radisson 披露 ChatGPT 插件与广告协同的酒店获客路径

- OpenAI 10月7日客户案例披露 Radisson 与 Accenture Song 构建酒店插件：在 ChatGPT 内显示地图、价格与设施，转到 Radisson 官网完成预订；安装插件后可在相关查询自动出现。
- 客户披露7–8月2026早期访问到预订转化率约为自身自然搜索的1.5倍，并结合赞助广告。这是本期公开的旧期间客户结果，缺少随机对照、样本和归因校准，不能当成因果增益、行业普遍效果或今天新增成交。
- 与昨日企业研究/编码采用案例相比，新增消费发现到直营成交的具体渠道，MCP/API复用至广告体验。发布时刻依官方RSS 2026-10-07T07:00:00Z。

**产业判断：** 品牌可在消费者形成短名单时进入对话，把流量导向直营渠道，酒店品牌和连接服务商可能受益，传统搜索入口承压。客户选择和广告归因可能解释部分差异；观察增量预订、获客成本、插件安装与跨渠道归因。

**来源与核验范围：**
- [OpenAI News · Radisson Hotel Group brings hotel discovery into ChatGPT](https://openai.com/index/radisson)；发布时间：2026-10-07T07:00:00+00:00；定位：客户案例 A new front door for hotel discovery / Building for the next era of travel，7–8月转化口径；已读正文；厂商与客户披露，不是独立实验。；阅读范围：full-text；ID：`4e324623ab7ca6fee0e1`。

### Sonnet 5.5 缓存读取价格减半，订阅附 API credits 分期推送

- Anthropic 在Haiku公告中将 Sonnet 5.5 缓存读取价从USD0.20降至0.10/百万token；只针对cache read，不是所有输入/输出价格减半。实际节省取决于缓存命中与读写比例，未采用厂商平均节省百分比。
- 本周开始推送月度API credits：Max 5x USD100、Max 20x USD200，Team最高USD500池化；额度、套餐订阅与API现金收入/ARR不同，尚不能认为每个账户已启用。相对前期资格访问变化，本期新增成本与分发激励。
- 日期只有10月7日，时区和窗口边界不确定；未核查实际账户到账与完整续期/使用条款。

**产业判断：** 缓存读价降低会优先惠及复用长系统提示和工作上下文的Agent；套餐赠额可降低开发者试用门槛。低命中率、频繁写缓存或过期额度会削弱收益；观察真实账单、命中率及赠额使用后的付费留存。

**来源与核验范围：**
- [Anthropic Newsroom · Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)；发布时间：2026-10-07（仅日期，源站时区未知）；定位：Haiku公告 Lower pricing for Sonnet 5.5 / API credits段；已读价格与额度段，未测账单或核实账户启用。；阅读范围：full-text；ID：`cdb1d51fae0431106fed`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Nous Research 披露9000万美元B轮，计划扩展 Hermes 企业产品

- Nous官网带10月7日日期的公告确认Series B，CEO融资正文披露USD90 million；参与方包括NVIDIA、Microsoft M12、Samsung、Robot Ventures、USV、YC及Menlo。融资正文只标October 2026，事件日来自官网公告；精确时刻未知。
- 已核实Nous Research与Hermes Agent归属，CEO Dillon Rolnick称团队2023年形成，Hermes Agent今年2月以MIT发布。企业产品“will build and deliver Hermes for Businesses”仍属交付计划，不把融资、估值、收入或ARR混用。
- 相对固定名单新增一个开放Agent生态公司；未使用媒体估值/收入预测或公司clone数作为活跃用户。仅日期窗口边界不确定，已对照昨日去重。

**产业判断：** 开放harness可让企业选择模型并积累自身流程，系统集成和模型路由服务可能受益，绑定单一模型的分发面临竞争。可迁移性若牺牲治理和支持，企业采用未必扩大；观察正式交付、客户续约、切换成本与完整任务账单。

**来源与核验范围：**
- [Nous Research Official · Nous Research Oct 7 Series B announcement and CEO funding disclosure](https://nousresearch.com/)；源站公告时间：2026-10-07（仅日期，源站时区未知）；补充来源：[CEO融资正文（仅月份）](https://nousresearch.com/a-note-on-our-fundraise)；定位：官网 Announcements Oct 7 Series B；浏览器阅读全文 A Note on Our Fundraise 的USD90M、投资方、CEO署名、Hermes企业路线；官网嵌入公告与CEO文章同一主体，不是独立核实。；阅读范围：full-text；ID：`0304daca2f1d8fb29989`。
  日期仅精确到天，无法确认 18:00 边界。

### Healthleap 披露3800万美元种子及A轮融资，切入住院营养不良识别

- Healthleap 于10月7日公司发布的WebWire新闻稿披露种子与A轮合计USD38 million，投资方Sequoia、First Round、Hummingbird；没有在本条拆分每轮金额、推导估值或收入。
- 已核实官网产品为住院患者风险识别工作流，先从营养不良入手，把EHR笔记、检验和生命体征等信号交给临床团队评估；公司称用于50多家医院。由Josiah与Jemima Meyer于2022年创立，其他病种扩张仍是计划。
- 新公司发现带来垂直工作流供给对象。医院数及效果属于公司reported，未读完临床研究或独立核验医院结果；新闻稿只到日，窗口边界不确定。

**产业判断：** 把分散临床记录转为团队待处理风险清单可能减少遗漏，医院流程与EHR集成环节可能受益。错误警报或额外复核若增加负担，部署数未必转化为临床价值；观察独立验证、误报、工作流耗时和客户续约。

**来源与核验范围：**
- [Healthleap Official · Healthleap Raises $38M to Help Hospitals Find Patients with Undiagnosed Conditions](https://www.webwire.com/ViewPressRel.asp?SESSIONID=&aId=361525)；发布时间：2026-10-07（仅日期，源站时区未知）；补充来源：[Healthleap官网](https://www.healthleap.ai/)；定位：公司官网身份/产品；公司发布新闻稿资金、About Healthleap、50+ hospitals及未来病种段；已读全文，临床论文和医院财务主张未核验，不采用收益数。；阅读范围：full-text；ID：`3897a6cf402f68d83d8a`。
  日期仅精确到天，无法确认 18:00 边界。

## 3. 模型能力与技术演进

### Claude Haiku 5.5 发布：可调effort，价格按100K提示长度分档

- Anthropic 10月7日发布claude-haiku-5-5，首个支持可调effort的Haiku；可经自有平台、AWS、Google Cloud、Azure获得。厂商定位摘要、分类、压缩与子Agent工作，复杂编码仍可能更适合较大模型，未据跨口径评测排名。
- USD/百万token，提示≤100K / >100K：输入0.10/0.50，输出0.50/2.50，缓存读取0.01/0.05、写入0.125/0.625。新版tokenizer可能使用更多token，报价降幅不等于任意工作流总成本降幅。
- 相对CVP访问分层，本期增量是低价小模型的预算控制与正式平台供给；日期仅到日、边界不确定。系统卡和全部harness未审阅，不采用厂商领先/提速数字。

**产业判断：** 把可分解任务交给低价模型并按任务调effort，可降低子Agent的边际计算费，编排平台和高频分类应用可能受益。失败重试、tokenizer变化和长提示高档价会抵消收益；观察同任务成功率、重试次数与总账单。

**来源与核验范围：**
- [Anthropic Newsroom · Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)；发布时间：2026-10-07（仅日期，源站时区未知）；定位：Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。；阅读范围：full-text；ID：`cdb1d51fae0431106fed`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

### Dynamo v1.5.1 正式补丁：修复路由恢复并收紧多模态输入边界

- 正式release v1.5.1（tag关联commit2093662）修复路由请求过期后空闲worker恢复、SGLang min_tokens及Qwen3-VL视频契约等问题；不是提案或候选版。官方Atom更新时间2026-10-07T01:54:13Z用于窗口，页面显示10月7日；不把更新时间当精确首次发布时间。
- 多模态输入新增大小/尺寸边界和地址固定；环境代理仅DYN_MM_TRUST_EGRESS_PROXY=1时信任，本地路径需DYN_MM_LOCAL_PATH配置，属于兼容性变化。捆绑SGLang0.5.18、vLLM0.28.0等后端，不等于跟随所有上游最新版本。
- 已知问题仍包括SGLang sidecar协议错配HTTP500与部分H264解码后续崩溃；计划1.6修复不能写成当前已修。相对已有vLLM0.31发布，本期新增编排层稳定性与输入契约，无性能排名。

**产业判断：** 更明确的恢复和输入边界有助于减少服务中断，但环境配置变化会增加升级验证负担，运维和集成环节受益。已知sidecar/解码问题仍可能阻碍部署；观察错误率、恢复时间、配置迁移和兼容后端范围。

**来源与核验范围：**
- [NVIDIA Dynamo · Dynamo v1.5.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.1)；更新时间：2026-10-07T01:54:13+00:00；定位：官方release v1.5.1全部正文：Bug fixes / Security / Breaking Changes / Known Issues / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。；阅读范围：feed-content；ID：`1097b3ace96bedcd2f3c`。

## 5. 模型与AI Infra论文

### ReFold：保留完整历史，用可逆折叠控制长时Agent上下文

- ReFold保留不可变完整历史，把重复工具输出和已完成轮次折成提示片段，可将原轮次恢复追加到提示，兼顾可逆性与prefix cache；不需要重新训练基础模型。相对昨日HEAR跨层协作，增量是harness内历史渲染方法。
- 已读方法与§4.1：mini-swe-agent，Qwen3.6-27B/35B-A3B，两张RTX6000 Ada、TP、vLLM prefix cache，temperature0、250步、每步至多16384输出、256K上下文，五个SWE/Terminal基准各50任务；精度、软件版本及完整结果/附录未审阅，不采用加速或成本倍数。
- v1发表于2026-10-06T07:09:54Z，10月7日cs.CL公告；按公告日纳入，日期仅到日、边界不确定，不能称今天首次投稿。

**产业判断：** 可逆折叠可能减少持续Agent的历史重复计算并保留追溯入口，harness与缓存服务环节可能受益。折叠选择错误、恢复开销或过期工具结果会削弱效果；观察同任务成功率、恢复率、KV占用与并发尾时延。

**来源与核验范围：**
- [arXiv model and infra papers · ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents](https://arxiv.org/abs/2610.07863)；源站公告时间：2026-10-07（仅日期，源站时区未知）；补充来源：[已读HTML方法和设置](https://arxiv.org/html/2610.07863v1)；定位：arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL Oct7列表。未完整审阅实验、附录/代码或独立复现。；阅读范围：abstract；ID：`f2c1d7f20282ba4c458b`。
  日期仅精确到天，无法确认 18:00 边界。

### Mosaic 提议用内核干扰预测选择GPU共置或SM分区

- Mosaic摘要提出内核级干扰预测，结合线程块放置、内存层级、SM内部干扰的解析与轻量学习模型；MosaicSched做在线准入，在全GPU共置与SM分区间选择，以满足尾时延SLO。是论文方案，未核实社区合并、正式发布或生产采用。
- v1提交于2026-10-05T23:09:45Z，10月7日cs.DC公告。本次仅读摘要和提交历史；四种GPU架构的具体硬件、精度、并发/长度、基线及软件版本未读，不引用倍数或视为任意负载的时延保证。公告日仅到日，边界不确定。

**产业判断：** 能预测干扰时，共享调度可在利用率和服务尾时延间更精细取舍，推理云与调度框架可能受益。负载迁移、预测误差或准入开销可能破坏SLO；观察校准成本、p99违约率与不同GPU/任务分布的泛化。

**来源与核验范围：**
- [arXiv model and infra papers · Mosaic: GPU Sharing with Latency Guarantees through Kernel-Level Interference Prediction](https://arxiv.org/abs/2610.07504)；源站公告时间：2026-10-07（仅日期，源站时区未知）；定位：arXiv2610.07504v1摘要、Submission history；cs.DC Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。；阅读范围：abstract；ID：`8fa89a6af5613f0e9c9a`。
  日期仅精确到天，无法确认 18:00 边界。

## 6. GPU与供应链

### RTX Spark 笔记本开放预订，NVIDIA 公布Windows本地Agent硬件路线

- NVIDIA 在10月7日与Microsoft的Windows活动公告中称RTX Spark笔记本当天预订、10月16日可购买，紧凑桌面机11月上市；DGX Station Windows版仍为预览。区分预订、发售和未来交付。
- 公司披露RTX Spark最高128GB统一内存，Blackwell RTX GPU与Grace CPU通过600GB/s互连；这些为产品规格，不是本项目负载实测。FP4峰值不能作为实际LLM吞吐，未核实价格、功耗和长任务成本。
- 公告将本地Agent与Windows受控执行环境结合；相比昨日集群AICR，新增个人/工作站供给路径。证据为已读NVIDIA官方RSS完整正文，发布2026-10-07T18:45:28Z；独立硬件测试和微软全套政策未覆盖。

**产业判断：** 更大统一内存可能把部分Agent和开发任务迁至本地，设备与私有数据工作流受益，也可能减少某些云推理需求。散热、内存带宽或系统权限若限制长任务，本地方案未必更便宜；观察发售交付、持续吞吐、功耗与云端同任务总成本。

**来源与核验范围：**
- [NVIDIA Blog · NVIDIA, Microsoft Kick Off a New Beginning for Windows PCs With RTX Spark and AI Agents](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/)；发布时间：2026-10-07T18:45:28+00:00；定位：NVIDIA官方feed-content全文，RTX Spark devices / DGX Station preview / Microsoft Windows Agent；未读取图表外链、实际试用或独立跑分。；阅读范围：feed-content；ID：`e85b9e2ad448ed75ecf9`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 294 条（其中线索 23 条），精选 12 个事件；未注明日期 1 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Nous Research Official：checked；真实浏览器阅读全文CEO融资声明，官网带Oct7日期公告确认B轮；月度正文日期不伪造具体发布时间。；已知截断 0 条。
- Healthleap Official：checked；官网产品/身份与公司WebWire新闻稿全文已读；临床论文、医院结果未独立核验。；已知截断 0 条。
- OpenAI News：checked；已读UI、青少年规划、Radisson官方主文，核对RSS时刻与帮助中心Oct7；其余候选仅标题/日期筛选；未审阅新的安全系统卡。；已知截断 0 条。
- OpenAI API Changelog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Anthropic Newsroom：checked；已读Haiku5.5完整HTTP与官网正文，核对模型/缓存价格和平台；未审阅全部系统卡、评测或实际credits到账。；已知截断 0 条。
- Anthropic Research：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Anthropic 站点地图：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- DeepSeek Research & News：checked；官网Research & News可见最新9月10日V4.1；API/HF入口本轮无已核实新条目。融资媒体线索未回查法定披露，不认定已发生；私域未覆盖。；已知截断 0 条。
- DeepSeek API Change Log：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- DeepSeek 模型与价格：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- DeepSeek · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Alibaba / Qwen Blog：failed；真实浏览器打开qwen.ai/blog，仍只有导航/页脚，正文列表不足；HF前50模型列表无新链接只说明可见范围，不证明没有新闻。；已知截断 0 条。
- Qwen · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；官网博客可见最新7月16日K3等；本期未核实新正式公告。媒体融资/IPO线索没有官方证据，不作事实；公众号/私域未覆盖。；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Z.ai 发布记录：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 智谱开放平台发布记录：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 智谱 · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- MiniMax News：checked；真实浏览器News Updates列表最新8月26日等；本期无已核实列表新事件；公众号未覆盖。；已知截断 0 条。
- MiniMax · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Mistral AI：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Meta Newsroom：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- AI at Meta Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Google DeepMind：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Google AI Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Google Cloud Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Tencent Newsroom：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Tencent · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- ByteDance Seed Blog：checked；真实浏览器研究/出版列表最新8月5日等；已检查可见范围，无本期列示；未覆盖所有豆包产品渠道。；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Alibaba Cloud Press Room：checked；真实浏览器Press Room完整可见列表最新9月23日；已检查列表无本期新发布日期，其他产品文档/公众号未全覆盖。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；新模型链接为lead，模型卡/版本日期未完整核实，保留候选不发布。；已知截断 0 条。
- xAI News：checked；浏览工具完整读取官方news列表最新9月28日Team Bots，其他可见日期早于窗口；文档入口变化未当新发布。；已知截断 0 条。
- NVIDIA Newsroom：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- NVIDIA Blog：checked；读取RTX Spark官方RSS完整正文，HTML浏览失败；其他技术/工业候选仅筛标题/日期，未全读。；已知截断 0 条。
- AMD Press Releases：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- About Amazon：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Qualcomm Newsroom：checked；同域浏览核查官方News Releases最新10月5日Huawei合作；可见列表无10月7日事件；其他渠道不作完整覆盖声明。；已知截断 0 条。
- Samsung Newsroom：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- SK hynix Newsroom：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- ASML News：failed；同官方来源浏览兜底仍internal error，未恢复；不能写无新闻。；已知截断 0 条。
- TSMC Newsroom：checked；浏览核查官方Latest News最新9月10日收入及9月8日合作；可见列表无本期日期。；已知截断 0 条。
- Volantis（公司新闻稿）：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Reflection AI Blog：checked；官网Blog实际读可见Beam介绍及2025旧文，Beam已在10月5日报告；未核实本窗口新增版本。；已知截断 0 条。
- Namespace Blog：checked；官网Blog最新10月5日USD42M B轮，已在前期记录；本期可见列表无新增日期。；已知截断 0 条。
- Vinci Official Blog：checked；官网getvinci.ai/blog可见最新10月6日融资，已在昨日入库/报告；其余无核实本期发布日期，不重复采用。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；官方release采集ok未变，已检查版本候选；未阅读全部历史PR或自行跑分。；已知截断 0 条。
- SGLang Blog：checked；官方技术博客入口本轮未变，候选范围检查；不推导所有社区渠道无进展。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；正式release列表本轮未变，既有0.31.0已在10月5日入库；未把RC更新作为正式版。；已知截断 0 条。
- vLLM Blog：checked；列表发现1条新链接，仅为lead且未核实本期正文日期；保留待核查，不当合格事件。；已知截断 0 条。
- NVIDIA Dynamo：checked；全文读取1.5.1正式release及Atom updated时刻，已记录breaking/known issues；未逐项审阅PR或复现。；已知截断 0 条。
- FlashInfer：checked；v0.7.1rc5是候选版更新时间，不当正式版发布；未补读全PR。；已知截断 0 条。
- Mooncake：checked；release入口本轮ok，14日候选0；没有据此声明整个项目无进展。；已知截断 0 条。
- NVIDIA Technical Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- PyTorch Foundation Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；260条候选本地上限60、196条未归档；补读ReFold方法/设置与Mosaic摘要、Oct7 cs.CL/cs.DC列表；论文分页和其余全文未覆盖。；已知截断 196 条。
- METR：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- UK AI Security Institute Blog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Artificial Analysis Articles：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Artificial Analysis Changelog：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- SemiAnalysis：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- NIST News：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- US BIS News & Updates：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 工业和信息化部：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 最高人民法院：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 外交部例行记者会：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 中国政府网 政策：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 重庆市大数据应用发展管理局：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 国家数据局：failed；浏览兜底官网返回空正文，无可核对日期文章。；已知截断 0 条。

### 媒体直连 feed

- TechCrunch AI：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- The Decoder：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- The Verge AI：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- The Information：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Bloomberg Technology：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条；可能漏采 2026-10-07T01:06 至 2026-10-07T09:48。
- Financial Times Technology：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Financial Times AI：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- New York Times Technology：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- SCMP Tech：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- MIT Technology Review：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Ars Technica AI：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- Tom's Hardware：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 量子位：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 虎嗅：failed；RSS采集timeout，同RSS浏览兜底仍失败；无法补回中断时段。；已知截断 0 条。
- IT之家：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条；可能漏采 2026-10-07T01:06 至 2026-10-07T15:35。
- 36氪：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 钛媒体：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 雷峰网：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 极客公园：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 智东西：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- C114 通信网：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。
- 快科技（驱动之家）：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条；可能漏采 2026-10-07T01:07 至 2026-10-07T11:18。
- 机器之心：failed；官网浏览可达但仅服务页，文章列表不足；公众号未补齐。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；机器采集入口与候选标题/日期已检查；未逐篇阅读全文，不据采集成功断言无新闻。；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；执行日期限定的Reuters AI/芯片/融资线索检索；发现线索未取得支持新增事实的完整一手材料，不采用摘要。
- bloomberg-ai：checked；执行Bloomberg日期限定检索并筛feed；原始媒体漏采窗口未补回，未把二手融资传闻当官方披露。
- ft-nyt-wsj-ai：checked；执行FT/NYT/WSJ AI日期检索；NYT robots受限，Nous线索回查官网；付费媒体未阅读全文。
- china-ai-companies-zh：checked；执行中文公司/模型/融资检索，发现DeepSeek/Kimi等融资IPO转载；官方或法定原始依据缺失，不写已完成融资。
- china-ai-policy-zh：checked；执行政策/算力中文检索；未采用有核实本期日期和正文的新事件，国家数据局正文仍获取失败。
- china-chips-zh：checked；执行芯片/存储/供给中文检索，命中研究与旧材料/传闻；未取得足够一手证据的窗口事件。
- embodied-world-models-zh：checked；执行具身/世界模型中文检索，发现Ropedia相关GAMES研讨会线索；身份、产品和长期增量待核实，非已入库公司。
- supply-chain-en：checked；执行HBM/CoWoS/出口管制等英文检索；本期采用RTX Spark官方供给计划，其他媒体价格/融资线索未一手核验。
- newsroom-fallback：checked；执行被拦官网定域检索并实际浏览Qwen、MiniMax、Qualcomm、TSMC、ASML与xAI；ASML失败，Qwen正文不足。

- 新公司发现：checked；已执行中英文Oct7新公司/融资/产品检索，回查Nous和Healthleap官网/公司新闻稿，新建2公司页；Ropedia研讨会线索尚未核实公司身份/产品，保留候选。

证据包：`data/packets/daily/2026/10/2026-10-07/7ac5b52892ad0a3d365a318e69e5c76666f37ca3c71fb71c8bf7bbd17111d428.json`；采集 run：`20261008T010431-29690273`。

补充覆盖限制：96个采集来源中82个ok、13个needs-browser、虎嗅1个timeout；浏览兜底后Qwen正文不足，ASML、国家数据局、机器之心与虎嗅仍未恢复可核查文章。Techmeme的10月6/7日h2355快照失败，媒体缺口未补齐。机器date-only午夜为占位，正文只显示原始日期；融资正文月份不能替代官网公告日。完整HTTP正文、浏览文本提取与摘要的范围分别记录。

知识入库：新建并发布14页（9来源、2论文、2公司、1综合），更新0页；重复背景（Vinci/Namespace/Reflection、既有学习功能及已发布版本）去重跳过，未核实材料保留候选，详见pending-evidence.md及research-audit.json。[[research/synthesis/interactive-agents-cost-and-local-supply-20261007|交互Agent、成本与本地供给综合]]；[[reference/entities/nous-research|Nous Research]]；[[reference/entities/healthleap|Healthleap]]。
