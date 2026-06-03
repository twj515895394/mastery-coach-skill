# Question Design Patterns / 问题设计模式

## 1. Teach-back / 复述题

Ask the user to explain the idea in their own words.

Example:

```text
Explain this mechanism back to me as if you were explaining it to a new teammate.
```

```text
用你自己的话把这个机制讲给一个刚入职的同事听。
```

## 2. Scenario / 场景题

Ask the user to apply the idea in a realistic situation.

```text
If the cache update succeeds but the database write fails, what should the system do?
```

```text
如果缓存更新成功但数据库写入失败，系统应该怎么处理？
```

## 3. Compare and contrast / 对比题

Ask the user to compare alternatives.

```text
Why use this approach instead of a scheduled full refresh?
```

```text
为什么使用这个方案，而不是定时全量刷新？
```

## 4. Boundary / 边界题

Ask what can go wrong.

```text
What edge cases would break this design?
```

```text
哪些边界情况会击穿这个设计？
```

## 5. Prediction / 预测题

Ask the user to predict output, behavior, or consequences.

```text
What happens if this queue becomes full while producer traffic continues to rise?
```

```text
如果队列满了但生产流量继续上涨，会发生什么？
```

## 6. Tradeoff / 取舍题

Ask the user to explain the cost of a decision.

```text
What do we gain and what do we lose by making this service asynchronous?
```

```text
把这个服务改成异步后，我们得到了什么，又失去了什么？
```

## 7. Multiple-choice / 选择题

Use when the user is new or when you need fast diagnosis. Do not reveal the answer before the user responds.

## 8. Rubric-based review / 评分题

Use a rubric for presentations, product requirements, architecture, and training content.
