---
name: pivot-table-generation
description: Build pivot/cross-tab summaries to compare metrics across categorical dimensions.
---

# Pivot Table Generation

Build pivot/cross-tab summaries to compare metrics across categorical dimensions.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: build pivot/cross-tab summaries to compare metrics across categorical dimensions.

## Procedure
- Choose the right aggregation (sum/mean/count) for the metric's meaning.
- Watch for Simpson's paradox when aggregating across an uneven-sized dimension.
- Keep pivot tables to 2 dimensions max for human readability; use faceting beyond that.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
