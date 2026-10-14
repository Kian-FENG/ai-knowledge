---
id: source-anthropic-edge-replication-20261012
title: Anthropic端侧复制研究：设备能运行模型不等于完整自主传播
type: source
domain:
- models
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-13'
updated: '2026-10-13'
summary: 原始HTML发布时间2026-10-12T19:30:00Z、更新时间10月13日00:44:16Z，均早于本期开始01:00Z，故仅背景。
evidence_kind: reported
verification: source-checked
sources:
- https://www.anthropic.com/research/self-replicating-ai
related: []
aliases: []
last_verified: '2026-10-13'
verification_note: Agent已阅读标注范围并核对有限陈述支持关系；不表示独立测量、融资审计或部署复现。 HTML时间；主文A/B、简化cyber与外部server说明、Conclusion、AppendixA；未复现。
source: raw/2026-10-14/37043e7b2cc407ed8d4818e5cebf2c696cebc04f9929d14b3bf5fe62be74bb43.body
url: https://www.anthropic.com/research/self-replicating-ai
published_at: '2026-10-12T19:30:00+00:00'
source_category: official
raw_path: raw/2026-10-14/37043e7b2cc407ed8d4818e5cebf2c696cebc04f9929d14b3bf5fe62be74bb43.body
sha256: 37043e7b2cc407ed8d4818e5cebf2c696cebc04f9929d14b3bf5fe62be74bb43
fetched_at: '2026-10-14T01:09:11.034648+00:00'
reading_scope: HTML时间；主文A/B、简化cyber与外部server说明、Conclusion、AppendixA；未复现。
date_precision: timestamp
date_basis: published
evidence:
- source: raw/2026-10-14/37043e7b2cc407ed8d4818e5cebf2c696cebc04f9929d14b3bf5fe62be74bb43.body
  locator: HTML时间；主文A/B、简化cyber与外部server说明、Conclusion、AppendixA；未复现。
  version: sha256:37043e7b2cc407ed8d4818e5cebf2c696cebc04f9929d14b3bf5fe62be74bb43
reviewed_by: Codex
reviewed_at: '2026-10-14'
reviewed_content_sha256: 0634042dec9c7b50bef22113b2882faf008f6826952685f79895d8f905533ff7
---

# Anthropic端侧复制研究：设备能运行模型不等于完整自主传播

## Key Takeaways

原始HTML发布时间2026-10-12T19:30:00Z、更新时间10月13日00:44:16Z，均早于本期开始01:00Z，故仅背景。

作者人工组织15台4GB Android TV盒子，以pipeline parallel运行Gemma4-26B-A4B；这是分布式推理演示，不是自主在真实互联网传播。

封闭GCP/redroid网络评估用无认证ADB简化执行权限，以Llama3.1-8B统一部署任务；被测大模型自身由外部推理服务器运行。GLM-5.2完成编排不等于它把自己的权重装入8B设备；当前小模型容量与完整复制能力尚未同时满足。

已读引言、威胁模型、推理设置/传播方法、主文限制及Memento附录部分：每次1.5小时、总6小时预算；未完整读所有附录、图像和代码。年底可能实现是趋势外推，不是已发生事实。

## Detailed Notes

阅读范围：HTML时间；主文A/B、简化cyber与外部server说明、Conclusion、AppendixA；未复现。

## Evidence

[原始来源](https://www.anthropic.com/research/self-replicating-ai)。不可覆盖原始档案、采集时间和hash见元数据。浏览笔记明确为非逐字提取；日期未知不补采集日，日期占位不视为实际时刻。

## Questions Raised

判断（derived）：低成本端侧推理增加潜在部署面，但能力、设备可达性和权限仍是共同约束；观察独立封闭复现、真实默认安全和能力/容量是否同时满足。
