# File Structure Check

## What is this

`file-structure-check` 是一个结构审计型 skill，用来基于目录、规则配置和 profile 检查仓库布局，并输出结构化报告。

它保留原有脚本、profile、strictness 和配置机制，但把执行过程明确组织为 `audit -> report -> fix(optional)`。

## When to use

适合在你需要检查目录结构、识别缺失路径、发现错位文件，或为后续治理提供结构审计输入时使用。

如果你的目标是直接做目录改造而不是先做审计，这个 skill 不是第一步。

## Quick Start

```text
Use the `file-structure-check` skill on this repository and audit the repo layout.
Project root: <project-root>
```

如需更细控制，可补充 `profile`、`strictness`、`config path`、`json output` 等参数。详细审计模式见 [SKILL.md](/d:/dev/codex-skill-hub/skills/file-structure-check/SKILL.md)。
