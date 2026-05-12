# File Structure Check

## What is this

`file-structure-check` 是一个结构审计型 skill，用来基于目录、规则配置和 profile 检查仓库布局，并输出结构化报告。

## When to use

适合在需要检查目录结构、识别缺失路径、发现错位文件，或为后续治理提供结构审计输入时使用；如果目标是直接做目录改造，这个 skill 不是第一步。

## Quick Start

```text
Use the `file-structure-check` skill on this repository and audit the repo layout.
Project root: <project-root>

# optional
# Profile: <application | data-project | docs-only | monorepo | custom>
# Strictness: <relaxed | standard | strict>
```

详细审计模式见 [SKILL.md](SKILL.md)。

## Detailed Guidance Moved From SKILL.md

The sections below were moved out of `SKILL.md` during the semantic split so the README can carry explanation-oriented material while `SKILL.md` stays execution-focused.

## 1. 背景（Problem Context）

这个 skill 用来解决仓库结构治理中的一个常见问题：不同项目的目录形态并不相同，但团队又需要检查“当前结构是否符合约定”，例如源码、测试、文档、配置文件是否放在合理位置，必需目录或关键路径是否缺失，以及某些文件是否落在了错误位置。

`file-structure-check` 的目标不是强行把所有仓库变成同一种布局，而是基于可配置规则、project profile 和 strictness，对当前仓库进行结构审计，并给出结构化报告与后续修复建议。

它在 skill-hub 中属于典型 `tool` 型 skill，但更适合被抽象为审计型 pattern，而不是单纯脚本说明，因为它稳定处理的是“输入规则 → 扫描校验 → 输出报告 → 可选修复”这条链路。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要检查一个仓库的目录结构是否符合既定规则或 profile
- 需要识别缺失目录、缺失必需路径或错位文件
- 需要比较不同项目类型，如 `application`、`data-project`、`docs-only`、`monorepo` 的结构差异
- 需要为后续治理、重构或文档治理提供结构审计输入
- 需要通过项目本地配置覆盖共享默认规则，而不是修改共享 skill 本体

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 当前目标是直接重构目录结构，而不是先做结构审计
- 项目已经有更成熟且强制执行的本地结构检查机制，并且不需要额外报告
- 任务只需要回答某一个文件为什么存在，而不是检查整体结构约束
- 希望自动移动文件、创建目录或执行批量修复，但并未显式授权后续 fix 动作
- 仓库结构规则尚未定义，且当前不希望先建立最小审计基线

## 8. 风险（Risks）

- 误判风险：启发式分类可能把某些特殊文件误判为错位文件或缺失结构
- 误修复风险：如果跳过人工判断直接按建议修复，可能破坏项目原有约定或兼容层
- 规则不完整风险：默认规则或项目配置不完整时，报告可能遗漏真实问题或产生不必要告警
- profile 选择错误风险：选错 `application`、`data-project`、`docs-only`、`monorepo` 会让报告偏离项目实际形态
- strictness 使用不当风险：过严会制造噪音，过松会漏掉应关注的问题

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准结构审计模板

```text
请使用 `file-structure-check` 处理以下任务。

背景：
- 需要检查仓库目录结构是否符合当前项目约定

目标：
- 审计结构问题，并输出结构化报告

范围：
- 检查目录布局
- 检查 required paths
- 识别错位文件
- 输出建议修复项，但默认不执行修复

约束：
- 默认只做 audit 和 report
- fix 必须显式触发

预期输出：
- 按 `audit -> report -> fix(optional)` 推进
- 审计结果
- 问题清单
- 建议修复项
```

### 模板 2：严格审计执行模板

```text
请按 `file-structure-check` 的方法执行本次任务。

要求：
- 先总结你对审计目标的理解
- 按 `audit -> report -> fix(optional)` 三段执行
- 明确当前使用的 profile、strictness 和配置来源
- 报告中区分“已发现问题”和“建议修复”
- 未显式授权时，不执行任何 fix

任务内容：
- Project root: <project-root>
- Profile: <application | data-project | docs-only | monorepo | custom>
- Strictness: <relaxed | standard | strict>
- Config path: <path-or-none>
- JSON output: <yes-or-no>
```

## 10. 总结（Summary）

`file-structure-check` 最适合解决“当前仓库结构是否符合既定规则，以及有哪些结构问题需要治理”这一类问题。它的核心价值是提供结构化审计与可追踪报告，而不是直接重构仓库。

使用时最重要的边界是两条：第一，默认只做 `audit` 和 `report`；第二，任何 `fix` 都必须显式触发，并结合项目本地规则判断，而不能把建议修复自动当成正确答案。

## Supporting Assets

- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

## 文档语言与 SSOT 说明（2026-05-11）

- 本文档面向开发人员（developer-facing），统一采用**中文为主、英文术语辅助**（例如：`Pattern`、`Invocation`、`Constraints`、`read_only`、`write_files`）。
- 本仓库的 **SSOT（Single Source of Truth）** 仍是当前 skill 目录下的 `SKILL.md`；`README.md` 仅提供可读性说明与快速上手，不得与 `SKILL.md` 发生规则分叉。
- 若 `README.md` 与 `SKILL.md` 出现冲突，必须以 `SKILL.md` 为准，并在后续修订中消除偏差。
- 本节为当前状态声明，更新日期：**2026-05-11**。

