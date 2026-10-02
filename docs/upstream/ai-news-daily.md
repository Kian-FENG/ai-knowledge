# 每日自动采集与周报

工作目录固定为 `/Users/kian/workspace/ai-news`。遵循本项目 AGENTS.md。所有日期按 Asia/Shanghai 计算。

1. 运行 `scripts/ai-news validate`，再运行 `scripts/ai-news collect --days 14 --limit 40`，检查 JSON 结果及 `scripts/ai-news status`。每次采集都会在 data/runs/ 记录健康情况。需要公开互联网访问；遇到沙箱网络阻断时使用工具允许的网络执行权限，不能把阻断记为“无新闻”。若仍受限，报告具体失败，保留已有档案。
2. 读取最近采集记录，必要时检查新资料的日期和分类。分类目录为模型、产品、平台、商业、政策、芯片、基础设施。抓取未知日期的内容只归档、不作为当周新闻。
3. 每次计算最近一个完整自然周（周一至周日）。若 output/weekly/<start>_<end>/manifest.json 不存在，或 status 为 draft/empty，则按步骤 4 生成或补做该周报告。已有 analyzed 报告时，本次只采集，不重复通知。这个检查可补做机器关机错过的周一报告。
4. 运行 `scripts/ai-news packet`，读取输出路径，按 prompts/weekly.md 完成中文选题、去重、事实核验与分析，将 JSON 写入 data/editorial/<start>_<end>.json。资料不足时明确写覆盖不足。不要把过期的旧闻标成最新动态，不要把参考 PDF 中的事实当新材料。
5. 若有合格内容，运行 `scripts/ai-news report --editorial data/editorial/<start>_<end>.json`；无合格内容时运行 `scripts/ai-news report` 输出明确的空报告。周报保存为 Markdown，检查章节、来源链接和覆盖说明完整，同时保留 JSON 和 manifest 供追溯。不要生成或保留 PDF 周报，不发到外部账户。不要修改采集程序或来源配置，除非用户明确要求或已确认的维护故障确需修复。
6. 通知策略：平日资料新增但无重要状态变化时保持安静；周报首次完成或有实质补全时，给出中文简讯及 Markdown 周报的本地文件链接；来源首次失败、失败集合变化、全部采集失败、需要用户处理时通知。相同的非关键失败集合不重复通知。用 data/notification-state.json 保存已通知的报告周期和失败集合，只有发送通知后更新。
