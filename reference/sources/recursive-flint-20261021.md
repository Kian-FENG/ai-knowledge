---
id: source-recursive-flint-20261021
title: Recursive发布Flint开放权重，本地编码与自动化研发共同优化
type: source
domain:
- models
- infra
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: Recursive官方更新列表将Flint发布日期标为10月21日：40B总参数、每token激活约2.5B的MoE编码模型，官方与链接模型卡标为Apache-2.0权重。Eureka
  Machine参与数据、训练和推理优化是公司披露，不等于已证明开放式递归自我改进。
evidence_kind: reported
verification: source-checked
sources:
- https://recursive.com/updates/introducing-recursive-flint
- https://vllm.ai/blog/2026-10-21-flint
related: []
aliases: []
source: raw/2026-10-23/e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515.txt
url: https://recursive.com/updates/introducing-recursive-flint
published_at: '2026-10-21'
source_category: official
last_verified: '2026-10-22'
verification_note: Agent实际阅读所列来源范围并核对支持关系；公司/作者披露保留reported，未独立实测。审核发布不等于独立核验。
raw_path: raw/2026-10-23/e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515.txt
sha256: e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515
fetched_at: '2026-10-22T22:10:33.136359+00:00'
reading_scope: Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。
evidence:
- source: raw/2026-10-23/e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515.txt
  locator: Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。
  version: sha256:e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515
- source: raw/2026-10-23/47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df.body
  locator: Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。
  version: sha256:47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: 91af25c04bcbee3c0f15fa8602c272716efbf40f5bbf00ca250aa33551f6a99a
---

# Recursive发布Flint开放权重，本地编码与自动化研发共同优化

## Key Takeaways

Recursive官方更新列表将Flint发布日期标为10月21日：40B总参数、每token激活约2.5B的MoE编码模型，官方与链接模型卡标为Apache-2.0权重。Eureka Machine参与数据、训练和推理优化是公司披露，不等于已证明开放式递归自我改进。

## Detailed Notes

官网称最高512K上下文、建议编码在256K以内；同日vLLM文章写262K，两者口径未消解，部署应以检查点及具体实现核对。vLLM提供专用flint镜像，文章仍称支持正在合并，不能写成已进入正式release。NVFP4检查点在该路径实际按W4A16运行，激活和KV为BF16。

评测为厂商自测：Terminal-Bench 2.1用Terminus 2 XML并联网但检索命中解答计失败，SWE-Bench Pro v2/Verified用mini-swe-agent且不联网；温度1、top-p0.95、top-k20，Agent最长5小时、至少5次取pass@1均值。未审图表原始分数、完整模型revision及速度负载，不转述领先排名或速度倍数。日精度边界不确定。

## Evidence

[原始来源](https://recursive.com/updates/introducing-recursive-flint)；`raw/2026-10-23/e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515.txt`，SHA-256 `e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515`。

[原始来源](https://vllm.ai/blog/2026-10-21-flint)；`raw/2026-10-23/47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df.body`，SHA-256 `47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df`。

Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。

## Questions Raised

判断：小激活MoE与模型专用运行栈有机会把部分编码任务留在本地，硬件和本地工具生态受益；能力与效率也更依赖整套交付。反例是长任务失败、内存容量或后端限制抵消API节省。观察固定任务质量、内存、长上下文延迟及上游正式支持。
