# Copilot 主控 / Codex 施工工作流：整体施工收束总结

## 1. 文档目的

本文用于收束本轮围绕 **“Copilot 主控 / Codex 施工”** 所展开的完整施工主线，概括：

- 施工目标
- 关键阶段
- 主要结论
- 当前达成度
- 当前边界
- 后续是否继续推进的判断

本文是阶段性工作总结，不替代长期治理文档或 canonical skill 说明。

---

## 2. 本轮主线目标

本轮工作的核心目标，不是直接做一套可分发的多仓 runtime pack，而是逐步建立并验证一条受控的协作链路：

- **Copilot** 负责：
  - 读仓库
  - 收束问题
  - 生成 task package / decision memo
  - 做阶段规划与 handoff 组织

- **Codex** 负责：
  - 读取 task package
  - 做 bounded execution
  - 在白名单内施工
  - 输出 execution report

围绕这条链路，本轮持续回答了以下关键问题：

1. `ai-skill-hub` 是否继续作为母库  
2. `chatgpt-handoff-pilot` 是否继续复用  
3. workflow bootstrap 应如何在 canonical 层落地  
4. project-side 最薄主入口是谁  
5. `.github/copilot-instructions.md` 应扮演什么角色  
6. canonical guidance 如何被强制回指  
7. 这些结论在 template sketch、validation sketch、single-repo implementation pilot 中是否成立  
8. canonical path 在当前 repo 中是否应硬实体化  

---

## 3. 施工阶段概览

### Phase 0：规划与任务打包
由 Copilot 负责：
- 读取仓库现状
- 收束问题与边界
- 生成 task package / decision memo

本阶段形成的核心前提：
- `ai-skill-hub` 继续作为 canonical 母库
- `chatgpt-handoff-pilot` 继续作为协议层
- 不新建平行 workflow repo
- workflow 资产继续沉淀在 canonical 层，再逐步推演 project-side runtime pack

---

### Phase 1：canonical workflow 壳层落地
由 Codex 最小施工，完成：
- `workflow-bootstrap` canonical skill
- 最小 discoverability / compatibility 入口
- 索引更新与 execution report

本阶段解决的问题：
- workflow 壳层是否有 canonical 承载体
- “Copilot 主控 / Codex 施工” 是否能被清晰表达

---

### Phase 2：薄入口与强制回指 drafts
在 canonical 层内形成：
- future `AGENTS.md` 主入口草案
- future `.github/copilot-instructions.md` 薄适配草案
- canonical guidance 强制回指规则草案

本阶段的核心结论：
- `AGENTS.md` 是 project-side 最薄主入口
- `.github/copilot-instructions.md` 是 Copilot-specific thin adapter
- canonical guidance 必须优先
- project-side 不得膨胀成第二规则库

本阶段中间发生过一次 cloud snapshot 缺少 task package 的 bounded re-run；最终以当前 draft assets 与最新 execution report 为准。

---

### Phase 3A：template sketch
从 draft 进入模板级 sketch，完成：
- required / optional / not recommended 文件集合
- `AGENTS.md` 的固定字段与项目自填字段
- `.github/copilot-instructions.md` 的最薄边界
- path backreference 表达方式
- anti-second-rulebook 约束

本阶段仍停留在 canonical 层，尚未进入真实 repo。

---

### Phase 3B：pilot validation sketch
以**单一 consumer repo 画像**为对象做验证草案，验证：
- 入口组合是否成立
- 字段、占位符、路径回指是否成立
- anti-second-rulebook 约束是否成立

本阶段仍不创建真实 consumer repo 文件，只做单仓画像验证。

---

### Phase 3C：single consumer repo implementation pilot
在一个真实单仓中最小实现：
- `AGENTS.md`
- `.github/copilot-instructions.md`

本阶段完成后，主线首次拥有了 implementation 级证据，证明：

- `AGENTS.md` 作为主入口可落地
- `.github/copilot-instructions.md` 作为薄适配可落地
- 两者职责分工没有明显冲突

但本阶段仍未进入 multi-repo rollout。

---

### Phase 3D：canonical path calibration
围绕一个最容易漂移的问题做收口：

> 当前 repo 中 `<project-local-canonical-skill-path>` 是否要硬实体化？

