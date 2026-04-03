# Skill Governance

## What is this

`skill-governance` 是一个 `governance` 型 meta-skill，用来先评估单个 skill，再在显式授权时执行受控重写。

## When to use

适合在需要快速判断某个 skill 是否符合 `SKILL_TEMPLATE.md`、先拿到评分与诊断、再决定是否进入受控重写时使用；一次只处理一个 skill，不跨 skill 扩散。

## Quick Start

```text
Use skill-governance on <skill-path>
rewrite=false

# if explicitly allowed
# change to rewrite=true
```

## Supported Prompts

- `skill-evaluator.md`
- `skill-refactor.md`
- `skill-governor.md`
- `skill-refinement.md`
- `skill-batch-evaluator.md`
- `skill-invocation.md`

详细治理方法见 [skills/skill-governance/SKILL.md](skills/skill-governance/SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

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

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)
- Commit validation rule: [references/commit_convention_check.md](references/commit_convention_check.md)
- Commit validation script: [scripts/commit_convention_check.py](scripts/commit_convention_check.py)

