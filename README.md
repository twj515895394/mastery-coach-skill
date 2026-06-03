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

## General learning use cases / 通用学习场景

This skill is not limited to coding or work. It can also be used for:

- children learning science, language, math, history, stories, or everyday concepts;
- teenagers preparing for exams, projects, reading comprehension, or writing;
- adults learning new tools, hobbies, domains, languages, or professional skills;
- parents guiding children through questions instead of simply giving answers;
- teachers designing staged lessons, classroom questions, review drills, and mastery checks;
- self-learners converting passive reading into active understanding.

它不仅适合代码、架构和业务，也适合：

- 小孩学习科学、语言、数学、历史、故事或生活常识；
- 青少年准备考试、课题、阅读理解或写作；
- 成年人学习新工具、新兴趣、新领域、语言或职业技能；
- 家长用引导式问题辅导孩子，而不是直接给答案；
- 老师设计分阶段课程、课堂提问、复习训练和掌握度检查；
- 自学者把被动阅读变成主动理解。

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

```text
Use $mastery-coach to teach my 8-year-old daughter what AI is. Use simple analogies and check her understanding gently.
```

```text
使用 $mastery-coach 帮我教 8 岁孩子理解什么是 AI。用简单类比，并温和检查她是否理解。
```
