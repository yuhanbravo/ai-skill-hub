# workflow-bootstrap 角色协议演化蓝图

Status: Draft  
Scope: `workflow-bootstrap` / non-git workflow / role-based AI collaboration  
Source: non-git workflow pilot、`workflow-bootstrap` runtime profile 回灌、角色协议演化讨论

---

## 1. 文档目的

本文档用于定义 `workflow-bootstrap` 的未来演化蓝图。

核心方向是：从当前偏工具名驱动的协作方式：

```text
Copilot 起草 / Codex 施工
```

逐步升级为更稳定、更可迁移的角色协议：

```text
Drafter → Reviewer → Implementer → Reporter → Final Reviewer
```

本文档不是当前执行协议，也不替代 `chatgpt-handoff-pilot`。

`workflow-bootstrap` 应继续聚焦：

- workflow shell：工作流壳层
- role split：角色分工
- runtime profile：运行时画像
- project-side workflow bootstrap guidance：项目侧工作流启动指导
- tool-agnostic collaboration framing：工具无关的协作框架

`chatgpt-handoff-pilot` 继续负责：

- task package protocol：任务包协议
- bounded execution protocol：边界化执行协议
- execution report protocol：执行报告协议

---

## 2. 当前设计判断

前一轮 non-git / low-git pilot 已验证出若干有效经验：

- 在 non-git / low-git bounded work 中，`tasks/` 可作为 task package 和 execution report 的 preferred project-local evidence path；但如果项目已经有更清晰的既有位置，不应强制迁移。
- task package 与 execution report 成对落盘，有助于补足 Git history 不充分的问题。
- execution report 可以作为 per-task evidence trail。
- handoff / status 不应变成 per-task trace log，只适合做 minimal closure。
- `archive/` 应保持 historical / inactive，不应恢复为 active workflow line。
- `AGENTS.md` 可以作为 project-side master thin entry。
- `.github/copilot-instructions.md` 可以作为 Copilot-specific thin adapter。
- `.github/copilot-instructions.zh-CN.md` 这类翻译镜像应保持 translated mirror 定位，不应成为第二规则库。
- `tasks/README.md` 可以作为 lightweight task evidence index，帮助人类和 AI agent 快速理解多轮任务链。

这些结论应被保守吸收。项目侧事实、业务路径、环境命令不应直接复制进 canonical skill guidance。

---

## 3. Ownership Boundary

`workflow-bootstrap` 的职责是定义：

```text
什么时候、以什么方式，把一个项目工作流引导到 task package / bounded execution / execution report 机制中。
```

但它不重新定义这些协议本身。

推荐长期边界表述：

```text
workflow-bootstrap defines the workflow shell, role split, and runtime profile.
chatgpt-handoff-pilot owns the task package, bounded execution, and execution report protocols.
```

中文口径：

```text
workflow-bootstrap 负责工作流壳层、角色分工和运行时画像；
chatgpt-handoff-pilot 负责 task package、bounded execution 和 execution report 协议。
```

这条边界应贯穿所有后续 phase。

---

## 4. 目标架构

长期目标不是维护一套固定的 “Copilot + Codex” 工作流，而是形成：

```text
Role protocol + Runtime profile + Thin project adapters
```

即：

```text
角色协议 + 运行时画像 + 项目侧薄适配层
```

目标分层如下：

```text
workflow-bootstrap
  ↓
role protocol
  ↓
runtime profile
  ↓
project-side thin adapters
  ↓
task package / bounded execution / execution report handoff
```

其中：

- `workflow-bootstrap` 不应成为第二套 execution protocol；
- project-side adapter 不应成为第二规则库；
- tool-specific guidance 只能在角色协议稳定后作为 optional adapter 出现；
- 任何工具名都不应成为 canonical requirement。

---

## 5. Phase 0：Non-git Runtime Profile Absorption

### 5.1 状态

已完成或基本完成。

### 5.2 目标

将 non-git / low-git pilot 中已经验证的通用经验吸收到 `workflow-bootstrap`，但不复制项目侧事实。

### 5.3 已完成或预期产物

```text
skills/workflow-bootstrap/non_git_runtime_profile.md
skills/workflow-bootstrap/examples/invocation_examples.md
skills/workflow-bootstrap/SKILL.md
```

### 5.4 核心内容

