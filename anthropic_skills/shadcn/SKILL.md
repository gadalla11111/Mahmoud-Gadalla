---
name: shadcn
description: Manage shadcn/ui components and projects — add, search, fix, style, and compose. Activates on projects with a components.json; injects project context via shadcn info, prioritizes existing registry components over custom UI, and enforces shadcn composition + Tailwind v4 patterns. Strengthens the Design → Frontend stacks.
auto-trigger:
  - '"add a shadcn component", "shadcn init", building UI in a project with components.json"'
  - composing forms/dialogs/tables with shadcn/ui
  - switching presets (Radix vs Base UI) or working with the component registry
do-not-trigger:
  - non-shadcn UI work / no components.json (use frontend-design)
  - pure visual/brand decisions with no components (use design / brand-guidelines)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# shadcn — shadcn/ui component management

**Activation:** projects with a `components.json`. CLI via `npx shadcn@latest` (or `pnpm dlx` / `bunx --bun`).

## Core principles

1. **Prioritize existing components** — search the registry before building custom UI.
2. **Compose strategically** — combine components rather than reinventing patterns.
3. **Use built-in variants** — semantic styling before custom CSS.
4. **Semantic colors** — design tokens like `bg-primary`, never raw hex values.

## Critical rules

**Styling / Tailwind v4**
- `gap-*` with `flex`, not `space-x-*` / `space-y-*`.
- `size-*` for equal dimensions instead of separate width/height.
- `truncate` shorthand; avoid semantic color overrides in dark mode.

**Forms**
- Nest inputs in `FieldGroup` + `Field`.
- `ToggleGroup` for 2–7 option sets.
- `data-invalid` / `aria-invalid` for validation states.

**Structure**
- Keep items in their parent groups (`SelectItem` → `SelectGroup`).
- Accessible titles required on overlays (Dialog, Sheet, Drawer).
- Full Card composition (header + footer).

**Icons**
- `data-icon="inline-start"` / `"inline-end"` on icons in buttons.
- Never add sizing classes to icons inside components.

## Workflow

1. Inject project context: `npx shadcn@latest info --json`.
2. Check installed components before adding new ones.
3. Fetch docs: `npx shadcn@latest docs <component>`.
4. Use `--dry-run` and `--diff` when updating existing components.
5. Verify added files match the composition rules above.

## Common selections

| Need | Component |
|---|---|
| Forms | `Input`, `Select`, `Combobox`, `Checkbox`, `RadioGroup` |
| Data | `Table`, `Card`, `Badge`, `Avatar` |
| Navigation | `Sidebar`, `Tabs`, `Breadcrumb`, `Pagination` |
| Overlays | `Dialog`, `Sheet`, `Drawer`, `AlertDialog` |
| Feedback | `sonner` toast, `Alert`, `Progress`, `Skeleton` |
