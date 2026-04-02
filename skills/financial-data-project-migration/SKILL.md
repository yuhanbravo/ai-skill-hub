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

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

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

## Invocation

### When to use

- 当你面对一个 Excel、Wind、桌面运行或根目录脚本耦合较强的 Python 项目，需要先判断迁移边界时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)

