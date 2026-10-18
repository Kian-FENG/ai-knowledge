# AI 产业分析日报（2026.10.17）

统计窗口：2026-10-16T18:00:00-07:00 至 2026-10-17T18:00:00-07:00（洛杉矶时间，右端不含）。

实际生成：2026-10-18T03:04:34.961337-07:00 America/Los_Angeles（UTC 2026-10-18T10:04:34.961337+00:00）；18:00为计划开始时间，本次为延迟补报。

本期四项核实增量集中于DeepSeek模型与检索供给、Replit默认分发澄清和RTX Spark零售可用声明。任务成本需合并模型、检索、重试和harness理解，厂商单次评测不能直接排竞争位次。本次为延迟补报；Infra与论文栏目留空，媒体漏采、动态页面及付费正文限制见覆盖说明。

## 1. MaaS市场与产品形态

### DeepSeek开放Search与Fetch，工具调用开始独立按成功请求计费

- DeepSeek在10月17日更新日志宣布开放自研搜索能力。Search返回结构化搜索结果，Fetch返回单页Markdown；两者均是可独立调用的JSON API，并非发布一个新的对话订阅。指南无独立发布日期，事件日来自更新日志；日期精度到日，窗口边界仍不确定。
- 国际站指南标价：Search和Fetch分别USD0.75/1000次成功且非空的请求；失败、空搜索和超时不计费，返回结果数不改变单次价格。每账户两者各限5QPS，Fetch另有目标域名限制。
- 通过DeepSeek API在DeepSeek Harness、Claude Code或Codex使用的服务端工具调用目前免费，自北京时间2026年11月1日00:00开始按次计费；不能把这项临时优惠外推到所有独立API请求。相比既有模型token账单，新增独立工具供给与调用计价。

**产业判断：** 搜索与抓取从模型附属功能变成可替换的Agent组件，有助开发者控制检索链路，也新增工具调用预算。反例是目标站点访问失败或结果质量不佳抵消低价；观察同任务检索成功率、有效引用率、调用次数和11月后的完整账单。