- non-git / low-git runtime profile
- `tasks/` as preferred project-local evidence path，而不是 mandatory global path
- `archive/` as inactive historical reference
- handoff / status as minimal closure，而不是 per-task trace log
- `workflow-bootstrap` / `chatgpt-handoff-pilot` ownership boundary
- invocation examples 中的 non-git handoff framing

### 5.5 验收标准

- `tasks/` 没有被写成所有项目必须使用的路径。
- `archive/` 没有被恢复为 active workflow line。
- `workflow-bootstrap` 没有声称拥有 task package / bounded execution / execution report 协议。
- non-git runtime guidance 保持 soft / contextual / project-aware。
- project-local facts 没有进入 canonical skill guidance。

### 5.6 不做事项

- 不新增 validator。
- 不新增 CI。
- 不创建 `tool_adapters/`。
- 不创建 `.github/instructions/`。
- 不创建 `.github/agents/`。
- 不把 `tasks/` 写成全项目强制规则。

---

## 6. Phase 1：Role Split Canonicalization

### 6.1 状态

下一阶段优先事项。

### 6.2 目标

将当前 Copilot / Codex 协作经验抽象为工具无关的角色协议。

### 6.3 核心角色链

```text
Drafter
  ↓
Reviewer
  ↓
Implementer
  ↓
Reporter
  ↓
Final Reviewer
```

### 6.4 角色定义

| Role | 中文定位 | 核心职责 | 不负责 |
|---|---|---|---|
| Drafter | 起草者 | 起草 task package、workflow plan 或 bounded scope proposal | 不在未经 review 的情况下直接施工 |
| Reviewer | 审包者 | 检查路径、scope、authorized files、out of scope、acceptance criteria、ownership boundary | 不随意扩大任务范围 |
| Implementer | 执行者 | 只在已审阅边界内执行 bounded implementation | 不重写授权边界 |
| Reporter | 报告者 | 生成 execution report 和 evidence trail | 不替代 final review |
| Final Reviewer | 终审者 | 检查越界、误改、validation 质量、commit readiness、是否需要 handoff/status 收口 | 不重新发明执行协议 |

### 6.5 推荐修改文件

```text
skills/workflow-bootstrap/role_split_and_integration.md
skills/workflow-bootstrap/SKILL.md
skills/workflow-bootstrap/examples/invocation_examples.md
```

### 6.6 实现路径

第一步，新增或更新：

```text
skills/workflow-bootstrap/role_split_and_integration.md
```

该文件应包含：

- role chain；
- 各 role 的职责和边界；
- task package review 作为 bounded execution safety gate 的解释；
- 同一工具可以承担多个角色，但必须显式阶段切换；
- Copilot / Codex / ChatGPT / Cline / DeepSeek 只是 adapter examples，不是 canonical requirements；
- `workflow-bootstrap` 只定义 workflow shell / role split / runtime profile；
- task package / bounded execution / execution report 协议仍归 `chatgpt-handoff-pilot`。

第二步，在 `SKILL.md` 中加最小回指，例如：

```text
For role-based workflow handoff, see role_split_and_integration.md.
```

不要把 supporting asset 全文复制进 `SKILL.md`。

第三步，如有必要，在：

```text
skills/workflow-bootstrap/examples/invocation_examples.md
```

中补一个短例：

```text
Example: Move from tool-name workflow to role-based handoff
```

### 6.7 验收标准

- role split 是 tool-agnostic 的。
- 当前工具只作为 examples 出现，不成为 requirements。
- review before implementation 被定义为 safety gate。
- 同一工具多角色执行时，需要显式阶段切换。
- `workflow-bootstrap` 仍只定义 workflow shell / role split / runtime profile。
- `chatgpt-handoff-pilot` 仍是 task package / bounded execution / execution report 协议 owner。

### 6.8 不做事项

- 不创建 `tool_adapters/`。
- 不把 Copilot / Codex 固定分工写成 canonical rule。
- 不修改 `chatgpt-handoff-pilot`。
- 不新增 validator / scripts / tests / CI。
- 不新增 `.github/instructions/`。
- 不新增 `.github/agents/`。
- 不把当前订阅差异或模型强弱写入 canonical guidance。

---

## 7. Phase 2：Review Tier Guidance

### 7.1 状态

建议在 Phase 1 后执行。