本阶段的稳定结论是：

- 当前 repo **不应**硬实体化该路径
- 因为仓库中并不存在独立的 project-local canonical payload artifact
- 在这种前提下，**受控占位**比伪真实路径更稳

---

## 4. 已达成的内容

截至当前阶段，已明确达成：

1. `workflow-bootstrap` 已在 canonical 层稳定落地  
2. `chatgpt-handoff-pilot` 继续作为 task package / bounded execution / execution report 的协议层  
3. `AGENTS.md` 作为 project-side 最薄主入口的路线已经形成并完成单仓 pilot  
4. `.github/copilot-instructions.md` 作为 Copilot-specific thin adapter 的路线已经形成并完成单仓 pilot  
5. canonical guidance 的强制回指机制已形成完整逻辑链  
6. anti-second-rulebook 原则已从 draft 推进到 pilot implementation / calibration 层  
7. 当前 repo 中 canonical path 不应硬实体化，受控占位更稳  

---

## 5. 明确保留的边界

以下内容是**刻意未做**，不是遗漏：

- 未进入 multi-repo rollout
- 未进入 distribution
- 未进入 adoption
- 未改 sync / export / import / check 工具逻辑
- 未新增 `.github/instructions/*.instructions.md`
- 未新增 `.github/agents/*.agent.md`
- 未把当前 pilot 包装成通用定稿
- 未把 project-side 入口文件扩写成第二规则库

---

## 6. 当前稳定结论

截至目前，可以将这条主线收束为以下稳定结论：

1. `ai-skill-hub` 仍是 canonical 母库  
2. `workflow-bootstrap` 是 workflow 壳层与 project-side runtime pack 设计承载体  
3. `chatgpt-handoff-pilot` 仍是协议层  
4. `AGENTS.md` 是 project-side 最薄主入口  
5. `.github/copilot-instructions.md` 是 Copilot-specific thin adapter  
6. canonical guidance 必须优先  
7. project-side 不得形成第二规则库  
8. 当前 single-repo pilot 已完成，但尚未进入 multi-repo rollout  
9. 当前 repo 中 canonical path 不应硬实体化，受控占位更稳  

---

## 7. 当前状态判断

当前最合理的状态不是继续主动推进新阶段，而是：

## 条件触发型暂停态

即：

- single-repo pilot 已完成
- canonical path calibration 已完成
- 暂不启动 rollout-readiness
- 仅在满足明确 trigger 时，才重新开启施工

---

## 8. 后续触发条件

只有满足以下条件之一，才值得重启下一轮施工：

### Trigger A：出现明确的 project-local canonical payload artifact
条件包括但不限于：
- 有明确路径
- 有维护责任
- 不是临时占位
- 可被 project-side entrypoints 稳定回指

触发后，才值得重新评估 canonical path 是否从受控占位升级为真实路径。

### Trigger B：需要验证第二种 consumer repo 类型
如果未来需要验证与当前 single-repo pilot 明显不同的 repo 类型，才值得开启新的 validation sketch 或 implementation pilot。

---

## 9. 当前不应触发新施工的情况

以下情况不足以触发新 phase：

- 只是觉得链路已经比较完整，想继续推进
- 想提前做 rollout 准备，但没有新证据
- 想顺手把 `.github/instructions/*.instructions.md` 或 `.github/agents/*.agent.md` 补出来
- 没有新的 payload artifact
- 没有新的 repo 类型验证需求

---

## 10. 总体评价

这轮施工的特点是：

- 节奏稳
- 边界清
- 每一步都尽量 bounded
- 没有为了推进而推进
- 没有因为“已经接近可用”就过早进入 rollout 叙事

结果是：

- 这条 workflow 主线已经拥有真实单仓 implementation 证据
- 但仍保持保守边界
- 当前结论已经足够稳定，可进入“条件触发型暂停态”

---

## 11. 一句话总结

**本轮已完成从 canonical workflow 设计到 single-repo implementation pilot，再到 canonical path calibration 的完整闭环；当前结论稳定，后续默认暂停，只有在出现明确 project-local canonical payload artifact 或需要验证第二种 consumer repo 类型时，才重新开启施工。**