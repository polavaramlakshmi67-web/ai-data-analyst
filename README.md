# AI Data Analyst — 25 Subagents / 45 Skills

Repo: https://github.com/polavaramlakshmi67-web/ai-data-analyst

A Claude Code project scaffold implementing a multi-agent data analysis system.

## Structure

```
.claude/
  agents/         25 subagent definitions (.md, one per file)
  skills/         45 skills, each its own folder with SKILL.md + references/scripts/assets
```

## How it works

Drop this `.claude/` folder into the root of a project and open it in Claude Code.
The main session acts as the **orchestrator** — it reads your request, picks the
right subagent(s) by matching their `description` field, and delegates. Each
subagent runs in its own context window with only the tools it needs, and
preloads a handful of skills for domain procedure.

## Subagents (grouped by pipeline stage)

| Stage | Subagents |
|---|---|
| Ingestion | csv-loader, database-connector, api-fetcher, streaming-ingest |
| Cleaning/prep | schema-validator, missing-data-handler, outlier-detector, deduper |
| Exploration | eda-summarizer, correlation-explorer, distribution-profiler, segment-explorer |
| Statistics | hypothesis-tester, time-series-analyst, causal-inference-analyst |
| Modeling/ML | feature-engineer, model-trainer, model-evaluator, forecaster |
| Visualization | chart-builder, dashboard-designer, geo-mapper |
| Reporting | insight-writer, exec-summary-writer |
| Governance | data-quality-auditor |

## Skills

45 skills live under `.claude/skills/<skill-name>/SKILL.md`, one per reusable
procedure (e.g. `missing-value-imputation`, `sql-query-patterns`,
`hypothesis-testing-framework`). Subagents preload the skills relevant to
their job via the `skills:` field in their frontmatter, and can pull in any
other skill on demand through the Skill tool.

## Customizing

- **Tighten tool access**: edit the `tools:`/`disallowedTools:` fields in each
  agent file — e.g. give `database-connector` a read-only DB credential only.
- **Fill in real procedure**: each SKILL.md currently ships a short checklist.
  Add worked code to `scripts/`, longer docs to `references/`, and templates
  to `assets/` as each skill matures — keep SKILL.md itself short.
- **Right-size the agent count**: 25 narrow subagents is a lot to maintain.
  Many teams start by using ~8-10 of these (one per pipeline stage) and only
  split further once a stage's subagent is clearly overloaded.
- **Model assignment**: mechanical/deterministic agents default to `haiku`
  (cheap, fast); reasoning-heavy ones (hypothesis-tester, causal-inference-analyst,
  data-quality-auditor) default to `opus`. Adjust to your budget.

## Regenerating

`generate.py` at the project root builds this whole tree from a single
Python list of agent/skill definitions — edit that list and re-run it to
add, remove, or rename agents/skills in bulk.
