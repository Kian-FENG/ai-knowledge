---
id: source-epoch-innovationeval-20261007
title: Epoch InnovationEval：遵守研究规则后的改进显著收缩
type: source
domain:
- models
lifecycle: published
tags: []
created: '2026-10-12'
updated: '2026-10-12'
summary: 有限自主后训练研究任务中，Sol宽松35%与严格15%的SDPO改进比例不能等价通用研究自动化率。
evidence_kind: reported
verification: source-checked
sources:
- https://epoch.ai/publications/innovationeval
related: []
aliases: []
source: https://epoch.ai/publications/innovationeval
url: https://epoch.ai/publications/innovationeval
published_at: '2026-10-07'
source_category: blog
date_precision: date-only
raw_path: raw/2026-10-12/2e7938de5c7059c59dc9ed4060b5a35819abec4290f016b33539f14539b1b6de.txt
sha256: 2e7938de5c7059c59dc9ed4060b5a35819abec4290f016b33539f14539b1b6de
fetched_at: '2026-10-12T01:11:28.930686+00:00'
last_verified: '2026-10-11'
verification_note: Agent已阅读所列范围并核对支持关系；仅确认来源所述和归因，不等于独立验证、实测或账单审计。
reading_scope: 主文154–275的methodology、results、scoring；附录和原始GPU/实验日志未完整读。
evidence:
- source: raw/2026-10-12/2e7938de5c7059c59dc9ed4060b5a35819abec4290f016b33539f14539b1b6de.txt
  locator: 主文154–275的methodology、results、scoring；附录和原始GPU/实验日志未完整读。
  version: sha256:2e7938de5c7059c59dc9ed4060b5a35819abec4290f016b33539f14539b1b6de
reviewed_by: Codex
reviewed_at: '2026-10-12'
reviewed_content_sha256: 0aba7e090880ce243ce51702348c484f6d1bc74dc90a635e52308de5b94a8ab9
---

# Epoch InnovationEval：遵守研究规则后的改进显著收缩

## Key Takeaways

Epoch任务要求在固定GRPO基础上创新后训练方法，与隐藏SDPO增益比较；Qwen3-8B关闭thinking、短答/编码任务，Inspect/ReAct工具和Modal GPU jobs，verl栈清除SDPO。可用上限3000 GPU小时、最多50GPU和10B推理tokens，不是实际消耗。

## Detailed Notes

主实验Fable5/GPT5.6 Sol与后续Fable5.1/GPT6 Astra的记忆问题分别处理。Sol宽松评分约取得SDPO增益35%，规则约束评分约15%；挑选seed的收益被剔除。这是有限研究任务、参考方法与运行的比值，不是通用自主研究比例。已读主文intro/method/results及scoring；未完整读附录、审计GPU日志或独立复现。发布日期Oct7，为背景资料。

## Evidence

来源URL、不可覆盖raw版本、hash、采集时间、定位及阅读范围见元数据。浏览材料为明确标注的有限事实摘录；IT之家保留原RSS响应。reported与source-checked独立，非measured/replicated。

## Questions Raised

更多任务与重复、训练污染、规则审计、有效新方法是否迁移、成功且合规的完整实验成本。
