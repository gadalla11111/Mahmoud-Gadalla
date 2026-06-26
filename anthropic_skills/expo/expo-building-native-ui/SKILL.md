---
name: building-native-ui
description: Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs.
auto-trigger:
  - '"add a screen", "set up navigation", "Expo Router", native tabs, app UI in an Expo project"'
  - building React Native screens/navigation/animations/styling with Expo
do-not-trigger:
  - building/submitting/shipping the app (use expo-deployment)
  - web (non-React-Native) UI (use frontend-design / shadcn)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# Building native UI (Expo Router)

Build beautiful apps with Expo Router. Expo + Expo Router docs are the source of truth.

> Upstream reference files: `animations.md`, `controls.md`, `form-sheet.md`, `gradients.md`, `icons.md`, `media.md`, `route-structure.md`, `search.md`, `storage.md`, `tabs.md`, `toolbar-and-headers.md`, `visual-effects.md`, `webgpu-three.md`, `zoom-transitions.md`.

## Running the app

**Always try Expo Go first before creating custom builds** — most Expo apps work without custom native code.
1. `npx expo start`, scan with Expo Go. 2. Test thoroughly. 3. Only use `npx expo run:ios/android` or `eas build` when required.

Custom builds needed only for: local Expo modules with native code, Apple targets (widgets/app clips/extensions), third-party native modules absent from Expo Go, custom native config beyond `app.json`.

## Code style

- kebab-case file names (`comment-card.tsx`); no special characters.
- Remove old route files when restructuring navigation.
- tsconfig path aliases over relative imports; imports at top of file.

## Routes

- Routes belong in the `app/` directory. **Do NOT co-locate** components/types/utilities there (anti-pattern).
- Requires a route matching `/` (may be inside a group route). See `route-structure.md`.

## Library preferences

- **Don't use:** removed RN modules (Picker, WebView, SafeAreaView, AsyncStorage), legacy `expo-permissions`.
- **Prefer:** `expo-audio`/`expo-video` (not expo-av); `expo-image` (incl. `source="sf:name"` for SF Symbols, not `img`); `react-native-safe-area-context`; `process.env.EXPO_OS` (not `Platform.OS`); `React.use` (not `useContext`); `expo-glass-effect` for liquid glass; `Color` from `expo-router` for native semantic colors. SDK 56+: import from `expo-router/react-navigation`.

## Responsiveness

- Wrap root in a ScrollView; use `<ScrollView contentInsetAdjustmentBehavior="automatic" />` instead of SafeAreaView (also on FlatList/SectionList).
- Flexbox over the Dimensions API; `useWindowDimensions` over `Dimensions.get()`.

## Styling (Apple HIG)

- **CSS and Tailwind are unsupported — use inline styles.**
- Prefer flex `gap` over margin/padding; padding over margin.
- Account for safe area via headers/tabs or `contentInsetAdjustmentBehavior="automatic"`; handle top + bottom insets.
- `{ borderCurve: 'continuous' }` for rounded corners; CSS `boxShadow` (never legacy shadow/elevation).
- Colors: `Color` API from `expo-router` (iOS re-resolves on theme change; on Android call `useColorScheme()` in color-rendering components). Don't pass `Color`/`PlatformColor` into Reanimated styles — use static colors there.
- `<Text selectable />` for important/copyable data; `{ fontVariant: 'tabular-nums' }` for counters; format large numbers (1.4M, 38k).

## Navigation

- `<Link href="/path" />`; wrap custom components with `asChild`. Include `<Link.Preview>` to follow iOS conventions where possible. Context menus via `Link.Trigger` / `Link.Menu` / `Link.MenuAction`.
- **ALWAYS use `_layout.tsx` to define stacks**; `Stack` from `expo-router/stack`. Page title: `<Stack.Screen options={{ title: "Home" }} />`.
- Modal: `presentation: "modal"`. Sheet: `presentation: "formSheet"` with `sheetGrabberVisible` / `sheetAllowedDetents`; `contentStyle: { backgroundColor: "transparent" }` gives liquid glass on iOS 26+.

Common structure:
```
app/
  _layout.tsx        // <NativeTabs />
  (index,search)/
    _layout.tsx      // <Stack />
    index.tsx        // main list
    search.tsx       // search view
```

## Behavior

- `expo-haptics` conditionally on iOS. Stack routes: ScrollView with `contentInsetAdjustmentBehavior="automatic"` as first child.
- Search bars via `headerSearchBarOptions` in `Stack.Screen`. Never use intrinsic elements (`img`/`div`) outside webviews/Expo DOM components.
