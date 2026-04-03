# Skill Hub Commit 命名规范（Commit Convention）

## 0. Quick Start

在新的 clone / worktree 中启用提交校验：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\install_git_hooks.ps1
```

最短提交流程：

```text
clone / new worktree
  -> run tools/install_git_hooks.ps1 once
  -> write commit message
  -> commit-msg hook validates
  -> commit accepted or message corrected
```

快速要点：

- `.git/hooks/` 是 Git 本地目录，不作为仓库版本化资产维护
- 仓库版本化的是 `.githooks/` 和 `tools/install_git_hooks.ps1`
- 每个新的 clone / worktree 需要单独执行一次安装脚本
- 正常 `git commit` 和 `tools/export_bundle.ps1` 的 auto-commit 都会走同一套校验

## 1. 目的

本规范用于统一 `ai-skill-hub` 仓库的 commit message 写法，使其具备：

- 清晰表达“本次改动做了什么”
- 可追踪工程阶段（Phase-driven evolution）
- 快速定位影响范围（scope）
- 与 `HANDOFF / STATUS` 文档形成分层协同

本仓库采用：

> “轻量结构化，必要时带 Phase”的 commit 规范

## 2. 基本格式

```text
<type>: <action>
<type>(<scope>): <action>
<type>: Phase <n>[.<m>] - <scope> - <action>
```

合法示例：

- `docs: complete bridge reference audit and confirm mirror-only role`
- `feat(sync): add non-git project skill sync script`
- `chore(bundle): auto-commit before export (2026-03-26 17:44:09)`
- `docs: Phase 2 - bridge - define SSOT and mirror boundaries`
- `fix: Phase 3 - bridge - switch compatibility links to active sources`

## 3. 字段说明

### 3.1 type（改动类型）

表示本次提交的性质。

推荐使用以下集合：

| type | 说明 |
| --- | --- |
| `docs` | 文档、handoff、status、协议、说明 |
| `feat` | 新功能、新 skill、新能力 |
| `fix` | bug 修复、错误路径、错误引用 |
| `refactor` | 结构重构（不改变行为） |
| `test` | 测试、smoke、回归保护 |
| `chore` | 杂项维护 |

当前校验只接受以上六类 `type`。若未来需要新增 type，应先在 Git 历史中出现稳定使用模式，再同步更新本规范、校验脚本和测试。

### 3.2 Phase（阶段）

`Phase` 表示仓库 / 系统演进阶段，而不是单次执行动作。

格式：

- `Phase 1`
- `Phase 2`
- `Phase 2.5`
- `Phase 2.6`
- `Phase 3`
- `Phase 4`

作用：

- 将 Git history 转换为“工程演进时间线”
- 与 `HANDOFF / STATUS` 对齐

使用场景：

- 本次提交明确属于某个仓库阶段的收口、切换或阶段性里程碑
- 提交主题需要和当前系统状态文档中的 phase 叙事直接对齐

不适用场景：

- 普通工具脚本、局部修复、日常文档更新
- skill 执行 phases，例如 `scan / understand / audit / report / fix`
- 只是想表达“做了一次检查”，但并没有真正对应仓库阶段

判断原则：

- 如果 `Phase` 后面不是数值阶段，就不要写 `Phase`
- 如果写了 `Phase`，应使用 `<type>: Phase <n>[.<m>] - <scope> - <action>`

当前仓库状态以 [HANDOFF.md](../HANDOFF.md) / [skill-hub-status.md](../status/skill-hub-status.md) 为准；截至当前，`ai-skill-hub` 处于 `Phase 3 - Controlled System`。

### 3.3 scope（作用范围）

表示改动的主要落点（模块/层）。

文档与三层结构：

- `bridge`
- `bridge-audit`
- `ai-protocol`
- `human-docs`
- `doc-architecture`
- `handoff`
- `status`

skill / 能力：

- `system-handoff`
- `system-status-update`
- `system-takeover`
- `project-takeover`
- `skill-governance`
- `chatgpt-handoff-pilot`
- `skill`

工具 / 分发：

- `router`
- `pipeline`
- `sync`
- `adapter`
- `metadata`
- `reseed-audit`
- `tools`
- `bundle`

仓库整体：

- `repo`
- `documentation`
- `governance`

### 3.4 action（动作描述）

简短描述本次改动做了什么。

推荐写法：

`动词 + 结果/对象`

示例：

- `introduce AI/Human/Bridge layering`
- `define SSOT and mirror boundaries`
- `normalize protocol naming`
- `audit bridge references`
- `confirm mirror-only role`
- `stabilize wrapper invocation`

## 4. 示例（结合本仓库实际）

阶段型提交：

- `docs: Phase 1 - documentation - introduce AI/Human/Bridge layering`
- `docs: Phase 2 - bridge - define SSOT and mirror boundaries`
- `docs: Phase 2.5 - ai-protocol - normalize protocol naming`
- `docs: Phase 2.6 - bridge-audit - scan mirror dependencies`
- `fix: Phase 3 - bridge - switch compatibility links away from bridge paths`
- `docs: Phase 4 - bridge-audit - confirm mirror-only role`

日常提交：

- `docs: complete bridge reference audit and confirm mirror-only role`
- `feat(tools): add import/export bundle scripts`
- `feat(sync): add non-git project skill sync script`
- `chore(bundle): auto-commit before export (2026-03-26 17:44:09)`

带 body 的提交：

```text
feat: add commit convention validator

