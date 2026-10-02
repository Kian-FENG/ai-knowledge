# Source collection

`data/sources.yaml` 是机器采集源，`data/watchlist.yaml` 是公司、社区和新公司发现清单。
feed 自动解析 RSS/Atom；web 仅存入口快照，必须由每日 Agent 打开带日期的具体文章。
入口页面采集成功不代表完成该公司的新闻核查。固定清单之外每天做新公司开放检索。

```bash
scripts/ai-news validate
scripts/ai-news collect --days 14 --limit 60
scripts/ai-news status
scripts/ai-news fetch 'https://官方文章地址' --source anthropic
scripts/ai-news import data/editorial/source.json --source anthropic
scripts/ai-news packet
```

import JSON 包含 title、url、text、published_at 或 updated_at、date_basis
（published/updated/announced/unknown）、extraction（full-text/feed-content/abstract）。
arXiv RSS 日期是公告时间，保存为 announced_at，不能冒充论文初次投稿时间；
打开摘要页再记录 published_at 和版本，报告明确列出公告/投稿区别。
可附 raw_path 指向 fetch 返回的原始档案；浏览器读取的正文无 HTTP bytes 时，保存为
agent-source-extract 文本快照，明确提取方式。不要拿搜索摘要写成全文。
仅日期写 YYYY-MM-DD，系统标记 date-only。未知日期写 null 和 unknown，不补采集日。

每次获取的响应字节按 SHA-256 归档，HTTP 错误也保留；gzip 解码在解析阶段进行。
解析后的文章按 canonical URL ID 去重；先前正文不会被后来较短的 feed 替代。
来源健康、每来源上限造成的截断、未知/未来日期、正文阅读待办保存在 data/runs/。
RSS/API 自身列表可能不完整，即使本地未截断也不能宣称完整覆盖。

每次变更证据会生成新的 packet hash。editorial 必须对应当前 packet；不能把旧编辑
结果套到新证据包上。机器质量检查不替代 Agent 对原文和结论的核验。
候选归档和日报编辑不自动发布知识页，选出的长期知识走 docs/workflows.md。
