---
id: source-vals-multi-agent-cost-20261009
title: Vals评测：多Agent费用增加，收益取决于模型与预算
type: source
domain:
- models
lifecycle: published
tags: []
created: '2026-10-12'
updated: '2026-10-12'
summary: 50个UI测试应用、8种单/多Agent配置；费用1.8–5.1倍，单次运行和不同harness限制结论。
evidence_kind: reported
verification: source-checked
sources:
- https://www.vals.ai/blogs/multi-agent-vibe-code-bench
related: []
aliases: []
source: https://www.vals.ai/blogs/multi-agent-vibe-code-bench
url: https://www.vals.ai/blogs/multi-agent-vibe-code-bench
published_at: '2026-10-09'
source_category: blog
date_precision: date-only
raw_path: raw/2026-10-12/e63ba469558791dda095de8e9f3309bb315855dd0f6d266e5fe761ee2a8669e8.txt
sha256: e63ba469558791dda095de8e9f3309bb315855dd0f6d266e5fe761ee2a8669e8
fetched_at: '2026-10-12T01:11:28.833761+00:00'
last_verified: '2026-10-11'
verification_note: Agent已阅读所列范围并核对支持关系；仅确认来源所述和归因，不等于独立验证、实测或账单审计。
reading_scope: 完整主文、结果表、统计、delegation配置和长上下文费用局限；未执行代码或审计账单。
evidence:
- source: raw/2026-10-12/e63ba469558791dda095de8e9f3309bb315855dd0f6d266e5fe761ee2a8669e8.txt
  locator: 完整主文、结果表、统计、delegation配置和长上下文费用局限；未执行代码或审计账单。
  version: sha256:e63ba469558791dda095de8e9f3309bb315855dd0f6d266e5fe761ee2a8669e8
reviewed_by: Codex
reviewed_at: '2026-10-12'
reviewed_content_sha256: 58c730d64723006c4a34991b94f400ecd080a4ccb8c120170d19f66b7ed2023b
---

# Vals评测：多Agent费用增加，收益取决于模型与预算

## Key Takeaways

Vals AI在50个Docker Compose全栈应用上按浏览器UI流程测试通过比例评估GPT-6 Sol（OpenAI Agents API）和Claude Opus5.5（headless Claude Code CLI），medium/max、单Agent/团队共8配置，每配置只运行一次；最多5个并行子Agent。作者报告团队费用1.8–5.1倍，只有Sol medium的7.3个百分点改善达到统计显著性。

## Detailed Notes

Sol medium单Agent77.6%/USD1.22/12.4分钟，团队84.9%/USD3.07/11.9分钟；95%CI2.3–12.4、p=.005。团队额外delegation提示、跨模型harness不同，不是单纯模型排名。Sol费用用基础层USD2/M输入、.2缓存、10输出，超过272k的逐请求长上下文费未重构，可能低估；子Agent重复读缓存会放大费用。单次运行不估计重复运行方差，UI通过率不涵盖生产安全。日期Oct9是背景，不列本期论文首发。

## Evidence

来源URL、不可覆盖raw版本、hash、采集时间、定位及阅读范围见元数据。浏览材料为明确标注的有限事实摘录；IT之家保留原RSS响应。reported与source-checked独立，非measured/replicated。

## Questions Raised

相同harness/提示与多次重复，按任务拆分团队收益、失败成本、并发上限、真实长上下文费用和安全测试。
