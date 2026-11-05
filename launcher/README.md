# Liquid Glass Home (Minimalist Apple-style Android Launcher)

<p align="center">
  <img src="../docs/liquid-glass-home.jpg" alt="Liquid Glass Home UI" width="450">
</p>

A super-clean, lightweight Android home screen inspired by Apple's minimalist frosted glass design.
Built as the second stage of **CleanYourPhone** to replace ad-bloated OEM home screens.

<p align="center">
  <img src="../docs/glass-dock-detail.jpg" alt="Liquid Glass Dock Detail" width="650">
</p>

---

## Key Features

- **Liquid Glass Dock:** A floating, rounded translucent glass pill at the bottom housing your top 4–5 favorite apps.
- **Apple-Inspired Minimalist Typography:** Thin San Francisco / Outfit-style digital clock and date pill.
- **Frosted Search Pill:** Fast real-time app search with zero online network requests or telemetry.
- **Fluid Spring Physics:** Scale-bounce touch feedback and spring animations.
- **Contextual Glass Dialog:** Long-press any app to pin/unpin from the dock, view system app info, or uninstall.
- **Extreme Battery & Memory Efficiency:**
  - Written in clean Java & AndroidX (no heavy web runtimes or Kotlin bloat).
  - Uses less than 15 MB of RAM (compared to OEM launchers taking 250 MB–500 MB).
  - 100% offline, zero ads, zero tracking permissions.

---

## Building and Installing

### Automated (One-Click)

#### On Linux / macOS:
```bash
./launcher/build-and-install.sh
```

#### On Windows (PowerShell):
```powershell
.\launcher\build-and-install.ps1
```

### Manual Build via Gradle
```bash
cd launcher
./gradlew assembleRelease
adb install app/build/outputs/apk/release/app-release.apk
```
