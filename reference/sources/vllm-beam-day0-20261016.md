---
id: source-vllm-beam-day0-20261016
title: vLLM给出Beam部署与AgentX口径，缓存吞吐不能等同输出吞吐
type: source
domain:
- infra
lifecycle: published
tags: []
created: '2026-10-18'
updated: '2026-10-18'
summary: 10月16日Inferact、Reflection、NVIDIA联合文章提供Beam专用容器与推理、工具调用及结构化输出支持；是部署集成与优化文章，不等于通用vLLM稳定版全部配置已验证。
evidence_kind: reported
verification: source-checked
sources:
- https://vllm.ai/blog/2026-10-16-reflection-beam
related: []
aliases: []
source: https://vllm.ai/blog/2026-10-16-reflection-beam
url: https://vllm.ai/blog/2026-10-16-reflection-beam
published_at: '2026-10-16T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-18/d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1.body
sha256: d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1
fetched_at: '2026-10-18T10:01:04.248832+00:00'
last_verified: '2026-10-18'
verification_note: Getting started、AgentX benchmark及DFlash2负载说明；正文和文本表已读，未审代码或独立复现。
  source-checked仅确认上述支持关系；不表示独立验证、测量或复现。
evidence:
- source: raw/2026-10-18/d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1.body
  locator: 官方文章全文；模型与AgentX表格文本，未审代码或重跑
  version: sha256:d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: 32800f5ac5ae40c3c8b7700ebcd1cf0f62dc7ccb59692318a1201da96341a803
---

# vLLM给出Beam部署与AgentX口径，缓存吞吐不能等同输出吞吐

## Key Takeaways

10月16日Inferact、Reflection、NVIDIA联合文章提供Beam专用容器与推理、工具调用及结构化输出支持；是部署集成与优化文章，不等于通用vLLM稳定版全部配置已验证。

AgentX实例为Beam1.0 NVFP4、4×GB300、TP4/EP1、目标与drafter FP8 KV、DFlash2实际接受、block8、temperature1.0、每点20分钟、vLLM8e0922。文中约88K total token/s/GPU含输入、输出和缓存输入，命中率91.4%–95.6%，不可当作纯输出吞吐或成本。

单请求708token/s来自另一TP8、低熵SPEED-Bench throughput_1k配置，不与AgentX混排；本文不复现。相对预览模型，此次增量是可用部署入口与公开负载定义；日期仅到日。

## Detailed Notes

Getting started、AgentX benchmark及DFlash2负载说明；正文和文本表已读，未审代码或独立复现。

原始材料及本期published与显式草稿按对象、URL/hash查重；相同版本不重复建页，相关对象优先更新。

## Evidence

[原始来源](https://vllm.ai/blog/2026-10-16-reflection-beam)；归档 `raw/2026-10-18/d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1.body`；SHA-256 `d44aa5eea4666e1a5351f656e96625e0e1e3e305e9aaeb38f67948835ab6a6a1`；实际采集 2026-10-18T10:01:04.248832+00:00。

## Questions Raised

判断（derived）：公开配置有利服务商复核真实Agent轨迹的缓存收益；高命中轨迹可同时抬高总token计数。反例是短会话或开放聊天降低复用和草稿接受；观察同SLO下goodput、输出时延、内存及每成功任务成本。
