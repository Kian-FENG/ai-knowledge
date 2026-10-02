# AI 产业分析日报编辑契约

版式参考用户桌面 `AI产业分析日报`（原文件无扩展名，已复制到 docs/examples/）。
仅借鉴组织和分析深度；样例中的新闻、日期、数据与图片不作为新证据。

## 时间与栏目

每天北京时间 08:00，标题使用窗口结束日。窗口为前一天 08:00 至当天 08:00（右端不含）。
使用 `scripts/ai-news packet` 的窗口；手工补报用 `--date YYYY-MM-DD`。
迟到运行只补最近到期窗口，旧窗口需要用户要求才回补。日期仅精确到天的资料
按来源日期与窗口的交集筛选，必须注明边界不确定，不伪造小时；未能判定边界的事件
对照前一期去重。没有发布、更新或源站公告日期只能归档；arXiv 公告日不称投稿日。

六个固定栏目（editorial section 为从 0 开始的编号）：

0. MaaS市场与产品形态
1. AI公司发展与新公司
2. 模型能力与技术演进
3. AI Infra社区与工程趋势
4. 模型与AI Infra论文
5. GPU与供应链

每条：具体标题 → 事实要点 → 单独的产业判断 → 原始来源、日期、定位和阅读范围。
没有核实事件的栏目明确标空；0–24 个事件，由重要性决定，不能凑数量。
同一发布多篇报道共用 event_key；同一公司不同事件分别记录。标注相对既有知识的新变化。

## 事实与判断

链接须指向支持该条事实的原始页面。优先官网、release note、模型卡、论文、法定披露；
可靠媒体用于发现、独立观察和当事方未披露信息，保留归因。社交帖、转载不自动多源证实。
技术主张尽量追至论文/源码/官方文档，涉及数字要有定位与口径。

先完整读取拟引用资料。feed-content、abstract 支持的事实仅限其明确内容；涉及方法、
跑分、局限时打开原文和关键表格。无法获取则缩小结论或不收录，注明阅读范围。
判断解释机制、受益/承压环节、反例与观察指标，不把厂商营销或预测升级为行业事实。

## 编辑 JSON

文件放 `data/editorial/YYYY-MM-DD.json`，格式：

```json
{
  "date": "窗口结束日 YYYY-MM-DD",
  "packet_sha256": "当前 packet 返回的真实 hash",
  "overview": "2–4 句中文概述变化及覆盖限制。",
  "source_checks": [
    {"source_id": "anthropic", "status": "checked", "note": "查看官网并核对本期发布，写明实际覆盖范围"},
    {"source_id": "startup-discovery", "status": "checked", "note": "本次发现检索和回查的来源范围"}
  ],
  "items": [
    {
      "event_key": "company-product-version-event",
      "section": 0,
      "title": "具体的中文标题",
      "article_ids": ["packet 中真实 ID"],
      "facts": ["带归因、日期和必要口径的事实。"],
      "analysis": "判断：可能的产业影响；仍需观察……",
      "locators": {"packet 中真实 ID": "原文小节/表格/段落/版本"},
      "reviewed": true
    }
  ]
}
```

`reviewed: true` 由完成原文审阅的 Agent 填写，不是自动采集标记。
source_checks 的 status 为 checked/failed/not-checked；失败不能标成没有新闻。
报告生成器验证证据 ID、窗口、重复事件和字段；不声称自动判断事实支持关系。
报告保留 Markdown、JSON、manifest、packet，修订归档至 revisions/。不输出 PDF。
