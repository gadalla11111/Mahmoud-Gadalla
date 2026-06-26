---
name: sentry-create-alert
description: Create Sentry alerts via the workflow engine API (beta). Gathers the alert config, resolves names to IDs, builds the triggers/conditions/actions JSON payload, POSTs to the workflows endpoint, and verifies with the dashboard link. Routes notifications to email, Slack, PagerDuty, or Discord.
auto-trigger:
  - '"create a Sentry alert", "notify me when X errors", "set up a Slack alert for issues"'
  - configuring notifications/automations around issue priority or regressions
do-not-trigger:
  - fixing an existing issue (use sentry-fix-issues)
  - setting up the SDK or monitoring (use a sentry setup skill)
allowed-tools: Bash, Read
---

# sentry-create-alert — alerts via the workflow engine API

**Prerequisite:** org slug, an auth token with `alerts:write` scope, and the region (US or DE).

## 5-phase workflow

1. **Gather** — alert name, the trigger event(s), conditions, and notification targets from the user.
2. **Resolve IDs** — look up users, teams, and integrations by name via the API to get their IDs.
3. **Build payload** — assemble the JSON: `triggers` (e.g. `logicType: "any-short"`, events like `first_seen_event` / `regression_event`), `actionFilters` (conditions + actions nested here — NOT directly in triggers), and `frequency` (0–1440 min).
4. **POST** to the workflows endpoint — expect `201`.
5. **Verify** — return the monitoring dashboard link.

## Critical structural detail

Actions nest inside `actionFilters`, not inside the trigger directly. Conditions use polymorphic comparison formats that vary by condition type — match the exact shape from the API docs per type.
