---
name: terraform-test
description: Write and run Terraform tests — `.tftest.hcl` files with run blocks, assertions, provider mocking, and module validation. Use when creating test scenarios, validating infrastructure behavior, mocking providers/data sources, testing module outputs, or troubleshooting test syntax/execution.
auto-trigger:
  - '"test this Terraform module", "write a .tftest", "validate the module behavior"'
  - adding assertions/mocks around Terraform config
do-not-trigger:
  - authoring the Terraform config itself (use terraform-style-guide)
  - Terraform Stacks deployment config (use terraform-stacks)
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# terraform-test — the Terraform testing framework

Validate that config changes don't break existing infra by running against temporary resources. Mock providers require Terraform 1.7.0+.

## Concepts

- **Test file** `.tftest.hcl` — holds run blocks.
- **run block** — one scenario; optional variables/providers/asserts.
- **assert block** — condition that must be true to pass.
- **Mock provider** — simulates a provider without real infra.
- **Modes** — `plan` validates logic only; `apply` creates resources.

## Layout

```
my-module/
├── main.tf  variables.tf  outputs.tf
└── tests/
    ├── defaults_unit_test.tftest.hcl
    ├── validation_unit_test.tftest.hcl
    └── full_stack_integration_test.tftest.hcl
```
`*_unit_test` / `*_integration_test` naming enables CI filtering.

## Patterns

```hcl
assert {
  condition     = output.vpc_id != null
  error_message = "VPC ID output must be defined"
}
```
- Conditional resources: assert `length(aws_nat_gateway.main) == 0` when disabled.
- Resource counts: assert `length(aws_instance.workers) == 3`.
- Invalid-input rejection: `expect_failures = [var.environment]`.
- Sequential deps: `vpc_id = run.setup_vpc.vpc_id`; isolate with `state_key`.

## Commands

```bash
terraform test                                 # all
terraform test tests/defaults.tftest.hcl       # one file
terraform test -filter=test_vpc_configuration  # one run block
terraform test -verbose
terraform test -no-cleanup                     # debug: preserve resources
```

## Best practices

- Default `command = plan` unless testing real behavior.
- Descriptive run-block names; specific error messages.
- Mock external providers (faster, no credentials).
- Unit tests on PRs, integration tests on merge.
- Resources destroy in reverse run-block order.
