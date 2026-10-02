# 信息渠道修复记录（2026-10-02）

对象：桌面样例 `AI Industry Analysis Daily`（SHA-256
`1c6a34c4…a816`，与 [docs/examples](examples/ai-industry-daily-reference.md) 一致）。
前置审计：[渠道能力审计](source-coverage-audit-2026-10-02.md)，以及用户提供的逐条在线核查
（49 个去重事件：7 条可在现有来源找到、5 条部分、1 条仅在关注名单、36 条找不到）。
本次在北京时间 10:30–11:40 实测端点、修改配置与采集器，并做了真实采集与回测。

## 结论

修复后 49 个事件按“最可靠的渠道”归类如下。样例本身不是事实基准（见审计），这里只
说明渠道能否把事件送到每日 Agent 面前，不证明事件内容属实。

| 渠道 | 事件 | 数量 |
|---|---|---|
| 一手来源自动进入候选或线索 | #4 #7 #8 #9 #12 #14 #17 #18 #20 #27 #28 #30 #31 #33 #36 #37 #38 #39 #41 #42 #45 #46 #49 | 23 |
| 媒体 feed 或 Techmeme 自动产生候选：Techmeme 快照回测命中，或原发报道来自已配置 feed 的媒体 | #1 #10 #11 #25 #26 #29 #34 #35 #43 #44 #47 #50 | 12 |
| 中文媒体 feed 可能捕获（feed 只留 1–2 天，无法回测），Agent 检索兜底 | #3 #5 #6 #15 #16 #21 #22 #23 #24 #32 #48 | 11 |
| 主要依赖 Agent 检索 | #2 #19 #40 | 3 |

修复前对应为 7 / 5 / 1 / 36。仍然没有稳定自动渠道的内容主要是：公众号或用户群首发、
只在社交平台发布、付费媒体独家且未被聚合站收录的条目。

## 修改内容

**修正已有入口**（逐项实测，见下节）：

- 智谱：`z.ai` 首页跳转 chat.z.ai，改为 docs.z.ai 发布记录，并加智谱开放平台中文发布记录。
- DeepSeek：增加 API Change Log 与人民币价格页（正文变化检测）和 Hugging Face 仓库列表。
  Change Log 当前写明“9/14 后应用户需求继续提供 V4 Pro”，与官网文章的强制路由说法不同。
- Anthropic：增加 Research 列表和站点地图新 URL 发现。威胁情报报告位于根路径
  `/threat-intelligence-report-september-2026`，不在 Newsroom；站点地图 lastmod 不是发布时间。
- Meta：关注名单与来源改为 about.fb.com/news（Muse 首发处），保留 ai.meta.com/blog。
- Qwen、MiniMax：标记 `fetch: browser`，不再把空入口当成已检查；补 Hugging Face 列表。
  Kimi 博客 HTML 实际含文章链接（无日期），改为新链接发现，不需要浏览器。
- Mistral、NVIDIA 技术博客：由网页入口改为官方 RSS。SGLang 文章已迁到 sglang.io，
  原 lmsys.org 列表需 JS 且无 RSS，停用。

**新增一手来源**：PyTorch Foundation、CISA、NIST、BIS、Meta Newsroom、NVIDIA Newsroom 与
公司博客、Google AI/Cloud 博客、AMD、About Amazon、Samsung、SK hynix、SemiAnalysis、
Artificial Analysis（文章与 changelog）、METR、UK AISI、OpenAI API Changelog、腾讯集团新闻、
工信部首页、最高法首页、外交部例行记者会、中国政府网政策页、重庆市大数据局，
以及腾讯、字节 Seed、蚂蚁、灵波、京东、小米、面壁的 Hugging Face 列表。

**新增媒体层**：TechCrunch AI、The Decoder、The Verge AI、The Information、Bloomberg
Technology、FT（科技与 AI）、NYT 科技、SCMP 科技、MIT Technology Review、Ars Technica AI、
Tom's Hardware、量子位、虎嗅、IT 之家、36 氪、钛媒体、雷峰网、极客公园、智东西、
快科技（驱动之家）、C114，以及聚合站 Techmeme River。泛科技媒体加关键词过滤。

**采集器能力**（`scripts/news.py`，说明见 [采集说明](ingest-automation.md)）：来源分组；
`poll_hours` 与 `collect --due`；feed 漏采窗口检测并写入证据包和报告；网页新链接、
站点地图新 URL、Hugging Face 新仓库与页面正文变化转为线索；检索与聚合结果只作线索、
不能作证据；关键词过滤；GB 编码识别；中文 feed 日期格式；按 RFC 9309 遵守 robots.txt；
同一主机串行请求；截断只计尚未归档条目；报告覆盖说明按来源组列出状态、漏采与列表上限。

