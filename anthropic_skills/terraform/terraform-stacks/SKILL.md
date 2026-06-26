---
name: terraform-stacks
description: Create, modify, and validate Terraform Stacks — the configuration layer above modules for orchestrating components across environments, regions, and cloud accounts. Use for `.tfcomponent.hcl` / `.tfdeploy.hcl` files, stack components/deployments, multi-region/multi-env infra, and Stacks syntax. Requires Terraform CLI v1.13+ (Stacks GA).
auto-trigger:
  - '"Terraform Stack", ".tfcomponent.hcl", ".tfdeploy.hcl", multi-environment/multi-region infra"'
  - orchestrating components/deployments above plain modules
do-not-trigger:
  - plain Terraform `.tf` authoring (use terraform-style-guide)
  - writing `.tftest.hcl` tests (use terraform-test)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# terraform-stacks — orchestration above modules

Stacks = **components** (modules with source/inputs/providers) + **deployments** (instances per env/region/account). Stack Language is HCL-based but distinct from regular Terraform HCL.

## Files (all at repo root, processed in dependency order)

- `.tfcomponent.hcl` — component config (variables, providers, components, outputs)
- `.tfdeploy.hcl` — deployment config (identity tokens, deployments, groups)
- `.terraform.lock.hcl` — generated; commit it
- `.terraform-version` — require Terraform v1.13+ (use 1.14.x for current CLI)

## Component config essentials

- **variable** — needs `type`; no `validation`. Use `ephemeral = true` for credentials/tokens so they never persist to state.
- **required_providers** + **provider "aws" "alias"** — provider blocks support `for_each`, define alias in the header, configure via a `config {}` block.
- **component "vpc"** — `source` (local/registry/Git) + `inputs` + `providers`. Dependencies inferred from `component.<name>.<output>` references.
- **output** — needs `type`; no `preconditions`.

## Deployment config essentials

- **identity_token "aws"** — OIDC JWT for workload-identity auth (preferred over static creds); reference as `identity_token.aws.jwt`.
- **deployment "production"** — inputs per environment (1–20 per Stack); each has isolated state.
- **deployment_group** + **deployment_auto_approve** — auto-approval rules (Premium). `orchestrate` blocks are deprecated.
- **publish_output / upstream_input** — link Stacks together.

## CLI (no plan/apply — upload triggers runs)

```bash
terraform stacks init        # providers, modules, lock file
terraform stacks validate    # syntax, no upload
terraform stacks configuration upload   # triggers deployment runs
terraform stacks deployment-group watch -deployment-group=...
```
For automation/CI/agents, use the HCP Terraform API (not CLI watch, which streams indefinitely).

## Key rules

- Use **workload identity (OIDC)**; mark tokens `ephemeral = true`.
- Modules used in Stacks must NOT include provider blocks — configure providers in the Stack.
- Test public-registry modules before production (some have Stacks compatibility issues).
- Commit `.terraform.lock.hcl`; each deployment isolates its own state.
- Upstream reference files (component-blocks, deployment-blocks, linked-stacks, examples, api-monitoring) hold the full detail.
