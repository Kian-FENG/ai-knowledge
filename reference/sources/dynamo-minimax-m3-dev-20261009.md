---
id: source-dynamo-minimax-m3-dev-20261009
title: Dynamo MiniMax-M3 实验快照提供固定部署组合
type: source
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-10'
updated: '2026-10-10'
summary: v1.6.0-minimax-m3-dev.1正文明确实验性、未经QA、不适合生产；尽管GitHub prerelease字段为false，不能据此写成生产正式版。最新release说明更新在10月10日00:03:10Z，属于本洛杉矶窗口。
evidence_kind: reported
verification: source-checked
sources:
- https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-minimax-m3-dev.1
related: []
aliases: []
source: raw/2026-10-10/e150139a09f0172d39526e4a73e3a2482d1d8ae7a72db1ea518ed7027b91693c.body
url: https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-minimax-m3-dev.1
published_at: '2026-10-09T20:54:29+00:00'
source_category: official
raw_path: raw/2026-10-10/e150139a09f0172d39526e4a73e3a2482d1d8ae7a72db1ea518ed7027b91693c.body
sha256: e150139a09f0172d39526e4a73e3a2482d1d8ae7a72db1ea518ed7027b91693c
fetched_at: '2026-10-10T01:14:10.897736+00:00'
last_verified: '2026-10-10'
verification_note: 已核对本页有限陈述与实际读取的来源；已读完整release正文及Known issues/NOT PRODUCTION标注；固定模型revision和release
  branch 1cf43bce3fc865a14dcd8f9bb857f6b726617ed0；未部署；API prerelease与正文语义不同以正文为准。
  非独立复现。
reading_scope: 已读完整release正文及Known issues/NOT PRODUCTION标注；固定模型revision和release branch
  1cf43bce3fc865a14dcd8f9bb857f6b726617ed0；未部署；API prerelease与正文语义不同以正文为准。
evidence:
- source: raw/2026-10-10/e150139a09f0172d39526e4a73e3a2482d1d8ae7a72db1ea518ed7027b91693c.body
  locator: 已读完整release正文及Known issues/NOT PRODUCTION标注；固定模型revision和release branch
    1cf43bce3fc865a14dcd8f9bb857f6b726617ed0；未部署；API prerelease与正文语义不同以正文为准。
  version: sha256:e150139a09f0172d39526e4a73e3a2482d1d8ae7a72db1ea518ed7027b91693c
- source: raw/2026-10-10/c8fabb906fb699581b6840c490695a767a28a5a4b2bd39612447798a0cd23b66.json
  locator: 官方API的时间、版本/tag/revision字段；https://api.github.com/repos/ai-dynamo/dynamo/releases/tags/v1.6.0-minimax-m3-dev.1
  version: sha256:c8fabb906fb699581b6840c490695a767a28a5a4b2bd39612447798a0cd23b66
date_precision: timestamp
date_basis: updated
updated_at: '2026-10-10T00:03:10+00:00'
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: d6f978c44605859e58d813875a4bf5d630755cd8157c20aac0f49cafb4b440d7
---

# Dynamo MiniMax-M3 实验快照提供固定部署组合

## Key Takeaways

v1.6.0-minimax-m3-dev.1正文明确实验性、未经QA、不适合生产；尽管GitHub prerelease字段为false，不能据此写成生产正式版。最新release说明更新在10月10日00:03:10Z，属于本洛杉矶窗口。

相对昨日Kimi快照，本期目标是MiniMax-M3-NVFP4/EAGLE3组合，固定vLLM nightly 8a728663c1c3、CUDA13、NIXL1.3.2，排除vLLM-Omni；GB200 TP4/FP8 KV部署分别需聚合12 GPU或分离24 GPU。

示例区分真实EAGLE3和绕过验证的synthetic acceptance；后者不代表模型推理表现。仅核对部署说明，不据此确定MiniMax模型独立发布日期或性能排名。

## Detailed Notes

已读完整release正文及Known issues/NOT PRODUCTION标注；固定模型revision和release branch 1cf43bce3fc865a14dcd8f9bb857f6b726617ed0；未部署；API prerelease与正文语义不同以正文为准。

## Evidence

[原始来源](https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-minimax-m3-dev.1)。原始路径、hash、采集时间与日期口径见元数据。source-checked仅表示所写披露有出处支持，非真实性独立审计。

## Questions Raised

判断（derived）：快照将模型权重、引擎和互连约束打包，可缩短适配探索，但GB200规模和版本锁定提高资源门槛。观察进入稳定版的条件、真实验收率和生产故障；小集群不一定获得同样收益。
