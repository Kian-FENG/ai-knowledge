---
id: entity-reflection
title: Reflection：Beam 模型的开发者
type: entity
domain:
- companies
- models
lifecycle: published
tags:
- moe
- open-weights
created: '2026-10-06'
updated: '2026-10-18'
summary: Reflection开发Beam；10月5日预览后，10月16日正式交付Apache2.0权重与API生态，实际采用和性能仍须独立核查。
evidence_kind: reported
verification: source-checked
sources:
- source-reflection-beam-preview-20261005
- source-reflection-beam-release-20261016
related:
- source-reflection-beam-preview-20261005
- note-agent-execution-stack-20261005
- source-reflection-beam-release-20261016
aliases:
- Reflection AI
entity_kind: company
last_verified: '2026-10-18'
verification_note: 本次核对10月16日权重/第一方API与模型身份；旧10月5日预览保留历史范围，不视为本轮重新验证全部评测。
evidence:
- source: raw/2026-10-06/151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba.txt
  locator: 模型结构与 inference compute 解释；The Path Ahead。
  version: sha256:151d4158fa2f083aaac2e010074cb2f216862f55bca944f8533865a0934c3bba
- source: source-reflection-beam-release-20261016
  locator: 10月16日交付公告与HF模型概览/Apache2.0标识
  version: 2026-10-18归档版本
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: 72c79e15e2a941c03eb377de11b0b316c4ab6673a37e28529574d7b3bf5bbcfe
---

# Reflection：Beam 模型的开发者

## Identity and Scope

官方域名 reflection.ai 的 Reflection 自述开发 Beam；本文不从模型品牌推断独立公司，也不采用媒体融资估值。

## Products and Capabilities

Beam：文本MoE模型，501B总参数/23B激活参数为公司披露；10月5日为有限预览；10月16日已公布权重与第一方API，BF16/FP8/NVFP4等格式。

## Development Timeline

2026-10-05 官网预览Beam；承诺本月后续发布权重与Apache2.0许可。计划与已发生状态分开记录。

2026-10-16官方兑现权重交付，HF可见Apache2.0；1M上下文、文本输入输出。[[reference/sources/reflection-beam-release-20261016|交付状态与证据边界]]。

## Evidence

[[reference/sources/reflection-beam-preview-20261005|官方来源页]]；已读范围、raw版本和日期精度见来源页。

## Open Questions

判断（derived）：若权重与部署材料按计划交付，企业自部署和托管 MaaS 会多一个模型选择，开源工具链可能受益。反例是大 MoE 总权重仍带来显存、分发和预填充成本，激活参数少不等于整机成本低。观察真正发布的权重/许可、完整评测预算，以及同硬件和负载下的服务质量与成本。

日期仅到2026-10-05、时区未知，边界不确定，前期无重复；已读官网文本，未读完整技术报告、模型卡或评测harness。不把open-weight标题当作当前权重可下载。
