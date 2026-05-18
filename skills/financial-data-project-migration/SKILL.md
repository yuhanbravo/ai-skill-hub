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
- Shared assessment output protocol: [../_protocol/skill_assessment_output.md](../_protocol/skill_assessment_output.md)

## 4. 核心模式（Pattern）

### Phase-Based Migration Advisory Pattern（阶段化迁移顾问模式）

这个 pattern 的核心是把迁移建议组织成：

`scan current scripts -> classify runtime coupling -> classify migration readiness -> choose desktop-script vs package-project path -> propose target src profile -> define wrapper and test safety net -> produce first executable task package`

Input:
- 项目根目录
- 当前文件树
- Python 脚本
- Excel 资产
- 文档入口与耦合信号

Process:
- `scan`
- `coupling classification`
- `readiness classification`
- `path decision`
- `target profile planning`
- `wrapper/test planning`
- `task package output`

Output:
- 项目类型
- 运行耦合分类矩阵
- 迁移 readiness 分类
- desktop-script vs package-project 决策结论
- `src/` 目标蓝图 profile（规划型）
- legacy wrapper 策略
- 最小测试安全网
- 第一阶段可执行任务包（仅计划，不执行迁移）

### Coupling Taxonomy & Readiness Scoring（耦合分类与迁移就绪度）

对每个耦合维度使用 `0-3` 分值（0=无明显耦合，1=弱耦合，2=中耦合，3=强耦合），并给出证据路径：

1. Excel file coupling（Excel 文件耦合）
2. Wind / external data source coupling（Wind 或外部数据源耦合）
3. local absolute path coupling（本机绝对路径耦合）
4. network drive coupling（网络盘耦合）
5. current working directory coupling（当前工作目录耦合）
6. manual desktop operation coupling（人工桌面操作耦合）
7. database coupling（数据库耦合）
8. scheduler / batch coupling（调度/批处理耦合）
9. report output coupling（报表产物耦合）

Readiness 分类建议（可按总分与阻塞项联合判断）：

- `inventory_only`
  - 典型条件：存在 1 个以上强耦合阻塞项（例如手工桌面流程 + 网络盘 + 绝对路径）。
  - 建议：只做资产清单、入口清单、依赖清单和风险登记。
- `wrapper_first`
  - 典型条件：逻辑可识别，但入口耦合仍重，直接拆包风险高。
  - 建议：先加兼容 wrapper，把可纯化逻辑边界显式化。
- `module_extract_ready`
  - 典型条件：已有可复用函数片段，可在不改变外部行为前提下提取模块。
  - 建议：先抽取 `src/` 外围的纯函数或数据转换模块，再评估包化。
- `src_package_ready`
  - 典型条件：耦合可控、入口稳定、最小测试可建立。
  - 建议：进入标准 `src/` 布局规划（仍需分阶段执行，不自动重构）。

### Desktop Script vs Package Project Decision Tree（桌面脚本 vs 包化项目决策树）

按以下顺序做保守决策：

1. 是否存在强人工桌面操作 + 强外部客户端依赖（如 Wind 终端绑定）？
   - 是：`Keep as desktop script for now`，只做清单和边界识别。
2. 是否存在多个历史入口且业务方依赖固定脚本路径？
   - 是：`Add wrapper only`，先保留旧入口并增加 wrapper 层。
3. 是否能稳定识别纯计算、清洗、映射等可复用逻辑边界？
   - 是：`Extract reusable functions`，先做模块抽取建议。
4. 是否已具备最小测试安全网并能约束 I/O 副作用？
   - 是：`Introduce src/ layout`。
5. 是否已经需要可发布包、可测试接口、可复用命令入口？
   - 是：`Introduce package + tests + CLI`。
6. 是否需要跨团队服务化访问？
   - 是：`Introduce API / service layer later`（后续阶段，不在本轮执行）。

### Target `src/` Blueprint Profiles（目标 src 规划蓝图）

这些 profile 是“规划参考”，不是强制目录模板：

1. `script_wrapper_profile`
   - 适用：历史脚本多、先保留入口兼容。
   - 典型方向：`scripts/` 保留入口，`src/<pkg>/` 逐步承载纯逻辑。
2. `batch_pipeline_profile`
   - 适用：批处理、调度任务、日终/周终作业。
   - 典型方向：`src/<pkg>/pipelines`、`jobs`、`io`、`transforms`。
3. `data_service_profile`
   - 适用：已有稳定数据访问边界，计划走服务/API。
   - 典型方向：`clients`、`repositories`、`services`，接口层后置。
4. `analytics_report_profile`
   - 适用：分析与报表主导项目。
   - 典型方向：`analysis`、`metrics`、`reporting`、`templates`。

### Legacy Wrapper Strategy（旧入口兼容包装策略）

在建议迁移时，必须写出 wrapper 策略：

- wrapper purpose：保证旧脚本入口、参数和调用习惯在过渡期可用。
- compatibility window：给出兼容窗口（例如 1-2 个发布周期或 2-4 周）。
- rollback trigger：定义回滚触发条件（关键报表失败、核心表字段偏差、批量任务异常）。
- old script preservation：旧脚本保留为 thin wrapper，不删除历史入口。
- module extraction boundary：只提取纯逻辑与稳定 I/O 适配层，避免一次性搬迁全部副作用逻辑。

