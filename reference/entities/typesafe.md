---
id: entity-typesafe
title: TypeSafe：Jev 与机器可读决策模型基础设施
type: entity
domain:
- companies
- products
lifecycle: published
tags:
- startup
- typed-decision
created: '2026-10-10'
updated: '2026-10-10'
summary: TypeSafe开发Jev/System One决策模型接口，10月9日披露USD870M A轮与USD7.5B估值；客户采用口径有差异，未核实收入。
evidence_kind: reported
verification: source-checked
sources:
- source-typesafe-series-a-20261009
- https://docs.typesafe.ai/introduction
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
related: []
aliases:
- TypeSafe AI
- Jev
entity_kind: company
last_verified: '2026-10-10'
verification_note: 已读公司融资/介绍与投资方公告核对名称、CEO及产品归属；注册日期/法定地址、ARR、独立客户采用和性能尚未核实。
evidence:
- source: raw/2026-10-10/5db48353702ff454e700c0eef808fba3b5fefb2f6ce5df2b4c153e7b5c4259f6.body
  locator: 官方融资全文及尾注；a16z dated announcement；另读Jev介绍/发布页。未核实法律注册地、客户样本、ARR或独立性能。
  version: sha256:5db48353702ff454e700c0eef808fba3b5fefb2f6ce5df2b4c153e7b5c4259f6
- source: raw/2026-10-10/d70048d01325c5b8e673c2d621ba6f88c6dabaeaf54c0b91c22e18d3aa14b2cf.body
  locator: 官方Jev/System One介绍；发布日期未核实，仅作身份、产品归属与输出类型背景；未采用速度/质量营销数字。
  version: sha256:d70048d01325c5b8e673c2d621ba6f88c6dabaeaf54c0b91c22e18d3aa14b2cf
- source: raw/2026-10-10/aff70ee42a0fed73944e107ed8dbf73108fe51ff90885a89129224f5c17e0766.body
  locator: 官方Jev/System One介绍；发布日期未核实，仅作身份、产品归属与输出类型背景；未采用速度/质量营销数字。
  version: sha256:aff70ee42a0fed73944e107ed8dbf73108fe51ff90885a89129224f5c17e0766
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: d8f9cf0573f93f90cdf386046fec329f0bce15cf871b2d51988713868b5bf1be
---

# TypeSafe：Jev 与机器可读决策模型基础设施

## Identity and Scope

TypeSafe AI；创始人兼CEO Diogo Almeida（公司发布页与a16z公告）。Jev是其产品，System One是其机器可读决策模型路线。主页定位旧金山，法定实体名称、注册日期及法定所在地尚未核实，不把网站地点等同注册地。

## Products and Capabilities

官方文档描述Choice/Score等类型化值、概率与置信度；格式确定并不保证语义判断正确。介绍与发布页日期未知，只作背景；未采用“cannot hallucinate”等营销断言或未对齐性能排名。

## Development Timeline

10月9日融资披露：USD870M A轮，USD7.5B估值，a16z领投，Sequoia/DCVC等参与；不等同收入、ARR或客户实际付款。公司“三分之一Fortune 500”与投资方“25%集成”口径/期间未定义，保留冲突而不选取较高值。

[[reference/sources/typesafe-series-a-20261009|融资与投资方来源、日期和采用口径]]

## Evidence

公司融资、Jev文档、产品发布及a16z投资声明已读；原始路径/hash在元数据及来源页。身份产品支持关系已核对，投资方与公司均为利益相关披露，非独立市场审计。

## Open Questions

核实法定身份、真实付费采用、价格/许可、语义错误率与任务级账单。判断（derived）：资金和类型化接口可能降低决策集成摩擦，但通用模型专用接口、错误处置及企业销售效率决定长期竞争力。

融资页未标发布日期；a16z明确Posted October 9提供该轮公开事件的日期，交易完成时刻未知。Jev背景原文的采集时间见data/extracted对应hash，未填为发布日。
