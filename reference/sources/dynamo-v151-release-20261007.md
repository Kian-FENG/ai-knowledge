---
id: source-dynamo-v151-release-20261007
title: Dynamo v1.5.1 正式补丁：修复路由恢复并收紧多模态输入边界
type: source
domain:
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-08'
updated: '2026-10-08'
summary: 正式release v1.5.1（tag关联commit2093662）修复路由请求过期后空闲worker恢复、SGLang min_tokens及Qwen3-VL视频契约等问题；不是提案或候选版。官方Atom更新时间2026-10-07T01:54:13Z用于窗口，页面显示10月7日；不把更新时间当精确首次发布时间。
evidence_kind: reported
verification: source-checked
sources:
- https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.1
related: []
aliases: []
source: raw/2026-10-08/c9ff2e00d6525c3b5bdc4a0d317975b78ef3bc0a74e4f851265622c45670495d.body
url: https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.1
published_at: '2026-10-07'
source_category: official
raw_path: raw/2026-10-08/c9ff2e00d6525c3b5bdc4a0d317975b78ef3bc0a74e4f851265622c45670495d.body
sha256: c9ff2e00d6525c3b5bdc4a0d317975b78ef3bc0a74e4f851265622c45670495d
fetched_at: '2026-10-08T01:04:58.162592+00:00'
last_verified: '2026-10-08'
verification_note: 已阅读并核对所列有限陈述与原始来源的支持关系；官方release v1.5.1全部正文：Bug fixes / Security
  / Breaking Changes / Known Issues / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。；未独立复现。
reading_scope: 官方release v1.5.1全部正文：Bug fixes / Security / Breaking Changes / Known
  Issues / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。
evidence:
- source: raw/2026-10-08/c9ff2e00d6525c3b5bdc4a0d317975b78ef3bc0a74e4f851265622c45670495d.body
  locator: 官方release v1.5.1全部正文：Bug fixes / Security / Breaking Changes / Known Issues
    / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。
  version: sha256:c9ff2e00d6525c3b5bdc4a0d317975b78ef3bc0a74e4f851265622c45670495d
source_updated_at: '2026-10-07T01:54:13+00:00'
date_precision: date-only
version: v1.5.1 / commit2093662
reviewed_by: Codex
reviewed_at: '2026-10-08'
reviewed_content_sha256: 1e893f0bf90c62461aa6be978f8f1cbd94e8eecc26dc046c76e7bc5edc87326e
---

# Dynamo v1.5.1 正式补丁：修复路由恢复并收紧多模态输入边界

## Key Takeaways

正式release v1.5.1（tag关联commit2093662）修复路由请求过期后空闲worker恢复、SGLang min_tokens及Qwen3-VL视频契约等问题；不是提案或候选版。官方Atom更新时间2026-10-07T01:54:13Z用于窗口，页面显示10月7日；不把更新时间当精确首次发布时间。

多模态输入新增大小/尺寸边界和地址固定；环境代理仅DYN_MM_TRUST_EGRESS_PROXY=1时信任，本地路径需DYN_MM_LOCAL_PATH配置，属于兼容性变化。捆绑SGLang0.5.18、vLLM0.28.0等后端，不等于跟随所有上游最新版本。

已知问题仍包括SGLang sidecar协议错配HTTP500与部分H264解码后续崩溃；计划1.6修复不能写成当前已修。相对已有vLLM0.31发布，本期新增编排层稳定性与输入契约，无性能排名。

## Detailed Notes

官方release v1.5.1全部正文：Bug fixes / Security / Breaking Changes / Known Issues / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。

## Evidence

[原始来源](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.1)。定位与阅读范围：官方release v1.5.1全部正文：Bug fixes / Security / Breaking Changes / Known Issues / backend versions；Atom updated时刻；未运行服务、复现性能或读取每个关联PR。 原始路径、hash、采集/事件时间见元数据；source-checked只表示所列陈述支持关系已核对，非独立结果验证。

## Questions Raised

判断（derived）：更明确的恢复和输入边界有助于减少服务中断，但环境配置变化会增加升级验证负担，运维和集成环节受益。已知sidecar/解码问题仍可能阻碍部署；观察错误率、恢复时间、配置迁移和兼容后端范围。
