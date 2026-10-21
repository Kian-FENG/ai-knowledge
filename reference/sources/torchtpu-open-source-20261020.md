---
id: source-torchtpu-open-source-20261020
title: TorchTPU开放原生PyTorch后端，vLLM插件明确区分推荐与实验硬件
type: source
domain:
- infra
- ecosystem
lifecycle: published
tags: []
created: '2026-10-21'
updated: '2026-10-21'
summary: Google 10月20日宣布TorchTPU已在GitHub开放，与Meta/PyTorch合作支持eager、torch.compile及分布式接口，并对接vLLM、SGLang和训练生态；这是后端与集成发布，不是新TPU芯片发布。
evidence_kind: reported
verification: source-checked
sources:
- https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus/
- https://vllm.ai/blog/2026-10-20-vllm-torchtpu
related: []
aliases: []
source: raw/2026-10-22/0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f.body
url: https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus/
published_at: '2026-10-20T11:30:00+00:00'
source_category: official
raw_path: raw/2026-10-22/0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f.body
sha256: 0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f
fetched_at: '2026-10-21T22:09:59.309135+00:00'
reading_scope: Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。
last_verified: '2026-10-21'
verification_note: Agent实际阅读所列范围并核对结论支持关系；公司和作者披露为reported，无独立复现；发布审核不提高核验等级。
evidence:
- source: raw/2026-10-22/0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f.body
  locator: Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。
  version: sha256:0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f
- source: raw/2026-10-22/72114dffded95c1c0f04248fd9849fa17033a69d761d7bb810edc9515e7c59ff.body
  locator: Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。
  version: sha256:72114dffded95c1c0f04248fd9849fa17033a69d761d7bb810edc9515e7c59ff
date_precision: timestamp
reviewed_by: Codex
reviewed_at: '2026-10-22'
reviewed_content_sha256: b8f7bde993f9fb5b50a77abe3af041ab97de93ce7e386480838f2c7655b0199e
---

# TorchTPU开放原生PyTorch后端，vLLM插件明确区分推荐与实验硬件

## Key Takeaways

Google 10月20日宣布TorchTPU已在GitHub开放，与Meta/PyTorch合作支持eager、torch.compile及分布式接口，并对接vLLM、SGLang和训练生态；这是后端与集成发布，不是新TPU芯片发布。

## Detailed Notes

Inferact/Google同日发布out-of-tree vllm-torchtpu插件，复用上游调度、KV管理与API，提供Pallas算子、主机KV卸载和分离服务；推荐v7x，v6e/v5e/v5p标实验。首次shape编译需时间，未来24小时新模型CI、部分路由与diffusion路径仍在路线图。

相对先前合作宣布，增量是开源后端和可安装插件；Google称“minimal code changes”，不意味着迁移后自动获得峰值性能。PyTorch文章采集版带21日更新，本条以20日Google与vLLM正文为事实依据，未纳其后更新；不作跨芯片跑分比较。

## Evidence

[原始来源](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus/)；`raw/2026-10-22/0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f.body`，hash `0c11f07ef175061317673af34d9f8e575c9743e7d3cb2d8caf426be6f7dab36f`。

[原始来源](https://vllm.ai/blog/2026-10-20-vllm-torchtpu)；`raw/2026-10-22/72114dffded95c1c0f04248fd9849fa17033a69d761d7bb810edc9515e7c59ff.body`，hash `72114dffded95c1c0f04248fd9849fa17033a69d761d7bb810edc9515e7c59ff`。

Google 20日主文与vLLM文章全文已读；PyTorch引言用于旁证；未审全部仓库/依赖许可、运行支持矩阵或数字基准。vLLM为日精度，边界不确定。

## Questions Raised

判断：共用框架/API可降低TPU试用和模型迁移的固定成本，云客户获得更多议价与部署选择；但形状、分片、编译和容量仍约束实际替代。反例是特定模型移植后SLO或成本恶化。观察真实迁移工时、验证矩阵、冷启动及固定负载账单。
