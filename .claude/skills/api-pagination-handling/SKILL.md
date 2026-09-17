---
name: api-pagination-handling
description: Correctly page through REST/GraphQL API results without missing or duplicating records.
---

# Api Pagination Handling

Correctly page through REST/GraphQL API results without missing or duplicating records.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: correctly page through REST/GraphQL API results without missing or duplicating records.

## Procedure
- Detect pagination style: offset/limit, cursor-based, or link-header based.
- Respect rate limits with backoff; log how many pages were fetched.
- Deduplicate on a stable ID field across pages in case of overlap.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
