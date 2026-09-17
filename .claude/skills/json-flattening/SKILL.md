---
name: json-flattening
description: Flatten deeply nested JSON API responses into analysis-ready tabular form.
---

# Json Flattening

Flatten deeply nested JSON API responses into analysis-ready tabular form.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: flatten deeply nested JSON API responses into analysis-ready tabular form.

## Procedure
- Use pandas.json_normalize with explicit record_path/meta rather than manual recursion when possible.
- Decide up front how to handle arrays of objects (explode vs. aggregate).
- Preserve a reference to the original nested structure in case flattening loses information.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
