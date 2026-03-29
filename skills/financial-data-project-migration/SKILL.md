---
name: financial-data-project-migration
description: "Use when assessing migration readiness for a financial-data Python project with script sprawl, Excel assets, or Wind/Desktop coupling."
metadata:
   triggers:
      - assess financial data project migration readiness
      - classify Excel and Python script sprawl
      - recommend a safe target structure for a data project
      - evaluate Wind or desktop Excel coupling
      - draft a minimal migration todo
   side_effects:
      - read_only
      - write_files
---

# Financial Data Project Migration

## 1. 背景（Problem Context）

这个 skill 用来解决一类很具体但常见的问题：金融数据类 Python 项目往往不是标准工程仓库，而是从大量根目录脚本、Excel 资产、桌面环境依赖、Wind 数据源、网络盘路径和逐步演进出来的半成品结构开始。此时如果直接套用“建立 `src/` 并迁移代码”的通用建议，往往会过度乐观，甚至破坏真实运行边界。

`financial-data-project-migration` 的目标不是直接执行重构，而是在真正动手之前，先做一轮保守的迁移 advisory：判断项目到底是什么类型、处于什么迁移阶段、有哪些固定风险、现在最小可行的下一步是什么，以及未来目标结构应如何表达。

它在 skill-hub 中更适合作为 `project` 型 skill，因为它处理的是一个阶段化项目判断过程，而不是单次脚本检查。重点是先理解当前仓库，再组织迁移建议，而不是直接给出 package-first 方案。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要评估一个金融数据 Python 项目是否适合进入结构迁移阶段
- 仓库存在大量根目录脚本、Excel 文件、报表资产或桌面自动化依赖
- 需要判断项目属于数据提取、分析报表、批处理流水线，还是桌面 Excel + Wind 脚本系统
- 需要形成保守的目标结构建议、文件角色分类和最小迁移 TODO
- 需要在真正重构前，为后续 `file-structure-check`、`documentation-governance`、`project-takeover` 或 `update-project-status` 提供判断基础

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 项目已经是清晰稳定的 `src` 结构仓库，不再需要迁移 advisory
- 当前任务是直接移动文件、重构模块或修改运行逻辑，而不是先判断迁移边界
- 仓库并不是金融数据或 Excel / Wind / 报表耦合类项目，相关判断信号不成立
- 只需要做一般性的目录审计，那更适合 `file-structure-check`
- 当前不允许做任何项目观察、扫描或结构判断，只希望直接执行迁移动作

## 4. 核心模式（Pattern）

### Phase-Based Migration Advisory Pattern（阶段化迁移顾问模式）

这个 pattern 的核心是把迁移建议组织成 `scan -> understand -> structure -> output` 四个阶段：

- `scan`：扫描目录结构、脚本分布、Excel 资产、文档入口和运行耦合信号
- `understand`：判断项目类型、迁移阶段和固定风险，尤其识别是否属于桌面 Excel + Wind + 网络盘耦合脚本系统
- `structure`：组织目标结构建议、文件角色分类、映射示例和最小迁移 TODO
- `output`：输出迁移 advisory 结果，并把结论衔接到后续 skill 或后续阶段工作

Input:
- 项目根目录
- 当前文件树
- Python 脚本
- Excel 资产
- 文档入口与耦合信号

Process:
- `scan`
- `understand`
- `structure`
- `output`

Output:
- 项目类型
- 迁移阶段
- 固定风险
- 目标结构建议
- 映射候选与最小 TODO

这样组织的原因是，这类项目真正困难的不在“如何设计理想结构”，而在“是否已经到了能安全迁移的阶段”。先 `scan`，再 `understand`，再 `structure`，最后 `output`，可以避免跳过现实边界直接给出激进方案。

### Phase → Execution Mapping

- `scan` → `directory inspection`、`python file collection`、`excel asset collection`、`document entrypoint detection`、`runtime coupling signal detection`
- `understand` → `project type classification`、`migration stage detection`、`fixed risk extraction`、`desktop Excel / Wind conservative downgrade`
- `structure` → `target layout recommendation`、`file role classification`、`example mapping candidate generation`、`minimal migration TODO drafting`
- `output` → `migration advisory summary`、`next-step coordination with related skills`、`safe follow-up recommendations`

## 5. 核心原则（Principles）

- 先理解现状，再谈结构迁移。  
  Understand the current repository before proposing structure changes.

- 默认不改变项目，只做观察和结构化输出。  
  Do not modify the project unless explicitly allowed.

- 风险越强，建议越保守。  
  The stronger the runtime coupling, the more conservative the migration advice should be.

- 优先给出最小安全下一步，而不是理想化终局。  
  Prefer the smallest safe next step over an idealized end state.

- 旧入口脚本在过渡期可以保留为兼容包装层。  
  Preserve legacy entry scripts as temporary compatibility wrappers during transition.

## 6. 执行流程（Execution Steps）

1. `scan`：收集当前仓库事实。  
   读取项目根目录，检查顶层目录与文件分布，收集 Python 文件、Excel 资产、文档入口和可能的运行痕迹；特别观察 `src/` 是否存在、根目录脚本数量、Excel 文件占比、报表或归档目录分布。

