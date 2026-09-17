---
name: versioning-datasets
description: Track dataset versions so analyses remain reproducible as data changes.
---

# Versioning Datasets

Track dataset versions so analyses remain reproducible as data changes.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: track dataset versions so analyses remain reproducible as data changes.

## Procedure
- Snapshot or hash datasets at the point of analysis rather than pointing at a live, mutable source.
- Record schema changes between versions explicitly.
- Tag which dataset version each model or report was built on.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
