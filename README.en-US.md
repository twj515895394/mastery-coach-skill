# Mastery Coach Skill

Mastery Coach is a bilingual Agent Skill that turns explanations into verified understanding. It is inspired by the idea that a learner has not truly mastered a topic until they can restate it, apply it, handle edge cases, critique tradeoffs, and transfer it to new scenarios.

## Why this skill exists

A normal AI answer often creates an illusion of understanding: the explanation sounds complete, but the user may not be able to use it independently. This skill changes the interaction pattern from “answer delivery” to “mastery coaching.”

## Core workflow

```text
Identify learning target
→ Define mastery outcome
→ Build mastery checklist
→ Ask user to restate current understanding when useful
→ Detect gaps and misconceptions
→ Teach the next useful layer
→ Verify with questions or scenarios
→ Update checklist
→ Continue or summarize
```

## Design decision: should README be bilingual?

Yes. The recommended design is:

- `README.md`: short bilingual entry page;
- `README.en-US.md`: detailed English README;
- `README.zh-CN.md`: detailed Chinese README;
- `SKILL.md`: the only official skill entry, with English metadata and bilingual instructions;
- `SKILL.zh-CN.md`: Chinese mirror for maintainers, not a second installed skill.

This avoids duplicated skill discovery while still making the project friendly to both English and Chinese readers.

## Directory structure

```text
mastery-coach-skill/
├── SKILL.md                         # Required skill entry
├── SKILL.zh-CN.md                   # Chinese mirror for maintainers
├── README.md                        # Short bilingual entry
├── README.en-US.md                  # Detailed English README
├── README.zh-CN.md                  # Detailed Chinese README
├── agents/
│   └── openai.yaml                  # Optional UI metadata and invocation policy
├── assets/
│   ├── mastery_checklist_template.md
│   ├── session_notes_template.md
│   └── quiz_result_template.md
├── references/
│   ├── mastery_levels.md
│   ├── question_design_patterns.md
│   ├── coding_session_guide.md
│   ├── non_coding_session_guide.md
│   └── facilitation_guardrails.md
├── examples/
│   ├── coding_debugging_example.md
│   ├── architecture_review_example.md
│   ├── business_process_example.md
│   ├── product_requirement_example.md
│   └── creative_workflow_example.md
├── scripts/
│   └── init_session.py              # Optional helper to create a session notes file
├── .handoff/
│   └── mastery-coach-skill-handoff-*.md
├── LICENSE
└── .gitignore
```

## Use cases

### Coding

- Understand a bug fix before merging.
- Learn a codebase module.
- Review a pull request.
- Explain stack traces, data flow, concurrency, caching, or database behavior.
- Prepare for technical interviews.

### Non-coding

- Learn a business process.
- Review product requirements.
- Prepare training materials.
- Analyze architecture or operational tradeoffs.
- Practice management communication.
- Train creative workflows such as storyboards, prompt systems, or content strategy.

## Example prompts

```text
Use $mastery-coach to teach me this PR. Start with the problem and data flow, then quiz me on the root cause and edge cases.
```

```text
Use $mastery-coach to help me understand this WMS transfer process. I want scenario-based questions after each stage.
```

```text
Use $mastery-coach in Interview mode. Quiz me on Redis distributed locks and evaluate my answers.
```

## Installation

For user-level local use:

```bash
git clone git@github.com:twj515895394/mastery-coach-skill.git
mkdir -p ~/.agents/skills
ln -s "$(pwd)/mastery-coach-skill" ~/.agents/skills/mastery-coach
```

For repo-scoped use:

```bash
mkdir -p .agents/skills
cp -R /path/to/mastery-coach-skill .agents/skills/mastery-coach
```

## Maintainer notes

Keep `SKILL.md` focused. Add long examples, rubrics, and domain-specific guides under `references/` or `examples/` rather than bloating the main skill instructions.
