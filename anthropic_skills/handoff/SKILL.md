---
name: handoff
description: >
  Structured work handoff skill. Use when transferring unfinished work
  to another agent, reviewer, or resumed session. Produces a turnover
  record covering: last completed action, changed conditions, remaining
  scope, authority limits, open evidence, and stop conditions. The
  receiving owner must confirm scope before acting. Do not use when the
  same owner continues uninterrupted with full context.
allowed-tools: [Read, Write, Bash, Glob]
argument-hint: "[incoming owner/role] [change-record path]"
---

# Handoff

A handoff transfers responsibility, not just context. The next person or agent must know what changed, what is left, what they are allowed to do, and when to stop.

---

## Inputs

- Current change record path or working context
- Last action that completed
- Completed artifacts and produced evidence
- Conditions that changed since work started
- Assumptions still in play
- Remaining work scope
- Authority limits: allowed files/commands/tools; forbidden actions
- Evidence still owed
- Stop or hold conditions
- Incoming owner and their role (reviewer / verifier / releaser / agent)

---

## Process

1. **State what is done** — last action that finished, artifacts completed, evidence produced
2. **State what changed** — odd findings, failed attempts, assumptions not yet checked
3. **Define the controlled zone** — exact items under control, targets not to touch, hold points, approval gates
4. **Name the next decision** — next action, most important action, most likely error, and how to guard against it
5. **Require confirmation** — the incoming owner must restate scope, authority, proof owed, and stop conditions before acting

---

## Output: turnover record

Write to `turnover.md` (or inline if no file system):

```markdown
# Turnover Record
**Date**: [date]
**Outgoing**: [role]
**Incoming**: [role]

## Done
- Last action: [description]
- Artifacts: [list]
- Evidence produced: [list]

## Changed conditions
[What changed since work started; anomalies; failed attempts]

## Remaining scope
[Exact items remaining; what is explicitly out of scope]

## Authority limits
- Allowed: [files / commands / tools]
- Forbidden: [actions the incoming owner must not take]
- Evidence still owed: [list]

## Stop conditions
[When to pause and escalate; who approves what]

## Next action
[Most important next step; most likely error; control against it]

---
**Incoming owner confirmation required before acting:**
Please restate: (1) your scope, (2) what you may do, (3) proof you owe, (4) when to stop.
```

---

## Rules

- A new agent must be able to resume without reading the full chat history
- "The next agent can figure it out" — handoffs fail when state is only implied
- Chat is not a controlled record
- The incoming owner must confirm limits before acting — especially when credentials, production data, or release authority are involved
- If the incoming owner cannot restate their limits: stop and escalate

---

## Escalation triggers

- Credentials, production data, or release authority involved
- Open evidence gaps with no named owner
- Public claims or compliance assertions in scope
- Incoming owner unable to confirm scope and stop conditions
