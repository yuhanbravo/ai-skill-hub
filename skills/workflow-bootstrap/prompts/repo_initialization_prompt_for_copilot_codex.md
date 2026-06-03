# 其他仓库初始化提示词模板（面向 Copilot / Codex）

## 目的
用于在新仓库启动时，快速生成一套「AI 可理解、可执行、可交接」的最小协作上下文，便于后续接入 `ai-skill-hub` 的 workflow。

## 推荐提示词（可直接复制）

你现在是该仓库的“初始化助手”。请按下面目标产出一份**最小但可执行**的仓库 AI 协作初始化方案，面向 GitHub Copilot 与 Codex。

### 背景
- 仓库类型：<单体应用 / 多包仓库 / 库 / 数据项目>
- 主要语言与框架：<例如 Python + FastAPI / Node + Next.js>
- 当前状态：<新建 / 遗留项目接管 / 结构混乱待整理>
- 团队协作方式：<PR 驱动 / issue 驱动 / 文档驱动>

### 目标
1. 让不同 AI（Copilot/Codex）快速理解仓库结构、边界、约束。
2. 建立最小可维护的入口文件，避免形成“第二规则库”。
3. 为后续接入 ai-skill-hub 的 workflow（task package / bounded execution / execution report）预留路径。

### 你必须完成的输出
请严格按以下顺序输出：

1. **仓库现状扫描摘要（不超过 15 条）**
   - 目录结构
   - 关键模块
   - 构建/测试命令
   - 已有规范文件（README、CONTRIBUTING、AGENTS 等）
   - 风险点与信息缺口

2. **最小入口文件建议（只建议，不要一次性扩写）**
   - `AGENTS.md`：项目侧薄入口，主要做 canonical backreference
   - `.github/copilot-instructions.md`：Copilot 专属薄适配层
   - `tasks/README.md`：任务包与执行回执目录约定
   - 说明每个文件的“必要字段 / 不该写什么”

3. **边界与反膨胀规则（必须明确）**
   - 哪些内容属于 canonical source（单一事实源）
   - 哪些文件只能做“薄入口”
   - 如何防止把入口文件写成第二规则库

4. **首轮任务包模板（可直接执行）**
   - 任务名、目标、范围、非目标
   - 授权修改路径
   - 验收标准
   - 输出格式（execution report）

5. **建议落地步骤（按优先级）**
   - P0：今天可完成
   - P1：本周完成
   - P2：后续优化

6. **你做出的关键假设**
   - 用“假设-影响-如何验证”三列呈现

### 强约束
- 不要发明新的治理体系；优先复用现有规范。
- 不要在初始化阶段引入过厚文档。
- 不要给出与仓库现状无关的通用空话。
- 输出应偏执行，不偏概念。

如果信息不足，请先列“最小补充信息清单（最多 8 条）”，再给出带假设的初版方案。

## 使用说明
- 把尖括号内容替换成你的仓库信息后，直接发给 Copilot/Codex。
- 如果是遗留仓库，先跑一轮“信息缺口版”；补充信息后再跑一轮“收敛版”。
- 建议把 AI 的输出沉淀到 `tasks/`，并保留每次执行回执，便于后续接入 `ai-skill-hub`。

## 已有 AI 文件仓库的增量接入提示词 / Workspace Linkage Prompt

### Purpose
用于已经存在 AI 文件体系的仓库，在保留既有规则、入口、任务记录和本地约定的前提下，补充 `ai-skill-hub` 的入口配置与 canonical guidance 回指。

这是 incremental linkage，不是 fresh repo initialization，不是 migration，不是 distribution rollout。

