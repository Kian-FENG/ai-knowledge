---
id: source-anthropic-haiku-55-pricing-20261007
title: Claude Haiku 5.5 发布：可调effort，价格按100K提示长度分档
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-08'
updated: '2026-10-08'
summary: Anthropic 在Haiku公告中将 Sonnet 5.5 缓存读取价从USD0.20降至0.10/百万token；只针对cache read，不是所有输入/输出价格减半。实际节省取决于缓存命中与读写比例，未采用厂商平均节省百分比。
evidence_kind: reported
verification: source-checked
sources:
- https://www.anthropic.com/claude-haiku-5-5
related: []
aliases: []
source: raw/2026-10-08/93b9bd71aecf534b7d3bd9f7b3677925b03d020dcd047fd0c64e03bb31ff105a.body
url: https://www.anthropic.com/claude-haiku-5-5
published_at: '2026-10-07'
source_category: official
raw_path: raw/2026-10-08/93b9bd71aecf534b7d3bd9f7b3677925b03d020dcd047fd0c64e03bb31ff105a.body
sha256: 93b9bd71aecf534b7d3bd9f7b3677925b03d020dcd047fd0c64e03bb31ff105a
fetched_at: '2026-10-08T01:06:13.269259+00:00'
last_verified: '2026-10-08'
verification_note: 已阅读并核对所列有限陈述与原始来源的支持关系；Haiku公告 Lower pricing for Sonnet 5.5 / API
  credits段；已读价格与额度段，未测账单或核实账户启用。；Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。；未独立复现。
reading_scope: Haiku公告 Lower pricing for Sonnet 5.5 / API credits段；已读价格与额度段，未测账单或核实账户启用。；Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。
evidence:
- source: raw/2026-10-08/93b9bd71aecf534b7d3bd9f7b3677925b03d020dcd047fd0c64e03bb31ff105a.body
  locator: Haiku公告 Lower pricing for Sonnet 5.5 / API credits段；已读价格与额度段，未测账单或核实账户启用。；Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。
  version: sha256:93b9bd71aecf534b7d3bd9f7b3677925b03d020dcd047fd0c64e03bb31ff105a
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-08'
reviewed_content_sha256: fe1cc2fb5c1050981f5d80a1fb11fed2e9915b30e035d04b17155fb55f72cfa9
---

# Claude Haiku 5.5 发布：可调effort，价格按100K提示长度分档

## Key Takeaways

Anthropic 在Haiku公告中将 Sonnet 5.5 缓存读取价从USD0.20降至0.10/百万token；只针对cache read，不是所有输入/输出价格减半。实际节省取决于缓存命中与读写比例，未采用厂商平均节省百分比。

本周开始推送月度API credits：Max 5x USD100、Max 20x USD200，Team最高USD500池化；额度、套餐订阅与API现金收入/ARR不同，尚不能认为每个账户已启用。相对前期资格访问变化，本期新增成本与分发激励。

日期只有10月7日，时区和窗口边界不确定；未核查实际账户到账与完整续期/使用条款。

Anthropic 10月7日发布claude-haiku-5-5，首个支持可调effort的Haiku；可经自有平台、AWS、Google Cloud、Azure获得。厂商定位摘要、分类、压缩与子Agent工作，复杂编码仍可能更适合较大模型，未据跨口径评测排名。

USD/百万token，提示≤100K / >100K：输入0.10/0.50，输出0.50/2.50，缓存读取0.01/0.05、写入0.125/0.625。新版tokenizer可能使用更多token，报价降幅不等于任意工作流总成本降幅。

相对CVP访问分层，本期增量是低价小模型的预算控制与正式平台供给；日期仅到日、边界不确定。系统卡和全部harness未审阅，不采用厂商领先/提速数字。

## Detailed Notes

Haiku公告 Lower pricing for Sonnet 5.5 / API credits段；已读价格与额度段，未测账单或核实账户启用。；Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。

## Evidence

[原始来源](https://www.anthropic.com/claude-haiku-5-5)。定位与阅读范围：Haiku公告 Lower pricing for Sonnet 5.5 / API credits段；已读价格与额度段，未测账单或核实账户启用。；Haiku公告能力、availability及价格表；已读完整HTTP正文和官网，未运行模型或逐项审阅GDPval-AA/OSWorld/Terminal-Bench等设置。 原始路径、hash、采集/事件时间见元数据；source-checked只表示所列陈述支持关系已核对，非独立结果验证。

## Questions Raised

判断（derived）：缓存读价降低会优先惠及复用长系统提示和工作上下文的Agent；套餐赠额可降低开发者试用门槛。低命中率、频繁写缓存或过期额度会削弱收益；观察真实账单、命中率及赠额使用后的付费留存。

把可分解任务交给低价模型并按任务调effort，可降低子Agent的边际计算费，编排平台和高频分类应用可能受益。失败重试、tokenizer变化和长提示高档价会抵消收益；观察同任务成功率、重试次数与总账单。
