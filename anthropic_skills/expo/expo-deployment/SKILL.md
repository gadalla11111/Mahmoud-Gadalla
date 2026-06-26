---
name: expo-deployment
description: Build, submit, and ship Expo / React Native apps — EAS Build (cloud iOS/Android binaries), EAS Submit (App Store / Play Store), TestFlight & internal distribution, EAS Update (OTA), and web hosting. Expo docs, Expo CLI, and EAS CLI are the source of truth — verify against current docs rather than training data.
auto-trigger:
  - '"build the app", "submit to App Store / Play Store", "TestFlight", "EAS build", "ship the Expo app"'
  - deploying or distributing an Expo / React Native app
  - setting up OTA updates (EAS Update) or web hosting for an Expo project
do-not-trigger:
  - authoring app screens/navigation/UI (use expo-building-native-ui)
  - non-Expo mobile stacks (native iOS/Android without Expo/RN)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# expo-deployment — build, submit, ship

**Source of truth:** Expo docs + Expo CLI + EAS CLI. Verify commands/flags against current docs; Expo/EAS evolve.

## Build (EAS Build)

- Configure profiles in `eas.json` (`development`, `preview`, `production`).
- `eas build --platform ios|android|all --profile <profile>` — cloud binaries.
- Development builds (`expo-dev-client`) for local/TestFlight dev; preview for internal QA; production for store releases.
- Credentials: let EAS manage signing where possible; never commit certificates/keystores or secrets.

## Submit (EAS Submit)

- `eas submit --platform ios|android --profile production` — pushes the built binary to App Store Connect / Play Console.
- TestFlight: submit to App Store Connect, distribute via TestFlight for beta.
- Internal distribution: `preview` profile builds shareable via EAS without the stores.

## Over-the-air updates (EAS Update)

- `eas update --branch <branch>` — ship JS/asset changes without a new store build.
- Match update branches to build channels; gate rollouts and watch health (see eas-update-insights upstream).
- OTA only covers JS/assets — native changes require a new EAS Build.

## Web

- `npx expo export -p web` then deploy the static output (EAS Hosting or any static host).

## Rules

- Never commit signing credentials, keystores, or `.env` secrets.
- Bump native version/build numbers for store submissions; OTA for JS-only changes.
- Test the `preview` profile before `production`.