## 访问规则与取舍

- 采集器使用固定 UA，不伪装浏览器，不处理 Cloudflare、401/403。被拦截的入口改为
  `fetch: browser`：Qualcomm、ASML、TSMC、xAI、Alibaba Cloud、ByteDance Seed、Qwen、
  MiniMax、机器之心；国家数据局要求的 TLS 版本超出本机 Python（LibreSSL 2.8.3）支持范围。
- Google News RSS 检索效果最好：用样例一周回测，Reuters 常驻查询命中 #10 #31 #32 #48
  全部 4 条路透报道，Bloomberg 查询命中 #29 #40，FT、NYT、The Information 的相关报道
  也都能检到。但 news.google.com 的 robots.txt 对所有 UA 禁止 `/rss`（并点名 Anthropic
  的爬虫），reuters.com 与 feeds.finance.yahoo.com 也禁止，所以没有放进自动采集。
  这些查询保留在 watchlist 的 `discovery.searches`，由 Agent 在日报流程里用搜索工具执行。
- Techmeme 的 robots.txt 允许首页、River 和历史快照。用 9/6–9/14 每日 23:55 快照、按实际
  链接规则和关键词过滤模拟：9 天共产生 285 条线索，样例中 14 个事件以原发媒体直链出现
  （#10 #11 #12 #25 #26 #29 #30 #31 #36 #43 #44 #45 #47 #50）。未出现：#2 #32 #34 #35
  #40 #48（#2 #35 出现在页面文字里，但链接不在规则内）。

## 端点实测

北京时间 2026-10-02，采集器 UA。保留时长为 feed 最新与最早条目的跨度。

| 来源 | 结果 | 设置 |
|---|---|---|
| Bloomberg Technology | 20 条约 15 小时；正文付费 | 每 4 小时；关键词 |
| IT 之家 | 60 条，审计时约 14 小时、复测约 25 小时 | 每 4 小时；关键词 |
| 虎嗅 | 审计时约 10 小时；10:40 起 GET 无响应超时 | 每 4 小时；30 秒超时；失败照实报告 |
| 36 氪 | 必须用 www 域名；30 条，日期格式需专门解析 | 每 6 小时；关键词 |
| 钛媒体、快科技 | 约 20 小时 / 23 小时 | 每 6 小时 |
| TechCrunch AI、The Decoder、The Verge AI、The Information | 25–29 小时 | 每 8 小时 |
| 量子位 | 10 条约 36 小时，feed 只有副标题 | 每 8 小时 |
| FT 科技 / FT AI | 约 35 / 57 小时 | 每 8 / 12 小时 |
| SK hynix、About Amazon | 约 49 / 41 小时 | 每 12 小时 |
| Techmeme River | 约 6 天，直链原发媒体 | 每 12 小时 |
| 一手 feed（OpenAI、Mistral、PyTorch、CISA、NVIDIA、Samsung、SemiAnalysis 等） | 数天到全量 | 每 24 小时 |
| VentureBeat | Vercel 429 | 未加入 |
| WSJ 官方 RSS、Nikkei Asia RSS、TrendForce feed | 停更（2025-01）/ 0 条 / 停在 2026-07 | 未加入 |
| METR feed.xml | 全文解压后超过 8 MB 上限 | 改为博客列表新链接 |

当前 feed 中仍可直接看到的样例事件：CISA 9/8 联合声明（#31）、Mistral 9/8 融资（#45）、
SemiAnalysis 9/7 TPU 文章（#46）。列表与快照中可见：Anthropic Research 9/9 事件评估（#41）、
站点地图中的威胁情报报告（#4 #12）、DeepSeek Change Log 9/10 记录（#7 #33 #38）、
DeepSeek-V4.1-Flash 仓库建于 9/10（#38）、MiniCPM5 系列仓库建于 9/6–9/9（#28）、
lingbot-world-v2 仓库建于 9/4（#39，早于样例所说的 9/9–9/10 发布，说明建库时间不能当发布时间）、
外交部 9/9 例行记者会实录（#31）、重庆市大数据局 9/10 征求意见公告（#49）、
SGLang 9/9–9/10 DeepSeek V4.1 Flash 支持文章。

首次全量采集（run `20261002T031049-e7d85f1b`）：93 个启用来源中 42 个 ok、38 个建立首个
快照（needs-review）、10 个 needs-browser、3 个失败（METR、虎嗅、钛媒体；前两项已改配置，
钛媒体放宽超时后恢复）。10-02 日报窗口的候选为 464 条（arXiv 313、媒体 131），证据包约 1.2 MB。
全部来源一次约归档 12 MB 原始响应，加上高频来源每天约 20 MB。

