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

## 1. 背景（Problem Context）

这个 skill 用来解决“如何接管一个能力系统”这一类问题，而不是解决普通业务项目 onboarding 的问题。

当目标对象是 `skill-hub`、AI agent system、orchestration layer 或 capability OS 时，调用方通常面对的不是单一代码库，而是一个由 `skills`、`protocol`、`router`、`pipeline`、`adapter`、`tooling` 和 `governance` 组成的能力系统。仅用普通 `project-takeover` 视角去看，会遗漏 system layer、invocation readiness、discoverability 和 orchestration maturity 这些核心问题。

`system-takeover` 的目标是把这类系统的接管过程稳定组织成“先识别系统结构，再盘点能力与协议，再评估路由、编排、适配和治理成熟度，最后输出瓶颈与演进建议”的系统分析流程。

它在 skill-hub 中属于 `project` 型 system-skill：重点不是单个技能执行，而是对整个 capability system 做分层接管分析。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要分析 `skill-hub` 的能力地图、调用协议和系统边界
- 需要评估一个 AI capability system 的 architecture、layering 和 maturity
- 需要分析 multi-agent system 的 router、pipeline 和 adapter readiness
- 需要接管一个 orchestration system，并判断其 bottlenecks 和 next phase
- 需要从 capability OS 视角，而不是业务项目视角，生成系统级 takeover 结论

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用：

- 当前目标只是首次进入普通业务仓库并生成基础 onboarding 材料，此时更接近 `project-takeover`
- 任务只要求修改单个 skill，此时更接近 `skill-governance`
- 任务只要求更新最近进展或周报，而不是接管系统结构，此时更接近 `update-project-status`
- 当前无法读取 `skills/`、`tools/`、`docs/`、adapter 或测试等系统层材料，导致无法形成分层判断
- 需要直接重构 router、pipeline 或 protocol，而不是先形成 system-level diagnosis

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
- top bottlenecks
- evolution plan

这样组织的原因是，能力系统接管的难点不在于单点扫描，而在于把多个层的事实组织成可决策的系统视图。只有把 capability、invocation、routing、pipeline、adapter、tooling 和 governance 作为一个整体来分析，输出才真正服务后续系统演进。

## 5. 分析维度（Analysis Dimensions）

### Capability Map

- 盘点当前 skills 列表与能力域分布
- 判断哪些能力已经有 canonical skill，哪些仍是空洞
- 区分职责重叠、边界相邻和真正冲突的能力单元

### Invocation Readiness

- 检查是否存在统一 invocation protocol
- 检查各 skill 是否包含完整 invocation section 和示例
- 判断 readiness 是文档约定级、测试校验级，还是 enforcement 级

### Routing Layer

- 检查是否存在 router 与 runtime index
- 判断是否支持 `top-k`、confidence、scoring 和多候选输出
- 评估 routing 是否仅为 heuristic，还是已经具备稳定调度基础

### Pipeline Layer

- 检查是否支持 task splitting 与 subtask routing
- 判断是否仅支持 ordered sequence，还是具备 orchestration 能力
- 评估 context passing、dependency handling 和 failure strategy 是否存在

### Adapter Layer

- 检查 `.agents`、`.github` 和其他 adapter entry 是否覆盖 canonical skills
- 判断 discoverability 是单 AI 兼容，还是 multi-AI discoverability
- 检查 canonical 与 adapter 是否存在 drift 风险

### Tooling & Automation

- 盘点 metadata generator、bundle、import/export、sync 和其他自动化脚本
- 判断这些工具是否只支持维护，还是已能支撑 capability system 的分发与同步
- 检查测试、生成器和索引之间是否闭环

### Governance

- 检查 lifecycle、phase model、status management 和 governance skill 是否存在
- 判断治理是否只是文档说明，还是已经进入 CI / enforcement
- 输出治理缺口及下一阶段治理重点

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
   使用结构化格式回传 `System Structure`、`Capability Map`、`Maturity Assessment`、`Top Bottlenecks` 和 `Evolution Plan`；如果用户允许写文件，再把分析结果写入 takeover 文档或 status 文档。

## 8. 输出格式（Output Structure）

输出必须尽量包含以下五部分：

1. `System Structure`
2. `Capability Map`
3. `Maturity Assessment`
4. `Top Bottlenecks`
5. `Evolution Plan`

