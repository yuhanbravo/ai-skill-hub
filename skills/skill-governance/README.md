# Skill Governance

## What is this

`skill-governance` 是一个 `governance` 型 meta-skill，用来先评估单个 skill，再在显式授权时执行受控重写。

## When to use

适合在需要快速判断某个 skill 是否符合 `SKILL_TEMPLATE.md`、先拿到评分与诊断、再决定是否进入受控重写时使用；一次只处理一个 skill，不跨 skill 扩散。

## Quick Start

```text
Use skill-governance on <skill-path>
rewrite=false

# if explicitly allowed
# change to rewrite=true
```

## Supported Prompts

- `skill-evaluator.md`
- `skill-refactor.md`
- `skill-governor.md`
- `skill-refinement.md`
- `skill-batch-evaluator.md`
- `skill-invocation.md`

详细治理方法见 [skills/skill-governance/SKILL.md](skills/skill-governance/SKILL.md)。