### Minimal Test Safety Net（最小测试安全网）

在进入模块提取或 `src/` 规划前，至少定义这些测试：

1. import smoke test：新模块与 wrapper 可以被导入。
2. sample input/output test：对代表性样本做输入输出一致性检查。
3. schema/column test：关键 DataFrame/表结构字段一致性检查。
4. idempotency or duplicate-write test（如相关）：避免重复写入或重复入库。
5. report artifact existence check（如相关）：关键报表文件是否按预期生成。

### First Executable Migration Task Package Template（首个可执行迁移任务包模板）

输出模板（用于下一轮 bounded execution，不代表本 skill 自动执行迁移）：

```md
# Task Package: <migration_step_name>

## Scope
- 本轮只做：<single bounded step>
- 本轮不做：<explicit exclusions>

## Files to Inspect
- <paths>

## Files Allowed to Change
- <paths>

## Files Not Allowed to Change
- <paths>

## Migration Readiness Class
- <inventory_only | wrapper_first | module_extract_ready | src_package_ready>

## Coupling Matrix
- Excel coupling: <0-3> (evidence: <path/line>)
- Wind/external coupling: <0-3> (evidence: <path/line>)
- Local absolute path coupling: <0-3> (evidence: <path/line>)
- Network drive coupling: <0-3> (evidence: <path/line>)
- CWD coupling: <0-3> (evidence: <path/line>)
- Manual desktop coupling: <0-3> (evidence: <path/line>)
- Database coupling: <0-3> (evidence: <path/line>)
- Scheduler/batch coupling: <0-3> (evidence: <path/line>)
- Report output coupling: <0-3> (evidence: <path/line>)

## Proposed First Step
- <wrapper creation | function extraction | inventory freeze>

## Validation Commands
- <command 1>
- <command 2>

## Rollback Notes
- trigger:
- rollback action:

## Execution Report Requirement
- 必须输出结构化 execution report：
  - Scope Restatement
  - Files Changed
  - What Changed / What Not Changed
  - Validation Performed
  - Boundary Checks
  - Risks and Assumptions
```

## 5. 核心原则（Principles）

- 先理解现状，再谈结构迁移。  
  Understand the current repository before proposing structure changes.

- 默认不改变项目，只做观察和结构化输出。  
  Do not modify the project unless explicitly allowed.

- 风险越强，建议越保守。  
  The stronger the runtime coupling, the more conservative the migration advice should be.

- 明确区分 assessment 与 execution。  
  Keep assessment output separate from execution work.

- 优先给出最小安全下一步，而不是理想化终局。  
  Prefer the smallest safe next step over an idealized end state.

- 旧入口脚本在过渡期可以保留为兼容包装层。  
  Preserve legacy entry scripts as temporary compatibility wrappers during transition.

## 6. 执行流程（Execution Steps）

1. `scan current scripts`：收集当前仓库事实。  
   读取项目根目录，检查脚本分布、Excel 资产、文档入口和运行痕迹；观察 `src/` 是否存在、根目录脚本数量与类型。

2. `classify runtime coupling`：填充耦合矩阵。  
   按 9 维耦合 taxonomy 打分并记录证据，仅观察不改造。

3. `classify migration readiness`：给出 readiness class。  
   输出 `inventory_only / wrapper_first / module_extract_ready / src_package_ready`，并解释触发条件。

4. `desktop-script vs package-project`：做路径决策。  
   使用决策树明确本轮建议停在哪一层（保持脚本、wrapper、模块抽取、src、包化+CLI）。

5. `propose target src blueprint profile`：选择规划蓝图。  
   在 `script_wrapper_profile / batch_pipeline_profile / data_service_profile / analytics_report_profile` 中选择最匹配项，必要时给出主次 profile。

6. `define wrapper strategy + minimal test safety net`：明确风险控制。  
   输出 wrapper 兼容策略与最小测试集，不触发自动重构。

7. `produce first executable migration task package`：交付下一步可执行包。  
   生成有边界的任务包模板实例，并要求后续执行方输出 execution report。

## 7. 约束（Constraints）

- 默认只做迁移 advisory，不自动移动文件、不创建 `src/` 结构、不执行重构
- 不授权自动化迁移、批量改写、CI/validator 引入
- 不得改变既有 CLI 行为或脚本原始判断逻辑，只能围绕其语义做文档标准化
- 对 Excel-heavy、Wind、网络盘、桌面环境强耦合项目，必须优先保守判断，避免 package-first 建议
- 生成报表、导出文件、缓存、本地数据和运行时资产应继续被视为非源码对象，不应被纳入源代码包
- 后续若进入结构检查、文档治理、接管或状态更新，应由其他 skill 协同处理，而不是在本 skill 内越权扩展

## Invocation

### When to use

- 当你面对一个 Excel、Wind、桌面运行或根目录脚本耦合较强的 Python 项目，需要先判断迁移边界并规划首个可执行迁移步骤时使用。

### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- References: [references/](references/)
