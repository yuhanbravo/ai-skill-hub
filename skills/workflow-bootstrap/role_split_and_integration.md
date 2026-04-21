# Role Split And Integration

## Default Chain

推荐默认链路是 `Copilot 主控 / Codex 施工`：

- Copilot 更适合收敛方案、明确边界、决定本轮是否进入实施。
- Codex 更适合按任务包做 bounded execution、落文件、跑验证并回传结果。
- reviewer 负责最后一道边界与质量检查，不额外扩 scope。

这个默认值是工作流壳层，不是强制排他规则；如果项目本地已有更明确的主控关系，应优先服从本地规则。

## Minimal Roles

### `planner`

- 负责把目标、范围、明确不做、授权路径和验收标准收敛成可执行 task package。
- 负责判断本轮是否只是 workflow bootstrap，还是需要转交 `project-takeover`、`documentation-governance`、`update-project-status`、`file-structure-check` 等更专门的 skill。

### `implementer`

- 负责先读取 task package，再复述边界，然后仅在授权范围内实施。
- 负责在需要 handoff 协议时复用 `chatgpt-handoff-pilot`，输出 bounded execution 和 execution report。

### `reviewer`

- 负责检查角色边界是否被遵守。
- 负责检查 canonical / adapter / index 是否一致，验证是否真实执行，future runtime pack 是否没有被误写成当前已实现事实。

## Integration With `chatgpt-handoff-pilot`

`workflow-bootstrap` 不重新定义 handoff 协议，而是推荐这样衔接：

1. planner 用 `workflow-bootstrap` 明确默认链路和角色分工。
2. planner 按 `chatgpt-handoff-pilot` 组织 task package。
3. implementer 按 task package 做 bounded execution。
4. implementer 输出 execution report。
5. reviewer 审核边界、验证和文档表达是否收口。

换句话说，`workflow-bootstrap` 负责 workflow 壳层，`chatgpt-handoff-pilot` 负责任务包协议层。

## Recommended Flow

### Planning / Task Package

- 先收敛目标、范围、明确不做、授权目录、验收标准。
- 如果任务需要多 agent 协作，先指定 planner / implementer / reviewer 的最小责任边界。

### Bounded Execution

- implementer 先复述理解。
- implementer 只在白名单路径内施工。
- 范围外问题只记录，不顺手修复。

### Validation

- 先跑本轮被要求的最小验证。
- 若环境阻塞导致某条验证无法执行，显式记录未运行原因，不伪造成功。

### Execution Report

- 报告实际改动。
- 报告明确未实现的内容。
- 报告验证结果、风险、假设和下一步最小建议动作。

## Thin Entry Guidance

未来项目侧若使用 `.github/copilot-instructions.md` 或其他 runtime-pack 入口，推荐保持薄入口定位：

- 只写最高频、最高约束规则。
- 更细 guidance 回指 `AGENTS.md`、canonical skill 或项目本地 instructions。
- 不在薄入口中复制整套 canonical workflow 文档。
