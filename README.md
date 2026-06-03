# Mastery Coach Skill / 掌握度教练 Skill

A bilingual Agent Skill for turning explanations into verified understanding.

一个用于把“听过解释”升级为“真正掌握”的双语 Agent Skill。

- English README: [README.en-US.md](./README.en-US.md)
- 中文 README: [README.zh-CN.md](./README.zh-CN.md)
- Main skill entry: [SKILL.md](./SKILL.md)
- 中文 Skill 镜像说明: [SKILL.zh-CN.md](./SKILL.zh-CN.md)

## What it does / 它解决什么问题

Mastery Coach guides an AI agent to teach through a structured mastery loop:

```text
learning target → mastery checklist → user restatement → gap detection → targeted teaching → verification → next stage
```

它让 AI 不再只是一次性输出答案，而是通过结构化闭环帮助用户真正理解：

```text
学习目标 → 掌握清单 → 用户复述 → 查漏补缺 → 针对讲解 → 掌握验证 → 进入下一阶段
```

## Recommended repository design / 推荐目录设计

This repository keeps one official `SKILL.md` at the root so Codex can discover the skill directly. The Chinese mirror file is provided for human reading and maintenance, but should not be installed as a second skill with the same name.

本仓库在根目录保留唯一正式入口 `SKILL.md`，方便 Codex 直接识别。中文镜像文件用于阅读和维护，不建议作为第二个同名 Skill 单独安装。

## Install / 安装

For user-level local use:

```bash
git clone git@github.com:twj515895394/mastery-coach-skill.git
mkdir -p ~/.agents/skills
ln -s "$(pwd)/mastery-coach-skill" ~/.agents/skills/mastery-coach
```

For repo-scoped use, copy or symlink this folder to:

```text
<your-repo>/.agents/skills/mastery-coach/
```

## Quick prompt / 快速调用示例

```text
Use $mastery-coach to help me understand this architecture design. First build a mastery checklist, then quiz me stage by stage.
```

```text
使用 $mastery-coach 帮我理解这个架构设计。先建立掌握清单，然后分阶段测验我。
```
