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

对每个耦合维度使用 `0-3` 分值（0=无明显耦合，1=弱耦合，2=中耦合，3=强耦合），并给出证据路径。评分只用于 advisory，不自动授权改造。

1. Excel file coupling（Excel 文件耦合）
   - 观察：硬编码 workbook/sheet 名称、宏、公式依赖、人工打开保存步骤、共享 Excel 模板。
   - 风险：数据输入和业务逻辑混在文件状态中，直接搬迁容易改变计算口径。
2. Wind / external data source coupling（Wind 或外部数据源耦合）
   - 观察：WindPy、桌面终端、行情客户端、HTTP/SDK token、外部系统登录状态。
   - 风险：运行依赖不可在普通 CI 或无桌面环境中复现。
3. absolute local path coupling（本机绝对路径耦合）
   - 观察：`C:\...`、`D:\...`、用户目录、桌面路径、单机安装路径。
   - 风险：迁移后路径不可用，且可能泄露本机环境假设。
4. network drive coupling（网络盘耦合）
   - 观察：盘符映射、UNC 路径、共享目录、权限依赖、手动同步目录。
   - 风险：权限、锁文件、延迟和离线状态影响可重复运行。
5. current working directory coupling（当前工作目录耦合）
   - 观察：相对路径基于启动目录、`os.chdir`、从 IDE 或批处理目录启动才成功。
   - 风险：包化后入口变化会改变文件解析位置。
6. manual desktop operation coupling（人工桌面操作耦合）
   - 观察：复制粘贴、手动下载、弹窗确认、Excel 刷新、人工改文件名。
   - 风险：自动化前缺少可验证边界，必须先记录人工步骤。
7. database coupling（数据库耦合）
   - 观察：直连生产库、存储过程、写表副作用、隐式 schema、共享账号。
   - 风险：迁移测试可能误写真实环境或改变事务语义。
8. scheduler / batch coupling（调度/批处理耦合）
   - 观察：Windows Task Scheduler、bat 文件、crontab、手工日终顺序、依赖前置产物。
   - 风险：单脚本改动可能破坏批处理顺序、重跑策略或时间窗口。
9. report output coupling（报表产物耦合）
   - 观察：固定输出文件名、覆盖写、邮件附件、监管/客户报表、人工归档路径。
   - 风险：路径或格式变化会影响下游阅读、归档或审计。

Readiness 分类必须同时写明使用条件、允许事项、不授权事项和下一步：

- `inventory_only`
  - When to use：存在强人工桌面流程、强外部客户端依赖、生产数据库写入不清、网络盘/绝对路径密集，或无法用样本数据复现。
  - Allows：资产清单、入口清单、依赖清单、耦合矩阵、风险登记、样本数据需求说明。
  - Does not authorize：移动文件、创建 `src/`、抽取模块、改入口、接触真实生产数据或执行迁移。
  - Next safe step：冻结 inventory，向维护者确认真实入口、样本数据和不可变输出口径。
- `wrapper_first`
  - When to use：业务方依赖旧脚本路径或运行习惯，逻辑边界可见但入口/路径/调度耦合仍重。
  - Allows：设计兼容 wrapper、声明参数/环境约束、选择一个无副作用或低副作用的第一步边界。
  - Does not authorize：删除旧脚本、改变 CLI/批处理行为、大规模搬迁副作用逻辑、强制包化。
  - Next safe step：保留旧入口，先让 wrapper 调用原逻辑或一个小的已验证函数边界。
- `module_extract_ready`
  - When to use：可识别纯计算、清洗、映射、schema 标准化等可复用逻辑，且样本输入/输出可验证。
  - Allows：提取小型模块、增加 import smoke/sample/schema 测试、保持旧入口输出不变。
  - Does not authorize：重排项目结构、引入服务层、改数据库写入策略、一次性迁移全部脚本。
  - Next safe step：抽取一个低耦合函数或文件级模块，并用 wrapper 或旧脚本继续承接入口。
- `src_package_ready`
  - When to use：耦合可控、入口稳定、样本数据可用、最小测试安全网可建立，且维护者接受 staged package path。
  - Allows：规划 `src/` layout profile、分阶段移动可复用模块、添加测试与可选 CLI 入口。
  - Does not authorize：自动重构、删除兼容入口、默认新增 API/service、改变真实调度或生产写入。
  - Next safe step：生成一个 bounded task package，先迁移最小模块或 wrapper-to-`src` 调用链。

### Desktop Script vs Package Project Decision Tree（桌面脚本 vs 包化项目决策树）

按以下顺序做保守决策，并把结论写成“建议路径”，不是直接执行许可：

1. 是否存在强人工桌面操作 + 强外部客户端依赖（如 Wind 终端绑定）？
   - 是：`Keep as desktop script for now`，只做清单、运行手册、样本数据需求和风险边界。
2. 是否存在多个历史入口、批处理或业务方依赖固定脚本路径？
   - 是：`Add compatibility wrapper`，先保留旧入口，并让 wrapper 逐步隔离参数、路径和环境。
3. 是否能稳定识别纯计算、清洗、映射、schema 归一化等可复用逻辑边界？
   - 是：`Extract reusable modules`，先抽取一个小模块，旧脚本继续负责外部行为。
4. 是否已具备最小测试安全网并能约束 I/O 副作用？
   - 是：`Move toward src/ layout`，仅迁移已验证模块，不把 `src/` 当成全量搬家命令。
