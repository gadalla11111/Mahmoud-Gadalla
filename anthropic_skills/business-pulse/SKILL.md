---
name: business-pulse
description: >
  Generates a one-page weekly/daily business snapshot for an SMB — cash, sales,
  pipeline, calendar, watch list, and the single thing to act on today —
  synthesized from connected tools. Pulls connectors in parallel (QuickBooks,
  PayPal, HubSpot, Gmail, Slack, Square), computes AR aging/pipeline coverage/
  revenue trend, tags each section green/yellow/red against thresholds, flags
  overdue invoices/stalled deals/urgent threads by name, and writes a scannable
  brief with the #1 priority on top. Trigger on: "business pulse", "brief me on
  the business", "summarize today's metrics", "KPI digest", "pulse check".
  Archetype: Workflow Automation. Needs connected data tools/MCP for live numbers.
allowed-tools: [Read, Write, Bash, WebFetch]
argument-hint: "[--daily | --weekly]"
auto-trigger:
  - give me a business pulse or brief me on the business
  - summarize today's metrics or show the KPI digest
  - daily/weekly one-page snapshot of cash, sales, pipeline
do-not-trigger:
  - deep financial modelling (use creating-financial-models)
  - HR/people analytics (use people-analytics)
  - one specific report with no cross-tool synthesis
health:
  last_eval: 2026-06-27
  pass_rate: 1.0
  trigger_accuracy: 1.0
  open_issues: []

---

# Business Pulse

One page that answers "how is the business doing?" — cash, sales, pipeline, and
the single thing that needs the owner today. Synthesized from connected tools, the
#1 priority on top.

---

## Process

1. **Pull every connector in parallel** — accounting (QuickBooks), payments (PayPal/Square/Stripe), CRM (HubSpot), inbox (Gmail), comms (Slack). Use whatever is connected via MCP/tools.
2. **Compute** — cash on hand + WoW change, revenue MTD + MoM, AR aging (overdue buckets), pipeline coverage by stage, deal movement.
3. **Threshold-tag** each section **green / yellow / red**.
4. **Flag by name** — overdue invoices ("$3,400 from Acme, 47 days overdue"), stalled deals ("Vertex Labs $38k, 11 days no activity"), urgent threads ("refund escalation from Riley K. in Gmail").
5. **Write the brief** — scannable, #1 priority first.

---

## Output Format

```markdown
# Business Pulse — [day · date] · [sources]

How the Business Is Doing, in One Page
*Cash, sales, pipeline, and what needs you today.*

| CASH ON HAND | REVENUE MTD | OVERDUE AR | OPEN PIPELINE |
| $48.2k ▼$6.1k WoW | $43.0k ▲8% MoM | $12.4k · 3 invoices 30d+ | $186k ▲4 deals moved |

## 01 · Needs You Today
- CASH  [overdue invoice, who, how many days, the action]
- DEAL  [stalled deal, value, days cold, the action]
- INBOX [urgent thread, who, where, the action]

## 02 · Pipeline by Stage
[weighted value per stage]

LIVE CONNECTOR DATA · synced [time]
```

---

## Data Integrity

- **Never fabricate numbers.** Pull from live connectors; if a source isn't connected, say so and leave its section marked "not connected" — don't estimate silently.
- Show every metric **with direction** (▲/▼ and the delta), not a bare figure.
- Name names only from real data (the overdue customer, the cold deal) — never invent.

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Connectors aren't set up | connect data tools/MCP first |
| Deep forecast/scenario modelling | `creating-financial-models` |
| Ratio/statement analysis | `analyzing-financial-statements` |
| Turn the pulse into a shareable image | `infographic-maker` |

---

## Rules

- **#1 priority on top** — the owner reads one thing and knows what to do.
- **Never fabricate** — live data only; flag unconnected sources.
- **Direction, not bare numbers** — every metric carries its trend.
- **Flag by name** — the specific overdue invoice / cold deal / urgent thread.
- **Threshold-tag** every section green/yellow/red.
