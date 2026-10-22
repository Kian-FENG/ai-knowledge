---
id: source-blacksmith-series-c-20261021
title: Blacksmith披露10亿美元估值C轮，Agent代码增长推高CI需求
type: source
domain:
- companies
- infra
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: Blacksmith联合创始人兼CEO Aditya Jayaprakash于10月21日宣布Sequoia领投C轮，估值USD1B，累计融资USD125M。官方未在该文披露本轮金额，累计融资不能当作本轮金额，也未说明估值的投前/投后口径。
evidence_kind: reported
verification: source-checked
sources:
- https://www.blacksmith.sh/blog/series-c
related: []
aliases: []
source: raw/2026-10-23/2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07.txt
url: https://www.blacksmith.sh/blog/series-c
published_at: '2026-10-21'
source_category: official
last_verified: '2026-10-22'
verification_note: Agent实际阅读所列来源范围并核对支持关系；公司/作者披露保留reported，未独立实测。审核发布不等于独立核验。
raw_path: raw/2026-10-23/2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07.txt
sha256: 2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07
fetched_at: '2026-10-22T22:10:32.708643+00:00'
reading_scope: CEO署名官方公告全文及官网页尾Blacksmith Software Inc已读；未审法定注册、融资到账、客户账单和ARR原始报表。
evidence:
- source: raw/2026-10-23/2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07.txt
  locator: CEO署名官方公告全文及官网页尾Blacksmith Software Inc已读；未审法定注册、融资到账、客户账单和ARR原始报表。
  version: sha256:2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: 8f4a7333c4a36c63e5fa41e58f378344312c7bdbc5f9cfb482cce0c46eb42e2d
---

# Blacksmith披露10亿美元估值C轮，Agent代码增长推高CI需求

## Key Takeaways

Blacksmith联合创始人兼CEO Aditya Jayaprakash于10月21日宣布Sequoia领投C轮，估值USD1B，累计融资USD125M。官方未在该文披露本轮金额，累计融资不能当作本轮金额，也未说明估值的投前/投后口径。

## Detailed Notes

公司称自2026年1月以来每周CI任务由500万增至逾9000万、ARR增至17倍；没有披露ARR绝对金额，这不是同期确认收入。现有计算设施功率规模不到10MW、2027年扩大5倍是公司披露和计划。相对库内Scion对验证负载的观察，本期增加独立CI供应商的商业信号。仅日精度，边界不确定。

## Evidence

[原始来源](https://www.blacksmith.sh/blog/series-c)；`raw/2026-10-23/2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07.txt`，SHA-256 `2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07`。

CEO署名官方公告全文及官网页尾Blacksmith Software Inc已读；未审法定注册、融资到账、客户账单和ARR原始报表。

## Questions Raised

判断：代码生成加速可把瓶颈推向构建、测试和合并，弹性CI及缓存服务获得新增需求。反例是生成代码缺少商业价值，或客户自建与云价格竞争压低利润。观察付费任务留存、算力利用率、失败重跑、毛利及ARR绝对值。

[[reference/sources/anthropic-scion-20261013|背景：Scion与Agent源码验证负载]]