5. 是否已经需要可测试接口、可复用命令入口或团队内重复调用？
   - 是：`Add CLI/tests`，优先覆盖旧入口等价性和样本输出，不默认改调度。
6. 是否需要跨团队服务化访问、长期 API、权限模型或在线系统集成？
   - 是：`Defer API/service layer`，把服务化写入后续任务包；本 skill 只记录前置条件与风险。

### Target `src/` Planning Profiles（目标 src 规划蓝图）

这些 profile 是 planning-only profiles，不是强制目录结构，也不代表必须创建 `src/`。输出时可以选择主 profile 和 fallback profile。

1. `script_wrapper_profile`
   - Use when：历史脚本多、旧路径被批处理/人工手册引用、需要兼容窗口。
   - Planning direction：旧入口保留在原位置或 `scripts/`，`src/<pkg>/` 只逐步承载纯逻辑和稳定适配层。
   - First step：让一个旧脚本通过 wrapper 调用一个小的可测试函数。
2. `batch_pipeline_profile`
   - Use when：日终/周终批处理、调度任务、顺序依赖、重跑和幂等性是主要风险。
   - Planning direction：把 pipeline step、I/O adapter、transform、job config 分层表达。
   - First step：抽出一个无生产写入的 transform，并定义重跑/重复写入检查。
3. `data_service_profile`
   - Use when：数据访问边界相对稳定，未来可能由多个消费者复用。
   - Planning direction：把 external clients、repositories、services 的责任分开；API/service layer 后置。
   - First step：先封装只读 client 或 repository 边界，不创建在线服务。
4. `analytics_report_profile`
   - Use when：分析、指标、Excel/HTML/PDF 报表或归档产物是核心输出。
   - Planning direction：把 metrics、reporting、template、artifact output 规划为可测试边界。
   - First step：用样本数据验证一个报表 artifact 存在、schema 稳定、文件名策略不变。

### Legacy Wrapper Strategy（旧入口兼容包装策略）

在建议迁移时，必须写出 wrapper 策略；wrapper 是过渡控制面，不是掩盖不受控重构的理由。

- preserving old entrypoints：旧脚本路径、文件名、参数和调用习惯默认保留，除非任务包明确授权变更。
- extracting logic into modules：先提取纯逻辑、schema 标准化、只读数据转换或稳定 I/O adapter；不把所有副作用一起搬入模块。
- compatibility window：给出兼容窗口（例如 1-2 个发布周期或 2-4 周），最终由维护者确认。
- rollback trigger：关键报表缺失、核心字段偏差、批处理失败、重复写入、数据库异常或业务方无法按原方式运行。
- old script preservation：旧脚本保留为 thin wrapper 或 frozen legacy entry；不得在首轮删除。
- wrapper retirement condition：新入口连续通过样本/生产影子验证，旧入口无调用者，回滚窗口结束，并有维护者确认。
- first-step extraction boundary：首轮只选择一个低耦合、可测试、可回滚的函数/模块/adapter；不做跨项目或跨目录大搬迁。

### Minimal Test Safety Net（最小测试安全网）

在进入模块提取或 `src/` 规划前，至少定义这些测试；默认使用 sample data / no-real-data-first，除非任务包明确授权真实数据访问。

1. import smoke test：新模块、wrapper、旧入口调用链可以被导入或以 dry-run 方式加载。
2. sample input/output test：对代表性样本做输入输出一致性检查，记录样本来源和脱敏假设。
3. schema/column test：关键 DataFrame、Excel sheet、数据库结果或报表字段保持一致。
4. idempotency or duplicate-write test（如相关）：批处理、写库、导出、归档任务不得重复写入或重复入库。
5. report artifact existence check（如相关）：关键报表文件、命名规则、sheet 名称或导出目录按预期生成。
6. side-effect boundary check：需要写入文件、数据库、网络盘或发送邮件时，必须先使用临时目录、样本库或 dry-run。

### First Executable Migration Task Package Template（首个可执行迁移任务包模板）

输出模板（用于下一轮 bounded execution，不代表本 skill 自动执行迁移）。模板必须实例化到一个最小可执行步骤，并保留 assessment 与 execution 分离：

```md
# Task Package: <migration_step_name>

## Scope
- 本轮只做：<single bounded step>
- 本轮不做：<explicit exclusions>
- Advisory source：<assessment report / migration planning note>

## Files to Inspect
- <paths>

## Files Allowed to Change
- <paths>

## Files Not Allowed to Change
- <paths>

## Migration Readiness Class
- <inventory_only | wrapper_first | module_extract_ready | src_package_ready>
- Rationale: <why this class was chosen>

## Desktop Script vs Package Decision
- Recommended path: <keep desktop script | compatibility wrapper | extract reusable module | move toward src layout | add CLI/tests | defer API/service>
- Deferred path(s): <what is intentionally not happening now>

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

## Target Planning Profile
- Primary profile: <script_wrapper_profile | batch_pipeline_profile | data_service_profile | analytics_report_profile>
- Fallback profile: <optional>
- Note: planning profile only; not a mandatory folder template.

## Legacy Wrapper Strategy
- old entrypoint preservation:
- first-step extraction boundary:
- compatibility window:
- rollback trigger:
- wrapper retirement condition:

## Minimal Test Safety Net
- import smoke test:
- sample input/output test:
- schema/column test:
- idempotency or duplicate-write test, if relevant:
- report artifact existence check, if relevant:
- no-real-data / sample-data-first assumption:

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
  - Deferred Follow-ups
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
