---
name: skill-governance
description: 作为 Skill OS 的控制层，按受控治理流程评估、诊断并在显式授权时重写单个 skill，默认只做 dry-run 评估。
---

# Skill Governance

## 1. 背景（Problem Context）

这个 skill 用来解决 skill-hub 在扩展过程中常见的一类元治理问题：当 skill 越来越多时，团队需要一个稳定的控制层来判断某个 skill 是否结构完整、类型清晰、原则稳定、prompt 可执行，并在必要时做受控修整。

`skill-governance` 的目标不是替代具体 skill，也不是引入新的脚本逻辑，而是为 skill 本身提供治理工作流。它把治理动作限定为“先评估、再诊断、再决定、可选重写”，从而避免直接修改、批量漂移和跨 skill 污染。

它在 skill-hub 中属于 `governance` 型 skill，也可以理解为 Skill OS 的 Control Plane：负责治理 skill，而不是直接治理项目产物。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要评估某个 skill 是否符合 `SKILL_TEMPLATE.md` 的 10 段结构标准
- 需要给单个 skill 生成 `SCORECARD`、`DIAGNOSIS` 和成熟度 `LEVEL`
- 需要判断某个 skill 的类型是否对齐 `pattern`、`project`、`tool` 或 `governance`
- 需要在显式授权下，对单个 skill 做受控重写，而不是自由改写
- 需要让 skill-hub 具备可复用的 skill 治理入口，而不是每次临时判断

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 需要修改多个 skill，此时不应把多个治理动作混在一次调用里
- 需要调整脚本、测试、运行逻辑或仓库功能，这超出 skill 文档治理范围
- 只想生成新的业务 skill 内容，但不需要治理评估流程
- 需要跨 skill 合并、重组或迁移目录，这不属于默认治理动作
- 用户没有明确授权重写，却希望直接进入修改阶段

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
   输出 `SCORECARD`、`DIAGNOSIS` 和 `LEVEL`，明确结构缺口、原则偏差、类型错位、prompt 不可执行点和潜在风险，不在此阶段做任何改写。

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

## 8. 风险（Risks）

- 如果把治理结果直接当成强制改写指令，可能导致过度重构
- 如果未区分 `evaluate` 与 `refactor`，容易在无授权时产生副作用
- 如果一次处理多个 skill，评分与诊断会相互污染，削弱治理结论
- 如果类型判断错误，可能把 `project` 型 skill 重写成 `tool` 型表达
- 如果忽略 Non-intrusive 原则，重写可能引入原任务之外的内容漂移

## 9. Prompt 模板（Reusable Prompt）

本 skill 复用以下三个 prompt 资产：

- `prompts/skill-governor.md`：治理入口，负责路由 `rewrite=true/false`
- `prompts/skill-evaluator.md`：只做评分与诊断，不允许重写
- `prompts/skill-refactor.md`：基于评估结果执行受控重写
- `prompts/skill-refinement.md`：只做表达层收口，不进入结构重写
- `prompts/skill-batch-evaluator.md`：按顺序批量评估 `skills/` 下的一级 skill
- `prompts/skill-invocation.md`：定义统一 skill 调用协议，规范 `skill / target / parameters` 的传递方式

### 模板 1：标准治理调用

```text
Use skill-governance on <skill-path>
rewrite=false

Goal:
- Evaluate one skill against SKILL_TEMPLATE and governance rules

Expected output:
- SCORECARD
- DIAGNOSIS
- LEVEL
```

### 模板 2：受控重写调用

```text
Use skill-governance on <skill-path>
rewrite=true

Requirements:
- Evaluate first
- Show SCORECARD and DIAGNOSIS
- Refactor only the target skill
- Keep the rewrite non-intrusive
- Preserve the skill type alignment
```

## 10. 总结（Summary）

`skill-governance` 最适合解决“如何在 skill-hub 内稳定治理单个 skill，而不是临时凭感觉改写”这一类问题。它的核心价值是把 skill 治理提升为可复用控制流程，而不是一次性文档编辑。

使用时最重要的边界有三条：默认只评估、不批量处理、且不跨 skill 执行。只有在 `rewrite=true` 且证据充分时，才进入受控重写。

## Invocation

This skill follows the unified invocation protocol.

```text
Use skill-governance on <skill-path>
rewrite=false
```

If rewrite is explicitly allowed:

```text
Use skill-governance on <skill-path>
rewrite=true
```

See also:

* prompts/skill-invocation.md
