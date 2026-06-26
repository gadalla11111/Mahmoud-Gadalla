---
name: expo-building-native-ui
description: Build Expo / React Native app UI — Expo Router screens and navigation, styling, animations, native tabs, and common app UI patterns. Expo docs and Expo Router docs are the source of truth — verify APIs against current docs.
auto-trigger:
  - '"add a screen", "set up navigation", "Expo Router", native tabs, app UI in an Expo project"'
  - building React Native screens/navigation/animations with Expo
do-not-trigger:
  - building/submitting/shipping the app (use expo-deployment)
  - web (non-React-Native) UI (use frontend-design / shadcn)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# expo-building-native-ui — Expo Router app UI

**Source of truth:** Expo + Expo Router docs. Verify APIs against current docs.

## Navigation (Expo Router)

- File-based routing under `app/` — files become routes; `_layout.tsx` defines navigators.
- Stack, Tabs, and Drawer via Expo Router layouts; use **native tabs** for platform-correct tab bars.
- Typed routes and `<Link>` / `router.push()` for navigation; dynamic segments via `[param].tsx`.

## Screens & patterns

- Compose screens from React Native primitives + Expo modules.
- Use platform-aware safe areas, headers configured in `_layout`, and modal routes for overlays.
- Data loading: pair with native data-fetching patterns (React Query / SWR / Router loaders).

## Styling & animation

- Styling via StyleSheet, or Tailwind for RN (`react-native-css` / NativeWind) where the project uses it.
- Animations via Reanimated / the Animated API; keep gestures on the UI thread.

## Rules

- Keep routes thin — push logic into components/hooks.
- Respect platform conventions (iOS vs Android navigation/tab behavior).
- For shipping the result, hand off to `expo-deployment`.
