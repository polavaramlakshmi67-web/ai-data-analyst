---
name: sql-query-patterns
description: Write safe, efficient, read-only SQL for exploratory data extraction.
---

# Sql Query Patterns

Write safe, efficient, read-only SQL for exploratory data extraction.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: write safe, efficient, read-only SQL for exploratory data extraction.

## Procedure
- Always add LIMIT during exploration; never run unbounded SELECT * on large tables.
- Prefer explicit column lists over SELECT *.
- Use EXPLAIN before running a query you suspect is expensive.
- Parameterize queries — never string-concatenate user input into SQL.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
