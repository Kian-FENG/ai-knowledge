---
id: source-amd-helion-20261012
title: AMD展示Helion Agent执行机架蓝图，计划11月提供配置
type: source
domain:
- hardware
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-12'
updated: '2026-10-12'
summary: AMD于10月12日09:00美东公告基于OCP规范的Helion机架蓝图：CPU配置面向工具执行/编排并连接外部模型推理，混合配置结合EPYC与MI350P用于一体部署。
evidence_kind: reported
verification: source-checked
sources:
- https://ir.amd.com/news-events/press-releases/detail/1301/introducing-amd-helion-agentic-ai-compute-at-rack-scale
related: []
aliases: []
source: raw/2026-10-13/c705a53f53eb32460994769924ae3d8f90de32acd2328261c8ef256bb71e2d97.body
url: https://ir.amd.com/news-events/press-releases/detail/1301/introducing-amd-helion-agentic-ai-compute-at-rack-scale
published_at: '2026-10-12T09:00:00-04:00'
source_category: official
raw_path: raw/2026-10-13/c705a53f53eb32460994769924ae3d8f90de32acd2328261c8ef256bb71e2d97.body
sha256: c705a53f53eb32460994769924ae3d8f90de32acd2328261c8ef256bb71e2d97
fetched_at: '2026-10-13T01:09:49.557402+00:00'
last_verified: '2026-10-12'
verification_note: 已阅读所标范围并核对有限陈述支持关系；source-checked不表示融资审计、模型独立评测或部署复现。官方主文CPU-only/hybrid配置、32768cores、token
  router、OCP计划与availability November；前瞻风险段。
reading_scope: 官方主文CPU-only/hybrid配置、32768cores、token router、OCP计划与availability November；前瞻风险段。
evidence:
- source: raw/2026-10-13/c705a53f53eb32460994769924ae3d8f90de32acd2328261c8ef256bb71e2d97.body
  locator: 官方主文CPU-only/hybrid配置、32768cores、token router、OCP计划与availability November；前瞻风险段。
  version: sha256:c705a53f53eb32460994769924ae3d8f90de32acd2328261c8ef256bb71e2d97
date_precision: timestamp
date_basis: published
reviewed_by: Codex
reviewed_at: '2026-10-13'
reviewed_content_sha256: c2013561a1c3705f9f125657b546ef43a01433f9cb73bd2e9cbfa82416415794
---

# AMD展示Helion Agent执行机架蓝图，计划11月提供配置

## Key Takeaways

AMD于10月12日09:00美东公告基于OCP规范的Helion机架蓝图：CPU配置面向工具执行/编排并连接外部模型推理，混合配置结合EPYC与MI350P用于一体部署。

CPU配置最高32768个第六代EPYC核心，并支持风冷/液冷和token router。公司计划向OCP贡献规范，配置仍在开发，计划2026年11月可用；不能说已贡献通过、今天正式发货或有生产客户。

增量是将Agent执行层与模型推理层分别组织。核心数不是GPU推理能力或已测系统吞吐，未取得独立任务基准/部署成本。

## Detailed Notes

官方主文CPU-only/hybrid配置、32768cores、token router、OCP计划与availability November；前瞻风险段。

## Evidence

[原始来源](https://ir.amd.com/news-events/press-releases/detail/1301/introducing-amd-helion-agentic-ai-compute-at-rack-scale)。原始路径、hash、采集时间及版本见元数据；有限摘录/摘要范围与缺失条件不被自动发布改变。

## Questions Raised

判断（derived）：工具和沙箱执行扩张可能产生独立CPU机架需求，AMD及执行平台受益，同时与模型GPU集群形成互补。若任务主要受推理或外部工具等待约束，大CPU配置会低利用率；观察CPU时间占比、并发隔离、实际11月交付和每任务完整成本。
