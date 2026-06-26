---
name: neon-postgres
description: Guide any Neon Serverless Postgres task — setup, connections, code-like branching, autoscaling, and scale-to-zero. Matches connection drivers to runtime (TCP pooled for long-running, HTTP/serverless driver for edge/serverless). Neon's official docs are the source of truth — verify against them, prefer fetching current docs over training data.
auto-trigger:
  - '"set up Neon", "connect to Neon Postgres", "create a database branch", Neon connection string"'
  - working with a Neon serverless Postgres database (any language/ORM)
  - configuring autoscaling, scale-to-zero, or branch-per-preview
do-not-trigger:
  - diagnosing high Postgres egress / data-transfer bills (use neon-postgres-egress-optimizer)
  - a non-Neon Postgres host (generic Postgres setup; this skill is Neon-specific)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# neon-postgres — Neon Serverless Postgres

**Source of truth:** Neon's official docs. Neon's features/APIs evolve — verify claims against current docs rather than relying on training data. Keep direct quotes ≤125 chars; paraphrase otherwise.

## What Neon is

Serverless Postgres with compute/storage separated: autoscaling, code-like database **branching**, instant restore, and **scale-to-zero**. Fully Postgres-compatible — works with any language, framework, or ORM that speaks Postgres.

## Setup paths

1. **Self-driving** — `neonctl init --agent` scaffolds a project and writes connection config.
2. **CLI / MCP** — configure via the Neon CLI or the Neon MCP server for project/branch operations.
3. **Direct** — manage the connection string yourself; store it in `.env` (never commit it).

## Connection driver — match to runtime

- **Long-running** (servers, workers) → standard TCP connection, pooled.
- **Serverless / edge** (Workers, Vercel functions) → Neon's **HTTP/serverless driver** — avoids per-invocation TCP setup.

## Common tasks

- **Branching** — create a branch per preview/PR; branches are cheap and isolated. Tear down on merge.
- **ORM integration** — works with any Postgres ORM; Drizzle has first-class Neon support.
- **Infra-as-code** — `neon.ts` to declare autoscaling limits and auto-expiration for non-prod branches.
- **Cost** — enable scale-to-zero on dev/preview branches so idle compute costs nothing.

## Rules

- Never commit the connection string / `.env`.
- Pick the driver by runtime, not by habit — the HTTP driver in a long-running server wastes Neon's pooling.
- For egress/bill problems, hand off to `neon-postgres-egress-optimizer`.
