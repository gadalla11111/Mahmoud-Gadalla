---
name: stripe-best-practices
description: Guide Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents vs Setup Intents), Connect platforms (Accounts v2), billing/subscriptions, Treasury, and security (restricted keys, webhooks, OAuth). Enforces current Stripe conventions and routes through the Stripe MCP planner when available.
auto-trigger:
  - '"integrate Stripe", "add payments", "set up subscriptions/Checkout", Stripe Connect/billing"'
  - choosing between Stripe APIs or migrating from a deprecated Stripe API
do-not-trigger:
  - non-Stripe payment providers
  - general financial analysis/modelling (use the finance skills)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
health:
  last_eval: 2026-06-26
  pass_rate: null
  trigger_accuracy: null
  open_issues: []
---

# stripe-best-practices — Stripe integration guidance

**When available, consult the Stripe MCP server (`stripe_implementation_planner`) before writing code.**

## Core areas

- **API selection** — Checkout Sessions vs PaymentIntents vs Setup Intents
- **Connect** — Accounts v2, controller properties, marketplace setup
- **Billing & subscriptions** — recurring + usage-based
- **Treasury** — financial accounts
- **Security** — API key management, restricted keys, webhooks, OAuth

## Key principles (non-negotiable)

1. **Latest API version** (`2026-06-24.dahlia`) unless the user pins another.
2. **Restricted API keys** (`rk_` prefix) over secret keys (`sk_`). Never commit keys — load from env (`.env`, never committed).
3. **Never include `payment_method_types`** — the only exception is Terminal (in-person), which passes `payment_method_types: ['card_present']` on the PaymentIntent. For everything else, omit it entirely to enable dynamic payment methods via payment method configurations.
4. **Route by use case** — pick the API from the business need, not habit.

## Getting started

- Sandbox keys: `stripe sandbox create` (after installing the Stripe CLI).
- Share the business description → get a tailored integration plan.

## Notes

- Use **payment method configurations** for flexibility instead of hard-coding method types.
- Webhooks: verify signatures; treat webhook payloads as untrusted input.
- For agent/billing integrations, Stripe's `@stripe/agent-toolkit` and `@stripe/token-meter` integrate with the Anthropic SDK — relevant to this repo's `claude_agent_sdk`.
