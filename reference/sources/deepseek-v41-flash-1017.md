---
id: source-deepseek-v41-flash-1017
title: DeepSeek V4.1 Flash 1017更新权重与API，单价维持不变
type: source
domain:
- models
lifecycle: published
tags: []
created: '2026-10-18'
updated: '2026-10-18'
summary: 官方10月17日更新日志称Web、App和deepseek-flash API已切至V4.1-Flash-1017，调用方式与价格不变；模型卡提供MIT许可权重。新增是9月10日版本之后的小版本升级，不能把“每任务成本下降”写成新一轮token降价。
evidence_kind: reported
verification: source-checked
sources:
- https://api-docs.deepseek.com/updates/
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/raw/main/README.md
related: []
aliases: []
source: https://api-docs.deepseek.com/updates/
url: https://api-docs.deepseek.com/updates/
published_at: '2026-10-17T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body
sha256: 1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07
fetched_at: '2026-10-18T10:01:03.648213+00:00'
last_verified: '2026-10-18'
verification_note: 2026-10-17更新节及脚注；官方README Introduction、benchmark表及脚注、sampling与MIT；未读完整技术报告或下载权重。
  source-checked仅确认上述支持关系；不表示独立验证、测量或复现。
evidence:
- source: raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body
  locator: Change Log Date2026-10-17整节及脚注；此前日期仅背景
  version: sha256:1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07
- source: raw/2026-10-18/414cac47fc769e0e07daadc1e096cd5d12fe00e012cd5d14fef581a0e5e31aec.body
  locator: README全文；发布日对应Change Log；未读完整报告、权重或推理实现
  version: sha256:414cac47fc769e0e07daadc1e096cd5d12fe00e012cd5d14fef581a0e5e31aec
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: 9c70fde25e5ad7fb149db5876f9b1674aab3da9ec3876c1296ce0f569610239d
---

# DeepSeek V4.1 Flash 1017更新权重与API，单价维持不变

## Key Takeaways

官方10月17日更新日志称Web、App和deepseek-flash API已切至V4.1-Flash-1017，调用方式与价格不变；模型卡提供MIT许可权重。新增是9月10日版本之后的小版本升级，不能把“每任务成本下降”写成新一轮token降价。

厂商模型卡报告Terminal-Bench4.0为42.3（旧版31.2），DeepSWEv1.1为77.0（旧版74.2）；分别使用Claude Code和Mini-SWE-V2。HLE纯文本子集与完整集、ZeroBench Pass@5须分开。测试预算、重试与全部基线配置未完整核实，不据表格跨厂商排名。

厂商称任务运行时间与输出长度减少；这是reported主张，尚无本项目独立任务成本复现。README推荐temperature1.0、top_p1.0、1M上下文；推荐值不等于每项评测实际预算。公告仅到日，边界不确定。

## Detailed Notes

2026-10-17更新节及脚注；官方README Introduction、benchmark表及脚注、sampling与MIT；未读完整技术报告或下载权重。

原始材料及本期published与显式草稿按对象、URL/hash查重；相同版本不重复建页，相关对象优先更新。

## Evidence

[原始来源](https://api-docs.deepseek.com/updates/)；归档 `raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body`；SHA-256 `1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07`；实际采集 2026-10-18T10:01:03.648213+00:00。

[原始来源](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/raw/main/README.md)；归档 `raw/2026-10-18/414cac47fc769e0e07daadc1e096cd5d12fe00e012cd5d14fef581a0e5e31aec.body`；SHA-256 `414cac47fc769e0e07daadc1e096cd5d12fe00e012cd5d14fef581a0e5e31aec`；实际采集 2026-10-18T10:01:03.849409+00:00。

## Questions Raised

判断（derived）：若相同任务成功率下输出更短，模型单价不变也能降低整项任务成本，并减少Agent等待时间；收益取决于harness和重试。反例是更短输出省略必要验证，或检索费抵消节约；观察固定任务集的成功率、时间、输出token与工具费用。
