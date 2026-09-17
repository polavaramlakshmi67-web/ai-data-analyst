---
name: t-test-anova
description: Compare means between two or more groups.
---

# T Test Anova

Compare means between two or more groups.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: compare means between two or more groups.

## Procedure
- Check variance homogeneity (Levene's test) to choose Student's vs. Welch's t-test.
- Use ANOVA for 3+ groups, followed by a post-hoc test (Tukey HSD) for pairwise differences.
- Report the effect size (Cohen's d or eta-squared), not just significance.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