### 7.2 目标

定义不同任务类型需要多强的 task package review。

核心不是“每次都重审包”，而是按风险分层：

```text
Light Review → Standard Review → Heavy Review
```

### 7.3 Review tiers

| Tier | 中文定位 | 适用场景 | 审查重点 | 第二角色 / 第二工具复核 |
|---|---|---|---|---|
| Light Review | 轻审包 | README 小更新、单文件非核心文档、索引更新 | path、scope、无明显越权 | 可选 |
| Standard Review | 标准审包 | workflow supporting asset、`AGENTS.md`、project adapter、handoff/status 小更新 | ownership boundary、authorized files、out of scope、evidence path | 推荐 |
| Heavy Review | 重审包 | canonical skill 修改、跨项目规则、runtime pack design、automation candidates | generalized vs project-local、protocol ownership、premature enforcement risk | 强烈推荐 |

### 7.4 推荐修改文件

```text
skills/workflow-bootstrap/review_tiers.md
skills/workflow-bootstrap/role_split_and_integration.md
skills/workflow-bootstrap/examples/invocation_examples.md
```

### 7.5 实现路径

第一步，新增：

```text
skills/workflow-bootstrap/review_tiers.md
```

第二步，定义：

- Light Review；
- Standard Review；
- Heavy Review。

第三步，在 `role_split_and_integration.md` 中轻量引用 review tiers。

第四步，在 `invocation_examples.md` 中补一个 heavy review 示例，尤其针对 canonical skill 变更。

### 7.6 验收标准

- review tier guidance 能帮助人类或 AI 判断本轮任务需要多强 review。
- canonical skill 修改默认进入 Heavy Review。
- project-local facts 不会被轻率吸收到 generalized guidance。
- review tiers 保持 advisory，不成为 CI enforcement。
- checklist 不应过度刚性化。

### 7.7 不做事项

- 不要求所有任务都必须完整审包。
- 不把 review tiers 转成脚本。
- 不接 CI。
- 不把 review checklist 写成 hard failure。
- 不让 review tier 替代人类或 AI 的上下文判断。

---

## 8. Phase 3：Runtime Pack Minimal Manifest

### 8.1 状态

中期阶段。

### 8.2 目标

定义项目侧 runtime pack 的最小组成，同时保持 thin-adapter 原则。

### 8.3 核心原则

Runtime pack 不是第二规则库。

它只是一个 project-side surface，用于帮助不同工具更稳定地发现 canonical workflow guidance。

### 8.4 可能的最小 runtime pack

```text
AGENTS.md
.github/copilot-instructions.md
.github/copilot-instructions.zh-CN.md
tasks/README.md
tasks/<task-package>.md
tasks/<execution-report>.md
```

### 8.5 文件定位

| 文件 | 定位 | 边界 |
|---|---|---|
| `AGENTS.md` | project-side master thin entry | 不复制 canonical skill 全文 |
| `.github/copilot-instructions.md` | Copilot-specific thin adapter | 不成为第二规则库 |
| `.github/copilot-instructions.zh-CN.md` | translated mirror | 不引入新规则 |
| `tasks/README.md` | task evidence index | 不替代 handoff/status |
| task package | execution authorization | protocol owned by `chatgpt-handoff-pilot` |
| execution report | per-task evidence | 不替代 final review |

### 8.6 推荐修改文件

```text
skills/workflow-bootstrap/runtime_pack_minimal_manifest.md
skills/workflow-bootstrap/examples/invocation_examples.md
```

### 8.7 实现路径

第一步，新增或更新：

```text
skills/workflow-bootstrap/runtime_pack_minimal_manifest.md
```

第二步，只定义 runtime pack 的最小组成和 thin adapter 边界。

第三步，连接：

- role split；
- non-git runtime profile；
- project-side thin adapter；
- task package / execution report handoff。

第四步，不把项目侧具体命令、环境、业务路径写进 canonical guidance。

### 8.8 验收标准

- runtime pack 保持 thin。
- project-side files 只做 route / pointer，不复制或重写规则。
- Git 项目与 non-git 项目都能使用该 guidance。
- 已有项目约定不会被强行覆盖。
- runtime pack 不变成 parallel canonical source。

### 8.9 不做事项

