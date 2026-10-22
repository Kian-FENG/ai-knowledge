---
id: entity-blacksmith
title: Blacksmith
type: entity
domain:
- companies
- products
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: 官网页尾主体为Blacksmith Software Inc，融资文由联合创始人兼CEO Aditya Jayaprakash署名；CI云产品与品牌归属已核。法定注册地和成立时间未独立核实。
evidence_kind: reported
verification: source-checked
sources:
- source-blacksmith-series-c-20261021
related: []
aliases: []
entity_kind: company
last_verified: '2026-10-22'
verification_note: 官网署名/页尾与产品链接核对身份和归属；未独立核验注册、财务或客户效果。
evidence:
- source: raw/2026-10-23/2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07.txt
  locator: CEO署名官方公告全文及官网页尾Blacksmith Software Inc已读；未审法定注册、融资到账、客户账单和ARR原始报表。
  version: sha256:2f5d263053744a9ccd845b0d62538762e730cbb12b04bfddcc588e46a3949a07
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: c250c845aeed43c1fa1057c1a84fd97a2095bb768056a0609e621b3d7508bf33
---

# Blacksmith

## Identity and Scope

官网页尾主体为Blacksmith Software Inc，融资文由联合创始人兼CEO Aditya Jayaprakash署名；CI云产品与品牌归属已核。法定注册地和成立时间未独立核实。

## Products and Capabilities

弹性CI计算与构建/测试基础设施；用户数量、ARR、算力和成本效果均为公司披露。

## Development Timeline

Blacksmith联合创始人兼CEO Aditya Jayaprakash于10月21日宣布Sequoia领投C轮，估值USD1B，累计融资USD125M。官方未在该文披露本轮金额，累计融资不能当作本轮金额，也未说明估值的投前/投后口径。 新纳入跟踪不等于本期成立。

## Evidence

[[reference/sources/blacksmith-series-c-20261021|Blacksmith披露10亿美元估值C轮，Agent代码增长推高CI需求]]

## Open Questions

判断：代码生成加速可把瓶颈推向构建、测试和合并，弹性CI及缓存服务获得新增需求。反例是生成代码缺少商业价值，或客户自建与云价格竞争压低利润。观察付费任务留存、算力利用率、失败重跑、毛利及ARR绝对值。
