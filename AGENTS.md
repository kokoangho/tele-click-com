# AGENTS.md

## ⛔ CRITICAL: No personal info in any production file
Never put user's name, home directory paths, or personal identifiers in app files.
Use placeholders like `<your-jdk-path>` in docs. Build caches and local.properties are auto-generated exceptions.

## Config
Project config at `config` in repo root. Contains package name, version info, SDK targets.

## Build
Android project at `android/`. Package name in `config` must match `app/build.gradle`.

To build .aab:
```
cd android
# Set JAVA_HOME and ANDROID_HOME for your environment
./gradlew bundleRelease --no-daemon
```
Output: `app/build/outputs/bundle/release/app-release.aab`

## Game
Game source at `game/index.html`. Single-file HTML/CSS/JS. Copy to `android/app/src/main/assets/` before build.

## Key files
- `config` — package name, version, SDK
- `game/index.html` — game source
- `android/app/build.gradle` — app module config
- `android/app/src/main/java/com/teleclick/app/MainActivity.java` — WebView wrapper