2. `scan`：识别运行耦合信号。  
   检查是否存在 `WindPy`、`xlwings`、`openpyxl`、网络盘路径、当前工作目录依赖、脚本式 orchestration 入口，以及抓取、计算、Excel 写入混在单脚本内的单体脚本信号。此阶段默认只观察，不做任何文件移动或结构写入。

3. `understand`：判断项目类型与迁移阶段。  
   基于脚本命名、依赖信号、目录结构和资产分布，判断项目更接近 `data-extraction`、`analysis-reporting`、`batch-pipeline`、`migration-transition`，还是 `desktop_excel_wind_script_project`。如果 Excel 资产和桌面运行耦合较强，应优先下调到 `冻结现状 / 建立清单 / 边界识别`，而不是直接给出 package-first 建议。

4. `understand`：提炼固定风险。  
   明确是否存在外部桌面环境依赖、网络盘依赖、当前工作目录依赖、Excel 资产角色不清等固定风险，并区分哪些风险会阻止立即迁移，哪些风险只影响后续阶段设计。

5. `structure`：组织迁移 advisory。  
   在理解当前阶段后，整理目标结构建议、文件角色分类、示例映射候选和最小迁移 TODO；强调生成产物、缓存、本地数据和运行时资产不应直接混入 `src/` 包结构。

6. `output`：输出下一阶段建议。  
   形成迁移 advisory 结果，说明当前项目类型、迁移阶段、固定风险、目标结构方向、保守建议和后续协同 skill；如果项目尚未具备安全迁移条件，应把结论明确写成 inventory-first 或 boundary-first，而不是伪装成准备就绪。

## 7. 约束（Constraints）

- 默认只做迁移 advisory，不自动移动文件、不创建 `src/` 结构、不执行重构
- 不得改变既有 CLI 行为或脚本原始判断逻辑，只能围绕其语义做文档标准化
- 对 Excel-heavy、Wind、网络盘、桌面环境强耦合项目，必须优先保守判断，避免 package-first 建议
- 生成报表、导出文件、缓存、本地数据和运行时资产应继续被视为非源码对象，不应被纳入源代码包
- 后续若进入结构检查、文档治理、接管或状态更新，应由其他 skill 协同处理，而不是在本 skill 内越权扩展

## 8. 风险（Risks）

- 如果把脚本型金融项目误判成普通 Python 工程，迁移建议会过于激进
- 如果 Excel 资产数量被误当成唯一信号，可能把普通分析项目误降级为高耦合桌面系统
- 如果忽略网络盘、当前工作目录和桌面依赖，目标结构建议会脱离真实运行边界
- 如果 example mapping candidates 过于抽象，输出会失去对当前仓库的可操作性
- 如果过早建议大规模 `src` 迁移，可能破坏现有调度、操作路径或人工执行习惯

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准迁移评估模板

```text
请使用 `financial-data-project-migration` 处理以下任务。

背景：
- 这是一个金融数据 Python 项目，当前结构可能处于脚本堆积或迁移过渡状态

目标：
- 判断项目类型与迁移阶段，并输出最小安全迁移建议

范围：
- 扫描目录结构、脚本分布、Excel 资产和运行耦合信号
- 输出目标结构建议、文件角色分类和最小 TODO

约束：
- 默认不改变项目，只做观察和结构化输出
- 不直接执行文件迁移或 package-first 重构

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- 项目类型判断
- 迁移阶段判断
- 固定风险
- 目标结构建议
- 最小迁移 TODO
```

### 模板 2：严格阶段化执行模板

```text
请按 `financial-data-project-migration` 的方法执行本次任务。

要求：
- 先总结你对当前迁移评估目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 显式说明是否存在 Excel / Wind / 网络盘 / 当前工作目录依赖
- 如果项目风险较高，优先输出保守建议，而不是直接建议迁移到 `src`
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Special context: <none-or-extra-notes>
- Need mapping candidates: <yes-or-no>
- Need minimal TODO: <yes-or-no>
```

## 10. 总结（Summary）

`financial-data-project-migration` 最适合解决“一个金融数据脚本项目是否已经具备安全迁移条件，以及下一步最小可行迁移动作是什么”这一类问题。它的价值不在于直接改结构，而在于先建立保守、可信、贴近真实运行边界的迁移判断。

使用时最重要的边界是两条：第一，默认只做观察和结构化输出，不自动迁移项目；第二，越是 Excel、Wind、网络盘、桌面环境耦合强的仓库，越要优先采取 inventory-first 和 boundary-first 的保守建议。

## Invocation

### When to use

- 当你面对一个 Excel、Wind、桌面运行或根目录脚本耦合较强的 Python 项目，需要先判断迁移边界时使用。

### Input Example

```text
Use financial-data-project-migration for this task.

task_description:
- Assess whether this financial-data Python repository is ready for structure migration.

constraints:
- Do not move files or create a src/ layout.
- Keep recommendations conservative if desktop Excel or Wind coupling is detected.

expected_output:
- Migration advisory
- Risk summary
- Minimal next-step todo

context_files:
- *.py
- *.xlsx
- README.md
```

### Output Example

```text
execution_plan:
- Scan Python scripts, Excel assets, and document entrypoints.
- Classify project type and migration stage.
- Produce a conservative migration advisory.

changes_made:
- No project files were modified.
- Produced a migration readiness assessment.

files_touched:
- README.md
- root Python scripts
- Excel asset inventory

risks:
- Wind/Desktop coupling may block any immediate package-first migration.
```
