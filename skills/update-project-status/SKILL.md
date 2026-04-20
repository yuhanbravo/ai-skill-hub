---
name: update-project-status
description: "Use when refreshing project status from Git-first signals, workspace signals, and task sources to generate a handoff-ready status report."
metadata:
   triggers:
      - refresh project status from Git-first or workspace-based signals
      - generate a weekly project summary
      - merge commits and task sources into a status report
      - sync project status to a shared document
      - produce a handoff status update
   side_effects:
      - read_only
      - write_files
---
# Update Project Status

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Templates: [templates/](templates/)
- References: [references/](references/)

## 4. 核心模式（Pattern）

### Phase-Based Status Refresh Pattern（阶段化状态更新模式）

这个 pattern 的核心是把项目状态更新组织成四个稳定阶段：

- `scan`：解析配置、source mode、Git 可用性、提交范围、workspace/task 信号和同步目标
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

- `scan` → `config resolution`、`source_mode detection`、`git repository detection`、`recent commit loading`、`workspace signal resolution`、`task source resolution`、`sync target discovery`
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
   在 Git 可用时读取最近提交历史；按配置解析 `workspace_signal_paths`、`task_sources` 或 `extra_source_globs`；识别本地复制、命令执行、Confluence、Google Docs 等同步目标。此阶段默认只观察，不写文件、不发布外部内容。

3. `understand`：形成近期状态理解。  
   按关键字对提交做分类，提取外部任务项与 workspace status signals，推断下一步工作方向，并区分“已发生的进展”“可能的风险”“待继续推进的事项”。如果 Git 不可用或信号源不足，应把缺失上下文显式记录，而不是隐式补全。

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
- Git 不可用、任务源缺失或远程同步未配置时，应保留原有降级行为，不引入新的强依赖；在 no-git 场景下优先输出 workspace/task-source based refresh
- 认证信息应继续通过环境变量或项目密钥提供，不能写回配置文件或文档

## Invocation

### When to use

- 当你需要根据 Git 优先信号、workspace 信号和可用任务源刷新项目状态，并明确哪些动作会写文件或同步时使用。支持 `git` / `workspace` / `hybrid` 模式（SSOT-lite）。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
- Templates: [templates/](templates/)
- References: [references/](references/)
