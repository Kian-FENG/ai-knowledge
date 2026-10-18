---
id: source-reflection-beam-release-20261016
title: Reflection Beam从预览转为权重与托管API交付
type: source
domain:
- models
lifecycle: published
tags: []
created: '2026-10-18'
updated: '2026-10-18'
summary: Reflection10月16日公告发布Beam权重并以Apache2.0提供，包含BF16、FP8、NVFP4及drafter；501B总参数、23B激活。官方HF模型卡可见，模型为文本输入/输出、1M上下文。相比10月5日有限预览和本月发布承诺，这是交付状态变化。
evidence_kind: reported
verification: source-checked
sources:
- https://reflection.ai/blog/beam-is-available
- https://huggingface.co/reflection/Beam-1.0-501B-A23B
related: []
aliases: []
source: https://reflection.ai/blog/beam-is-available
url: https://reflection.ai/blog/beam-is-available
published_at: '2026-10-16T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-18/bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06.body
sha256: bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06
fetched_at: '2026-10-18T10:01:04.149815+00:00'
last_verified: '2026-10-18'
verification_note: 官方发布Building/Deploy/Customize/Start Using；HF Model Overview/License/Usage；未下载权重或完整审计评测。
  source-checked仅确认上述支持关系；不表示独立验证、测量或复现。
evidence:
- source: raw/2026-10-18/bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06.body
  locator: 官方发布主文及Deploy/Customize；未读安全技术报告和完整模型评测
  version: sha256:bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06
- source: raw/2026-10-18/46ee96ec349aa002d8bfd1d3be996ac157924c85043e6feeaeca87010d0e860f.body
  locator: 模型概览、许可与Usage段；未采用评测排名或安全结论
  version: sha256:46ee96ec349aa002d8bfd1d3be996ac157924c85043e6feeaeca87010d0e860f
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: dab5749721cf091691f1deaf1c2e10517b2a05a04b80c4779b603ff257aea37c
---

# Reflection Beam从预览转为权重与托管API交付

## Key Takeaways

Reflection10月16日公告发布Beam权重并以Apache2.0提供，包含BF16、FP8、NVFP4及drafter；501B总参数、23B激活。官方HF模型卡可见，模型为文本输入/输出、1M上下文。相比10月5日有限预览和本月发布承诺，这是交付状态变化。

公司同时提供第一方API、Mirror CLI与部署/后训练生态，部分自蒸馏配方仍承诺未来数日发布。公告日期仅到日；未读完整安全技术报告、逐项核实所有40多伙伴交付或采用厂商排行榜。

## Detailed Notes

官方发布Building/Deploy/Customize/Start Using；HF Model Overview/License/Usage；未下载权重或完整审计评测。

原始材料及本期published与显式草稿按对象、URL/hash查重；相同版本不重复建页，相关对象优先更新。

## Evidence

[原始来源](https://reflection.ai/blog/beam-is-available)；归档 `raw/2026-10-18/bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06.body`；SHA-256 `bda041991ba13abc1e3fd006a1fb01d4945937e95fae78d46e04d4276fd3bc06`；实际采集 2026-10-18T10:01:04.149815+00:00。

[原始来源](https://huggingface.co/reflection/Beam-1.0-501B-A23B)；归档 `raw/2026-10-18/46ee96ec349aa002d8bfd1d3be996ac157924c85043e6feeaeca87010d0e860f.body`；SHA-256 `46ee96ec349aa002d8bfd1d3be996ac157924c85043e6feeaeca87010d0e860f`；实际采集 2026-10-18T10:01:57.785078+00:00。

## Questions Raised

判断（derived）：开放许可和多精度交付增加企业自部署、定制及MaaS供给选择；总权重驻留与服务运维仍决定经济性。反例是API质量或实际内存成本抵消可迁移优势；观察相同任务总成本、权重版本和各服务商可用性。
