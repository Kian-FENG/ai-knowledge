---
id: source-reflection-beam-preview-20261005
title: Reflection 预览 Beam：501B MoE，权重与 Apache 2.0 许可仍待本月发布
type: source
domain:
- models
- companies
lifecycle: published
tags:
- moe
- open-weights
created: '2026-10-06'
updated: '2026-10-06'
summary: Reflection 公布 Beam 文本模型预览，披露 MoE 总参数 501B、激活参数 23B；当前向少数早期用户开放并提供等待名单，权重、技术文档和
  Apache 2.0 发布是本月后续计划。
evidence_kind: reported
verification: source-checked
sources:
- https://reflection.ai/blog/introducing-beam
related:
- entity-reflection
aliases: []
source: raw/2026-10-06/151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba.txt
url: https://reflection.ai/blog/introducing-beam
published_at: '2026-10-05'
source_category: official
last_verified: '2026-10-06'
raw_path: raw/2026-10-06/151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba.txt
sha256: 151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba
fetched_at: '2026-10-06T01:14:55.575351+00:00'
reading_scope: 搜索工具返回的官方文章正文：已读模型结构、训练与Path Ahead；未审阅图像、完整技术报告或评测harness。日期只有日，时区未知。
verification_note: 已阅读并核对声明范围与出处：模型结构与 inference compute 解释；The Path Ahead。；日期仅到2026-10-05、时区未知，边界不确定，前期无重复；已读官网文本，未读完整技术报告、模型卡或评测harness。不把open-weight标题当作当前权重可下载。
evidence:
- source: raw/2026-10-06/151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba.txt
  locator: 模型结构与 inference compute 解释；The Path Ahead。
  version: sha256:151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba
date_precision: date-only
date_timezone: unknown
reviewed_by: Codex
reviewed_at: '2026-10-06'
reviewed_content_sha256: fe7cdd328516d2f3ac31b2fdb2f837f13332249eee10e267aee87451e23ae192
---

# Reflection 预览 Beam：501B MoE，权重与 Apache 2.0 许可仍待本月发布

## Key Takeaways

Reflection 公布 Beam 文本模型预览，披露 MoE 总参数 501B、激活参数 23B；当前向少数早期用户开放并提供等待名单，权重、技术文档和 Apache 2.0 发布是本月后续计划。

相对已有模型跟踪新增 Reflection/Beam；官网的推理计算优势按近似 FLOPs 口径估算，排除部分上下文与服务开销，不能直接换算实际价格、延迟或跨模型排名。

## Detailed Notes

日期仅到2026-10-05、时区未知，边界不确定，前期无重复；已读官网文本，未读完整技术报告、模型卡或评测harness。不把open-weight标题当作当前权重可下载。

## Evidence

搜索工具返回的官方文章正文：已读模型结构、训练与Path Ahead；未审阅图像、完整技术报告或评测harness。日期只有日，时区未知。

[原始来源](https://reflection.ai/blog/introducing-beam)；定位、版本hash、采集时间及raw路径见元数据。公司/维护者披露为reported，source-checked仅代表已核对来源支持。

## Questions Raised

判断（derived）：若权重与部署材料按计划交付，企业自部署和托管 MaaS 会多一个模型选择，开源工具链可能受益。反例是大 MoE 总权重仍带来显存、分发和预填充成本，激活参数少不等于整机成本低。观察真正发布的权重/许可、完整评测预算，以及同硬件和负载下的服务质量与成本。
