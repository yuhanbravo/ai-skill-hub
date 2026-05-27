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

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

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
- evidence / risk / scope / next-action fields from `skill_assessment_output`, trimmed to the audit scenario

这样组织的原因是，文档治理首先需要稳定判断“哪里失控、哪里重复、哪里越权”，而不是立刻改动文件。先 `audit`，再 `report`，最后才进入 `fix`，可以避免把治理规则误用成粗暴重写命令。

## 5. 核心原则（Principles）

- 先审计文档事实，再做结构治理。  
  Audit documentation facts before enforcing structure changes.

- 一个主题只保留一个工程事实源。  
  Keep one engineering source of truth per topic.

- 可变项目状态事实必须留在已声明的 current-state SSOT 中。
  Mutable project-status facts must stay in the declared current-state SSOT. `README.md`、`docs/README.md`、`docs/technical/`、`CLAUDE.md`、`AGENTS.md` 和 blueprint docs 可以引用 SSOT，但不应复制 active phase status、next-phase decisions、latest validation results、blocker status 或 pending-merge state，避免形成第二事实源。

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
   生成工程层摘要、阅读层摘要、高优先级问题、建议动作、冲突清单和归档候选；如启用 `--json`，输出机器可读结果；如指定 `--report`，则将治理报告写入目标文件。报告应清楚区分“问题发现”和“建议修复”，而不是把建议动作当成已执行事实。需要 assessment 口径时，引用 shared assessment output protocol，并按文档审计场景裁剪字段，不强制所有字段满配。

4. `fix`：决定是否进行显式修复。  
   只有在用户明确授权，且治理结论已经清楚时，才允许进入 fix，例如使用 `--write` 为 README 补齐缺失章节，或在后续单独执行归档、去重、readable 生成等受控动作。默认不应自动合并、删除、重命名或改写文档内容。

5. 输出治理回顾。  
   在最终结果中说明本次治理使用的配置来源、扫描范围、主要冲突、建议动作，以及哪些内容只是报告建议、哪些内容已经被显式写入或生成。

## 7. 约束（Constraints）

- 默认只做审计与报告输出，不自动重命名、归档、合并或删除文档
- `fix` 必须显式触发；`--write` 仅用于治理已经清楚后的 README 章节补写，不应扩展为任意文档重写
- 不得改变既有 CLI 参数、双层文档模型、分类词汇、命名禁用规则或报告语义
- `docs/` 应继续被视为工程事实层，`docs_readable/` 只能是衍生层，不能升格为第二权威层
- README、docs index、technical onboarding、agent wrapper 和 blueprint 文档不应默认复制 mutable project-status facts；如项目需要在这些入口展示状态，应保持短引用并指向已声明的 HANDOFF/status SSOT
- 支持文件可以解释规则，但 `SKILL.md` 仍是该 skill 的顶层规则表达，不应被辅助文件覆盖

## Invocation

### When to use

- 当任务目标是审计文档结构、识别重复主题、控制事实源边界，而不是直接写新文档时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)



## Audience-aware Round 1

- Built-in audience model: `human_machine_shared`, `human_primary_archive`, `ai_only_wrapper`, `unknown_or_mixed`.
- Built-in authority roles and doc intents are emitted in report fields without replacing existing `document_layer` model.
- Built-in conflict checks include AI-only SSOT misuse, shared-doc agent-only instructions, archive-as-current-fact references, navigation status duplication, and language mismatch for shared docs.
- Round 1 remains internal-only and does not integrate markdownlint/lychee/Vale/textlint.
