---
name: system-takeover
description: "Use when analyzing system-level architecture, capability hubs, multi-agent systems, or orchestration stacks rather than ordinary business projects."
metadata:
   triggers:
      - analyze system architecture
      - analyze skill hub
      - analyze ai capability system
      - multi agent system analysis
      - analyze orchestration system
      - capability os assessment
   side_effects:
      - read_only
      - write_files
---
# System Takeover

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

## 4. 核心模式（Pattern）

### Layered Capability System Takeover（分层能力系统接管）

这个 pattern 的核心是把能力系统接管组织成六个分析维度，并把维度结论汇总为系统成熟度判断：

- `Capability Map`：识别 skills、能力域、重叠与空洞
- `Invocation Readiness`：检查 protocol、invocation completeness 和 readiness
- `Routing Layer`：评估 router、scoring、top-k 和稳定性
- `Pipeline Layer`：评估 subtask splitting、ordering 和 orchestration depth
- `Adapter Layer`：评估 `.agents`、`.github` 和 multi-AI discoverability
- `Tooling / Governance`：评估 automation、lifecycle、status 和 enforcement

Input:
- 系统根目录
- canonical skills
- protocol 和 adapter 入口
- router / pipeline / tooling 实现
- docs、tests 和状态材料

Process:
- `scan`
- `map`
- `assess`
- `synthesize`
- `output`

Output:
- system structure
- capability map
- maturity assessment by layer
- assessment fields from `skill_assessment_output` where applicable: `maturity_score`, `evidence`, `inference`, `open_questions`, `risk_priority`, `impact_scope`, `next_action`
- top bottlenecks
- evolution plan

这样组织的原因是，能力系统接管的难点不在于单点扫描，而在于把多个层的事实组织成可决策的系统视图。只有把 capability、invocation、routing、pipeline、adapter、tooling 和 governance 作为一个整体来分析，输出才真正服务后续系统演进。

## 6. 核心原则（Principles）

- 先识别系统层，再下结论。  
  Map system layers before making maturity judgments.

- 不要把能力系统误判为普通业务项目。  
  Do not reduce a capability system to a normal product repository.

- 区分结构存在、调用就绪和治理闭环。  
  Separate structural existence from invocation readiness and governance enforcement.

- 优先输出分层判断，而不是零散观察。  
  Prefer layered assessment over disconnected observations.

- 演进建议必须对齐系统瓶颈，而不是泛化优化。  
  Tie evolution plans to actual bottlenecks instead of generic improvements.

## 7. 执行流程（Execution Steps）

1. `scan`：识别系统边界。  
   读取仓库结构、`skills/`、`tools/`、`docs/`、adapter 目录和测试文件，判断该对象是否属于 capability system，并区分 canonical source、discovery layer、tooling layer 和 governance layer。

2. `map`：建立能力地图。  
   盘点现有 skills、能力域、职责边界、重叠区与空洞区；确认哪些能力已经成为 canonical skill，哪些仍停留在隐式流程或缺失状态。

3. `assess`：分层评估 readiness 与 maturity。  
   按 `Capability Map`、`Invocation Readiness`、`Routing Layer`、`Pipeline Layer`、`Adapter Layer`、`Tooling & Automation`、`Governance` 七个维度检查系统现状，明确哪些层只是“存在”，哪些层已经“可用”，哪些层还没有形成 enforceable mechanism。

4. `synthesize`：形成系统级判断。  
   将分层发现组织成系统结构图、成熟度评估、Top 3 bottlenecks 和下一阶段演进建议；显式区分“已确认事实”“基于代码和文档的推断”“需要后续验证的点”。

5. `output`：输出 system takeover 结果。  
   使用结构化格式回传 `System Structure`、`Capability Map`、`Maturity Assessment`、`Top Bottlenecks` 和 `Evolution Plan`；在 assessment / takeover 输出中按 shared assessment output protocol 标注 `maturity_score`、`evidence`、`inference`、`open_questions`、`risk_priority`、`impact_scope` 和 `next_action`；如果用户允许写文件，再把分析结果写入 takeover 文档或 status 文档。

## 9. 约束（Constraints）

- 不要把普通项目 takeover 模板直接套用到 capability system
- 不要忽略 `protocol`、`adapter`、`router`、`pipeline`、`tooling` 和 `governance` 这些系统层材料
- 默认先做 read-only 分析；除非显式授权，否则不要修改 router、pipeline、protocol 或现有 skills
- 不要把“有文档”直接等同于“已 invocation-ready”或“已治理闭环”
- 当证据不足时，应显式说明未确认项，而不是补齐想象中的系统设计

## Invocation

### When to use

- 当你需要分析 `skill-hub`、AI capability system、multi-agent system 或 orchestration system 的整体结构与成熟度，而不是普通项目状态时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

