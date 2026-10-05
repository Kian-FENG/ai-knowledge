# Knowledge workflows

本文件是 ingest 的执行入口；查询回答见 [query](../prompts/query.md)。
用户说“ingest、收录、入库、更新知识库”时执行至审核发布与回查；明确要求只归档或
只起草则停在指定阶段。已授权的正常入库无需在 finalize 前重复询问。

## 输入与查重

- **URL**：打开原始正文并记录标题、作者/机构、原始 URL、发布时间/事件时间和版本。
  抓取成功时保留原始响应；浏览器提取或用户粘贴内容标明提取方式与阅读范围。
  下载到临时文件后交给 archive，不能让 archive 把 URL 当本地文件读取。
- **本地文件或目录**：先检查文件类型、目录结构和已有 tracker。PDF、仓库或多章资料
  按可读范围分块，相关章节归入同一来源页；不把每个文件都机械拆成独立知识页。
- **日报候选**：`data/articles/`、证据包和报告只是候选与材料；读取其 raw_path 和原文后
  才能用于标准知识页。采集成功、日报生成、知识页发布分别核对。
- **查重**：用标题、别名、对象检索；本次明确检查草稿，可加 `--include-unpublished`。
  继续检查候选页的 `url/source/sources/evidence/raw_path/sha256` 及归档记录中的 URL/hash。
  `grep_wiki.py` 只搜正文，不能代替元数据查重。相同来源同版本优先复用；新版本保留
  旧 raw 并更新原页面。断点续传接着已有草稿做，不重复创建 ID。
- **读取失败或范围不足**：记录失败、截断、仅摘要、日期未知及尚待阅读的部分。
  已读范围足以支撑有限结论时如实限定；否则停留在归档/草稿，不制造已审核或已发布状态。

## Ingest a source

1. 阅读来源，按上节查重及现有公司/产品/模型/主题页。取得的本地原文用
   `scripts/python scripts/ingest.py archive FILE --source-url URL` 留不可覆盖的 hash 版本。
   本地资料没有 URL 时省略 `--source-url`。下载器和日报采集器也遵循同样归档规则。
   将返回的 raw_path、sha256、fetched_at 连同原始文件名/路径记入来源页，
   evidence.version 引用实际 hash 或上游版本；不能以采集时间代替发布时间。
2. 用模板起草：`scripts/python scripts/ingest.py draft --type source --slug example
   --domain industry --title "标题"`。论文用 paper，公司/产品/社区用 entity，
   长期概念用 concept；方法用 technique，反复出现的模式用 pattern。
3. 填完模板和证据。来源摘要保留 source/URL/发布日期/定位/版本；深入分析放 note，
   跨对象比较用 comparison。不要把来源复述当成作者已验证的独立事实。
4. 对照旧知识做增量综合，更新相关实体、趋势、模型能力与时间线；保留反例和冲突。
   资料多时在 tracker 分块记录；原始文件版本始终保留。
5. 从 index、知识图谱或已经可达的页添加路径完整的链接；不能只形成孤立互链。
   `log.md` 追加本次新知、修正、涉及页面和来源，更新 tracker。
6. `scripts/python scripts/ingest.py review PAGE --reviewer Codex`。
   Agent 先核对事实与出处，命令检查结构与完整性并记录内容 fingerprint。
   编辑后必须重新审核；review 本身不改变 evidence verification。
7. `scripts/python scripts/ingest.py finalize PAGE [PAGE ...]`。
   验证 fingerprint、引用、导航可达性，暂存页面和六种索引，在写锁中发布。
   替换失败回滚；中断留下 journal，下次写入恢复。并发读者可能看到批次中间状态。
   finalize 不执行 Git commit。`commit PAGE` 是兼容别名；裸 commit 只校验和重建索引。
8. 运行 validate，并用默认 query 查询本次标题/别名，get_page `--follow-sources` 回读
   发布页及来源；确认页面可见、生命周期为 published、证据定位与阅读范围一致。
   工具变更运行相关离线测试；首次配置或整体健康声明运行 `tests/run.sh`。

工具只负责模板、归档、结构检查和发布事务；Agent 必须完成原文阅读、综合与审核。
JSON 输出可写在 ingest 子命令之前或之后，例如：

```bash
scripts/python scripts/ingest.py archive /path/to/article.txt --source-url https://example.org/article --json
scripts/python scripts/ingest.py draft --type source --slug example --domain industry --title "标题" --json
# 编辑生成页，填完所有内容与证据，并添加导航链接后：
scripts/python scripts/ingest.py review reference/sources/example.md --reviewer Codex --json
scripts/python scripts/ingest.py finalize reference/sources/example.md --json
scripts/python scripts/query.py "标题" --json
scripts/python scripts/get_page.py reference/sources/example.md --follow-sources --json
scripts/python scripts/validate.py --require-migrated reference --require-migrated research
```

一次入库的交付需说明：读了什么及覆盖范围，新建/更新页，去重跳过项，主要知识增量，
审核发布与回查结果，未完成项和原因。未读完、未通过审核或尚未发布时不能称“全部入库完成”。
“入库后回答”的请求在此后进入 query，答案引用回查后的已发布页面。

## Batch and resume

在 `ingest-tracker.md` 按来源及版本记录 raw 路径、阅读范围、目标页、归档/阅读/综合/
审核/发布/回查的实际状态和阻塞原因。开始前读 tracker，跳过已完成且证据未变的项目。
对失败项单独重试；发布命令中断时先检查页面和 journal 恢复结果，再回查，不凭旧记录
宣布成功。相互引用的一组页面完成审核后批量 finalize；其他未完成资料保留 draft。
批次日志合并追加到 `log.md`，保留前次记录。

## Verification and corrections

先读原文并记录 `evidence: [{source, locator, version}]`，再运行
`scripts/python scripts/ingest.py touch PAGE --verification-note "核验内容"`。
touch 更新实际核验日并使旧审核失效；核验日期不能替代来源日期。
replicated 只用于已记录的外部独立复现，不能因联网查到同一新闻就设置。
修改既有 published 页时先将 lifecycle 改回 draft 再编辑，审核发布后重返默认检索。
替换页使用 supersedes；旧页 deprecated 后仍能显式查看。

## Discovery and reports

采集所得只是候选；发布日报和发布知识页是两件事。每日编辑筛出长期价值事件时，
按以上完整流程入库。普通重发、纯补充不重复建页。未知日期只归档，不能填为采集日。
日报流程和质量规则见 `prompts/daily.md`；不要求用户每天重复批准正常采集和本地报告。
