# 待核实与覆盖边界（2026-10-10）

- 获取失败/不足：虎嗅RSS超时且同站浏览超时；Qwen博客仅导航；TODAY配置blog路径404；机器之心仅服务页；Techmeme Oct9/10 h2355快照读取失败。NDA根页、高通、MiniMax、阿里云列表已由原生浏览器恢复，不再归作同一故障。
- 媒体漏采：IT之家、雷锋网、钛媒体3段，精确时间见packet gaps（起终点带不同来源偏移，不能直接比较截短显示）；没有恢复成连续全天覆盖。高频launchd是否持续运行未独立检查。
- 自动采集101来源：82 ok、18 needs-browser、1 failed；来源配置本次新增5个browser入口，合计107（1 disabled），这些新增入口是手工检查，不冒称本次自动采集涵盖它们。
- 候选189（线索26），只采用4事件。OpenAI RSS1287条但按关键词/回溯筛30候选，30需全文；其他feed/API只暴露近期有限条目。已知自动截断0不等于网页、feed或检索完整；候选原文多数未逐篇阅读。
- 论文：arXiv本次RSS0条；执行日期限制发现检索，但聚合器日期不等于原论文公告日。cues媒体报道对应10月5日论文是背景；RACE/SELF等聚合线索未读原始公告/全文，未入本期论文栏。不宣称不存在本期新论文；前期Zepp/SWE-Journey仍只读摘要。
- MISSINGNO：原X入口失败，Portal公开概览不见名称，未测试账户；模型开发者/revision/LICENSE、免费期限、价格与可比harness未取得。
- 利太智药：融资成交/到账日和官方公司/投资方声明未取得；法定主体、具名管线、湿实验协议和药物候选证据缺失。来源页只核对媒体转述，不立已核实公司页。
- 长鑫：只有完整IT之家RSS转述；演讲日期、官方讲稿、DDR5规格、量产/良率/认证和实际价格未核实。未将4F²路线等同HBM或现成服务器供给。
- 背景已入库：Composer/Decision-1源站10月9日仅日期、更新时刻未知，不改原来源时区解释以强行归本期；Peppermint10月8日种子公告窗口外；Stacklok公司页未知发布日期、USD17.5M融资线索追至2023年，不记当日融资。
- 保留线索：Hone融资轮次/金额日期存在混乱；Apple-Huxe检索指向6月监管披露、5月产品关闭，不将10月媒体文章自动作新交易；NVIDIA/Reflection只有谈判报道，未作已完成收购；腾讯/字节个人Agent与RTX5080/5090、ASML涨价等缺已读一手支持。
- vLLM Rubin preview列表仅10月9日，无完整正文/图表、harness阅读，本期不采用7.8x。FlashInfer0.7.0 RSS日期与GitHub9月22日release显示有冲突且版本旧，保留原版待核验，不视为本期新发布。
- 延续待办：Qwen-Image2.1-Turbo LICENSE、DeepSeek媒体harness、Nous/Step5模型卡、Gudea投资者日期、Biren法定披露及Manus/Arena/OpenAI ARR/Broadcom线索，均未补足本期一手证据。

实际已检查但无合格增量、未读取全文、获取失败是不同状态；逐来源和9组发现检索见editorial.json及report.md。公司披露/作者主张保持reported，研究机制为derived；没有measured或replicated升级。
