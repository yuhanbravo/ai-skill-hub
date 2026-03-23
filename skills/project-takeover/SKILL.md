---
name: project-takeover
description: 为陌生仓库生成可交接的 takeover packet，通过阶段化扫描、理解、结构化整理与产出，支持新维护者接管和 onboarding。
---

# Project Takeover

## 1. 背景（Problem Context）

这个 skill 用来解决项目接管时最常见的一类问题：新维护者或 AI 代理第一次进入仓库时，往往不知道环境是否可用、文档在哪里、任务从哪里来、哪些信息值得优先看，也不知道该如何快速整理出一份可继续协作的接手材料。

`project-takeover` 的目标不是替代项目本身的治理文档，而是把“首次进入一个仓库并生成接手资料”的过程阶段化、可执行化。它保留项目差异，不强依赖固定文件名，通过配置、脚本和文档扫描来生成 takeover packet，帮助后续的 onboarding、handoff 和维护接手。

它在 skill-hub 中更偏向 `project` 型 skill：重点不是单次命令，而是围绕项目接管过程组织输入、判断、整理和输出。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要为一个陌生仓库准备接手资料、onboarding 材料或 handoff 输出
- 新开发者、新维护者或 AI 代理第一次进入项目，需要快速建立项目理解
- 希望同时检查环境 readiness、结构审计、文档概览和任务来源
- 希望生成可落盘、可共享的 takeover report、onboarding summary 和欢迎说明
- 希望复用项目本地配置或外部审计脚本，而不是把规则硬编码进共享 skill

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 任务只是回答单个代码问题，而不是接管整个仓库
- 项目已经有更成熟且固定的接管流程，并且不需要额外 takeover packet
- 当前目标是持续状态更新或阶段进度同步，那更接近 `update-project-status`
- 仓库上下文极少，无法读取关键文档、配置或目录结构
- 当前不允许生成任何输出文件或执行任何检查动作

## 4. 核心模式（Pattern）

### Phase-Based Takeover Pattern（阶段化项目接管模式）

这个 pattern 的核心是把项目接管组织成四个稳定阶段：

- `scan`：扫描仓库的环境、配置、文档候选、任务来源和可用支持脚本
- `understand`：基于扫描结果建立对项目现状、约束、任务入口和主要风险的初步理解
- `structure`：把离散信息整理成可交接结构，包括文档摘要、任务来源摘要和环境结论
- `output`：生成 takeover packet，并按需要写入报告目录或同步到本地共享目录

输入是项目根目录、可选配置、可选脚本覆盖和运行参数；中间动作是阶段化检查与整理；输出是三类接管文档以及相关风险、后续动作和环境结论。

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

## 8. 风险（Risks）

- 如果把这个 skill 当成普通仓库扫描器使用，可能忽略其“生成接手材料”的核心目标
- 如果文档候选模式或任务来源模式配置不当，输出会遗漏关键上下文
- 如果直接运行 `--install` 或 `--apply-safe-fixes` 而未确认范围，可能带来不必要副作用
- 如果把扫描结果直接当成完整事实，而不区分已确认与待验证信息，接手报告容易误导新维护者
- 如果 README 与 SKILL 职责不分，调用方可能只看到命令而不了解完整阶段流程

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准接管调用

```text
请使用 `project-takeover` 处理以下仓库接管任务。

背景：
- 这是一个需要接手或 onboarding 的项目

目标：
- 生成 takeover packet，并帮助新维护者快速理解仓库

范围：
- 扫描项目环境、关键文档、任务来源和可用审计脚本
- 整理接手所需的结构化输出

约束：
- 保留项目本地配置优先级
- 不做未授权的高风险副作用

预期输出：
- `project_takeover_report.md`
- `project_onboarding_summary.md`
- `welcome_email.md`
- 风险与下一步建议
```

### 模板 2：严格阶段化执行模板

```text
请按 `project-takeover` 的方法执行本次任务。

要求：
- 先总结你对项目接管目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 明确当前使用的配置、脚本和可选参数
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <takeover | onboarding | handoff prep>
- Config path: <path-or-none>
- Report dir: <path-or-default>
- Shared dir: <path-or-none>
- Dry run: <yes-or-no>
- Apply safe fixes: <yes-or-no>
- Install: <yes-or-no>
- Structure script override: <path-or-none>
- Docs script override: <path-or-none>
```

## 10. 总结（Summary）

`project-takeover` 最适合解决“第一次进入一个仓库，如何快速建立接手理解并生成可交付的 onboarding 材料”这一类问题。它的价值不只是扫描，而是把扫描结果组织成真正可用于交接的结构化产物。

使用时最重要的边界有两条：第一，优先尊重项目本地配置和本地工具链；第二，把整个过程按 `scan → understand → structure → output` 推进，而不是跳过理解阶段直接生成报告。
