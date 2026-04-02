---
name: file-structure-check
description: "Use when auditing repository folder structure, required directories, missing paths, or misplaced files against a profile."
metadata:
  triggers:
    - audit repository folder structure
    - check required directories and paths
    - detect misplaced files in a repo
    - validate project layout against a profile
    - generate a structure audit report
  side_effects:
    - read_only
    - write_files
---
# File Structure Check

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

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

## Invocation

### When to use

- 当任务目标是检查仓库目录结构是否符合约定、识别缺失路径或错位文件，而不是直接重构目录时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

