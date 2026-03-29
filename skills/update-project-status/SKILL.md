---
name: update-project-status
description: "Use when refreshing project status from Git history, merging task sources, or generating a handoff-ready status report."
metadata:
   triggers:
      - refresh project status from Git history
      - generate a weekly project summary
      - merge commits and task sources into a status report
      - sync project status to a shared document
      - produce a handoff status update
   side_effects:
      - read_only
      - write_files
      - requires_git
---

# Update Project Status

## 1. 背景（Problem Context）

这个 skill 用来解决项目状态维护中的一个常见问题：仓库里有提交历史，也可能有任务板、Jira 导出、Trello 导出或命令行来源，但这些信息通常是分散的。每次要做周报、阶段总结、handoff 状态说明或对外发布时，都要重复读取提交、筛任务、整理重点，再把结果写进状态文档。

`update-project-status` 的作用不是发明新的状态体系，而是把“收集近期变化并生成状态输出”的流程稳定下来。它保留原有 CLI、默认输出和同步机制，通过配置、Git 历史和外部任务源生成项目状态文档、状态日志，以及按配置触发的同步结果。

它在 skill-hub 中更适合被视为 `project` 型 skill，因为重点不是单个命令本身，而是围绕项目状态更新这一过程组织输入、判断、结构化输出和发布动作。

## 2. 适用场景（When to Use）

适合在以下场景使用：

- 需要基于近期 Git 提交生成或刷新项目状态报告
- 希望把仓库提交与任务来源信息合并成统一状态文档
- 需要准备阶段总结、handoff 状态说明或对外同步的项目更新
- 需要按配置把状态输出同步到本地副本、命令目标或远程文档目标
- 希望在不改变原始项目结构的前提下，持续生成可追踪的状态文档和日志

## 3. 不适用场景（When NOT to Use）

以下情况不适合使用这个 skill：

- 当前目标是首次接管仓库，而不是更新持续状态，那更接近 `project-takeover`
- 项目没有可用的 Git 历史，也没有任何替代任务来源，无法形成有效状态摘要
- 任务只需要解释某个提交或某个文件变化，而不是输出完整状态文档
- 当前不允许写入状态文件、日志文件或执行同步动作
- 团队已有强制的本地状态发布流程，且不需要额外的共享 skill 封装

## 4. 核心模式（Pattern）

### Phase-Based Status Refresh Pattern（阶段化状态更新模式）

这个 pattern 的核心是把项目状态更新组织成四个稳定阶段：

- `scan`：解析配置、Git 可用性、提交范围、任务源和同步目标
- `understand`：理解近期工作内容、任务信号、风险和待办方向
- `structure`：把离散输入整理成状态文档、状态日志和同步负载
- `output`：写入状态文件、追加日志，并按配置执行同步或安装 post-commit hook

Input:
- 项目根目录
- 配置
- 提交限制
- 可选输出覆盖

Process:
- `scan`
- `understand`
- `structure`
- `output`

Output:
- 状态 markdown
- 状态更新日志
- 可选同步或 hook 安装结果

这样组织的原因是，状态更新不只是“跑一个脚本”，而是一个从事实采集到内容整理再到发布的项目过程。把它按阶段建模后，AI 更容易稳定执行，并在每一步维持边界感和结果可解释性。

### Phase → Execution Mapping

- `scan` → `config resolution`、`git repository detection`、`recent commit loading`、`task source resolution`、`sync target discovery`
- `understand` → `commit classification`、`external task extraction`、`next-task inference`、`risk signal identification`
- `structure` → `status document building`、`status log entry building`、`sync payload preparation`
- `output` → `status file write`、`log file append`、`shared/local/remote sync execution`、`post-commit hook generation`

## 5. 核心原则（Principles）

- 先采集近期事实，再总结项目状态。  
  Collect recent project facts before summarizing status.

- 默认不改变项目，只做观察和结构化输出。  
  Do not modify the project unless explicitly allowed.

- 状态判断要基于配置与可见信号。  
  Base status interpretation on configuration and observable signals.

- 输出要服务持续同步与后续协作。  
  Produce outputs that support ongoing sync and follow-up collaboration.

- 发布动作要区分本地生成与外部同步。  
  Separate local status generation from external publishing actions.

## 6. 执行流程（Execution Steps）

1. `scan`：解析状态更新输入。  
   读取项目根目录、默认配置、项目覆盖配置和显式参数；确认 `--config`、`--status-file`、`--log-file`、`--shared-doc`、`--limit`、`--dry-run` 等输入，并识别当前是否为 Git 仓库，以及是否存在可用任务源与同步目标。

2. `scan`：收集原始状态信号。  
   在 Git 可用时读取最近提交历史；按配置解析 `task_sources` 或 `extra_source_globs`；识别本地复制、命令执行、Confluence、Google Docs 等同步目标。此阶段默认只观察，不写文件、不发布外部内容。

3. `understand`：形成近期状态理解。  
   按关键字对提交做分类，提取外部任务项，推断下一步工作方向，并区分“已发生的进展”“可能的风险”“待继续推进的事项”。如果 Git 不可用或任务源为空，应把缺失上下文显式记录，而不是隐式补全。

