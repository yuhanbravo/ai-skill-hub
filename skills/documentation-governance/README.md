# Documentation Governance OS

## What is this

`documentation-governance` 是一个文档治理审计型 skill，用来基于双层文档模型、单一事实源和命名规则检查仓库 markdown 结构，并输出治理报告。

## When to use

适合在需要检查 `docs/` 与 `docs_readable/` 的关系、识别重复主题、命名违规、归档候选或 README 治理缺口时使用；如果目标是直接批量改写文档，这个 skill 不应作为第一步。

## Quick Start

```text
Use the `documentation-governance` skill on this repository and audit the documentation structure.
Project root: <project-root>

# optional
# Config path: <path-or-none>
# Dry run: yes/no
```

详细治理模式见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决仓库文档治理中的一个高频问题：文档会随着项目演进不断增长，但如果缺少稳定规则，就容易出现同主题多份文档、工程文档与阅读文档混杂、命名失控、过时文件悬挂、`README.md` 过度膨胀，以及 `docs_readable/` 反过来变成第二事实源等问题。

`documentation-governance` 的目标不是简单“清理 markdown”，而是用一套稳定的治理模型来审计文档结构、识别来源冲突、控制双层文档关系，并在必要时对 README 或可读层文档进行受控修复。

它在 skill-hub 中更适合作为 `tool` 型 skill 理解，但不是普通脚本说明，而是一个围绕文档治理规则运行的审计型 pattern：先检查，再报告，最后才决定是否进入显式修复。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 仓库 markdown 文件持续增长，需要建立稳定文档治理结构
- 需要区分 `docs/` 的工程事实层与 `docs_readable/` 的阅读衍生层
- 需要识别重复文档、同主题多源、命名违规或归档候选文件
- 需要判断新文档应新建、合并、归档，还是生成 readable summary
- 需要对 README 章节完整性做治理检查，或在结构已明确后显式补写缺失章节

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 当前目标只是撰写单个新文档，而不是治理整体文档结构
- 项目已经有更成熟且强制执行的本地文档治理机制，并且不需要额外报告
- 任务只需要回答某个文档内容问题，而不是检查文档层级、命名和事实源关系
- 希望直接批量重写、迁移或清理文档，但并未先做治理审计
- 不允许对 README 或文档层做任何显式写入，而当前任务又要求自动修复

## 8. 风险（Risks）

- 误判风险：主题去重、层级归属或分类判断可能对边界模糊的文档产生 false positive
- 误修复风险：如果在未确认事实源前就执行归档、合并或 README 补写，可能强化错误结构
- 规则不完整风险：项目实际文档体系若未被配置充分描述，报告可能遗漏冲突或给出过强建议
- readable layer 风险：若忽视 `docs_readable/` 的衍生定位，可能让阅读文档反向成为第二事实源
- 权威冲突风险：若使用 supporting files 覆盖 `SKILL.md` 规则，可能造成治理口径不一致

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准文档治理审计模板

```text
请使用 `documentation-governance` 处理以下任务。

背景：
- 需要检查仓库文档结构、事实源关系和重复问题

目标：
- 输出文档治理审计结果，并给出建议动作

范围：
- 检查 `docs/` 与 `docs_readable/` 的层级关系
- 检查重复主题、命名违规、归档候选和 README 缺口
- 默认只做 audit 和 report

约束：
- 默认不改变项目，只做观察和结构化输出
- fix 必须显式触发

预期输出：
- 按 `audit -> report -> fix(optional)` 推进
- 治理报告
- 高优先级问题
- 建议动作与待确认项
```

### 模板 2：严格治理执行模板

```text
请按 `documentation-governance` 的方法执行本次任务。

要求：
- 先总结你对治理目标的理解
- 按 `audit -> report -> fix(optional)` 三段执行
- 明确当前使用的配置来源、扫描范围和输出方式
- 报告中区分“问题发现”和“建议修复”
- 未显式授权时，不执行任何 fix

任务内容：
- Project root: <project-root>
- Config path: <path-or-none>
- Dry run: <yes-or-no>
- JSON output: <yes-or-no>
- Report path: <path-or-none>
- Write README sections: <yes-or-no>
```

## 10. 总结（Summary）

`documentation-governance` 最适合解决“文档结构是否失控、事实源是否冲突、哪些文档应该合并归档或生成 readable summary”这一类问题。它的核心价值是把文档治理变成稳定的审计和决策流程，而不是随手整理 markdown。

使用时最重要的边界是两条：第一，默认只做 `audit` 和 `report`，不自动修改文档；第二，任何 `fix` 都必须显式触发，并基于单一事实源与双层文档模型做受控执行。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

