---
id: source-openai-low-resource-code-20261019
title: OpenAI公布低资源编程评测，将COBOL迁移的行为一致性纳入验证
type: source
domain:
- models
- products
lifecycle: published
tags: []
created: '2026-10-20'
updated: '2026-10-20'
summary: OpenAI 10月19日发布MultiLangBench与COBOL迁移评测：前者跨20种语言构建SQLite兼容引擎，后者要求迁移后可观察输出逐字节一致。文章涉及GPT-6
  Astra、GPT-6 Luna、GPT-6.1 Sol及GPT-5.6 Sol基线。
evidence_kind: reported
verification: source-checked
sources:
- https://openai.com/index/low-resource-programming-languages
related: []
aliases: []
source: raw/2026-10-21/d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873.txt
url: https://openai.com/index/low-resource-programming-languages
published_at: '2026-10-19T12:00:00+00:00'
source_category: official
raw_path: raw/2026-10-21/d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873.txt
sha256: d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873
fetched_at: '2026-10-20T22:08:29.113527+00:00'
reading_scope: 官方主文两项评测设计、模型结果和生产限制已读；GitHub测试套件/预算/全部图表未审，数字不作外部验证。
last_verified: '2026-10-20'
verification_note: Agent已阅读所列范围并核对支持关系；reported不等于独立审计或复现，审核发布不提高核验等级。
evidence:
- source: raw/2026-10-21/d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873.txt
  locator: 官方主文两项评测设计、模型结果和生产限制已读；GitHub测试套件/预算/全部图表未审，数字不作外部验证。
  version: sha256:d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873
reviewed_by: Codex
reviewed_at: '2026-10-21'
reviewed_content_sha256: 2af61bb7d12247c5310a6055c248d40bd29fc9d1af8b3dabeb7c3ad9e173a544
---

# OpenAI公布低资源编程评测，将COBOL迁移的行为一致性纳入验证

## Key Takeaways

OpenAI 10月19日发布MultiLangBench与COBOL迁移评测：前者跨20种语言构建SQLite兼容引擎，后者要求迁移后可观察输出逐字节一致。文章涉及GPT-6 Astra、GPT-6 Luna、GPT-6.1 Sol及GPT-5.6 Sol基线。

## Detailed Notes

新增是评测设计和厂商结果披露，并非本期发布这些模型。本文未审完整仓库、harness版本、任务预算与隐藏测试，不转载跨模型成本排名；生产迁移仍须检查业务规则、依赖和专家验收。

## Evidence

[原始来源](https://openai.com/index/low-resource-programming-languages)。官方主文两项评测设计、模型结果和生产限制已读；GitHub测试套件/预算/全部图表未审，数字不作外部验证。 原始路径、采集时间与hash见元数据。

## Questions Raised

判断（derived）：老系统现代化的价值取决于保留业务行为，受益环节可能是银行IT、迁移服务和测试工具；反例是隐藏依赖未被评测覆盖。观察真实代码库迁移、缺陷逃逸率和人工审阅成本。