4. `structure`：整理状态输出骨架。  
   基于近期提交、任务来源和配置，构建状态文档内容、状态日志条目和同步所需负载；明确哪些内容来自 Git，哪些来自外部任务源，哪些属于推断结论。这里仍保持非侵入原则，除非进入明确输出阶段，否则不应修改项目文件。

5. `output`：写入状态结果。  
   按配置或参数覆盖路径写入状态 markdown 和状态日志；若配置了 `shared_doc` 或 `sync_targets`，则在本地写入后执行对应同步；如果启用 `--dry-run`，则只预览将要写入和同步的结果而不真正改动文件。

6. 处理显式附加动作。  
   只有在用户明确要求时，才运行 `install_post_commit_hook.py` 安装 `.git/hooks/post-commit`。该动作属于显式修改项目行为的附加步骤，不应与默认状态生成混为一体。

7. 输出执行回顾。  
   在最终结果中说明本次使用的配置与参数、提交与任务源覆盖范围、实际写入的状态文件和日志文件、是否执行了同步、是否安装了 hook，以及当前主要风险与待确认项。

## 7. 约束（Constraints）

- 不得改变既有 CLI 参数、默认文件路径、同步目标类型或 hook 安装方式
- 默认只做观察和结构化输出；除写入状态文件、日志文件及显式要求的同步或 hook 安装外，不应修改项目内容
- `--dry-run` 必须保持“预览而不写入”的原有语义
- Git 不可用、任务源缺失或远程同步未配置时，应保留原有降级行为，不引入新的强依赖
- 认证信息应继续通过环境变量或项目密钥提供，不能写回配置文件或文档

## 8. 风险（Risks）

- 如果把提交分类结果当成精确事实，而忽略其关键字启发式本质，状态总结可能产生偏差
- 如果外部任务源过旧、缺失或格式不一致，状态报告可能遗漏真实进展或待办
- 如果未区分“本地写入”和“外部同步”，可能在未审阅内容前就发布到共享目标
- 如果忽略非侵入原则，可能把状态刷新误当成允许任意修改项目的操作
- 如果只看 README 而不看完整 SKILL，调用方可能低估 hook 安装和同步动作的边界

## 9. Prompt 模板（Reusable Prompt）

### 模板 1：标准状态刷新模板

```text
请使用 `update-project-status` 处理以下任务。

背景：
- 需要根据近期 Git 提交和可用任务来源刷新项目状态

目标：
- 生成或更新状态文档，并整理关键进展、风险和待办

范围：
- 读取最近提交
- 合并可用任务源
- 生成状态 markdown 与状态日志
- 如已授权，再执行同步

约束：
- 默认不改变项目，只做观察和结构化输出
- 未明确授权时，不安装 hook，不做额外发布

预期输出：
- 按 `scan -> understand -> structure -> output` 推进
- 刷新的状态文档
- 刷新的状态日志
- 风险、待办与后续动作摘要
```

### 模板 2：严格阶段化执行模板

```text
请按 `update-project-status` 的方法执行本次任务。

要求：
- 先总结你对本次状态更新目标的理解
- 按 `scan -> understand -> structure -> output` 四个阶段推进
- 显式说明 `Phase -> Execution Mapping`
- 明确哪些动作只是观察，哪些动作会写文件或同步
- 输出结果、风险和待确认项

任务内容：
- Project root: <project-root>
- Primary goal: <status refresh | recent change summary | publish status>
- Config path: <path-or-none>
- Status file override: <path-or-none>
- Log file override: <path-or-none>
- Shared doc override: <path-or-none>
- Commit limit: <n-or-default>
- Dry run: <yes-or-no>
- Install post-commit hook: <yes-or-no>
```

## 10. 总结（Summary）

`update-project-status` 最适合解决“如何把近期 Git 变化与任务来源整理成持续可维护的项目状态输出”这一类问题。它的价值不只是写一份状态文档，而是把状态采集、理解、结构化和发布串成稳定流程。

使用时最重要的边界有两条：第一，先按 `scan → understand → structure → output` 建立状态结论，再进入写入与同步；第二，默认坚持非侵入原则，只在显式授权时执行额外发布或 hook 安装动作。

## Invocation

### When to use

- 当你需要根据近期 Git 历史和可用任务源刷新项目状态，并明确哪些动作会写文件或同步时使用。

### Input Example

```text
Use update-project-status for this task.

task_description:
- Refresh the project status report from recent Git history and current task sources.

constraints:
- Do not install hooks unless explicitly requested.
- Treat external sync as opt-in.

expected_output:
- Updated status summary
- Risk and next-step summary
- Optional sync decision

context_files:
- .git/
- README.md
- status config files
```

### Output Example

```text
execution_plan:
- Load recent Git history and configured task sources.
- Build the status summary and log entry.
- Decide whether any sync action is authorized.

changes_made:
- Generated a refreshed status summary.
- Did not install post-commit hook.

files_touched:
- .git/
- status markdown output
- status log output

risks:
- Missing external task sources may reduce summary completeness.
```
