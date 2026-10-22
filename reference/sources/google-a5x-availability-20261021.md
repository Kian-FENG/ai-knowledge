---
id: source-google-a5x-availability-20261021
title: Google Cloud公布A5X扩展，正文明确Rubin实例下月才正式可用
type: source
domain:
- hardware
- infra
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: Google Cloud与NVIDIA于10月21日介绍基于Vera Rubin NVL72的A5X、Virgo网络和分层KV缓存。NVIDIA标题使用“宣布正式可用”，但两方正文均限定实例GA在下月；本报告按正文保留为计划，不能写成本期全面开放。
evidence_kind: reported
verification: source-checked
sources:
- https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026/
- https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/
related: []
aliases: []
source: raw/2026-10-23/7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d.body
url: https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026/
published_at: '2026-10-21T11:30:00+00:00'
source_category: official
last_verified: '2026-10-22'
verification_note: Agent实际阅读所列来源范围并核对支持关系；公司/作者披露保留reported，未独立实测。审核发布不等于独立核验。
raw_path: raw/2026-10-23/7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d.body
sha256: 7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d
fetched_at: '2026-10-22T22:10:36.687298+00:00'
reading_scope: Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。
evidence:
- source: raw/2026-10-23/7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d.body
  locator: Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。
  version: sha256:7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d
- source: raw/2026-10-23/38ffcb4bfef01cb6b4e58f90e3d1089f96933d86becfad1943a682e13286260c.body
  locator: Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。
  version: sha256:38ffcb4bfef01cb6b4e58f90e3d1089f96933d86becfad1943a682e13286260c
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: 6e3f02b9f27a6ab51a8ed05f0eb022175f1d233888640c296aa1f53548e663b6
---

# Google Cloud公布A5X扩展，正文明确Rubin实例下月才正式可用

## Key Takeaways

Google Cloud与NVIDIA于10月21日介绍基于Vera Rubin NVL72的A5X、Virgo网络和分层KV缓存。NVIDIA标题使用“宣布正式可用”，但两方正文均限定实例GA在下月；本报告按正文保留为计划，不能写成本期全面开放。

## Detailed Notes

单站80,000、多站最高960,000 Rubin GPU是拟支持的扩展规模，不是已安装、已售或可预订配额。NVIDIA披露Ineffable已先行访问，属于客户案例；与同文中Confidential G4及GDC B300各自GA的状态不能混用。未核A5X实际区域、价目、配额与集群规模。

## Evidence

[原始来源](https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026/)；`raw/2026-10-23/7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d.body`，SHA-256 `7d386a247cf511655ef59c29e0ce692a4113054b35862085d61b33a2f04ac95d`。

[原始来源](https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/)；`raw/2026-10-23/38ffcb4bfef01cb6b4e58f90e3d1089f96933d86becfad1943a682e13286260c.body`，SHA-256 `38ffcb4bfef01cb6b4e58f90e3d1089f96933d86becfad1943a682e13286260c`。

Google官方GTC主文与NVIDIA合作全文已读并对照标题/正文；未实测控制台、读完整实例规格/价目或核验客户规模。

## Questions Raised

判断：平台把训练、体验生成和长期Agent上下文放入统一系统，可让网络、存储与治理成为GPU之外的差异。反例是规模计划被设施和采购限制拖延。观察下月可用范围、承诺配额、固定负载SLO和全栈账单。