如果需要更细化，可以在 `Maturity Assessment` 中按以下层输出：

- skill layer
- routing layer
- pipeline layer
- adapter layer
- governance layer

## 9. 约束（Constraints）

- 不要把普通项目 takeover 模板直接套用到 capability system
- 不要忽略 `protocol`、`adapter`、`router`、`pipeline`、`tooling` 和 `governance` 这些系统层材料
- 默认先做 read-only 分析；除非显式授权，否则不要修改 router、pipeline、protocol 或现有 skills
- 不要把“有文档”直接等同于“已 invocation-ready”或“已治理闭环”
- 当证据不足时，应显式说明未确认项，而不是补齐想象中的系统设计

## 10. 风险（Risks）

- 如果把能力系统当作普通项目接管，输出会遗漏真正的系统瓶颈
- 如果只看 README 或单个 skill，而不看 router、pipeline 和 adapter，成熟度判断会偏高
- 如果把 invocation section 的存在误判为 enforcement，可能高估系统 readiness
- 如果忽略 capability overlap 与 capability gaps，演进建议会流于泛泛而谈
- 如果在证据不完整时做强判断，system takeover 结果会误导后续治理优先级

## 11. Prompt 模板（Reusable Prompt）

### 模板 1：标准系统接管模板

```text
请使用 `system-takeover` 处理以下任务。

背景：
- 目标对象是一个 capability system，而不是普通业务项目

目标：
- 分析系统结构、能力地图、调用就绪度、调度层、适配层、工具链和治理成熟度

范围：
- `skills/`
- `tools/`
- `docs/`
- `.agents/`
- `.github/`
- `tests/`

约束：
- 不修改现有 protocol、router、pipeline 或已有 skills
- 只做 system-level takeover analysis

预期输出：
- System Structure
- Capability Map
- Maturity Assessment
- Top Bottlenecks
- Evolution Plan
```

### 模板 2：严格分层分析模板

```text
请按 `system-takeover` 的方法执行本次任务。

要求：
- 先确认该对象是否属于 capability system
- 按 Capability Map、Invocation Readiness、Routing Layer、Pipeline Layer、Adapter Layer、Tooling & Automation、Governance 七个维度推进
- 明确哪些结论是已确认事实，哪些是推断
- 输出系统结构图、按层成熟度、Top 3 瓶颈和下一阶段建议

任务内容：
- System root: <project-root>
- System type: <skill-hub | multi-agent system | orchestration system | capability OS>
- Focus layers: <one-or-more>
- Output mode: <report | summary | takeover packet>
```

## 12. 总结（Summary）

`system-takeover` 最适合解决“如何接管一个能力系统，而不是一个普通项目”这一类问题。它的价值不在于列文件或做一般性审计，而在于把 capability、invocation、routing、pipeline、adapter、tooling 和 governance 组织成一个可判断、可演进的系统视图。

使用时最重要的边界有两条：第一，必须明确对象是 capability system；第二，必须区分“结构存在”“可调用”“可编排”“可治理”这几种不同成熟度，而不能把它们混为一谈。

## Invocation

### When to use

- 当你需要分析 `skill-hub`、AI capability system、multi-agent system 或 orchestration system 的整体结构与成熟度，而不是普通项目状态时使用。

### Input Example

```text
Use system-takeover for this task.

task_description:
- Analyze this skill-hub system and evaluate its capability architecture.

constraints:
- Do not modify protocol, router, pipeline, or existing skills.
- Treat this as a system-level takeover, not a business-project audit.

expected_output:
- System structure
- Capability map
- Layered maturity assessment
- Top bottlenecks
- Evolution plan

context_files:
- skills/
- tools/
- docs/
- .agents/
- .github/
- tests/
```

### Output Example

```text
execution_plan:
- Map the capability system structure and discovery layers.
- Assess invocation, routing, pipeline, adapter, tooling, and governance maturity.
- Synthesize bottlenecks and the next evolution phase.

changes_made:
- No source files were modified.
- Produced a structured system takeover analysis.

files_touched:
- skills/
- tools/
- docs/
- .agents/
- .github/
- tests/

risks:
- Some maturity judgments may remain provisional if enforcement evidence is incomplete.
- Adapter coverage can drift if canonical and compatibility layers are not continuously checked.
```
