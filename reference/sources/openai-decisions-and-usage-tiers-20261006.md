---
id: source-openai-decisions-and-usage-tiers-20261006
title: OpenAI API 更新：Decisions 公开 beta 与三档付费用量层级
type: source
domain:
- products
- models
lifecycle: published
tags: []
created: '2026-10-07'
updated: '2026-10-07'
summary: OpenAI 在10月6日changelog宣布 Decisions API 公开 beta，当前仅支持 gpt-6-luna；对文本/图像返回条件概率、固定选项或rubric分数，正式可用仍计划未来数周。
evidence_kind: reported
verification: source-checked
sources:
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/decisions
- https://developers.openai.com/api/docs/guides/rate-limits
related: []
aliases: []
source: raw/2026-10-07/00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280.txt
url: https://developers.openai.com/api/docs/changelog
published_at: '2026-10-06'
source_category: official
raw_path: raw/2026-10-07/00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280.txt
fetched_at: '2026-10-07T01:21:34.915185+00:00'
sha256: 00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280
last_verified: '2026-10-07'
reading_scope: 已读10月6日两项changelog、Decisions文档概述/问题类型/计费与可用性、rate-limits用量层级小节。文档是无日期的当前背景，不当作新发布；未调用API/测试速度，日期仅到日、时区未知。
verification_note: 已读所列官方小节，核对beta/计费/三档paid与Free区别；未复现性能、核查账户实际配额或对历史每档限流逐项比较。
evidence:
- source: raw/2026-10-07/00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280.txt
  locator: Changelog October 6两条；Decisions How decisions work / Choose a question
    type / Pricing and availability；Rate limits Usage tiers / Spend limits
  version: sha256:00cef5a38ef36dc4dc618f5392694a4dc255a1ca818eb85e4792786ac5661280
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: 0becc337ed87c2892fd0ce5736c5f7eecbe4a9a6e7767098dca61653bab8ea73
---

# OpenAI API 更新：Decisions 公开 beta 与三档付费用量层级

## Key Takeaways

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
