---
name: file-structure-check
description: 基于目录、规则配置与 profile 审计仓库结构，通过 audit、report 与可选 fix 建议，帮助识别缺失目录、缺失路径和错位文件。
---

# File Structure Check

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

## 4. 核心模式（Pattern）

### Audit Pattern（审计模式）

这个 pattern 的核心是把结构检查稳定组织为 `audit → report → fix(optional)`：

- 输入是目标目录、结构规则、project profile、strictness 和可选项目本地配置
- 处理中执行扫描与校验，检查 required directories、required paths，以及 source / config / test / doc 文件是否落在允许位置
- 输出是结构化 `report`，包括缺失项、错位项、配置来源和建议修复动作
- 可选的 `fix` 不是默认执行，而是基于报告结果，在后续单独、显式地进行人工修复或其他受控修复动作

Input:
- 目标目录
- 结构规则
- `profile`
- `strictness`
- 可选项目本地配置

Process:
- `audit`
- `report`
- `fix(optional)`

Output:
- 结构化 `report`
- 缺失项与错位项
- 建议修复动作

这样组织的原因是，结构治理首先需要可靠审计，而不是直接改动。先做 `audit`，再看 `report`，最后才决定是否需要 `fix`，可以避免把启发式规则误当成自动改造命令。

## 5. 核心原则（Principles）

- 先审计事实，再讨论修复。  
  Audit the current structure before discussing fixes.

- 规则应通过配置表达，而不是硬编码猜测。  
  Express structure rules through configuration instead of hard-coded guesses.

- 默认只做检查，不做修改。  
  Only audit by default and do not modify the repository.

- 报告要区分问题与建议修复。  
  Separate detected issues from suggested fixes in the report.

- fix 必须显式触发。  
  Any fix action must be explicitly requested.

## 6. 执行流程（Execution Steps）

1. `audit`：解析审计输入。  
   读取目标根目录、默认规则、项目覆盖配置和显式参数；确认 `--profile`、`--strictness`、`--config`、`--json`、`--dry-run` 等输入，并确定本次使用的 profile、strictness 和规则来源。

2. `audit`：扫描并校验结构。  
   递归扫描仓库文件，跳过配置中列出的忽略目录；检查 required directories、optional directories、required paths，并按 source / config / test / doc 分类识别错位文件。此阶段只检查结构，不创建目录、不移动文件。

3. `report`：生成结构化结果。  
   输出缺失目录、缺失必需路径、错位文件、建议修复项以及本次使用的配置路径；如启用 `--json`，则输出机器可读结构；否则输出可读文本报告。这里的 suggested fixes 属于建议，不等于已经执行 fix。

4. `fix`：决定是否进入后续修复。  
   只有在用户或项目流程显式要求时，才基于报告进入后续修复动作，例如人工调整目录、补充 required path，或更新项目本地配置。默认不在本 skill 内自动执行修复。

5. 输出审计回顾。  
   在结果中说明本次使用的目录、profile、strictness、配置来源、主要结构问题，以及哪些内容只是建议修复而非实际改动。

## 7. 约束（Constraints）

- 默认只执行审计与报告输出，不修改目录、不移动文件、不创建缺失路径
- fix 必须显式触发，且应作为后续独立动作处理，而不是自动跟随 audit 执行
- 不得改变既有 CLI 参数、profile 机制、strictness 语义或 `--json` 输出方式
- 项目有意偏离默认结构时，应优先通过项目本地配置覆盖规则，而不是直接改共享默认规则
- 审计结果应被视为治理输入，而不是无条件执行的重构指令

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
