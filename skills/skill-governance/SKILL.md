---
name: skill-governance
description: "Use when evaluating, scoring, diagnosing, or explicitly refactoring a single skill under controlled governance."
metadata:
  triggers:
    - evaluate a skill against the template
    - diagnose skill maturity and structure
    - score a skill and decide rewrite level
    - govern a single skill before refactor
    - perform a controlled skill rewrite
  side_effects:
    - read_only
    - write_files
---
# Skill Governance

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

## 4. 核心模式（Pattern）

### Governance Pattern（治理模式）

这个 pattern 的核心是：

- 对单个目标 skill 先做 `evaluate`
- 基于证据做 `decide`
- 只有在显式授权下才进入 `refactor(optional)`

它稳定组织为：`evaluate -> decide -> refactor(optional)`。

Input:
- 单个 skill 路径
- 当前结构与约束
- `rewrite=true/false`

Process:
- `evaluate`
- `decide`
- `refactor(optional)`

Output:
- 治理结论
- assessment fields from `skill_assessment_output` where applicable: `maturity_score`, `evidence`, `inference`, `open_questions`, `risk_priority`, `impact_scope`, `next_action`
- 风险边界
- 可选的受控重写结果

这样组织的原因是 skill 治理首先是控制问题，而不是内容生成问题。先 `evaluate` 再 `decide`，可以把修改建立在可复核证据上；把 `refactor` 设计成可选阶段，则能确保治理动作保持 Non-intrusive，不会默认改变现有 skill。

## 5. 核心原则（Principles）

- 默认只评估，不修改。  
  Evaluate first, do not modify by default.

- 修改必须显式触发。  
  Rewrite must be explicitly requested.

- 一次只处理一个 skill。  
  One skill at a time.

- 默认不改变项目。  
  Do not modify the project unless explicitly allowed.

- 评分要基于结构与证据。  
  Score against structure and evidence.

- 重写必须保持非侵入。  
  Keep refactoring non-intrusive.

## 6. 执行流程（Execution Steps）

1. `evaluate`：读取单个目标 skill。  
   读取目标目录中的 `README.md`、`SKILL.md`、相关 prompt 或 agent 文件，确认其是否完整、是否符合 `SKILL_TEMPLATE.md` 的 10 段结构、以及其主要类型和职责边界。

2. `diagnose`：生成治理诊断。  
   输出 `SCORECARD`、`DIAGNOSIS` 和 `LEVEL`，明确结构缺口、原则偏差、类型错位、prompt 不可执行点和潜在风险，不在此阶段做任何改写。治理 assessment 应按 shared assessment output protocol 在适用时标注 `maturity_score`、`evidence`、`inference`、`open_questions`、`risk_priority`、`impact_scope` 和 `next_action`。

3. `decide`：决定是否进入重写。  
   根据评分和诊断判断是否需要重写；若 `rewrite=false`，则停留在 dry-run 治理结果；若 `rewrite=true`，则明确本次只允许对当前 skill 做受控重写。

4. `refactor(optional)`：执行可选受控重写。  
   仅在显式授权时，基于 `SCORECARD` 与 `DIAGNOSIS` 进行最小必要重写，要求对齐 `SKILL_TEMPLATE.md`、对齐 skill 类型，并保持 Non-intrusive 原则，不扩展到其他 skill 或项目逻辑。

执行链路固定为：`evaluate -> diagnose -> decide -> refactor(optional)`。

## 7. 约束（Constraints）

- 默认 `dry-run`，未显式授权时只允许评估与诊断
- 禁止批量修改，单次只治理一个 skill
- 禁止跨 skill 操作，不得顺带调整其他目录或共享模板
- 禁止修改项目脚本、测试、运行逻辑或非目标 skill 文件
- 重写只能在 `rewrite=true` 时发生，且应是最小必要改动
- 若证据不足，应输出待确认项，而不是自行补完假设

## Invocation

### When to use

- 当你需要治理单个 skill 的结构完整性、成熟度或是否进入受控重写，而不是修改业务逻辑时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

