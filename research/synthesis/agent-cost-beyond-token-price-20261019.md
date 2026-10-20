---
id: note-agent-cost-beyond-token-price-20261019
title: Agent成本竞争从token单价扩展到迁移、留存与验收
type: note
domain:
- industry
lifecycle: published
tags: []
created: '2026-10-20'
updated: '2026-10-20'
summary: API价格、harness、工作流协调、软件迁移和KV留存共同约束Agent成本；本期是多个有条件信号，尚非统一因果趋势。
evidence_kind: derived
verification: source-checked
sources:
- source-minimax-m31-flash-20261019
- source-openai-orchestra-bio-20261019
- source-memsilicon-lpu-series-a-20261019
- source-openai-low-resource-code-20261019
- source-sglang-v0522-20261019
- source-vllm-elastic-ep-20261019
- source-microsoft-agentic-insider-20261019
- paper-kv-residency-261022863
- paper-self-hpo-261022791
- source-tenstorrent-series-e-20261019
- source-aws-torchneuron-announcement-20261019
related:
- source-minimax-m31-flash-20261019
- source-openai-orchestra-bio-20261019
- source-memsilicon-lpu-series-a-20261019
- source-openai-low-resource-code-20261019
- source-sglang-v0522-20261019
- source-vllm-elastic-ep-20261019
- source-microsoft-agentic-insider-20261019
- paper-kv-residency-261022863
- paper-self-hpo-261022791
- source-tenstorrent-series-e-20261019
- source-aws-torchneuron-announcement-20261019
- note-execution-governance-and-delivery-20261018
aliases: []
last_verified: '2026-10-20'
verification_note: 逐项核对本期有限来源；跨来源综合为推导，未进行因果识别、独立复现或生产审计。
evidence:
- source: source-minimax-m31-flash-20261019
  locator: Evidence及所列阅读范围
  version: sha256:ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6
- source: source-openai-orchestra-bio-20261019
  locator: Evidence及所列阅读范围
  version: sha256:25889d85b4ebca0d364d4aa661768326f919853ff4e0e5489b6af2ac4533bae1
- source: source-memsilicon-lpu-series-a-20261019
  locator: Evidence及所列阅读范围
  version: sha256:68516247b7a34fa3afcfdc8ab26d7d91c014e8b454bb7807f64be4fb37fb7e92
- source: source-openai-low-resource-code-20261019
  locator: Evidence及所列阅读范围
  version: sha256:d8cef12ccd5b18ab751ceb1973e3dec956112644ffdfee615dfcc1e3084d0873
- source: source-sglang-v0522-20261019
  locator: Evidence及所列阅读范围
  version: sha256:69112e48c5e668d4eaa34617858d83b2cc2d5c06872f95fc33b95d98c11dead4
- source: source-vllm-elastic-ep-20261019
  locator: Evidence及所列阅读范围
  version: sha256:ef0b1ec14e92866856c3054e682628e394889769383f1c694fb31426d21b4ff3
- source: source-microsoft-agentic-insider-20261019
  locator: Evidence及所列阅读范围
  version: sha256:b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a
- source: paper-kv-residency-261022863
  locator: Evidence及所列阅读范围
  version: sha256:19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8
- source: paper-self-hpo-261022791
  locator: Evidence及所列阅读范围
  version: sha256:57a53e004c218d35bba52dfe63ebfaceb2ad0851ded0c622734fac45ff2897c1
- source: source-tenstorrent-series-e-20261019
  locator: Evidence及所列阅读范围
  version: sha256:5cb94783207262f6961889f8e8f5e7d31020cbd124f23d8d8970fe6b9e66449e
- source: source-aws-torchneuron-announcement-20261019
  locator: Evidence及所列阅读范围
  version: sha256:a3d521c134e4d455ef8d5c2c720cb1264f7067f28b70a7df014fd45fd24c3740
reviewed_by: Codex
reviewed_at: '2026-10-21'
reviewed_content_sha256: dedff200059dadc5bbd3fdc231ea682ef645ab65c10aa7c4237beb3059357f82
---

# Agent成本竞争从token单价扩展到迁移、留存与验收

## What Is New

MiniMax降低服务单价，OpenAI收购工作流平台；AWS降低后端迁移摩擦，SGLang/vLLM处理正确性与扩容，KV论文提出闲置留存与路由成本。Tenstorrent融资和铭芯研发仅是供给形成的前置条件。

## Synthesis

研究推导：应按完成且验收的任务计算总成本，将模型调用、重试、缓存留存、软件适配、权限监督与人工复核共同计入。不同来源的指标不可相加或直接排名。低单价可能被重试抵消，后台扩容不等于即时容量，模拟驻留量不是生产HBM实测，科研工作流整合也不等于临床周期已经缩短。

## Evidence

[[reference/sources/minimax-m31-flash-20261019|MiniMax M3.1 Flash上线API与订阅，权重仍待发布]]

[[reference/sources/openai-orchestra-bio-20261019|OpenAI确认收购Orchestra Bio，将研发协调平台接入Rosalind]]

[[reference/sources/memsilicon-lpu-series-a-20261019|铭芯启睿披露超4亿元A轮与CEO变动，第一代LPU仍在研发]]

[[reference/sources/openai-low-resource-code-20261019|OpenAI公布低资源编程评测，将COBOL迁移的行为一致性纳入验证]]

[[reference/sources/sglang-v0522-20261019|SGLang 0.5.22正式发布，扩展推测解码并改变升级要求]]

[[reference/sources/vllm-elastic-ep-20261019|vLLM用异步准备与NIXL EP减少扩缩容停顿，容量就绪仍需时间]]

[[reference/sources/microsoft-agentic-insider-20261019|微软将内部Agent纳入持续风险控制，Guardian方案仍须验证]]

[[reference/papers/kv-residency-261022863|KV驻留论文提示：Agent的显存成本还取决于空闲留存与部署位置]]

[[reference/papers/self-hpo-261022791|Self-HPO交替优化harness与策略模型，避免把系统改进全归因于模型]]

[[reference/sources/tenstorrent-series-e-20261019|Tenstorrent宣布15亿美元E轮，62亿美元是投后估值]]

[[reference/sources/aws-torchneuron-announcement-20261019|AWS宣布TorchNeuron原生PyTorch后端，开源安排在次日]]

## Watchpoints

跟踪固定预算下的真实任务质量/账单、迁移工时、KV空闲驻留与跨部署命中、缩放就绪时间、样片/量产验收、权重和开源许可实际交付。论文只读摘要；不把多个厂商信号写成已验证全行业趋势。