- 不创建 `.github/instructions/`。
- 不创建 `.github/agents/`。
- 不要求所有项目采用同一 runtime pack。
- 不复制 project-specific facts。
- 不写具体工具订阅差异。

---

## 9. Phase 4：Multi-project Pilot

### 9.1 状态

中长期验证阶段。

### 9.2 目标

在不同项目类型中验证 role protocol 和 runtime profile。

至少应覆盖：

```text
1. non-git / low-git project
2. Git project
```

### 9.3 推荐 pilot 类型

| Project type | 验证重点 |
|---|---|
| non-git / low-git project | `tasks/` evidence path、inactive archive、minimal handoff/status closure |
| Git project | branch / commit / PR-style review 与 task package / execution report 的配合 |
| data analysis script project | runtime pack 是否仍然轻量 |
| ai-skill-hub 自身 | canonical skill 修改是否需要 Heavy Review |

### 9.4 实现路径

1. 每类项目选择一个小任务。
2. 适用时保留 task package + execution report pairing。
3. 每轮结束后写 concise pilot review memo。
4. 只回灌 generalized guidance。
5. 不回灌项目路径、业务事实、环境命令。

### 9.5 推荐 review memo 落点

skill-hub 级别 review：

```text
docs/reviews/
```

项目侧 pilot：

```text
tasks/
```

或项目已经明确的 established evidence path。

### 9.6 验收标准

- role protocol 在 Git / non-git 两类项目中都能成立。
- review tiers 能帮助选择 review intensity。
- runtime pack 没有变成第二规则库。
- generalized guidance 和 project-local facts 能被区分。
- `tasks/` 没有被强制推广到所有项目。

### 9.7 不做事项

- 不强制所有项目使用 `tasks/`。
- 不强制所有项目采用同一 adapter 文件。
- 不把单一项目的 local practice 直接提升为 canonical guidance。
- 不以 pilot 成功为由提前引入 validator。

---

## 10. Phase 5：Tool Adapter Candidates

### 10.1 状态

长期候选阶段，目前暂缓。

### 10.2 目标

在 role protocol 和 review tiers 稳定后，再定义可选的 tool-specific adapter guidance。

### 10.3 可能的 adapter

```text
Copilot as Drafter
Codex as Implementer / Reporter
ChatGPT as Reviewer / Final Reviewer
Cline as Local Implementer
DeepSeek as Model Backend
Future tools as role adapters
```

### 10.4 进入条件

只有满足以下条件后，才考虑进入 Phase 5：

- `role_split_and_integration.md` 已稳定。
- `review_tiers.md` 已稳定。
- `runtime_pack_minimal_manifest.md` 已稳定。
- 至少两类项目 pilot 已完成。
- 已经有证据表明 tool-specific guidance 确有必要。
- 工具映射已经能明确保持 optional adapter 定位。

### 10.5 未来可能落点

```text
skills/workflow-bootstrap/tool_adapters/
```

可能文件：

```text
skills/workflow-bootstrap/tool_adapters/copilot_as_drafter.md
skills/workflow-bootstrap/tool_adapters/codex_as_implementer_reporter.md
skills/workflow-bootstrap/tool_adapters/chatgpt_as_reviewer.md
skills/workflow-bootstrap/tool_adapters/cline_as_local_implementer.md
```

### 10.6 验收标准

- adapter 文件只描述工具如何承担角色。
- adapter 文件不要求必须使用某个工具。
- adapter 文件不写订阅等级依赖。
- adapter 文件不把模型强弱评价写成 canonical rule。
- adapter 文件不改变 role protocol。

### 10.7 不做事项

- 不把当前订阅差异写入 canonical guidance。
- 不把 Copilot / Codex 固定为永久架构。
- 不在 role protocol 稳定前创建 adapter。
- 不把 adapter 当作 workflow-bootstrap 主体。

---

## 11. Phase 6：Validator / Automation Preflight

### 11.1 状态

最后阶段候选，目前明确暂缓。

### 11.2 目标

在 guidance 足够稳定后，再考虑轻量 read-only audit。

### 11.3 可能的 audit checks

- project-side adapter 是否大段复制 canonical skill 正文。
- task package / execution report pairing 是否缺失。
- `archive/` 是否被引用为 active workflow line。
- handoff/status 是否被用成 per-task trace log。
- runtime pack files 是否形成 parallel rule set。
- `tasks/` 是否被写成 mandatory，而不是 preferred / optional。
- translated mirror 是否引入了新规则。
- project-local facts 是否被写入 generalized guidance。

