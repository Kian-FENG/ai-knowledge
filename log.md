# Activity log

## 2026-10-01 — 初始化

参考远端 LLM-Wiki、AI-News 和用户日报样例建立本地 Agent 与每日流程。
未将样例新闻或配置视为已验证知识。

## 2026-10-02 — 首次在线验证

完成首份试运行日报，选6个事件；归档368条机器候选并补读官方原文，首次入库6个来源/论文页与Volantis实体。arXiv公告日与投稿日分离；论文仅摘要级核验。直接HTTP受限的OpenAI文章用网页读取并保留阅读笔记，未伪造全文快照。

## 2026-10-02 — 信息渠道修复

按渠道审计与逐条在线核查修复来源：智谱改为发布记录页，DeepSeek 增加 Change Log、价格页与 Hugging Face，Anthropic 增加 Research 与站点地图，Meta 改为 Newsroom，Qwen/MiniMax 等 JS 或拦截页标记为浏览器核查。新增一手、政府、研究、中英文媒体与 Techmeme 聚合来源，共 94 个（93 个启用）。采集器支持按来源轮询间隔、漏采窗口、网页新链接与页面变化线索、关键词过滤和 robots.txt。Google News RSS 回测效果好但 robots.txt 禁止，改为 Agent 检索清单。首次全量采集 42 ok、38 建立快照、10 需浏览器、3 失败（2 项已修）。未改动已发布知识页。首次采集时 feed 扫描覆盖了 4 条已导入证据（原保护只认 full-text），已修复并从 article-history 恢复。详见 docs/source-remediation-2026-10-02.md。
