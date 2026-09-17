---
name: reproducibility-logging
description: Ensure an analysis can be reproduced from raw data to final result.
---

# Reproducibility Logging

Ensure an analysis can be reproduced from raw data to final result.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: ensure an analysis can be reproduced from raw data to final result.

## Procedure
- Log the exact data snapshot/version and code version used for any reported number.
- Pin library versions and random seeds for any stochastic step.
- Keep a run log mapping each report figure back to the script/query that produced it.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
