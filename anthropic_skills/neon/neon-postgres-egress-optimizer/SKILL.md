---
name: neon-postgres-egress-optimizer
description: Diagnose and fix excessive Postgres egress (network data transfer) in a codebase — the usual cause of surprise Neon bills. Uses pg_stat_statements to find the heaviest queries, then fixes the anti-patterns: SELECT *, missing pagination, high-frequency static reads, app-side aggregation, and JOIN row duplication.
auto-trigger:
  - '"high Neon bill", "reduce Postgres egress", "why is my data transfer so high"'
  - unexpectedly high data-transfer / egress costs on a Postgres database
do-not-trigger:
  - initial Neon setup / connection / branching (use neon-postgres)
  - query correctness bugs unrelated to data volume (use debug)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# neon-postgres-egress-optimizer — cut Postgres egress

Diagnose and fix excessive Postgres egress (data transferred over the wire), the common cause of surprise Neon bills.

## Diagnose (pg_stat_statements)

Enable `pg_stat_statements` and find:
- Queries transferring the most **total** rows
- Queries returning the most rows **per execution**
- Frequently-called queries (caching candidates)
- Long-running operations during cost spikes

## Fix the anti-patterns

| Anti-pattern | Fix |
|---|---|
| `SELECT *` | Select only needed columns — large JSONB/TEXT blobs get shipped then discarded |
| Missing pagination | Add LIMIT/keyset pagination — unbounded queries scale with table growth |
| High-frequency static data | Cache it — don't re-hit the DB thousands of times/day for unchanging rows |
| App-side aggregation | Push `GROUP BY`/aggregates into SQL instead of fetching full sets to sum in code |
| JOIN duplication | Parent columns repeat per child row — fetch parent once, children separately |

## Keep non-prod cheap

Use `neon.ts` infra-as-code to set autoscaling limits and auto-expiration on dev/preview branches.

## Notes

- Cross-reference with `sentry-setup-ai-monitoring` / `sipcode` when egress correlates with agent/LLM workloads pulling large result sets.
- Measure first (`pg_stat_statements`), then fix the top offenders — don't blanket-rewrite every query.
