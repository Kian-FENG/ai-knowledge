# Knowledge workflows

## Ingest a source

1. 阅读来源，先 query 查重及现有公司/产品/模型/主题页。URL 抓取或本地文件用
   `scripts/python scripts/ingest.py archive FILE --source-url URL` 留不可覆盖的 hash 版本。
   下载器和日报采集器也遵循同样归档规则。既有 ingest 请求即授权正常入库。
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
8. 运行 validate、相关离线测试并检查结果。首次配置或整体健康声明运行 `tests/run.sh`。

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
