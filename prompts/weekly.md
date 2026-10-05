# 每周 AI 产业分析周报 Agent

工作目录 `/Users/kian/workspace/ai-knowledge`。先读 AGENTS.md、SKILL.md、
docs/report-spec.md 和 docs/research-focus.md。每周五洛杉矶时间（America/Los_Angeles）18:00 生成一份周报。
按当地时区自动切换夏令时；标题、归档和 --date 均使用窗口结束的洛杉矶日期。

1. 运行 `scripts/ai-news validate` 和 `scripts/ai-news status`，使用
   weekly_due_window：洛杉矶当地上周五 18:00 至本周五 18:00，右端不含。迟到运行补最近到期周。
   读取该窗口的 manifest 和 `data/notification-state/weekly.json`（首次可不存在）。
   已完成且证据未变化的周报不重复生成或通知。周报与日报分别记录状态。
2. 检查该周的日报和原始证据。需要补充时运行 `scripts/ai-news collect --days 14 --limit 500`，
   按 prompts/daily.md 的来源核查步骤补齐网页正文、公司动态、Infra、论文和新公司发现。
   日报可帮助发现事件，事实仍需追至原始出处。失败、截断和未查范围写入覆盖说明。
   尚未关闭的周不生成正式周报；机器离线造成缺失时明确标注。
3. 运行 `scripts/ai-news packet --period weekly --brief`，读取返回的证据包。核对窗口、
   来源健康、漏采窗口（coverage.gaps）和拟收录文章；候选较多时以本周日报为事件索引，
   再按 `--group` 分组查看候选标题。text_truncated 时读取完整文章；lead 条目须先找到原文
   并 import。通过 import 归档补充材料后重新生成 packet，使用真实的 packet_sha256 与 article_ids。
4. 合并同一事件在一周内的重复报道与后续更新，保留时间线和仍有争议的部分。六个栏目，
   最多 24 个事件，优先有产业影响的变化。周度 overview 解释主要趋势、公司竞争变化、
   模型与 Infra 对能力/成本/供给的影响；各条区分事实与判断，数字保留口径和归因。
5. 按 report-spec 写 `data/editorial/weekly/YYYY/MM/YYYY-MM-DD.json`。date 是窗口结束日，
   period 必须为 weekly。填写 source_checks 与 reviewed；outlook 列出下周具体观察指标，
   依据本期证据解释待验证的假设，不把预测当事实。JSON 其他字段与日报相同。
6. 运行 `scripts/ai-news report --period weekly --date YYYY-MM-DD --editorial FILE`。
   真正没有候选时可省略 editorial，生成有覆盖说明的空报告。有候选但未选中时保存
   items=[] 的编辑说明，解释筛选理由。检查产物标题、七天窗口、来源、趋势与下周观察。
   周报保存在 `reports/weekly/YYYY/MM/YYYY-MM-DD/`，生成器自动更新报告索引。
7. 按 ingest 流程更新有长期价值的知识。新报告完成、实质更新、故障变化或需用户处理时，
   在当前聊天提供简短中文摘要与本地链接；相同状态保持安静。实际通知后才更新
   `data/notification-state/weekly.json`，记录日期、packet/editorial hash 和失败来源集合。
   本地保存，不自动提交、推送、发邮件或向其他账户发布。
