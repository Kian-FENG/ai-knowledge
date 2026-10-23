---
id: source-openai-decisions-and-usage-tiers-20261006
title: OpenAI Decisions API：公开beta、语音委派与正式可用
type: source
domain:
- products
- models
lifecycle: published
tags: []
created: '2026-10-07'
updated: '2026-10-23'
summary: OpenAI于10月22日将GPT-6 Luna支持的Decisions API从公开beta转为正式可用；相对库内10月6日beta和15日语音委派，新增正式供给、缓存与更大请求容量。
evidence_kind: reported
verification: source-checked
sources:
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/decisions
- https://developers.openai.com/api/docs/guides/rate-limits
- https://developers.openai.com/api/docs/guides/decisions-voice
- https://openai.com/index/decisions-api
related: []
aliases: []
source: raw/2026-10-24/32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c.txt
url: https://openai.com/index/decisions-api
published_at: '2026-10-22T19:00:00+00:00'
source_category: official
raw_path: raw/2026-10-24/32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c.txt
fetched_at: '2026-10-23T22:08:47.626645+00:00'
sha256: 32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c
last_verified: '2026-10-23'
reading_scope: 官方公告产品概述、三种输出类型、语音集成和Build/evaluate报价段已读；RSS确认19:00 UTC。未运行演示/API，未审缓存写入完整条款或客户原始测速。浏览快照为所列主文选段。
verification_note: Agent阅读所列来源并核对有限结论；reported保留披露主体归因，derived是研究推导，未独立复现。
evidence:
- source: raw/2026-10-07/00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280.txt
  locator: Changelog October 6两条；Decisions How decisions work / Choose a question
    type / Pricing and availability；Rate limits Usage tiers / Spend limits
  version: sha256:00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280
- source: raw/2026-10-16/5630d89fe634de54fde90578c147cf293c16460fef6866737e27f0c78dd3f31b.txt
  locator: 10月15日changelog；decisions-voice概述、触发与Run actions；未运行代码。
  version: sha256:5630d89fe634de54fde90578c147cf293c16460fef6866737e27f0c78dd3f31b
- source: raw/2026-10-24/32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c.txt
  locator: 官方公告产品概述、三种输出类型、语音集成和Build/evaluate报价段已读；RSS确认19:00 UTC。未运行演示/API，未审缓存写入完整条款或客户原始测速。浏览快照为所列主文选段。
  version: sha256:32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c
date_precision: timestamp
reviewed_by: Codex
reviewed_at: '2026-10-24'
reviewed_content_sha256: 874993dd53ca569761deb447fd43227d9e9d85babd9fe12e6551020c17137f52
---

# OpenAI Decisions API：公开beta、语音委派与正式可用

## Key Takeaways — 2026-10-06历史阅读版本

OpenAI 在10月6日changelog宣布 Decisions API 公开 beta，当前仅支持 gpt-6-luna；对文本/图像返回条件概率、固定选项或rubric分数，正式可用仍计划未来数周。

当前文档报价为 USD0.10/百万输入token，仅收输入费，不收cache读写或输出token费；区域处理溢价和长上下文输入乘数仍适用。这不是所有 gpt-6-luna 接口的统一价格。

新增产品形态是专用判别与路由接口，非自由生成或任意JSON工具调用；“约快10倍”为厂商主张，未提供本项目可复核的负载/基线，不视为实测。日期仅到日，边界不确定。

OpenAI 10月6日将付费用量层级从五档简化为 Build、Launch、Grow；按组织累计购买credit自动升级，仍保留 Free 层。

当前文档累计credit购买门槛为 USD5/100/500，对应月度用量上限 USD500/5,000/200,000；用量层级、模型速率限制和自行设置的spend cap是不同概念，不推导每个模型吞吐必然提升。

新增的是采购与扩容规则，既非模型token统一降价，也非月费套餐或ARR；日期仅到日、源站时区未知，已对照前期去重。

## Detailed Notes

已读10月6日两项changelog、Decisions文档概述/问题类型/计费与可用性、rate-limits用量层级小节。文档是无日期的当前背景，不当作新发布；未调用API/测试速度，日期仅到日、时区未知。

## Evidence

[官方changelog](https://developers.openai.com/api/docs/changelog)、[Decisions文档](https://developers.openai.com/api/docs/guides/decisions)、[用量层级文档](https://developers.openai.com/api/docs/guides/rate-limits)。版本和定位见元数据，数字属于服务商报价及配置披露。

## Questions Raised

判断（derived）：对固定分类和路由任务，仅输入计费可让高频判别组件更容易预算，应用编排与实时交互可能受益。若概率未校准或任务需要复杂工具调用，低延迟判别不能替代完整Agent；观察相同输入下准确率、尾时延和总账单。

更少层级和明确credit门槛可能降低从试验转向规模使用的采购摩擦，应用创业团队可能受益。实际吞吐还受模型限流与组织配置约束；观察扩容等待、限流和资金占用，不能把较高月度上限当成已实现收入。

## 2026-10-15：语音原生委派增量

OpenAI API 10月15日changelog为gpt-live-1/gpt-6-luna与v1/live/sessions列出原生Decisions集成：Live可直接委派，或根据输入/输出转写增量触发。文档要求应用执行动作后读取真实状态，再回报结果。

相对10月6日已入库的Decisions公开beta，新增的是语音会话内的调用通路；不由此宣称Decisions已全面GA或所有语音功能统一降价。日期仅到日，窗口边界不确定；已对照前期去重。

判断：省去应用中转的一次往返有望改善交互响应，实时助手和设备控制可受益，但动作正确性仍依赖状态读回与权限。反例是转写抖动导致错误触发；观察端到端尾时延、取消/重复执行率和完整账单。

新增证据：raw/2026-10-16/5630d89fe634de54fde90578c147cf293c16460fef6866737e27f0c78dd3f31b.txt；sha256:5630d89fe634de54fde90578c147cf293c16460fef6866737e27f0c78dd3f31b。10月15日changelog；decisions-voice概述、触发与Run actions；未运行代码。 原有价格/层级仅代表10月6日阅读版本。

## 2026-10-22：正式可用与缓存规则变化

OpenAI于10月22日将GPT-6 Luna支持的Decisions API从公开beta转为正式可用；相对库内10月6日beta和15日语音委派，新增正式供给、缓存与更大请求容量。

接口对文本、图像、原生JSON返回概率、固定选项或评分；单次上限从200增至400问，新增US/EU推理驻留。公告报价为USD0.10/百万输入token、缓存读取USD0.01/百万token，无输出token费；缓存写入与区域处理的完整条款未核，不能据此估算完整账单。

厂商及客户的速度倍数缺少本项目可比较的完整负载，不采作实测；新缓存规则也意味着10月6日历史版本的“无缓存读写费”不能继续视为当前报价。

判断：把重复分类、路由和动作评分抽成专用接口，可以减少复杂Agent每一步的等待和重复上下文费用，编排和实时交互受益。反例是概率校准不足或调用次数增长抵消单次节省。观察相同任务准确率、P95、缓存命中及含写入和区域费用的完整账单。

[原始来源](https://openai.com/index/decisions-api)；原始版本 `raw/2026-10-24/32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c.txt`，SHA-256 `32a3ac876f9f079f24dd12cf2ef809e4c965ac3c4f628cef8625caa058a23b9c`。

官方公告产品概述、三种输出类型、语音集成和Build/evaluate报价段已读；RSS确认19:00 UTC。未运行演示/API，未审缓存写入完整条款或客户原始测速。浏览快照为所列主文选段。
