---
name: data-type-coercion
description: Safely convert columns to their correct types without silent data loss.
---

# Data Type Coercion

Safely convert columns to their correct types without silent data loss.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: safely convert columns to their correct types without silent data loss.

## Procedure
- Check for values that fail coercion (e.g., '12,000' to int) before force-casting.
- Preserve original values in a shadow column when coercion is lossy.
- Watch for mixed-type columns (numbers stored as strings mixed with real strings).

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
