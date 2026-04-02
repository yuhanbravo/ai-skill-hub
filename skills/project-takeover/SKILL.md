---
name: project-takeover
description: "Use when onboarding a new maintainer or AI agent, scanning an unfamiliar repository, or generating a takeover packet."
metadata:
   triggers:
      - prepare a repository takeover packet
      - onboard a new maintainer or AI agent
      - scan docs config and task sources
      - generate an onboarding summary for a project
      - analyze an unfamiliar repository before maintenance
   side_effects:
      - read_only
      - write_files
---
# Project Takeover

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

## 4. 核心模式（Pattern）

### Phase-Based Takeover Pattern（阶段化项目接管模式）

这个 pattern 的核心是把项目接管组织成四个稳定阶段：

- `scan`：扫描仓库的环境、配置、文档候选、任务来源和可用支持脚本
- `understand`：基于扫描结果建立对项目现状、约束、任务入口和主要风险的初步理解
- `structure`：把离散信息整理成可交接结构，包括文档摘要、任务来源摘要和环境结论
- `output`：生成 takeover packet，并按需要写入报告目录或同步到本地共享目录

Input:
- 项目根目录
- 可选配置
- 可选脚本覆盖
- 运行参数

Process:
- `scan`
- `understand`
- `structure`
- `output`

Output:
- 三类接管文档
- 风险与后续动作
- 环境结论

这样组织的原因是，项目接管并不是一次普通扫描，而是一个需要逐步建立理解的过程。先 `scan`，再 `understand`，再 `structure`，最后 `output`，可以在不改变原始脚本逻辑的情况下，让 AI 更稳定地执行整个接手流程。

## 5. 核心原则（Principles）

- 先扫描事实，再组织判断。  
  Scan repository facts before forming conclusions.

- 项目差异优先于共享假设。  
  Prefer project-local reality over shared assumptions.

- 接管过程要按阶段推进。  
  Move the takeover workflow phase by phase.

- 输出应服务后续接手与协作。  
  Produce outputs that support real onboarding and handoff.

- 高风险动作默认显式选择。  
  Treat side-effecting actions as explicit opt-ins.

## 6. 执行流程（Execution Steps）

1. `scan`：解析输入与接管上下文。  
   读取项目根目录、默认配置、项目覆盖配置和显式 CLI 参数；确认 `--config`、`--report-dir`、`--shared-dir`、`--structure-script`、`--docs-script`、`--dry-run`、`--apply-safe-fixes`、`--install` 等输入，并识别项目本地是否已有接管相关目录或规则。

2. `scan`：执行基础扫描。  
   检查 Python、pip、conda 等环境可用性；展开 `doc_candidate_globs` 和 `priority_task_globs`；解析可用支持脚本；必要时运行结构审计和文档治理脚本。这里保留 soft-fail 逻辑，缺失工具或脚本时应记录结果，而不是直接中断。

3. `understand`：形成项目接管理解。  
   基于扫描结果判断仓库的核心文档入口、任务来源、环境 readiness、缺失信息和潜在阻塞项；区分“已经确认的信息”“待验证的信息”和“项目本地尚未提供的信息”，避免过度猜测。

4. `structure`：整理接手材料骨架。  
   将离散信息整理为可交接结构，包括文档摘要、任务来源摘要、环境检查结论、结构审计结果、需要跟进的风险和下一步建议；如果启用了 `--apply-safe-fixes` 或 `--install`，也要把实际动作与结果纳入整理结果。

5. `output`：生成 takeover packet。  
   按配置或默认路径输出 `project_takeover_report.md`、`project_onboarding_summary.md`、`welcome_email.md`；若指定了 `--shared-dir`，则同步到本地共享目录；若处于 `--dry-run`，则预览动作与输出路径而不真正写文件。

6. 输出执行回顾。  
   在最终结果中说明：使用了哪些输入参数、发现了哪些关键文档和任务来源、环境是否就绪、是否执行了结构/文档审计、是否发生副作用，以及当前最重要的风险与后续动作。

## 7. 约束（Constraints）

- 必须保留项目本地配置、项目覆盖和 CLI 参数的优先级逻辑，不把仓库特例硬编码进共享 skill
- 默认输出仍应围绕 `docs/takeover` 下的 takeover packet，不改变原有产物类型
- `--apply-safe-fixes` 仅限低风险目录创建，不应扩展为任意修复行为
- `--install` 只在显式启用时执行推断或配置的安装命令
- 缺失脚本、缺失工具或环境异常应尽量 soft-fail，并体现在输出中，而不是默认崩溃

## Invocation

### When to use

- 当一个新维护者或 AI 需要首次进入陌生仓库，并快速生成 takeover packet 与 onboarding 材料时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

