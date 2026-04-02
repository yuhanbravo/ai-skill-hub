# Skill Invocation Protocol

> Type: protocol, not a skill
>
> Use this document to understand how a skill should be invoked and what input/output contract the caller should expect.
>
> Do not treat this file as a callable skill or as the place to define discovery-layer routing rules.

## Scope

- Owns: how a skill is invoked, expected input and output structure, and the standard invocation flow across skills
- Does not own: execution-template authoring rules, skill section-writing guidance, or discovery-layer path rules
- See also:
  - [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md)
  - [DISCOVERY_AND_INVOCATION.md](DISCOVERY_AND_INVOCATION.md)

本文件定义 skill-hub 的统一调用协议，用于让不同 AI 在选择和调用 skill 时使用相同的输入结构、输出结构和标准步骤。

## Purpose

这个协议解决两个问题：

- 不同 AI 在“如何把任务交给 skill”上使用统一格式
- skill 被匹配后，执行结果可以被后续 AI 或人工继续接力

## Input Contract

调用 skill 时，输入应尽量组织为以下结构：

| Field | Required | Meaning |
| --- | --- | --- |
| `task_description` | Yes | 本次任务要解决什么问题，为什么要调用这个 skill |
| `constraints` | Yes | 本次任务的限制、禁止事项、边界和显式授权 |
| `expected_output` | Yes | 期望交付什么结果、报告、文件或结论 |
| `context_files` | Optional | 与任务最相关的文件、目录、配置或文档入口 |

### Minimal Input Example

```json
{
  "task_description": "Audit the repository documentation structure and identify duplicate markdown topics.",
  "constraints": [
    "Do not rewrite docs unless explicitly allowed.",
    "Keep docs/ as the engineering source of truth."
  ],
  "expected_output": [
    "Documentation audit summary",
    "List of duplicate or conflicting documents",
    "Suggested follow-up actions"
  ],
  "context_files": [
    "README.md",
    "docs/",
    "docs_readable/"
  ]
}
```

## Output Contract

skill 执行后，输出应尽量包含以下结构：

| Field | Required | Meaning |
| --- | --- | --- |
| `execution_plan` | Yes | 本次按什么步骤执行、为何选择该 skill |
| `changes_made` | Yes | 实际做了什么；如未写文件，也要明确说明 |
| `files_touched` | Yes | 读写过的关键文件列表；若没有写入，也可只列读取范围 |
| `risks` | Yes | 风险、未确认项、边界或后续需要人工确认的问题 |

### Minimal Output Example

```json
{
  "execution_plan": [
    "Matched documentation-governance from trigger phrases.",
    "Scanned markdown files and README structure.",
    "Reported duplicate topics and governance risks."
  ],
  "changes_made": [
    "No files were modified.",
    "Produced a documentation audit summary."
  ],
  "files_touched": [
    "README.md",
    "docs/PROJECT_LIFECYCLE.md",
    "docs/PHASE_MODEL.md"
  ],
  "risks": [
    "Some duplicate topics may require project-local judgment.",
    "No fix action was applied because write permission was not requested."
  ]
}
```

## Standard Invocation Flow

所有 skill 调用默认遵循以下五步：

1. 解析任务。  
   读取 `task_description`、`constraints`、`expected_output` 和 `context_files`，明确本次任务边界。

2. 匹配 skill。  
   根据 skill 的 `metadata.triggers`、`description`、类型和 side effects 选择最合适的 skill。

3. 生成执行计划。  
   在真正执行前，输出简短 `execution_plan`，说明为什么选择该 skill，以及准备如何落地。

4. 执行。  
   按目标 skill 的 `Execution Steps`、`Constraints` 和 `Risks` 执行，禁止越权扩写。

5. 输出结果。  
   按 `Output Contract` 回传结果，显式说明改动、涉及文件和未消除风险。

## Matching Rules

- 优先匹配 `metadata.triggers`
- 如果多个 skill 都匹配，优先选择边界更窄、风险更低的 skill
- 若任务明显跨多个 skill，先选主 skill，再把其他 skill 作为 follow-up，而不是一次混用
- 若任务不满足任何 skill 的边界，应该明确返回“不匹配”，而不是强行套用

## Side Effect Rules

- `read_only`：默认只读取和分析，不应写入文件
- `write_files`：允许在显式任务边界内修改或生成文件
- `requires_git`：依赖 Git 历史或仓库状态；若 Git 不可用，应降级或返回受限结论

## Invocation Prompt Skeleton

```text
Use <skill-name> for this task.

task_description:
- <what needs to be done>

constraints:
- <hard constraint 1>
- <hard constraint 2>

expected_output:
- <deliverable 1>
- <deliverable 2>

context_files:
- <path 1>
- <path 2>
```

## Interpretation Rule For Other AI Tools

- 把本协议视为 skill-hub 的统一调用契约
- 先读本协议，再读目标 skill 的 `SKILL.md`
- 若协议与单个 skill 的硬约束冲突，以目标 skill 的 `Constraints` 为准
