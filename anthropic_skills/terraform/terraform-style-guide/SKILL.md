---
name: terraform-style-guide
description: Generate Terraform HCL following HashiCorp's official style conventions — file organization, naming, formatting, variable/output requirements, version pinning, and pre-commit validation. Use when writing, reviewing, or generating Terraform configurations.
auto-trigger:
  - '"write Terraform", "generate the HCL", "review this .tf", Terraform config authoring'
  - creating or refactoring `.tf` files / modules
do-not-trigger:
  - writing Terraform tests (use terraform-test)
  - Terraform Stacks `.tfcomponent.hcl` / `.tfdeploy.hcl` (use terraform-stacks)
  - building a Terraform provider (out of scope — provider-development skills)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# terraform-style-guide — HashiCorp HCL conventions

Reference: https://developer.hashicorp.com/terraform/language/style

## Generation order

1. Provider config + version constraints → 2. data sources → 3. resources in dependency order → 4. outputs for key attributes → 5. variables for all configurable values.

## File organization

| File | Purpose |
|---|---|
| `terraform.tf` | Terraform + provider version requirements |
| `providers.tf` | Provider configurations |
| `main.tf` | Primary resources + data sources |
| `variables.tf` | Input variables (alphabetical) |
| `outputs.tf` | Outputs (alphabetical) |
| `locals.tf` | Local values |

## Formatting & naming

- Two-space indent (no tabs); align `=` for consecutive args; block order: meta-args → args → blocks → lifecycle.
- lowercase_with_underscores; descriptive nouns excluding the resource type; singular; default to `main` when a name would be redundant.
- Prefer `for_each` over `count` for multiple named resources; `count` only for conditional toggling.

## Variables & outputs

- Every variable: `type` + `description`; add `validation` for constrained values.
- Every output: `description`; mark secrets `sensitive = true`.

## Version control

- **Never commit:** state files, `.terraform/`, plan files, `.tfvars` with secrets.
- **Always commit:** config files + `.terraform.lock.hcl`.

## Validate before commit

`terraform fmt -recursive` → `terraform validate`. Additional: `tflint`, `checkov`, `tfsec`.
