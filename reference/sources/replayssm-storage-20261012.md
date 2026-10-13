---
id: source-replayssm-storage-20261012
title: NVIDIA详解ReplaySSM：减少混合模型状态写入，收益取决于批量
type: source
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-12'
updated: '2026-10-12'
summary: 10月12日新技术文章解释ReplaySSM的检查点+近期输入缓冲方案，将输出计算与状态写回分离，每L=16步刷新，面向SSM/混合模型解码。报道解释既有方法及集成，不把全部算法或集成的首次发布日标成今天。
evidence_kind: reported
verification: source-checked
sources:
- https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/
related: []
aliases: []
source: raw/2026-10-13/20d467f881f475653418f6d67cfda9687756154ef26d9fd683241f2304f073f6.body
url: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/
published_at: '2026-10-12T16:00:54+00:00'
source_category: official
raw_path: raw/2026-10-13/20d467f881f475653418f6d67cfda9687756154ef26d9fd683241f2304f073f6.body
sha256: 20d467f881f475653418f6d67cfda9687756154ef26d9fd683241f2304f073f6
fetched_at: '2026-10-13T01:09:49.753691+00:00'
last_verified: '2026-10-12'
verification_note: 已阅读所标范围并核对有限陈述支持关系；source-checked不表示融资审计、模型独立评测或部署复现。官方主文存储/flush机制；Table1模型/硬件；batch1/256图说明；量化表例外；集成PR引用。图像像素/代码与部署未复核。
reading_scope: 官方主文存储/flush机制；Table1模型/硬件；batch1/256图说明；量化表例外；集成PR引用。图像像素/代码与部署未复核。
evidence:
- source: raw/2026-10-13/20d467f881f475653418f6d67cfda9687756154ef26d9fd683241f2304f073f6.body
  locator: 官方主文存储/flush机制；Table1模型/硬件；batch1/256图说明；量化表例外；集成PR引用。图像像素/代码与部署未复核。
  version: sha256:20d467f881f475653418f6d67cfda9687756154ef26d9fd683241f2304f073f6
date_precision: timestamp
date_basis: published
reviewed_by: Codex
reviewed_at: '2026-10-13'
reviewed_content_sha256: 8ce1aa88b691a7d9107d8dba803ed689df960eddb8ef7804582ac3699195eb73
---

# NVIDIA详解ReplaySSM：减少混合模型状态写入，收益取决于批量

## Key Takeaways

10月12日新技术文章解释ReplaySSM的检查点+近期输入缓冲方案，将输出计算与状态写回分离，每L=16步刷新，面向SSM/混合模型解码。报道解释既有方法及集成，不把全部算法或集成的首次发布日标成今天。

文中4款模型单GPU、TP=1实验：小模型BF16/H100，大模型NVFP4/B300，状态FP32、L=16；batch256的decode-step为1.20–1.47倍，batch1无收益。基线为vLLM kernel；精确软件提交和统一输入输出长度未明确，不能推导通用端到端降本。

量化另测FP16/FP8与随机舍入，小模型出现明显精度损失例外。文中列出TRT-LLM/vLLM/SGLang/FlashInfer相关PR和Kimi使用相关输入缓存的说法；未逐项审核PR、正式release或实际生产部署。

## Detailed Notes

具体模型为Nemotron-3-Nano-4B、Nemotron-3-Super-120B-A12B、Qwen3.5-4B、Qwen3.5-122B-A10B；分别使用BF16/H100或NVFP4/B300，单GPU无tensor parallelism。

官方主文存储/flush机制；Table1模型/硬件；batch1/256图说明；量化表例外；集成PR引用。图像像素/代码与部署未复核。

## Evidence

[原始来源](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)。原始路径、hash、采集时间及版本见元数据；有限摘录/摘要范围与缺失条件不被自动发布改变。

## Questions Raised

判断（derived）：高并发状态带宽瓶颈下，重算少量递推换取少写内存可能提升混合模型服务吞吐，推理引擎受益；低batch、计算瓶颈或精度损失会消除收益。观察真实流量分布、尾延迟、显存峰值、精度和对应稳定版本，不直接把kernel倍数当成本降幅。
