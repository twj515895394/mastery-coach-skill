# Mastery Coach Skill / 掌握度教练 Skill

Mastery Coach 是一个中英文双语 Agent Skill，用于把 AI 的回答从“一次性解释”升级成“可验证的真正理解”。它的核心思想是：用户听过不代表懂了，只有能复述、应用、处理边界情况、评价取舍、迁移到新场景，才算真正掌握。

## 为什么需要这个 Skill

普通 AI 回答容易制造“我好像懂了”的错觉：答案看起来完整，但用户不一定能独立应用。这个 Skill 把交互模式从“答案投喂”改成“掌握度教练”。

## 核心流程

```text
识别学习目标
→ 明确掌握结果
→ 建立掌握清单
→ 必要时让用户复述当前理解
→ 发现缺口和误区
→ 只讲下一层必要内容
→ 用问题或场景验证
→ 更新清单
→ 继续下一阶段或总结
```

## 项目目录设计

```text
mastery-coach-skill/
├── SKILL.md
├── SKILL.zh-CN.md
├── README.md
├── README.en-US.md
├── README.zh-CN.md
├── agents/
├── assets/
├── references/
│   ├── mastery_levels.md
│   ├── question_design_patterns.md
│   ├── general_learning_guide.md
│   ├── coding_session_guide.md
│   ├── non_coding_session_guide.md
│   └── facilitation_guardrails.md
├── examples/
│   ├── child_learning_example.md
│   ├── adult_self_learning_example.md
│   ├── parent_child_coaching_example.md
│   ├── teacher_lesson_design_example.md
│   ├── coding_debugging_example.md
│   ├── architecture_review_example.md
│   ├── business_process_example.md
│   ├── product_requirement_example.md
│   └── creative_workflow_example.md
└── scripts/
```

## 适用场景

### 通用学习场景

- 儿童学习科学、语言、数学、历史、故事或生活常识；
- 青少年准备考试、课题、阅读理解、写作或学科复习；
- 成年人学习新工具、新兴趣、新领域、语言或职业技能；
- 家长使用引导式问题进行家庭学习辅导；
- 老师设计分阶段课程、课堂提问、复习训练和掌握度检查；
- 自学者把被动阅读变成主动理解。

### Coding 场景

- 理解一个 Bug 修复；
- 阅读代码模块；
- 评审 PR；
- 学习堆栈、数据流、并发、缓存、数据库等机制；
- 技术面试训练。

### 非 Coding 工作场景

- 学习业务流程；
- 评审产品需求；
- 准备培训资料；
- 分析架构或运营取舍；
- 管理沟通训练；
- 训练视频分镜、Prompt 系统、内容策略等创意工作流。

## 示例调用

```text
使用 $mastery-coach 帮我向 8 岁学习者讲解什么是 AI。用简单类比、短问题和复述检查。
```

```text
使用 $mastery-coach 帮我以成人初学者方式学习英语语法。不要幼稚化，带我一步步练习。
```

```text
使用 $mastery-coach 帮我设计一节分数入门课。要包含分阶段讲解和检查题。
```

```text
使用 $mastery-coach 帮我理解这个 PR。先讲问题和数据流，再测验我根因和边界情况。
```

```text
使用 $mastery-coach 帮我学习 WMS 调拨流程。每个阶段后用场景题检查我是否理解。
```

## 安装方式

用户级本地安装：

```bash
git clone git@github.com:twj515895394/mastery-coach-skill.git
mkdir -p ~/.agents/skills
ln -s "$(pwd)/mastery-coach-skill" ~/.agents/skills/mastery-coach
```

仓库级安装：

```bash
mkdir -p .agents/skills
cp -R /path/to/mastery-coach-skill .agents/skills/mastery-coach
```

## 维护建议

保持 `SKILL.md` 聚焦。长示例、评分标准、领域专项指南放到 `references/` 或 `examples/`，避免主 Skill 文件过长。
