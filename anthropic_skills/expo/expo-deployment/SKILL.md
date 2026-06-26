---
name: expo-deployment
description: Deploy Expo apps to production with EAS — build and submit to the iOS App Store, Google Play Store, and TestFlight, configure eas.json build and submit profiles, manage app versions and build numbers, publish App Store metadata and ASO, and deploy web bundles and API routes via EAS Hosting. Use whenever the user is preparing a production build, running eas build or eas submit, shipping to TestFlight, releasing or rolling out to the app stores, bumping version or build numbers, or setting up store listing metadata for an Expo app.
auto-trigger:
  - '"build the app", "submit to App Store / Play Store", "TestFlight", "eas build", "ship the Expo app"'
  - preparing a production build or bumping version/build numbers
  - setting up store metadata/ASO or deploying web bundles/API routes via EAS Hosting
do-not-trigger:
  - authoring app screens/navigation/UI (use building-native-ui)
  - non-Expo mobile stacks (native iOS/Android without Expo/RN)
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
---

# Deployment

Deploy Expo applications across all platforms using EAS (Expo Application Services). Expo docs + EAS CLI are the source of truth; verify against current docs.

> Upstream reference files (consult as needed): `workflows.md` (CI/CD, PR previews), `testflight.md`, `app-store-metadata.md` (ASO), `play-store.md`, `ios-app-store.md`.

## Quick start

```bash
npm install -g eas-cli
eas login
npx eas-cli@latest init      # creates eas.json with build profiles
```

## Build

```bash
npx eas-cli@latest build -p ios --profile production
npx eas-cli@latest build -p android --profile production
npx eas-cli@latest build --profile production            # both
```

## Submit to stores

```bash
npx eas-cli@latest build -p ios --profile production --submit       # App Store Connect
npx eas-cli@latest build -p android --profile production --submit   # Play Store
npx testflight                                                       # iOS TestFlight shortcut
```

## Web (EAS Hosting)

```bash
npx expo export -p web
npx eas-cli@latest deploy --prod    # production
npx eas-cli@latest deploy           # PR preview
```
Expo Router API routes deploy together with the web bundle — `eas deploy` ships both.

## eas.json (production)

```json
{
  "cli": { "version": ">= 16.0.1", "appVersionSource": "remote" },
  "build": {
    "production": { "autoIncrement": true, "ios": { "resourceClass": "m-medium" } },
    "development": { "developmentClient": true, "distribution": "internal" }
  },
  "submit": {
    "production": {
      "ios": { "appleId": "your@email.com", "ascAppId": "1234567890" },
      "android": { "serviceAccountKeyPath": "./google-service-account.json", "track": "internal" }
    }
  }
}
```

## Platform notes

- **iOS** — `npx testflight` for quick TestFlight; configure credentials via `eas credentials`.
- **Android** — Google Play service account; tracks: internal → closed → open → production.
- **Web** — EAS Hosting gives PR preview URLs; production to a custom domain.

## Version management

`appVersionSource: "remote"` lets EAS manage versions:
```bash
eas build:version:get
eas build:version:set -p ios --build-number 42
```

## Monitoring

```bash
eas build:list      # recent builds
eas build:view      # build status
eas submit:list     # submission status
```

EAS Workflows automate the build → submit → update → deploy pipeline for CI/CD.
Never commit signing credentials, keystores, or `.env` secrets.
