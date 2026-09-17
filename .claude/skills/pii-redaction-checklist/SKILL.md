---
name: pii-redaction-checklist
description: Identify and redact personally identifiable information before analysis or sharing.
---

# Pii Redaction Checklist

Identify and redact personally identifiable information before analysis or sharing.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: identify and redact personally identifiable information before analysis or sharing.

## Procedure
- Scan for direct identifiers (name, email, phone, SSN) and quasi-identifiers (zip+birthdate+gender).
- Redact or hash identifiers before data leaves a secure environment.
- Confirm aggregation thresholds (e.g., k-anonymity) before publishing grouped results.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
