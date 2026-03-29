---
name: documentation-governance
description: "Use when auditing documentation structure, duplicate markdown, README governance, or docs/docs_readable boundaries."
metadata:
  triggers:
    - audit repository documentation structure
    - detect duplicate markdown documents
    - fix README governance issues
    - classify docs and docs_readable layers
    - archive or merge outdated documentation
  side_effects:
    - read_only
    - write_files
---

# Documentation Governance OS

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

## 4. 核心模式（Pattern）

### Audit Pattern（审计模式）

这个 pattern 的核心是把文档治理稳定组织为 `audit -> report -> fix(optional)`：

- 输入是项目根目录、治理配置、markdown 文件树、可选 style guide，以及可选 `--write`、`--report`、`--json` 等输出控制参数
- 处理中执行扫描与校验，检查文档层级、分类归属、重复主题、命名违规、单一事实源冲突、README 章节缺口与 readable layer 风险
- 输出是结构化 `report`，包括治理摘要、高优先级问题、建议动作、可生成目标和冲突清单
- 可选的 `fix` 仅在显式授权时发生，例如补写缺失 README 章节或生成报告文件；默认不自动进入写入模式

Input:
- 项目根目录
- 治理配置
- markdown 文件树
- 可选 style guide
- 可选 `--write`、`--report`、`--json` 等输出控制参数

Process:
- `audit`
- `report`
- `fix(optional)`

Output:
- 结构化 `report`
- 高优先级问题
- 建议动作、可生成目标和冲突清单

这样组织的原因是，文档治理首先需要稳定判断“哪里失控、哪里重复、哪里越权”，而不是立刻改动文件。先 `audit`，再 `report`，最后才进入 `fix`，可以避免把治理规则误用成粗暴重写命令。

## 5. 核心原则（Principles）

- 先审计文档事实，再做结构治理。  
  Audit documentation facts before enforcing structure changes.

- 一个主题只保留一个工程事实源。  
  Keep one engineering source of truth per topic.

- 默认不改变项目，只做观察和结构化输出。  
  Do not modify the project unless explicitly allowed.

- `docs_readable/` 只能是衍生层，不能反向成为权威层。  
  Treat `docs_readable/` as a derivative layer, not an authority layer.

- fix 必须显式触发，并且晚于审计结论。  
  Any fix action must be explicit and come after the audit conclusion.

## 6. 执行流程（Execution Steps）

1. `audit`：解析治理输入。  
   读取项目根目录、默认治理配置、项目覆盖配置和显式参数；确认 `--config`、`--dry-run`、`--write`、`--report`、`--json` 等输入，并识别 style guide、`README.md`、`docs/`、`docs_readable/` 以及本次适用的分类与命名规则。

2. `audit`：扫描文档树并执行检查。  
   收集 markdown 文件，检查 heading 结构、README 必需章节、分类放置、层级归属、禁止命名、重复主题、单一事实源冲突、readable layer 第二事实源风险、归档候选与可读层生成目标。此阶段默认只观察，不写入文档。

3. `report`：输出治理结果。  
   生成工程层摘要、阅读层摘要、高优先级问题、建议动作、冲突清单和归档候选；如启用 `--json`，输出机器可读结果；如指定 `--report`，则将治理报告写入目标文件。报告应清楚区分“问题发现”和“建议修复”，而不是把建议动作当成已执行事实。

4. `fix`：决定是否进行显式修复。  
   只有在用户明确授权，且治理结论已经清楚时，才允许进入 fix，例如使用 `--write` 为 README 补齐缺失章节，或在后续单独执行归档、去重、readable 生成等受控动作。默认不应自动合并、删除、重命名或改写文档内容。

5. 输出治理回顾。  
   在最终结果中说明本次治理使用的配置来源、扫描范围、主要冲突、建议动作，以及哪些内容只是报告建议、哪些内容已经被显式写入或生成。

## 7. 约束（Constraints）

- 默认只做审计与报告输出，不自动重命名、归档、合并或删除文档
- `fix` 必须显式触发；`--write` 仅用于治理已经清楚后的 README 章节补写，不应扩展为任意文档重写
- 不得改变既有 CLI 参数、双层文档模型、分类词汇、命名禁用规则或报告语义
- `docs/` 应继续被视为工程事实层，`docs_readable/` 只能是衍生层，不能升格为第二权威层
- 支持文件可以解释规则，但 `SKILL.md` 仍是该 skill 的顶层规则表达，不应被辅助文件覆盖

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

## Invocation

### When to use

- 当任务目标是审计文档结构、识别重复主题、控制事实源边界，而不是直接写新文档时使用。

### Input Example

```text
Use documentation-governance for this task.

task_description:
- Audit the repository documentation structure and detect duplicate markdown topics.

constraints:
- Do not rewrite docs unless explicitly allowed.
- Keep docs/ as the engineering source of truth.

expected_output:
- Documentation audit summary
- Duplicate or conflict list
- Suggested follow-up actions

context_files:
- README.md
- docs/
- docs_readable/
```

### Output Example

```text
execution_plan:
- Scan markdown files and README structure.
- Check duplicate topics and docs/docs_readable boundaries.
- Produce an audit report without applying fixes.

changes_made:
- No repository files were modified.
- Produced a governance summary with follow-up suggestions.

files_touched:
- README.md
- docs/
- docs_readable/

risks:
- Some duplicate-topic judgments still require project-local confirmation.
```
