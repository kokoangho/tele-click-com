# Android update

The Android project now uses the same verified game runtime as `game/index.html`.

## Synchronized assets
- `game/index.html` == `android/app/src/main/assets/index.html`
- `game/tech-nodes.json` == `android/app/src/main/assets/tech-nodes.json`

## Native Android shell
- WebView DOM storage/database persistence disabled.
- WebView cache disabled and stale WebStorage cleared on launch.
- View state saving disabled.
- Overscroll, native haptic feedback, scrollbars, and long-click behavior disabled.
- Android app backup disabled so old WebView data is not restored through app backup.
- Native WebView background matches the game background.

## Build configuration
- compileSdk / targetSdk: 36
- AGP: 8.13.2
- Gradle wrapper target: 8.13
- Java source/target: 17
- versionCode: 2
- versionName: 1.1.0

## Included latest gameplay fixes
- Click page contains Revenue + Quality only at the top.
- No `TAP ANYWHERE HERE TO CONNECT` label.
- No click flash/tap highlight.
- Session-only game: no progress persistence.
- Bank credit limit = current revenue/s × 1,800.

## Validation performed
- JavaScript syntax checked with Node.
- Android XML files parsed successfully.
- Main and Android HTML hashes match.
- Main and Android tech-node JSON hashes match.

A full Gradle build could not be executed in the editing environment because it cannot download the Gradle distribution and no Android SDK is installed there.
