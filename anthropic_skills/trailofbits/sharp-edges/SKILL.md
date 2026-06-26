---
name: sharp-edges
description: Evaluate whether APIs, configurations, and interfaces resist developer misuse — finding "footgun" designs where insecure usage is the path of least resistance. Use when reviewing an API/SDK/config surface for error-prone design, dangerous defaults, and misuse-inviting interfaces.
auto-trigger:
  - '"is this API safe to misuse", "review this interface for footguns", dangerous defaults"'
  - designing/reviewing a security-relevant API or configuration surface
do-not-trigger:
  - scanning code for known vulnerability patterns (use semgrep / codeql)
  - runtime incident triage (use sentry-fix-issues)
allowed-tools: Read, Grep, Glob
---

# sharp-edges — footgun / misuse-resistance analysis

**Core principle:** secure usage should be the path of least resistance. If developers must understand cryptography, read docs carefully, or remember special rules to avoid vulnerabilities, the API has failed.

## Six sharp-edge categories

1. **Algorithm/mode selection footguns** — letting devs pick primitives invites weak ones (JWT `alg: none`).
2. **Dangerous defaults** — `timeout=0`, `verify=false` — disable security or carry ambiguous semantics.
3. **Primitive vs semantic APIs** — raw bytes instead of meaningful types let unrelated params swap without type errors.
4. **Configuration cliffs** — one misconfigured setting causes catastrophic failure with no validation warning.
5. **Silent failures** — security ops that fail without surfacing errors, or succeed on malformed input.
6. **Stringly-typed security** — security-critical values as plain strings (not enums) enable injection/confusion.

## Workflow

1. **Surface identification** — map security-relevant APIs.
2. **Edge-case probing** — test zero/empty/null semantics.
3. **Threat modeling** — consider three developer archetypes (rushed, inexperienced, adversarial).
4. **Validation** — reproduce actual vulnerabilities.

## Reject these rationalizations

"It's documented" · "advanced users need flexibility" · "it's the developer's responsibility" · "we need backwards compatibility" — all fail: developers work under pressure and shouldn't need expertise to avoid vulnerabilities.
