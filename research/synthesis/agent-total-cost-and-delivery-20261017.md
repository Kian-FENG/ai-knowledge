---
id: note-agent-total-cost-and-delivery-20261017
title: Agent总成本由模型、检索、部署与审阅共同决定
type: note
domain:
- industry
- infra
lifecycle: published
tags: []
created: '2026-10-18'
updated: '2026-10-18'
summary: DeepSeek单价不变而优化任务长度，检索另计成功调用；Beam权重交付、默认分发和人类审阅共同影响真实采用。这是有限来源综合推导。
evidence_kind: derived
verification: source-checked
sources:
- source-deepseek-search-fetch-20261017
- source-replit-default-openai-20261017
- source-deepseek-v41-flash-1017
- source-rtx-spark-retail-20261017
- source-chatgpt-slides-pro-20261016
- source-reflection-beam-release-20261016
- source-anthropic-employment-20261016
- source-pilotdeck20-20261015
- source-vllm-beam-day0-20261016
- source-humxn-home-service-data-20261006
related:
- source-deepseek-search-fetch-20261017
- source-replit-default-openai-20261017
- source-deepseek-v41-flash-1017
- source-rtx-spark-retail-20261017
- source-chatgpt-slides-pro-20261016
- source-reflection-beam-release-20261016
- source-anthropic-employment-20261016
- source-pilotdeck20-20261015
- source-vllm-beam-day0-20261016
- source-humxn-home-service-data-20261006
- entity-humxn
- entity-reflection
aliases: []
last_verified: '2026-10-18'
verification_note: 已读各来源页记录的有限原文范围并核对支持链；不把不同任务、设备、harness或收入口径并为统一实测。
evidence:
- source: source-deepseek-search-fetch-20261017
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-replit-default-openai-20261017
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-deepseek-v41-flash-1017
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-rtx-spark-retail-20261017
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-chatgpt-slides-pro-20261016
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-reflection-beam-release-20261016
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-anthropic-employment-20261016
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-pilotdeck20-20261015
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-vllm-beam-day0-20261016
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
- source: source-humxn-home-service-data-20261006
  locator: 该来源页Key Takeaways及所列阅读/限制
  version: 2026-10-18入库版本
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: f842220c1de9ec0e3b8c8a24fb1a81f67daec670d000c6856269633d94190a23
---

# Agent总成本由模型、检索、部署与审阅共同决定

## What Is New

DeepSeek单价不变而优化任务长度，检索另计成功调用；Beam权重交付、默认分发和人类审阅共同影响真实采用。这是有限来源综合推导。

## Synthesis

模型token标价只是成本的一层。DeepSeek1017强调较短输出与任务时间，Search/Fetch又新增工具账单；Replit的默认伙伴选择同时权衡表现、商务与成本。开放权重交付增加替代路径，但需要承受权重驻留、缓存、依赖和服务治理。

vLLM Beam的total token包含缓存输入，不能当纯输出速度；Anthropic组织内研究提示审阅注意力可能先成为瓶颈。PilotDeck的可编辑记忆和路由解决管理问题，但小样本成本表不能外推。Slides把成果置于共享交付物，RTX Spark扩展本地部署，HUMXN则提示物理任务数据获取本身需要支付成本。

反例：固定API在特定任务更便宜、廉价路由带来更多重试、长上下文缓存收益无法迁移到短会话、组织内就业变化受增长和选择偏差影响。这里不推断各公司的普遍能力排名或行业就业因果。

## Evidence

[[reference/sources/deepseek-search-fetch-20261017|DeepSeek开放Search与Fetch，工具调用开始独立按成功请求计费]]

[[reference/sources/replit-default-openai-20261017|Replit澄清OpenAI成为默认伙伴，Claude仍可选]]

[[reference/sources/deepseek-v41-flash-1017|DeepSeek V4.1 Flash 1017更新权重与API，单价维持不变]]

[[reference/sources/rtx-spark-retail-20261017|NVIDIA确认RTX Spark笔记本现售，起价USD2399]]

[[reference/sources/chatgpt-slides-pro-20261016|chatgpt-slides-pro-20261016]]

[[reference/sources/reflection-beam-release-20261016|Reflection Beam从预览转为权重与托管API交付]]

[[reference/sources/anthropic-employment-20261016|Anthropic内部研究：初级技术招聘占比下降，注意力成为约束]]

[[reference/sources/pilotdeck20-20261015|PilotDeck2.0以工作区、可编辑记忆和路由承接持续任务]]

[[reference/sources/vllm-beam-day0-20261016|vLLM给出Beam部署与AgentX口径，缓存吞吐不能等同输出吞吐]]

[[reference/sources/humxn-home-service-data-20261006|humxn-home-service-data-20261006]]

[[reference/entities/humxn|新增跟踪HUMXN：背景与身份边界]]

[[reference/entities/reflection|Reflection时间线更新]]

## Watchpoints

固定任务与预算，记录成功率、模型/检索/重试总账单、端到端时延、审阅负担和实际交付；下一周核对工具优惠到期与权重服务可用性。
