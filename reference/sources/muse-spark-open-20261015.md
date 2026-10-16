---
id: source-muse-spark-open-20261015
title: Meta发布Muse Spark Open权重，MaaS许可设收入门槛
type: source
domain:
- models
- ecosystem
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: Meta 10月15日发布Muse Spark Open：816B总参数/42B激活、1M上下文，输入含文本/图像/音频/视频、输出文本，提供BF16及NVFP4。PyTorch团队披露SGLang/vLLM推理和TorchTitan微调支持；未复核厂商“最强”等排名。
evidence_kind: reported
verification: source-checked
sources:
- https://pytorch.org/blog/muse-spark-open/
- https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
related: []
aliases: []
source: raw/2026-10-16/f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc.body
url: https://pytorch.org/blog/muse-spark-open/
published_at: '2026-10-15T17:55:52+00:00'
source_category: official
raw_path: raw/2026-10-16/f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc.body
sha256: f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc
fetched_at: '2026-10-16T01:03:04.286262+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。
retrieval_method: feed-content
evidence:
- source: raw/2026-10-16/f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc.body
  locator: PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。
  version: sha256:f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc
- source: raw/2026-10-16/990c71b5351d19747d97f282be4da0e3272ed15c72856906f80b910fc15d6363.txt
  locator: PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。
  version: sha256:990c71b5351d19747d97f282be4da0e3272ed15c72856906f80b910fc15d6363
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: 84426d8d8a4ac1d7b9dd37c847014818ca072569c02ee108b49568149a97a75f
---

# Meta发布Muse Spark Open权重，MaaS许可设收入门槛

## Key Takeaways

Meta 10月15日发布Muse Spark Open：816B总参数/42B激活、1M上下文，输入含文本/图像/音频/视频、输出文本，提供BF16及NVFP4。PyTorch团队披露SGLang/vLLM推理和TorchTitan微调支持；未复核厂商“最强”等排名。

相对8月Muse Spark及10月Muse Wonder消息，新增是Spark分支的权重交付和部署生态。Muse Model License要求署名及使用政策；经营MaaS的被许可方及关联方，任意连续12个月合计毛收入超过USD20M，须先通知并另签协议，门槛不是仅该模型营收。HF有访问申请门禁；不能称无限制MIT/Apache开源。日期部分仅到日，边界不确定。

## Detailed Notes

PyTorch全文；HF可见模型卡、访问及许可1–3条；未下载权重或审benchmark。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://pytorch.org/blog/muse-spark-open/)；归档 `raw/2026-10-16/f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc.body`，sha256 `f6ed89b3945384a3ddd55be4907d0df7c42188d88953ab39da84bd0692a006cc`。

[原始来源](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)；归档 `raw/2026-10-16/990c71b5351d19747d97f282be4da0e3272ed15c72856906f80b910fc15d6363.txt`，sha256 `990c71b5351d19747d97f282be4da0e3272ed15c72856906f80b910fc15d6363`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Questions Raised

判断：开放权重增加企业定制和多供应商部署选择，同时许可条款可能改变大规模MaaS的议价与分发成本。反例是总权重驻留、长上下文缓存和协议条件抵消API替代收益；观察许可协议、同任务成本与真实部署。
