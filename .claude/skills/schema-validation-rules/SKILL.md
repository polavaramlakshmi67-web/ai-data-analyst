---
name: schema-validation-rules
description: Define and check schema rules: types, ranges, required columns, referential integrity.
---

# Schema Validation Rules

Define and check schema rules: types, ranges, required columns, referential integrity.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: define and check schema rules: types, ranges, required columns, referential integrity.

## Procedure
- Encode expected schema as a declarative spec (e.g., pandera/pydantic) rather than ad hoc checks.
- Validate ranges/enums for categorical and bounded numeric fields.
- Fail loudly with the specific row and rule violated, not a generic error.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
