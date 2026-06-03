# Example: Architecture Review / 架构评审训练示例

## User prompt

```text
使用 $mastery-coach 帮我理解 MySQL 到 Elasticsearch 增量同步服务的架构设计。
```

## Mastery checklist

- [ ] 为什么需要同步服务？
- [ ] 数据源配置如何管理？
- [ ] 字段映射和多表 join 如何配置？
- [ ] 全量同步和增量同步有什么区别？
- [ ] 增量字段如何选择？
- [ ] 失败重试、幂等、断点续传如何处理？
- [ ] ES 索引变更如何兼容？
- [ ] 如何监控同步延迟和失败率？

## Example questions

```text
如果 update_time 被业务 SQL 批量刷新，但数据内容没变，增量同步会出现什么问题？你会怎么优化？
```

```text
如果一个 ES 文档由三张 MySQL 表 join 生成，其中子表变更但主表 update_time 没变，如何捕获增量？
```
