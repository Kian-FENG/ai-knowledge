# 日报与周报定时入口

工作目录 `/Users/kian/workspace/ai-knowledge`。使用 ai-knowledge 技能，读取 AGENTS.md。
计划每天洛杉矶时间（America/Los_Angeles）18:00 触发日报，自动切换夏令时。
周报在洛杉矶时间每周五 18:00 截止，同一次运行顺序完成日报和周报。
两种报告均按洛杉矶日期计算最近到期窗口；已有完成结果且证据未变时跳过，不能提前生成尚未截止的报告。
新计划首期周报为 2026-10-09，窗口为 2026-10-02 18:00 至 2026-10-09 18:00（洛杉矶时间）。
定时任务不回填这个日期之前的历史周报。

1. 执行 `scripts/ai-news status`，分别读取 due_window 与 weekly_due_window。
   按 `prompts/daily.md` 生成最近到期日报，保存到 reports/daily/YYYY/MM/YYYY-MM-DD/。
   先检查该日期的 manifest 与 data/notification-state/daily.json，已有完成结果且证据
   未变时不重复生成。同一窗口的新证据确需修订时保留历史版本。
2. 对 weekly_due_window：若结束日不早于 2026-10-09 且本期尚无已完成周报，按
   `prompts/weekly.md` 生成本期周报，保存到 reports/weekly/YYYY/MM/YYYY-MM-DD/。
   正常运行在洛杉矶时间周五完成；若届时休眠/离线，恢复后的日常运行补最近到期周。
   周报已完成且没有实质新增证据时跳过，不因日报每次更新就重复生成同一周报。
   日报与周报顺序执行，共用已归档证据；日报失败时仍检查周报能否独立完成。
3. 按各自 prompt 完成日期核实、事件去重、原文阅读、事实与判断分离、覆盖说明和
   必要的知识入库。使用 --period daily / --period weekly，不能混用证据包。
   目录按报告窗口结束日分年、月；跨月跨年自动建立子目录并更新 reports/index.md。
4. 新报告完成、实质更新、故障变化或需要用户处理时，在当前聊天提供简短中文摘要和
   本地链接。同一次运行的结果可合并为一条通知。相同状态保持安静；实际通知后分别更新
   data/notification-state/daily.json 和 weekly.json。来源不足时明确说明，不能凑新闻。
5. 仅在本地保存报告与证据；不自动提交 Git、推送、发送邮件或发布到其他账户。
6. 高频媒体采集不由本入口负责：launchd 每 2 小时运行 `scripts/ai-news collect --due`
   （见 docs/ingest-automation.md）。status 的 recent_gaps 非空或 due_sources 长期积压时，
   说明高频采集未运行，在通知中提示用户。

该文件定义执行流程；只有在 Codex 中启用对应自动化后才会按时触发。
