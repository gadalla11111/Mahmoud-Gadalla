---
name: prd-generator
description: >
  Product Requirements Document generator. Use when a user wants to plan a
  product, feature, or app — guides them through structured questioning,
  researches technology options, and produces a developer-ready PRD.md.
  Optimizes output for handoff to engineers (human or AI). Trigger on:
  "write a PRD", "product requirements", "feature spec", "help me plan this
  product", "I want to build X", "define scope before we start". Also trigger
  when a user describes a product idea and asks what to build or how to start.
  Produces tiered output: discovery one-pager (quick), alpha spec (standard),
  or full GA PRD (comprehensive). Cross-references adr for architecture decisions
  and tdd for acceptance criteria format.
allowed-tools: [WebSearch, WebFetch, Read, Write, Bash]
argument-hint: "[product idea or blank to start with questions]"
auto-trigger:
  - "write a PRD", "product requirements", "feature spec"
  - defining scope before engineering starts
  - stakeholder alignment document for a new product or feature
  - "I want to build X", "help me plan this"
do-not-trigger:
  - post-implementation docs
  - technical design docs (use adr instead)
  - quick feature additions with clear scope (use ultracode directly)
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []

---

# PRD Generator

Guides users from rough product idea → structured PRD ready for developer handoff. Friendly PM + developer persona. One question at a time.

---

## Step 0 — Choose the Right Tier

Before asking product questions, establish which PRD tier is needed. This scopes every subsequent step.

| Tier | Output | When | Time investment |
|---|---|---|---|
| **Discovery** | 1-page concept brief | Idea validation, stakeholder pitch, early scoping | 5–10 min conversation |
| **Alpha** | Standard PRD (~3–5 pages) | Feature definition, sprint planning, AI-agent handoff | 15–20 min conversation |
| **GA** | Full PRD (~8–12 pages) | Launch-ready product, team alignment, investor/partner docs | 30–45 min conversation |

Ask: "Are you at the idea stage (I can write a quick concept brief), planning a specific feature (standard PRD), or preparing a full product for launch (comprehensive PRD)?"

Default to **Alpha** if the user doesn't specify.

---

## Opening

Introduce as a product manager and developer. Explain the process for the chosen tier. Ask the user to describe their idea at a high level.

---

## Question Framework (one at a time, conversational)

Adapt depth based on tier. Cover in order — skip if already answered in the description:

### All tiers
1. Core value proposition ("What's the one thing this does that nothing else does?")
2. Target audience ("Who is this for, and what problem does it solve for them?")
3. Platform (web / mobile / desktop / API / embedded)

### Alpha + GA only
4. Core features ("What are the 3–5 must-have features for v1?")
5. UI/UX approach ("Wireframes? MVP style? Design system?")
6. Data storage and key entities
7. Authentication and security requirements
8. Third-party integrations

### GA only
9. Scalability ("Expected users at launch vs. 12 months?")
10. Cost constraints (API fees, hosting, subscriptions, team size)
11. Technical challenges ("What are you most uncertain about technically?")
12. Compliance and legal requirements (GDPR, HIPAA, SOC2, etc.)
13. Success metrics ("How will you know this worked — what's the KPI at 90 days?")

Use reflective questioning: "So if I understand correctly, you're building [summary] — is that right?"

---

## Stakeholder Matrix (GA tier only)

Before writing the PRD, map who cares about what:

| Stakeholder | Primary concern | Success looks like |
|---|---|---|
| End users | Solves their problem, easy to use | Adoption, retention |
| Engineering | Clear scope, testable criteria, tech constraints respected | Ship date, no scope creep |
| Product / PM | Aligned with roadmap, measurable outcomes | KPI improvement |
| Business / investor | Revenue, growth, defensibility | ARR, users, moat |

Include this table in the GA PRD. Ask the user to validate it before writing.

---

## Technology Discussion

When evaluating tech options:
- Research current best practices via WebSearch before recommending
- Give 2–3 alternatives with brief pros/cons
- Always make one recommendation with explicit rationale
- Keep it conceptual — no code-level detail at this stage
- Note if an ADR should be created for significant architecture decisions

