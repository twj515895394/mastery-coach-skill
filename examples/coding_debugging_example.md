# Example: Coding Debugging Session / Coding 调试训练示例

## User prompt

```text
Use $mastery-coach to help me understand this Metaspace OOM issue caused by Orika MapperFactory creation.
```

## Expected coach behavior

1. Build checklist:
   - What is Metaspace?
   - Why dynamic class generation affects it?
   - How Orika MapperFactory generates mapper classes?
   - Why frequent factory creation causes growth?
   - How caching or singleton factory fixes it?
   - How to verify with JVM tools?

2. Ask restatement:

```text
Before I explain the fix, tell me what you think happens when a new MapperFactory is created repeatedly.
```

3. Gap-fill:

```text
The key missing point is that Orika may generate classes dynamically. Those generated classes are loaded into Metaspace. If the factory is recreated frequently, generated metadata can accumulate.
```

4. Verify:

```text
Scenario: after caching MapperFactory, heap is stable but Metaspace still grows slowly. What would you check next?
```