## 采集中发现并修复的问题

- 首次全量采集时，OpenAI 与 arXiv 的 feed 扫描把 4 条 Agent 已导入、被 10-02 日报引用的
  记录（2 条 OpenAI 阅读笔记、2 条 arXiv 摘要页与投稿历史）替换成 feed 摘要。原有保护只
  覆盖 `extraction: full-text`。已改为 feed 扫描不替换任何 Agent 导入记录（import 新增
  `imported` 标记，旧记录按 retrieval_method 与 extraction 识别），并从 data/article-history
  恢复这 4 条，被替换掉的 feed 版本另存历史。日报 Markdown 未受影响；复采后记录不再变化。
- NVIDIA Newsroom 的 releases.xml 包含公司博客 feed 的全部 18 篇文章，两个来源并行写同一
  记录并来回覆盖。已改为不同来源遇到同一 URL 时只保留正文更长的版本。

## 样例逐条对照

“修复前”取自用户提供的逐条核查。代号：官=一手来源自动；媒=媒体 feed；聚=Techmeme 线索；
浏=浏览器核查；检=Agent 检索清单。

| # | 事件 | 修复前 | 现在的渠道 |
|---|---|---|---|
| 1 | 田永龙进入腾讯 CEO 办公室 | 未找到 | 媒：快科技 9/9 有报道（标题含 OpenAI，可过关键词）；检 |
| 2 | 字节聘前 Coatue 高管 | 未找到 | 检（Bloomberg）；Techmeme 9/9 页面提及但无合规链接 |
| 3 | 中国电信研究院词元预测 | 未找到 | 媒：C114、快科技等（关键词“词元”“中国电信”）；检。报道日期分散，需核对原报告日期 |
| 4 | Anthropic 威胁情报报告（军事滥用） | 已找到 | 官：站点地图新 URL、Newsroom |
| 5 | 腾讯文档 AI 工作台 | 未找到 | 媒（公众号首发，经转载）；检 |
| 6 | 阿里云进入 Gartner 领导者象限 | 未找到 | 浏：阿里云新闻页；媒；检 |
| 7 | V4.1-Flash 552B 与强制路由 | 部分 | 官：新闻链接、Change Log、价格页、Hugging Face；Artificial Analysis |
| 8 | V4.1 Flash 架构与评分 | 部分 | 官：同上；Artificial Analysis 文章与 changelog（样例 763B 与官方 552B 不一致） |
| 9 | OpenAI 暂停 Pro 订阅、Agents API 等 | 部分 | 官：RSS、API Changelog；浏：帮助中心（对采集器 403）；Techmeme 9/10 链接为 X 帖子 |
| 10 | 英伟达或做 Anthropic IPO 基石投资者 | 未找到 | 聚：9/11 Reuters 直链；检 |
| 11 | 25 位菲尔兹奖得主公开信 | 未找到 | 聚：9/8、9/10；媒 |
| 12 | Anthropic 报告点名中国实验室蒸馏 | 已找到 | 官：站点地图、Newsroom；聚 9/10；媒：TechCrunch、The Information |
| 14 | NVIDIA Robotaxi 与 Skild AI | 未找到 | 官：NVIDIA 公司博客 feed（Skild S1 官网日期为 8/18，非当周新事件） |
| 15 | Gurobi 停止中国免费学术许可 | 未找到 | 媒：快科技 9/9 有报道，标题未必命中关键词（已补“断供”等词）；检 |
| 16 | 智谱在天猫卖 Token | 未找到 | 媒：虎嗅（间歇失败）、36 氪等；检 |
| 17 | OpenAI 研究加速报告 | 已找到 | 官：OpenAI RSS |
| 18 | An Alien Mind | 已找到 | 官：OpenAI RSS |
| 19 | 黄仁勋称 AGI 已到来 | 未找到 | 检；社交平台首发，Techmeme 9/7 页面提及但无合规链接 |
| 20 | 最高法涉 AI 纠纷案件意见 | 未找到 | 官：最高法首页新链接（关键词“人工智能”）；检 |
| 21 | 千问办公多人工作台、微信小微 | 未找到 | 媒；检；浏：阿里云新闻页 |
| 22 | 智象、芝诺具身世界模型 | 未找到 | 媒：量子位、智东西、雷峰网等；检 |
| 23 | DeepSeek 开放约 150 个工程岗 | 未找到 | 媒；检（员工社交平台首发） |
| 24 | V4.1 Flash 内测 | 未找到 | 媒；检（用户群首发）；Change Log 若有记录会产生变化线索 |
| 25 | 字节实时空间视频模型（彭博） | 未找到 | 聚：9/7 Bloomberg 直链；Bloomberg feed |
| 26 | Anthropic 11 个月 5,170 亿美元算力合同 | 未找到 | 媒：The Information feed；聚：9/6、9/11 |
| 27 | 寒武纪成为 PyTorch 基金会白金成员 | 未找到 | 官：PyTorch Foundation feed；媒：快科技 9/8 |
| 28 | MiniCPM5-2B 开源 | 未找到 | 官：OpenBMB Hugging Face；Artificial Analysis |
| 29 | Anthropic 放弃收购 Decart | 未找到 | 聚：9/7；Bloomberg feed；检 |
| 30 | OpenAI 纳维-斯托克斯与学术争议 | 部分 | 官：OpenAI RSS（公司主张）；聚：9/8、9/10（争议报道） |
| 31 | 美三机构蒸馏指控、外交部回应 | 未找到 | 官：CISA feed（9/8）、外交部记者会列表（9/9）；聚 |
| 32 | DeepSeek 聘中信证券筹备 IPO | 未找到 | 检（Reuters）；中文媒体转载 |
| 33 | DeepSeek Flash 降价与闲时定价 | 部分 | 官：价格页与 Change Log 变化检测 |
| 34 | 证监会收紧人形机器人 IPO（传闻） | 未找到 | 媒：The Information feed（9/8 报道存在）；保留传闻归因 |
| 35 | Anthropic 未向英国 AISI 提交测试 | 未找到 | 媒：FT feed（9/8 报道存在）；UK AISI 博客 |
| 36 | Meta 发布 Muse | 未找到 | 官：Meta Newsroom feed；聚：9/8 |
| 37 | AlphaGenome Atlas | 已找到 | 官：DeepMind RSS |
| 38 | V4.1 Flash 上线并开源 | 已找到 | 官：新闻链接、Change Log、Hugging Face；SGLang 博客 |
| 39 | 高德、蚂蚁、京东世界模型 | 未找到 | 官：灵波、京东 Hugging Face（高德无）；媒；检 |
| 40 | 阿里领投 UniPat AI | 未找到 | 检（Bloomberg）；Bloomberg feed |
| 41 | Anthropic 第四起事件与 METR 调查 | 仅关注名单 | 官：Anthropic Research 列表、METR 博客 |
| 42 | 工信部信息通信“十五五”规划 | 未找到 | 官：工信部首页新链接（列表页需 JS）；媒：C114 |
| 43 | 浪潮绕过出口限制（NYT） | 未找到 | 媒：NYT 科技 feed；聚：9/6 |
| 44 | 高通与亚马逊定制芯片合作 | 未找到 | 聚：9/8；浏：Qualcomm；检（站内查询可找到 9/8 新闻稿） |
| 45 | Mistral D 轮融资 | 已找到 | 官：Mistral RSS（9/8）；聚 |
| 46 | SemiAnalysis TPU Ironwood 测算 | 未找到 | 官：SemiAnalysis feed（9/7，付费部分不可读） |
| 47 | 司法部调查英伟达—Groq 交易 | 未找到 | 媒：NYT 科技 feed；聚：9/9 |
| 48 | HBM 推动国产 AI 芯片提价、铠侠表态 | 未找到 | 检（Reuters）；媒：智东西、快科技等转载 |
| 49 | 重庆词元经济行动计划征求意见 | 未找到 | 官：重庆市大数据局首页（cq.gov.cn 路径为 404） |
| 50 | ASML 与三家客户 High-NA 进展 | 未找到 | 聚：9/8；浏：ASML、TSMC；Samsung Newsroom（关键词 High-NA）；检 |

## 仍需处理

1. **高频采集尚未启用。** 需要安装 launchd 任务（见[采集说明](ingest-automation.md#高频采集)），
   否则只在每天 08:00 采集，Bloomberg、IT 之家、虎嗅等会出现漏采窗口，报告会写明但无法补回。
   Techmeme 可用历史快照 `https://www.techmeme.com/YYMMDD/h2355` 补查。
2. 首次运行建立快照的 38 个来源，下一次采集起才会产生新链接线索；本次的 `top_links`
   需要在下一期日报时人工看一遍。
3. 公众号、用户群与社交平台首发内容没有合规的自动渠道，只能靠转载与检索；付费媒体
   只能读到标题和摘要，报告须注明阅读范围。
4. 虎嗅当天持续超时，需观察是否恢复；若连续失败可改为 browser。
5. 原始档案增长约每天 20 MB，`raw/` 是否纳入 Git 需要用户决定。