### Use This When
目标仓库已经存在部分或全部 AI 协作文件，例如：

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.agents/**`
- `.github/instructions/**`
- `tasks/**`
- 其他项目本地 AI instruction / agent / task 文件

### Do Not Use This For
- 新仓库初始化。
- skill 分发或 rollout。
- 规则迁移、目录重构或本地 AI 文件体系重写。
- 把 `ai-skill-hub` 的 skill 正文复制到目标仓库。

### Required Maintainer Inputs
执行前必须由维护者提供或确认：

| Field | Required confirmation |
| --- | --- |
| `target_repo_path` | 目标仓库路径。 |
| `ai_skill_hub_reference_location` | `ai-skill-hub` 在本次环境中的实际可访问位置；不要把 `/workspace/ai-skill-hub` 或任何 workspace sibling path 写成所有项目的通用默认路径。 |
| `allowed_patch_files` | 本次允许 patch 的文件列表。 |
| `allow_agents_md_patch` | 是否允许修改 `AGENTS.md`。 |
| `allow_copilot_instructions_patch` | 是否允许修改 `.github/copilot-instructions.md`。 |
| `allow_existing_agent_or_instruction_patch` | 是否允许修改已有 `.agents/**` 或 `.github/instructions/**`。 |
| `allow_new_files` | 是否允许新增文件；若允许，必须列出具体文件路径。 |
| `selected_entry_file` | 本次选定的最小入口文件。 |
| `linkage_mode` | 维护者确认的 linkage mode。 |
| `no_skill_body_copy` | 确认不复制 skill 正文。 |
| `no_second_rulebook` | 确认不创建本地第二套规则。 |
| `no_new_skill_registry` | 确认不新增本地 skill registry。 |
| `no_distribution_claim` | 确认不声称已完成 rollout 或 distribution。 |
| `preserve_existing_rules` | 确认保留既有 AI 文件体系与本地规则。 |

不要发明任何 project-local canonical skill path placeholder。不要假设所有项目都使用相同的 workspace sibling path。

### Step 1: Scan Existing AI Files
先扫描并报告 inventory，再决定是否 patch。至少覆盖：

- 已存在的 AI 入口文件。
- 已存在的 agent / instruction / task 目录。
- 是否已有 `skill-hub`、canonical guidance、`workflow-bootstrap` 相关引用。
- 是否存在相互冲突的规则。
- 哪些文件是入口文件，哪些只是历史任务记录或局部说明。

扫描输出必须先形成 inventory。不能在 inventory 缺失时直接改写入口文件。

### Step 2: Decide Linkage Mode
按最小接入原则选择 linkage mode：

- 如果已有 `AGENTS.md` 是主入口，优先只补一段 `ai-skill-hub` linkage 回指。
- 如果已有 `.github/copilot-instructions.md` 是 Copilot 主入口，优先补最小引用。
- 如果已有多个入口，选择最小公共入口，不重复写多份规则。
- 如果入口冲突或无法判断，停止并要求 maintainer confirmation。
- 如果已有规则已覆盖同类内容，只补 canonical reference，不复制规则正文。

### Step 3: Produce Minimal Patch Plan
patch 前先输出计划，必须包含：

- `candidate_files_to_patch`
- `proposed_linkage_mode`
- 每个文件修改的 exact reason
- `no_change_files`
- stop conditions
- maintainer confirmation fields

### Step 4: Apply Patch Only After Confirmation
仅在维护者确认后输出或应用 patch。patch 必须满足：

- patch-only
- preserve existing rules
- smallest viable change
- no second rulebook
- canonical guidance backlink only
- no copied skill body
- no generated local skill registry

### Anti-Bloat Check
提交 patch 建议前逐项检查：

- 是否复制了 skill 正文。
- 是否新增了本地第二套规则。
- 是否创建了禁止目录或文件。
- 是否发明了 project-local canonical skill path placeholder。
- 是否把 workspace sibling path 写成默认路径。
- 是否过度修改已有 AI 文件。
- 是否把任务描述成 multi-repo rollout 或 distribution 的完成态。

### Forbidden Changes
强约束：

- patch-only
- preserve existing rules
- no skill body copy
- no second rulebook
- no invented project-local canonical skill path placeholder
- do not create `.github/instructions/**`
- do not create `.github/agents/**`
- do not create `.agents/skills/**`
- do not create `.github/skills/**`
- do not create `skills_index.json`
- do not create `SKILLS_INDEX.md`
- do not treat workspace sibling path as universal default
- do not claim multi-repo rollout or distribution completion

### Final Report
输出最终回执时至少包含：

1. Scan inventory。
2. Files changed。
3. Files intentionally unchanged。
4. Selected linkage mode。
5. Boundary check。
6. Anti-bloat check result。
7. Maintainer confirmation fields used。
8. Remaining risks and next confirmation items。
