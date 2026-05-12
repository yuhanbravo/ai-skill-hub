# Invocation Examples

这些示例用于说明：如何先用 `workflow-bootstrap` 完成 workflow shell 与 runtime profile 的边界对齐，再把 task package / bounded execution / execution report 协议交给 `chatgpt-handoff-pilot`。

> Active canonical policy：本文件采用“中文为主、英文术语保留”的 active canonical 形式；不维护中英文双主本以避免 drift；旧版本如需保留仅作为 historical reference。

## Example 1: Review a non-git project-side trial

使用 `workflow-bootstrap` 评估一个 project-side 试跑是否保持薄入口与证据线分工。

Example prompt:

```text
Use workflow-bootstrap to review a non-git project-side trial.
Confirm that AGENTS.md stays the master thin entry, .github/copilot-instructions.md stays a Copilot-specific thin adapter, tasks/ is the primary trace path for task packages and execution reports, docs/HANDOFF.md and status surfaces only keep minimal closure, and archive/ remains historical-only.
Do not redefine the handoff protocol.
```

Expected framing:

- workflow shell 与 role split 在 scope 内
- task package / bounded execution / execution report protocol 仍由 `chatgpt-handoff-pilot` 持有
- project-local facts 保持 project-local，不进入 canonical guidance

## Example 2: Prepare non-git runtime conventions

使用 `workflow-bootstrap` 描述通用 non-git / low-git 运行约定，再决定是否调整 project-side thin entry。

Example prompt:

```text
Use workflow-bootstrap to draft a generic non-git runtime profile for a project-side pilot.
Keep tasks/ as the primary evidence directory, execution reports as the main per-task evidence trail, docs/HANDOFF.md and status docs as minimal closure only, and archive/ as inactive history.
Do not add new validators, automation, CI, hooks, or rollout tooling.
```

Expected framing:

- 输出停留在 workflow-shell / runtime profile 层
- 约定是保守、可选、项目感知的，不是全仓强制
- 不引入新的 task package schema

## Example 3: Hand off bounded execution cleanly

先用 `workflow-bootstrap` 对齐壳层，再切换到 `chatgpt-handoff-pilot` 执行 bounded execution。

Example prompt:

```text
First use workflow-bootstrap to align a role-based workflow shell for a low-git project-side task, using Copilot-as-Drafter and Codex-as-Implementer only as adapter examples if useful.
Then prepare the actual task package through chatgpt-handoff-pilot, keeping tasks/ as the artifact path and execution reports as the main evidence line.
Do not move per-task detail into docs/HANDOFF.md or reactivate archive/ as the active workflow line.
```

Expected framing:

- `workflow-bootstrap` 定义 shell、边界与证据放置建议
- `chatgpt-handoff-pilot` 持有 task package / bounded execution / execution report protocol
- active workflow line 留在当前 task artifacts，而非 historical surfaces

## Example 4: Move from tool-name workflow to role-based handoff

将 tool-name-first 表达改写为 role-chain-first，再把协议细节交回 `chatgpt-handoff-pilot`。

Example prompt:

```text
Use workflow-bootstrap to restate this workflow as Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer.
Treat Copilot, Codex, ChatGPT, Cline, and DeepSeek only as adapter examples, not canonical requirements.
Keep task package, bounded execution, and execution report protocol ownership with chatgpt-handoff-pilot.
```

Expected framing:

- role boundary 与阶段切换清晰
- task package review 是实现前 Safety Gate
- tool names 仅作 adapter examples，不是 requirements

## Example 5: Select review tier before bounded execution

使用 `workflow-bootstrap` 的 review tier 指引，在执行前确定 Reviewer 的审阅强度（advisory）。

Example prompt:

```text
Use workflow-bootstrap as Reviewer to classify this task package as Light Review, Standard Review, or Heavy Review.
Keep the tier advisory, preserve chatgpt-handoff-pilot protocol ownership, and do not treat runtime pack or automation examples as implementation authorization.
```

Expected framing:

- review tier 支持 Reviewer 判断
- `chatgpt-handoff-pilot` 仍是 protocol owner
- runtime pack / automation examples 不构成 implementation authorization

## Example 6: Review runtime pack minimal surfaces

使用 `workflow-bootstrap` 检查 runtime pack minimal surface guidance 是否仍薄、仍可选。

Example prompt:

```text
Use workflow-bootstrap to review runtime pack minimal surface guidance.
Confirm that AGENTS.md, Copilot instructions, and task artifacts are treated as project-side thin entries or evidence indexes, not canonical copies or mandatory global files.
Keep task package and execution report protocol ownership with chatgpt-handoff-pilot.
```

Expected framing:

- runtime pack guidance 维持 project-aware 且 optional
- `skills/` 仍是 canonical source
- deferred surfaces（如 .github/instructions、.github/agents、tool adapters、validators、automation）不是 implementation targets

## Transition: from invocation example to orchestration instance

当 invocation example 已完成 workflow-shell 对齐后，可用下面 bridge prompt 切到 `../orchestration_snippets.md` 的最小编排实例。

```text
Workflow shell is aligned. Now switch to the minimal orchestration instance:
1) Apply Boundary lock (Step 0).
2) Run Drafter -> Reviewer (Safety Gate) -> Implementer -> Reporter -> Final Reviewer (Closure Gate).
3) If Reviewer is not Pass, rollback to Drafter (max 2 rounds).
4) If Final Reviewer is No-Go, rollback to Implementer or Reporter with minimum backfill.
5) Use explicit [PHASE-SWITCH] statements whenever one tool continues across role transitions.
Keep chatgpt-handoff-pilot as protocol owner and avoid duplicating protocol body text.
```