### 11.4 实现路径

1. 从 read-only audit 开始。
2. 只输出 warnings。
3. 不 auto-fix。
4. 不 destructive cleanup。
5. 初期不接 CI。
6. 多轮人工确认后，再考虑进入 local check。

### 11.5 验收标准

- audit 保持 read-only。
- audit 不替代 human / AI review。
- audit 不 enforce 尚未稳定的 guidance。
- audit 不自动改文件。
- audit 不改变 workflow-bootstrap ownership。

### 11.6 不做事项

- 不 auto-remediate。
- 不删除或重写项目文件。
- 不直接进入 CI enforcement。
- 不把 warning 当作 hard failure。
- 不把 validator 作为当前阶段目标。

---

## 12. 推荐总路线

完整路线：

```text
Phase 0: Non-git runtime profile absorption
  ↓
Phase 1: Role split canonicalization
  ↓
Phase 2: Review tier guidance
  ↓
Phase 3: Runtime pack minimal manifest
  ↓
Phase 4: Multi-project pilot
  ↓
Phase 5: Tool adapter candidates
  ↓
Phase 6: Validator / automation preflight
```

短版路线：

```text
profile → roles → review tiers → runtime pack → pilots → adapters → audit
```

中文概括：

```text
先固化运行画像，
再固化角色分工，
再固化审包分级，
再整理项目侧 runtime pack，
再多项目试跑，
再考虑工具 adapter，
最后才考虑 read-only audit。
```

---

## 13. 实现路径总表

| Phase | 主要产物 | 可能文件 | 优先级 | 是否涉及工具/脚本 |
|---|---|---|---|---|
| Phase 0 | non-git runtime profile | `non_git_runtime_profile.md` | 已完成 | 否 |
| Phase 1 | role split guidance | `role_split_and_integration.md` | 最高 | 否 |
| Phase 2 | review tier guidance | `review_tiers.md` | 高 | 否 |
| Phase 3 | runtime pack manifest | `runtime_pack_minimal_manifest.md` | 中 | 否 |
| Phase 4 | pilot review memos | `docs/reviews/` 或 project evidence path | 中 | 否 |
| Phase 5 | tool adapters | `tool_adapters/*.md` | 低 | 否 |
| Phase 6 | read-only audit | `tools/` + tests | 最低，暂缓 | 是，但 deferred |

---

## 14. 下一步建议

不要一次性实现完整蓝图。

下一步只做 Phase 1：

```text
Add role_split_and_integration.md as a workflow-bootstrap supporting asset.
```

该任务应完成：

- 定义 role chain；
- 定义各 role 的职责；
- 将 task package review 定义为 safety gate；
- 说明 same-tool multi-role execution 需要显式阶段切换；
- 将 Copilot / Codex / ChatGPT 等工具只作为 examples；
- 保持 `workflow-bootstrap` / `chatgpt-handoff-pilot` ownership boundary。

推荐下一轮 commit message：

```text
docs(workflow-bootstrap): add role split integration guidance
```

---

## 15. 明确暂缓事项

以下事项应保持 deferred：

- `tool_adapters/`
- validators
- CI enforcement
- `.github/instructions/`
- `.github/agents/`
- subscription-specific model comparisons
- project-specific command / environment guidance
- 将 `tasks/` 设为全项目 mandatory path
- 修改 `chatgpt-handoff-pilot`
- 重定义 task package / bounded execution / execution report schema

---

## 16. 最终立场

长期方向不应是维护固定的 “Copilot + Codex” 工作流。

长期方向应是：

```text
role protocol + runtime profile + thin project adapters
```

也就是：

```text
稳定角色协议
+ 稳定运行画像
+ 可替换工具适配层
```

具体工具可以变化，但角色协议应保持稳定。

当前最值得落地的是：

```text
Phase 1: Role Split Canonicalization
```

而不是立即进入 tool adapters 或 validator。

---

## 17. 建议落盘位置与提交信息

建议落盘位置：

```text
docs/design/workflow-bootstrap-role-protocol-blueprint.md
```

推荐 git commit message：

```text
docs(workflow-bootstrap): add role protocol evolution blueprint
```