**来源与核验范围：**
- [DeepSeek API Change Log · DeepSeek October 17: Flash 1017 update and Search/Fetch announcement](https://api-docs.deepseek.com/updates/)；发布时间：2026-10-17（仅日期）；定位：Change Log 2026-10-17 Opening up the in-house search API；指南Search/Fetch、Billing、Rate Limits全文；未调用API或独立核验检索质量。；阅读范围：full-text；ID：`e547d0d8cbe359a05123`。
  日期仅精确到天，无法确认 18:00 边界。
- [DeepSeek API Change Log · DeepSeek Search & Fetch guide and billing](https://api-docs.deepseek.com/guides/search/)；源站公告时间：2026-10-17（仅日期）；定位：Change Log 2026-10-17 Opening up the in-house search API；指南Search/Fetch、Billing、Rate Limits全文；未调用API或独立核验检索质量。；阅读范围：full-text；ID：`4dc309c2f9cfbf220cd0`。
  日期仅精确到天，无法确认 18:00 边界。

## 2. AI公司发展与新公司

### Replit澄清OpenAI成为默认伙伴，Claude仍可选

- TechCrunch在10月17日更新的完整报道引述CEO Amjad Masad：OpenAI成为Replit Agent首选伙伴及默认模型提供方，理由包括表现、经济性和合作；用户仍能选Claude等模型。匿名知情者称Anthropic合作关系仍在，不能写成全面终止合作。
- 报道末尾明确初稿发布于10月16日14:22 PDT（本期之前）；本期增量是周末澄清和更正，更新于10月17日11:48 PDT。公司内部评测未公开完整harness，不据此判断通用模型胜负，也未披露迁移后的采购额。

**产业判断：** 默认入口可能比模型菜单更直接影响推理采购份额，平台议价将同时围绕成本、端到端任务表现和商务支持。反例是用户主动改选、不同任务路由或商业条款改变默认流量；观察实际模型流量、成功率、留存和总账单。

**来源与核验范围：**
- [TechCrunch AI · Replit makes OpenAI its default over Anthropic, CEO says](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)；更新时间：2026-10-17T11:48:08-07:00；定位：正文CEO澄清、匿名知情者反驳及末段originally published/update；完整正文阅读，未经双方合同核验。；阅读范围：full-text；ID：`fcf73aabe3e37fa7f998`。

## 3. 模型能力与技术演进

### DeepSeek V4.1 Flash 1017更新权重与API，单价维持不变

- 官方10月17日更新日志称Web、App和deepseek-flash API已切至V4.1-Flash-1017，调用方式与价格不变；模型卡提供MIT许可权重。新增是9月10日版本之后的小版本升级，不能把“每任务成本下降”写成新一轮token降价。
- 厂商模型卡报告Terminal-Bench4.0为42.3（旧版31.2），DeepSWEv1.1为77.0（旧版74.2）；分别使用Claude Code和Mini-SWE-V2。HLE纯文本子集与完整集、ZeroBench Pass@5须分开。测试预算、重试与全部基线配置未完整核实，不据表格跨厂商排名。
- 厂商称任务运行时间与输出长度减少；这是reported主张，尚无本项目独立任务成本复现。README推荐temperature1.0、top_p1.0、1M上下文；推荐值不等于每项评测实际预算。公告仅到日，边界不确定。

**产业判断：** 若相同任务成功率下输出更短，模型单价不变也能降低整项任务成本，并减少Agent等待时间；收益取决于harness和重试。反例是更短输出省略必要验证，或检索费抵消节约；观察固定任务集的成功率、时间、输出token与工具费用。

**来源与核验范围：**
- [DeepSeek API Change Log · DeepSeek October 17: Flash 1017 update and Search/Fetch announcement](https://api-docs.deepseek.com/updates/)；发布时间：2026-10-17（仅日期）；定位：2026-10-17更新节及脚注；官方README Introduction、benchmark表及脚注、sampling与MIT；未读完整技术报告或下载权重。；阅读范围：full-text；ID：`e547d0d8cbe359a05123`。
  日期仅精确到天，无法确认 18:00 边界。
- [DeepSeek · Hugging Face · DeepSeek-V4.1-Flash-1017 official model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/raw/main/README.md)；源站公告时间：2026-10-17（仅日期）；定位：2026-10-17更新节及脚注；官方README Introduction、benchmark表及脚注、sampling与MIT；未读完整技术报告或下载权重。；阅读范围：full-text；ID：`17aa6f2c9876fccb865e`。
  日期仅精确到天，无法确认 18:00 边界。

## 4. AI Infra社区与工程趋势

本期未收录经核验的新事件；覆盖情况见文末。

## 5. 模型与AI Infra论文

本期未收录经核验的新事件；覆盖情况见文末。

## 6. GPU与供应链

### NVIDIA确认RTX Spark笔记本现售，起价USD2399

- NVIDIA10月17日官方博客称RTX Spark笔记本现已可用，列ASUS、Dell、HP、Lenovo、Microsoft、MSI，起价USD2399、统一内存最高128GB；新增是相对此前上市前生态更新的零售可用声明。
- 官方介绍Blackwell RTX GPU与Grace CPU组合，并记录六地零售活动。最高内存与起价不一定属于同一SKU，本文未核各地区库存、税费、持续功耗和实际模型容量；不采用缺少精度与负载的峰值算力排名。

**产业判断：** 本地大内存设备可能降低私有原型和离线Agent的部署门槛，使PC厂商与推理软件同时受益。反例是带宽、功耗、兼容性和实际供货限制体验；观察指定SKU交付、持续推理速度、整机成本及与云端相同任务比较。

**来源与核验范围：**
- [NVIDIA Blog · RTX Spark Ignites Global Celebration as New Windows PCs Arrive](https://blogs.nvidia.com/blog/local-ai-rtx-spark-windows-laptops-celebration/)；发布时间：2026-10-17T21:00:13+00:00；定位：官方正文开头、A New Generation及六地活动段；发布时间取官方RSS21:00:13UTC；未作零售或性能独立验证。；阅读范围：full-text；ID：`3e1bb6f4d90247655c88`。

## 覆盖与证据说明

- 事实摘录与分析由 Agent 核验；结构校验不证明事实正确或模型能力已被独立复现。
- 候选 74 条（其中线索 0 条），精选 4 个事件；未注明日期 7 条不进入本期报告。
- RSS/Atom/API 只覆盖其暴露的近期条目；不声称全网覆盖。检索结果、网页新链接与页面变化只是线索，须读原文后才能引用。

### 公司与产品一手来源

- Meta Muse Official Model Card：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Visko Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Stacklok Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Peppermint Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Microsoft Command Line：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Satya Nadella Public Article：failed；X文章本轮获取失败，旧背景仍留库。；已知截断 0 条。
- Nous Research Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Healthleap Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- OpenAI News：checked；已查News、API changelog与ChatGPT release notes；News最新10月15日，帮助中心10月16日两节已读。无本窗口新公告被采用，不覆盖全站/账户。；已知截断 0 条。
- OpenAI API Changelog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Anthropic Newsroom：checked；已读News与Research列表；Research10月16日4项列出，内部就业主节补读；新闻最新10月15日。；已知截断 0 条。
- Anthropic Research：checked；Research列表与employment主节已读；量子电路、ECDSA等全文未审，留待跟进。；已知截断 0 条。
- Anthropic 站点地图：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- DeepSeek Research & News：checked；官网/文档与HF入口实际检查；本期以10月17日官方日志和模型卡为准，社区/用户群未覆盖。；已知截断 0 条。
- DeepSeek API Change Log：checked；已读2026-10-17更新与Search/Fetch指南，独立调用与工具优惠分开。；已知截断 0 条。
- DeepSeek 模型与价格：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- DeepSeek · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Alibaba / Qwen Blog：failed；网页工具和原生浏览器均未读到动态文章列表；已实际尝试；HF入口机器检查不能替代产品博客。；已知截断 0 条。
- Qwen · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Moonshot AI / Kimi Blog：checked；已查官方研究列表与HF入口，列表最新7月16日；SCMP信用卡报道未读足官方条款，未采用。；已知截断 0 条。
- Moonshot AI · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Z.ai 发布记录：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 智谱开放平台发布记录：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 智谱 · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- MiniMax News：failed；网页工具与原生浏览器只见导航，动态新闻未恢复。；已知截断 0 条。
- MiniMax · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Mistral AI：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Meta Newsroom：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- AI at Meta Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Google DeepMind：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Google AI Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Google Cloud Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Tencent Newsroom：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Tencent · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- ByteDance Seed Blog：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- ByteDance Seed · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Alibaba Cloud Press Room：failed；Press room只返回动态空列表，未能确认本期发布。；已知截断 0 条。
- 蚂蚁 inclusionAI · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 蚂蚁灵波 robbyant · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 京东 jdopensource · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Xiaomi MiMo · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 面壁 OpenBMB · Hugging Face：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- xAI News：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- NVIDIA Newsroom：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- NVIDIA Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- AMD Press Releases：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- About Amazon：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Qualcomm Newsroom：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Samsung Newsroom：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- SK hynix Newsroom：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- ASML News：checked；官方press列表本轮恢复，最新Oct14；复用本周财报原始证据。；已知截断 0 条。
- TSMC Newsroom：checked；已查官方latest-news；周报复用Oct15财报页1–2有限摘录，不重复核电话会。；已知截断 0 条。
- Volantis（公司新闻稿）：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Reflection AI Blog：checked；官方Oct16 Beam交付主文和HF概览/许可核查，较Oct5预览有实质增量。；已知截断 0 条。
- Namespace Blog：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Vinci Official Blog：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- TODAY Official Blog：failed；官方博客不可访问。；已知截断 0 条。
- TypeSafe AI Official Blog：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- GlobalFoundries Official News：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Meet Odyssey-3：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Decart官网：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Microsoft Official Blog：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- 模思智能官方新闻：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- ModCraft产品官网：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Apple Newsroom：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Pluto Security：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- SemiGraph 半图科技：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Third Moment Research Official：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- HUMXN Official：checked；本轮新发现；官网10月6日公告读完，核对品牌/Thomas Unise/服务换数据，作为背景入库而非当天新闻。；已知截断 0 条。

### AI Infra 社区与工程

- SGLang Releases：checked；已查release列表最新0.5.21 Oct2与官方blog Oct14；未发现本期可核新版本；不等于无合并PR。；已知截断 0 条。
- SGLang Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- LMSYS Blog：disabled；列表需 JS 渲染且无 RSS；SGLang 文章改由 sglang-blog 跟踪。
- vLLM Releases：checked；已查releases，0.32.0为Oct18 06:50UTC，在日报截止Oct18 01:00UTC之后，排除；补读Oct16 Beam文章入周报。；已知截断 0 条。
- vLLM Blog：checked；已查blog及Oct16 Beam全文；两篇Kimi优化全文未读，不能声称全部Infra检索完成。；已知截断 0 条。
- NVIDIA Dynamo：checked；已查releases，最新Nemotron dev.1为Oct15实验快照；未冒称稳定正式。；已知截断 0 条。
- FlashInfer：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Mooncake：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- NVIDIA Technical Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- PyTorch Foundation Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- OpenBMB PilotDeck Official Repository：checked；README核对2.0 Oct15、开源May28；后发媒体不作新首发。；已知截断 0 条。

### 论文、评测与研究机构

- arXiv model and infra papers：checked；本轮RSS entries=0；按Oct16–18补检索无合格结果；不代表无论文。9月28日insecure reporters不能作当天首发，周报选库内已核摘要。；已知截断 0 条。
- METR：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- UK AI Security Institute Blog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Artificial Analysis Articles：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Artificial Analysis Changelog：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- SemiAnalysis：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Vals AI：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- Epoch InnovationEval：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。

### 政府、监管与司法

- CISA News：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- NIST News：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- US BIS News & Updates：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 工业和信息化部：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 最高人民法院：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 外交部例行记者会：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 中国政府网 政策：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 重庆市大数据应用发展管理局：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 国家数据局：failed；主页正文为空，政策动态未完成核查。；已知截断 0 条。

### 媒体直连 feed

- 财联社正文（东方财富转载）：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。
- TechCrunch AI：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- The Decoder：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- The Verge AI：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- The Information：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Bloomberg Technology：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条；可能漏采 2026-10-16T01:03 至 2026-10-17T12:03。
- Financial Times Technology：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Financial Times AI：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- New York Times Technology：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- SCMP Tech：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- MIT Technology Review：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Ars Technica AI：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- Tom's Hardware：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 量子位：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 虎嗅：failed；采集超时，浏览工具同源亦超时。；已知截断 0 条。
- IT之家：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条；可能漏采 2026-10-16T01:03 至 2026-10-18T02:06。
- 36氪：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 钛媒体：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条；可能漏采 2026-10-16T01:03 至 2026-10-18T09:57。
- 雷峰网：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 极客公园：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 智东西：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- C114 通信网：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。
- 快科技（驱动之家）：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条；可能漏采 2026-10-16T01:03 至 2026-10-17T16:02。
- 机器之心：failed；主页仅有限导航/摘要，会员和公众号正文未覆盖。；已知截断 0 条。
- Reuters转述WSJ：checked；已用网页工具打开此配置入口，仅检查可见列表/主文；未见可核本期增量，动态隐藏、全部外链与客户效果未全面审阅。；已知截断 0 条。

### 聚合发现（仅作线索）

- Techmeme River：checked；已完成本轮机器入口采集并检查候选；状态与上限见证据包。未逐篇阅读全文，未据此断言整站无新闻。；已知截断 0 条。

### Agent 检索清单

- reuters-ai-exclusives：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- bloomberg-ai：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- ft-nyt-wsj-ai：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- china-ai-companies-zh：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- china-ai-policy-zh：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- china-chips-zh：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- embodied-world-models-zh：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- supply-chain-en：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。
- newsroom-fallback：checked；已按2026-10-16至18执行窗口检索；结果仅线索，部分返回旧文或无精确日期，不作为完整覆盖。未读取的付费正文和微信公众号仍有缺口。。

- 新公司发现：checked；已做中英文开放发现及官网回查：HUMXN公告Oct6纳背景；NEXFORM官网产品可确认但本期融资一手未补齐；搜索聚合融资/估值不采作事实。。

证据包：`data/packets/daily/2026/10/2026-10-17/fb3c8d9e3b01198aca95611ab0a384e66ebf4f6aa10f6744ec7f2c06ea9c8dac.json`；采集 run：`20261018T095526-3afefa67`。


## 本次补报与知识入库

本轮新增12页、更新Reflection实体1页，13页均已审核发布并通过默认query/get_page与raw hash回查。公司/作者披露为reported，综合判断为derived；source-checked不等于独立测量或复现。

- [综合研究：Agent总成本与交付](/Users/kian/workspace/ai-knowledge/research/synthesis/agent-total-cost-and-delivery-20261017.md)
- [新增跟踪HUMXN（10月6日背景）](/Users/kian/workspace/ai-knowledge/reference/entities/humxn.md)
- [Reflection交付时间线更新](/Users/kian/workspace/ai-knowledge/reference/entities/reflection.md)

### 未完成与排除边界

- 最近到期日报只补10月17日，10月16日日报未回填；本周Oct16增量用官方来源补入周报。
- GLM-Legal官方动态页无正文，媒体首发/日期与完整harness未补齐；Kimi信用卡官方条款未审。Anthropic量子电路与ECDSA研究、vLLM两篇Kimi优化仅看到列表，正文未审。
- PilotDeck2.0是Oct15公告，仅入周报；HUMXN Oct6、insecure-reporters论文Sep28是旧背景，均不当作Oct17首发。NEXFORM产品身份可确认，融资一手与法定注册仍待核；未将聚合融资表作为事实。
- arXiv本轮RSS0条；检索未找到可核本窗口论文，不推断无论文。本周此前arXiv采集存在60条本地上限和未读全文，已保留原始feed；精选论文只读摘要与版本史。
- 付费媒体正文、私域/公众号、官网动态隐藏项、全部仓库合并PR及独立性能/账单复现未覆盖。vLLM0.32.0时间Oct18 06:50UTC晚于日报截止Oct18 01:00UTC，排除。
- 本轮collector120启用入口：82 ok、37 needs-browser、1 failed（虎嗅）；新增HUMXN/PilotDeck两入口在采集后另行核查，不冒称起始采集覆盖。配置共有123来源（含停用项）。
- Qwen、MiniMax已用原生浏览器再次尝试，仍只见导航；阿里云Press Room空列表、国家数据局正文空、机器之心会员内容、TODAY/X文章和Techmeme快照未恢复。ASML入口本轮恢复。高频媒体存在漏采，不能说全行业无新闻。

### 尚未补齐的漏采区间（保留源时区）

- bloomberg-tech：[2026-10-16T01:03:17.341795+00:00, 2026-10-17T12:03:32+00:00)；detected_at=2026-10-18T09:55:49.722767+00:00。
- ithome：[2026-10-16T01:03:20.892089+00:00, 2026-10-18T02:06:55+00:00)；detected_at=2026-10-18T09:55:52.071326+00:00。
- mydrivers：[2026-10-16T01:03:29.044828+00:00, 2026-10-17T16:02:10+08:00)；detected_at=2026-10-18T09:55:58.730930+00:00。
- tmtpost：[2026-10-16T01:03:21.691382+00:00, 2026-10-18T09:57:07+08:00)；detected_at=2026-10-18T09:55:52.913499+00:00。
