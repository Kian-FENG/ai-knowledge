---
id: source-deepinfer-open-code-20261020
title: DeepSeek公开DeepInfer代码，离线引擎与完整在线服务仍有明确边界
type: source
domain:
- infra
- models
lifecycle: published
tags: []
created: '2026-10-21'
updated: '2026-10-21'
summary: 核对DeepInfer截止窗口内提交774ce244（10月20日11:03:13 UTC）的README：支持DeepSeek-V4.1-Flash，默认检查点Flash-1017；列NVIDIA
  SM100与华为Ascend 950、异步调度、推测解码、结构化输出及Apache-2.0许可。
evidence_kind: reported
verification: source-checked
sources:
- https://github.com/deepseek-ai/DeepInfer/blob/774ce244b87cc0eb8d4b94ab9f5de2ab22049f01/README.md
related: []
aliases: []
source: raw/2026-10-22/ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c.body
url: https://github.com/deepseek-ai/DeepInfer/blob/774ce244b87cc0eb8d4b94ab9f5de2ab22049f01/README.md
published_at: null
source_category: official
raw_path: raw/2026-10-22/ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c.body
sha256: ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c
fetched_at: '2026-10-21T22:09:59.111590+00:00'
reading_scope: 固定774ce244 README全文与GitHub commits API已读；未逐算子、性能图像素、eval harness或完整LICENSE文本审计，未部署复测。
last_verified: '2026-10-21'
verification_note: Agent实际阅读所列范围并核对结论支持关系；公司和作者披露为reported，无独立复现；发布审核不提高核验等级。
evidence:
- source: raw/2026-10-22/ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c.body
  locator: 固定774ce244 README全文与GitHub commits API已读；未逐算子、性能图像素、eval harness或完整LICENSE文本审计，未部署复测。
  version: sha256:ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c
source_updated_at: '2026-10-20T11:03:13+00:00'
date_precision: timestamp
reviewed_by: Codex
reviewed_at: '2026-10-22'
reviewed_content_sha256: 83c4f3fa9c78bc26d260a7b883cd75bcae98ba0bcffe2495f67496f7c8f403e9
---

# DeepSeek公开DeepInfer代码，离线引擎与完整在线服务仍有明确边界

## Key Takeaways

核对DeepInfer截止窗口内提交774ce244（10月20日11:03:13 UTC）的README：支持DeepSeek-V4.1-Flash，默认检查点Flash-1017；列NVIDIA SM100与华为Ascend 950、异步调度、推测解码、结构化输出及Apache-2.0许可。

## Detailed Notes

DeepSeek称其框架用于自身生产服务，但本次公开版提供离线推理；完整服务仍缺KV缓存系统、VE/Prefill/Decode分离配套和DP副本间负载均衡。增量是模型团队公开引擎代码，不能等同通用API服务可直接替换。

提交史最早条目为10月20日04:09:42 UTC；代码提交时间不等于精确公开时刻。当前main含21日更新，本条固定截止内版本。厂商曲线只见4卡prefill/64卡decode SM100说明，精度/负载/基线未完整核对，不转载性能或收益排名。

## Evidence

[原始来源](https://github.com/deepseek-ai/DeepInfer/blob/774ce244b87cc0eb8d4b94ab9f5de2ab22049f01/README.md)；`raw/2026-10-22/ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c.body`，hash `ba5a6e5232fb6d75e13709ee233fa00e09a68a2138ad65973fef8e485f3aba3c`。

固定774ce244 README全文与GitHub commits API已读；未逐算子、性能图像素、eval harness或完整LICENSE文本审计，未部署复测。

## Questions Raised

判断：专用模型与引擎共同开放可降低架构复用成本，并给CUDA与昇腾生态提供共同参考；实际部署优势仍受外部服务组件和运维投入约束。反例是模型或硬件适配范围过窄。观察完整服务配套、跨框架正确性、可复现端到端成本。