If the decision is high-stakes (e.g. SQL vs NoSQL, monolith vs microservices), say: "This is a significant architecture decision — after the PRD we should create an ADR via the `adr` skill to record the trade-offs formally."

---

## Success Metrics Scaffolding

For every major feature, define at least one measurable success criterion:

| Feature | Primary metric | Target at 90 days |
|---|---|---|
| User auth | Login success rate | >99% |
| Search | Queries returning results | >95% |
| Core workflow | Task completion rate | >80% |

These become the acceptance criteria in the PRD and the basis for TDD tests. Format them to be directly usable as test assertions.

---

## PRD Creation Process

After sufficient information (enough to fill the tier's template):

1. Announce you're generating the PRD
2. Use WebSearch/WebFetch to validate key technology choices against current best practices
3. Generate the document at the chosen tier
4. Present for feedback
5. Write to `PRD-[ProjectName]-[YYYY-MM-DD].md`

---

## PRD Templates

### Discovery (1-pager)

```markdown
# [Project Name] — Concept Brief
**Date**: [date]  **Stage**: Discovery

## Problem
[1 paragraph — the pain being solved and who has it]

## Proposed Solution
[1 paragraph — what this does and how it's different]

## Target User
[Who, in one sentence]

## Core Value Propositions (3 max)
- 
- 
-

## Key Assumptions to Validate
[What needs to be true for this to work — to be tested before building]

## Rough Scope (v1 only)
[5 bullet features max]

## Open Questions
[What's still unknown]
```

### Alpha (Standard PRD)

```markdown
# PRD: [Project Name]
**Date**: [date]  **Version**: 1.0  **Stage**: Alpha

## Overview
[2–3 sentence product vision]

## Target Audience
[Who, what problem, key user needs]

## Core Features
### Feature 1: [Name]
- Description
- Acceptance criteria (specific, testable — format for TDD handoff)
- Technical considerations
- Dependencies

[repeat per feature]

## Technical Stack Recommendation
| Layer | Recommendation | Rationale |
|---|---|---|

## Data Model
[Key entities, fields with types, relationships]

## Security Considerations
[Auth method, data protection, key risks]

## Development Phases
| Phase | Scope | Estimated effort |
|---|---|---|

## Success Metrics
| Feature | Metric | 90-day target |
|---|---|---|

## Out of Scope (v1)
[Explicit non-goals — what's NOT being built now]

## Potential Challenges
[Top 3 risks with mitigation strategies]
```

### GA (Full PRD)

Everything in Alpha, plus:

```markdown
## Stakeholder Matrix
[Table from framework above]

## Compliance & Legal
[GDPR, HIPAA, SOC2, accessibility, export control]

## Scalability Plan
[Architecture for current load; trigger points for scaling]

## Cost Model
[Hosting, APIs, personnel at launch vs. scale]

## Go-to-Market Alignment
[How engineering scope maps to launch milestones]

## Future Expansion (v2+)
[What's explicitly deferred and why]

## Architecture Decision Log
[Link to ADRs created for this product]
```

---

## Handoff Quality Rules

- Acceptance criteria: specific and testable — "users can log in via email or Google OAuth 2.0, receive a JWT, and stay logged in across restarts" not "users can log in"
- Data models: explicit field names, types, and relationships — not "user data"
- Feature groupings: organized to map to development sprints
- Complex features: include algorithm description or pseudocode
- Every recommended technology: link to documentation
- Success metrics: formatted so they can become direct TDD assertions

---

## Skill Cross-References

| Situation | Invoke |
|---|---|
| Significant architecture decision during questioning | `adr` (create during or after PRD) |
| Tech stack research needed | WebSearch → WebFetch for official docs |
| Acceptance criteria → test suite | `tdd` skill handoff after PRD is approved |
| Claims about market size or competitor landscape need verification | `fact-checker` |
| PRD is research-backed (requires due diligence) | `deep-research` → PRD |

---

## Iteration

After presenting the PRD:
- Ask section-specific questions, not "any feedback?"
- Example: "Does the technical stack align with your team's expertise?"
- Example: "Are the acceptance criteria testable as written?"
- Apply targeted updates and explain what changed
- Re-save the file after each revision
- Offer to create an ADR for any significant technology decision recorded in the PRD
