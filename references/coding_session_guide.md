# Coding Session Guide / Coding 场景指南

## Goals

A coding mastery session should verify that the user understands not only the final code, but also the original problem, root cause, data flow, tradeoffs, risk, and verification method.

Coding 掌握度训练不仅要确认用户懂最终代码，还要确认用户理解原始问题、根因、数据流、取舍、风险和验证方法。

## Checklist

- [ ] What was the original issue or requirement?
- [ ] Which files, functions, classes, or modules are involved?
- [ ] What is the execution flow?
- [ ] What is the root cause?
- [ ] Why does the chosen fix work?
- [ ] What alternatives were considered?
- [ ] What side effects or compatibility risks exist?
- [ ] What tests prove it?
- [ ] What logs or metrics can confirm it in production?

## Useful question types

- Trace this code path.
- Predict this output.
- Explain why this line is necessary.
- Identify which branch fails.
- Propose test cases.
- Explain how this change could break production.
- Explain why this fix is safe.

## Example

```text
Before I explain the fix, tell me what you think the current code does when two requests hit the same idempotency key at nearly the same time.
```

```text
在我解释修复方案前，你先说一下：如果两个请求几乎同时打到同一个幂等 key，当前代码会怎么执行？
```
