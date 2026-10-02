# Source collection

`data/sources.yaml` 是机器采集源，`data/watchlist.yaml` 是公司、社区、浏览器核查入口和
Agent 检索清单。来源的实测记录和对样例的覆盖对照见
[来源修复记录](source-remediation-2026-10-02.md)。入口采集成功不代表完成该公司的新闻核查；
固定清单之外每天做新公司开放检索。

```bash
scripts/ai-news validate
scripts/ai-news collect --days 14 --limit 60     # 全部启用来源
scripts/ai-news collect --due --summary          # 只抓到期来源，供高频定时任务使用
scripts/ai-news status                           # 健康、到期来源、近两天漏采窗口
scripts/ai-news fetch 'https://官方文章地址' --source anthropic
scripts/ai-news import data/editorial/source.json --source anthropic
scripts/ai-news packet --brief                   # 证据包 + 候选清单（id、日期、来源、标题）
scripts/ai-news packet --period weekly --brief --group official
```

## 来源字段

| 字段 | 含义 |
|---|---|
| `kind` | `feed` 解析 RSS/Atom；`web` 有 `link_pattern` 时发现新链接，否则检测正文变化；`sitemap` 发现新 URL；`hf-models` 发现 Hugging Face 新公开仓库 |
| `group` | `official`、`infra`、`research`、`government`、`media`、`aggregator`；报告覆盖说明按此分组 |
| `fetch` | `browser` 表示 JS 渲染或拒绝采集器，collect 不抓取，状态为 `needs-browser` |
| `poll_hours` | `collect --due` 的最短间隔，按实测 feed 保留时长设置（默认 24） |
| `include` | 关键词过滤 feed 标题与摘要、网页新链接文字与 URL；ASCII 词按单词边界匹配 |
| `limit` / `listing_cap` | 单源保存上限（取命令行与此值较大者）/ 列表本身的条数上限，达到时标记可能不完整 |
| `timeout` / `gap_check` | 单源超时秒数 / 是否做漏采判断（arXiv 这类每日整批替换的 feed 设为 false） |
| `checked_at` / `note` | 端点最近一次实测日期与已知限制 |

采集器使用固定 UA，不伪装浏览器、不绕过 401/403、Cloudflare 或 robots.txt。
news.google.com（含 /rss）、feeds.finance.yahoo.com、reuters.com 的 robots.txt 禁止本采集器
抓取，因此不进入 collect；对应查询写在 watchlist 的 `discovery.searches`，由 Agent 用自己的
搜索工具执行。新增来源前用 `urllib.robotparser` 核对，结果记入 note。

## 采集结果与线索

- **feed**：条目按日期、关键词过滤后保存为候选。`aggregator` 组的条目保存为
  `lead: true`、正文为空的 metadata-only 记录，摘要放在 `summary`。截断只统计尚未归档的条目。
- **新链接与页面变化**：第一次抓取只建立快照（`needs-review`，`baseline: true`，列出前 10 个
  链接或页面开头），之后与上一次成功快照比较。新链接、新仓库、新 URL 和页面正文变化
  保存为线索：`date_basis: discovered`，`discovered_at` 为发现时间，进入证据包时标记
  `date_boundary_uncertain`。线索不能作为报告证据；Agent 打开原文，核对发布日期后用
  `import` 归档，同一 URL 的线索会被正式文章替换。
- **失败判定**：匹配链接归零、正文少于 200 字时记为 `failed`，不覆盖上一快照；
  80% 以上链接同时变化视为改版，不保存线索并要求人工核查。
- **漏采窗口**：feed 中最早条目晚于上次成功读取时间，说明中间条目已被挤出列表，
  记录 `gap`（from/to），保存在 `data/source-state.json`，进入证据包哈希和报告覆盖说明。
  首次读取记录 `coverage_from`。搜索类或相关性排序的列表不做此判断，只看 `listing_cap`。

`data/source-state.json` 保存每个来源的最近尝试、最近成功快照（指向 raw 档案）和漏采记录。
每次获取的响应字节按 SHA-256 归档，HTTP 错误也保留；gzip 解码在解析阶段进行，按
Content-Type、XML 声明或 meta 识别 GB 编码。解析后的文章按 canonical URL ID 去重；
先前正文不会被后来较短的 feed 替代；feed 扫描不替换 Agent import 的记录（`imported`），
多个 feed 含同一 URL 时保留正文更长的版本。来源健康、截断、未知/未来日期、正文阅读待办
保存在 data/runs/；`--due` 没有到期来源时不写空记录。RSS/API 自身列表可能不完整，
即使本地未截断也不能宣称完整覆盖。

## 高频采集

媒体 feed 多数只保留 10 小时到 2 天（虎嗅约 10 小时、IT 之家 14–25 小时、Bloomberg
约 15 小时），每天 08:00 一次不够。用 launchd 每 2 小时运行一次 `collect --due`：

```bash
cp scripts/launchd/com.ai-knowledge.collect-due.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ai-knowledge.collect-due.plist
launchctl bootout gui/$(id -u)/com.ai-knowledge.collect-due    # 停用
```

日志写入 `.cache/collect-due.log`。电脑休眠或离线期间的缺口会在恢复后的第一次采集中
记录为漏采窗口；不能事后补回已被挤出 feed 的条目。按当前配置，全部来源一次约归档
12 MB 原始响应，加上高频来源每天约 20 MB。

## 导入格式

import JSON 包含 title、url、text、published_at 或 updated_at、date_basis
（published/updated/announced/unknown）、extraction（full-text/feed-content/abstract）。
arXiv RSS 日期是公告时间，保存为 announced_at，不能冒充论文初次投稿时间；
打开摘要页再记录 published_at 和版本，报告明确列出公告/投稿区别。
可附 raw_path 指向 fetch 返回的原始档案；浏览器读取的正文无 HTTP bytes 时，保存为
agent-source-extract 文本快照，明确提取方式。不要拿搜索摘要写成全文。
仅日期写 YYYY-MM-DD，系统标记 date-only。未知日期写 null 和 unknown，不补采集日。

每次变更证据会生成新的 packet hash。editorial 必须对应当前 packet；不能把旧编辑
结果套到新证据包上。机器质量检查不替代 Agent 对原文和结论的核验。
候选归档和日报编辑不自动发布知识页，选出的长期知识走 docs/workflows.md。
