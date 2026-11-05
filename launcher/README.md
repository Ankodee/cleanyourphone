# Liquid Glass Home (Minimalist Android Launcher)

<p align="center">
  <img src="../docs/liquid-glass-home.jpg" alt="Liquid Glass Home UI" width="450">
</p>

A super-clean, lightweight Android home screen with an ethereal liquid glass aesthetic.
Engineered with an Android-first philosophy (distinct from iOS clones) and tuned to 0.5x transition speed for a lag-free, ultra-responsive experience.
Built as the second stage of **CleanYourPhone** to replace ad-bloated OEM home screens.

<p align="center">
  <img src="../docs/glass-dock-detail.jpg" alt="Liquid Glass Dock Detail" width="650">
</p>

---

## Key Features

- **Android-First Liquid Glass Design:** Distinctly tailored for Android smartphones with centered punch-holes and curved edges. Features layered glass refraction, specular highlight edges, and dynamic live wallpaper pass-through.
- **0.5x Snappy Lag-Free Speed:** Transitions and touch responses tuned to 0.5x speed (50ms down, 80ms rebound) with hardware acceleration enabled for smooth 90Hz/120Hz scrolling.
- **Liquid Glass Glance Card:** Minimalist frosted glass card at the top displaying time, date, and clean status chips.
- **Frosted Search Capsule:** Fast real-time app search with zero online network requests or telemetry.
- **Floating Liquid Glass Dock:** Translucent glass island at the bottom housing your top 4–5 favorite apps.
- **Contextual Glass Dialog:** Long-press any app to pin/unpin from the dock, view system app info, or uninstall.
- **Extreme Battery & Memory Efficiency:**
  - Written in clean Java & AndroidX (no heavy web runtimes or Kotlin bloat).
  - Uses less than 15 MB of RAM (compared to OEM launchers taking 250 MB–500 MB).
  - 100% offline, zero ads, zero tracking permissions.
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
