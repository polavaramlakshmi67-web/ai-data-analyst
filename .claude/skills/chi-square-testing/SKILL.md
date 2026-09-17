---
name: chi-square-testing
description: Test independence or goodness-of-fit for categorical data.
---

# Chi Square Testing

Test independence or goodness-of-fit for categorical data.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: test independence or goodness-of-fit for categorical data.

## Procedure
- Ensure expected cell counts are >=5 before trusting the chi-square approximation.
- Use Fisher's exact test instead for small samples or 2x2 tables with low counts.
- Report Cramer's V as an effect size alongside the p-value.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