- wire commit-msg hook
- validate export auto-commit path
- document quick-start setup for new clones
```

## 5. 与 HANDOFF / STATUS 的关系

本仓库采用“三层信息分工”：

| 层 | 作用 |
| --- | --- |
| `commit` | 记录“发生了什么”（timeline） |
| `HANDOFF.md` | 记录“当前系统状态”（state） |
| `status` 文档 | 记录“阶段快照”（snapshot） |

因此：

- `commit` 不承担完整上下文说明
- 详细信息应写入 `HANDOFF / STATUS`

## 6. 是否需要多行 commit body

默认策略：

- 使用单行 subject
- 不强制使用多行 body

建议使用 body 的情况：

- `breaking change`
- 复杂逻辑修改
- 无法通过 `HANDOFF` 表达的额外说明

如果使用 body，建议采用标准多行格式：

1. 第一行只放 subject
2. 第二行留空
3. 后续 body 使用自然语言段落或 `- ` 列表补充背景
4. body 内容应是描述性信息，避免 `misc`、`stuff`、`update` 这类占位词

不推荐：

```text
docs: complete bridge reference audit
body without separator
```

推荐：

```text
docs: complete bridge reference audit

- confirm bridge references are documentation-facing
- keep active-source ownership unchanged
```

## 7. 常见失败与修正

- `update docs`  
  问题：缺少合法 `type` 结构  
  改成：`docs: refresh governance quick-start guidance`

- `feat(sync) add non-git project skill sync script`  
  问题：缺少 `:`  
  改成：`feat(sync): add non-git project skill sync script`

- `docs: Phase audit - bridge - check docs`  
  问题：`Phase` 后必须是数值阶段  
  改成：`docs: audit bridge reference wording`

- `feat: add validator` 后直接紧跟 body  
  问题：subject 和 body 之间缺少空行  
  改成标准多行格式

- `feat: add validator` 的 body 只写 `misc`  
  问题：body 不具备描述性  
  改成具体背景或动作说明

## 8. Future Expansion

未来可能出现的扩展方向：

- 在 body 中显式支持 `BREAKING CHANGE:` 一类约定
- 当仓库历史中出现稳定新模式时，审慎增加新的 `type` 或 `scope`
- 根据实际使用情况，对 body 描述性做更细粒度校验

扩展原则：

- 不凭空设计与当前仓库无关的新格式
- 先形成稳定实践，再调整规范
- 文档、校验脚本、测试必须同步更新

## 9. 维护约定

出现以下情况时，应回看并更新本规范：

- 新的 phase 命名已经稳定进入仓库叙事
- 新的 scope 在 Git 历史中反复出现
- 提交流程发生变化，例如 hook 安装路径或自动提交入口变化
- 规范文档和实际校验行为出现不一致

更新顺序：

1. 先更新本规范
2. 再更新 `skills/skill-governance/scripts/commit_convention_check.py`
3. 最后补充或调整 `tests/test_commit_convention_check.py`

## 10. 总结

本规范的核心不是格式本身，而是：

让 commit 成为“工程演进日志”，而不是“随手记录”

最终目标：

- `Git log` = 可读的系统演进历史
- `HANDOFF` = 可执行的系统状态接口
- `STATUS` = 可查询的阶段快照
