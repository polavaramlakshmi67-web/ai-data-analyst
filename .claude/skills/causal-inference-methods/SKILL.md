---
name: causal-inference-methods
description: Select and apply a causal inference design appropriate to the available data.
---

# Causal Inference Methods

Select and apply a causal inference design appropriate to the available data.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: select and apply a causal inference design appropriate to the available data.

## Procedure
- Use randomized A/B test results directly when available — it's the gold standard.
- For observational data, consider diff-in-diff, instrumental variables, or matching depending on the confounding structure.
- Explicitly state the identifying assumption the causal claim depends on.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
