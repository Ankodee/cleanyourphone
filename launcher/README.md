# Lawnchair Launcher (CleanYourPhone Integration)

[![Lawnchair Upstream](https://img.shields.io/badge/Upstream-LawnchairLauncher%2Flawnchair-blue?logo=github)](https://github.com/LawnchairLauncher/lawnchair)
[![License: GPL-3.0 / Apache-2.0](https://img.shields.io/badge/License-GPL--3.0%20%2F%20Apache--2.0-green.svg)](https://github.com/LawnchairLauncher/lawnchair/blob/15-beta/LICENSE.txt)
[![Android Compatibility](https://img.shields.io/badge/Android-5.0%20to%2015.0+-brightgreen.svg)](#supported-android-versions)

**CleanYourPhone** integrates **[Lawnchair Launcher](https://github.com/LawnchairLauncher/lawnchair)**—the legendary free and open-source Android home screen replacement based on AOSP Launcher3. It brings the pure Google Pixel launcher experience to any device, enriched with deep customization, dynamic Material You theming, and an uncompromising commitment to privacy and zero bloat.

The upstream Lawnchair source tree is integrated directly as a Git submodule at [`launcher/lawnchair`](https://github.com/LawnchairLauncher/lawnchair) pinned to official releases.

<p align="center">
  <img src="../docs/lawnchair-ui-showcase.jpg" alt="Lawnchair Launcher Clean UI Overview" width="850">
</p>

---

## What Does the UI Look Like?

Lawnchair delivers an uncluttered, distraction-free interface engineered for instant ergonomics:

1. **Smart "At a Glance" Card:**
   - Prominently displays the current day, date, and live local weather (`Sunny 24°C`) alongside calendar alerts and alarms.
   - Built-in Smartspacer and weather feed support with zero background battery drain.
2. **Unified Search Capsule:**
   - Floating search bar at the top or bottom of the screen with quick access to local apps, web search engines (Google, DuckDuckGo, Brave), and system shortcuts.
3. **Themed Material You App Grid:**
   - Symmetrical 4x4, 4x5, or 5x5 app grid featuring adaptive squircles tinted dynamically with colors extracted from your active wallpaper.
4. **Anchored Floating Dock:**
   - Translucent glass island at the bottom holding your 4 or 5 primary communication and utility apps (Phone, Messages, Browser, Camera).

---

## Special Features of Lawnchair Launcher

<p align="center">
  <img src="../docs/lawnchair-features.jpg" alt="Lawnchair Launcher 3-Screen Feature Progression" width="850">
</p>

### 1. Dynamic Monet Wallpaper Palette Theming
Lawnchair incorporates Android 12+ Material 3 Expressive theming. When you change your wallpaper, Lawnchair automatically recalculates five tonal palettes (Primary, Secondary, Tertiary, Neutral, Neutral Variant) and applies harmonious color accents across app icons, search capsules, dialogs, and folders.

### 2. Smart App Drawer & Real-Time Fuzzy Search
- **Instant Filtering:** Swipe up anywhere on the home screen to open the app drawer. Typing immediately filters installed applications with sub-millisecond response.
- **Categorized Tabs:** Group your apps into custom tabs (Work, Media, Games, Finance) or hide apps from view without uninstalling them.
- **Alphabet Quick-Scrubber:** Jump directly to any letter in your app catalog with a silky haptic touch scrubber.

### 3. Granular Customization Engine
- **Custom Icon Packs:** Full compatibility with Lawnicons, Google Material icons, and third-party icon packs from GitHub or Play Store.
- **Adaptive Icon Shapes:** Force uniform icon geometry across all apps (Circle, Squircle, Rounded Square, Teardrop).
- **Adjustable Grid Sizing:** Freely configure home screen and drawer rows/columns from 4x4 up to 7x7.
- **Dock Adjustments:** Customize icon counts, scale dock sizes from 70% to 150%, or hide labels completely.

### 4. 0.5x Ultra-Fast Transition Speed & Physics
CleanYourPhone automatically clocks animation scales to **0.5x** over ADB during install:
- **150ms App Launch Transitions:** Custom half-duration zoom & activity changes.
- **80ms Touch Physics:** Instantaneous feedback when tapping icons or swiping between pages.
- **Zero Lag on Any Hardware:** Silky 60Hz, 90Hz, and 120Hz refresh rates without frame drops, even on older or budget devices.

<p align="center">
  <img src="../docs/lawnchair-customization-detail.jpg" alt="Lawnchair Launcher Customization & RAM Benchmarks" width="850">
</p>

### 5. Extreme Resource Efficiency & Zero Bloat
- **<20 MB RAM Consumption:** Compared to OEM launchers (ColorOS Home, One UI Home, Funtouch Launcher) that constantly run 350MB–600MB recommendation daemons in the background.
- **100% Offline & Private:** Zero ads, zero commercial recommendations, zero tracking SDKs, and zero network analytics uploaders.

---

## Supported Android Versions

The CleanYourPhone installer automatically inspects the connected device via ADB and delivers the optimal Lawnchair edition for your Android build:

| Android Version | SDK Level | Lawnchair Release | Upstream Branch |
|---|---|---|---|
| **Android 14 & 15** | SDK 34–35+ | **Lawnchair 15 (Beta 3.0)** | `15-beta` |
| **Android 10 – 13** | SDK 29–33 | **Lawnchair 14 (Beta 3)** | `14-beta` |
| **Android 5 – 9** (ColorOS 5, older Oppo/Vivo) | SDK 21–28 | **Lawnchair 2.0 (Legacy)** | `legacy` |

---

## Installation & Setup

### Automated (One-Click ADB Installer)

Connect your phone via USB or Wireless ADB with USB Debugging enabled, then run:

#### Windows (PowerShell):
```powershell
.\launcher\build-and-install.ps1
```
*To automatically disable your OEM stock launcher (Oppo, Vivo, Xiaomi, Realme, etc.):*
```powershell
.\launcher\build-and-install.ps1 -DisableStock
```

#### Linux / macOS (Bash):
```bash
./launcher/build-and-install.sh
```
*To automatically disable your OEM stock launcher:*
```bash
./launcher/build-and-install.sh --disable-stock
```

The script will automatically:
1. Detect your connected device's manufacturer and Android SDK level.
2. Provide or download the matching official signed release APK directly from Lawnchair's GitHub releases.
3. Install the APK via `adb install -r -d`.
4. Set Lawnchair as your primary home activity (`cmd package set-home-activity` / `pm set-home-activity`).
5. Tune animation speeds to **0.5x** for immediate, stutter-free performance.
6. Launch Lawnchair directly onto your device.

---

## Building from Source

The complete upstream repository is included as a Git submodule:

```bash
# Initialize and fetch the upstream Lawnchair repository
git submodule update --init --recursive launcher/lawnchair

# Build release APK using Gradle
cd launcher/lawnchair
./gradlew assembleLawnchairRelease
```

---

## Credits & Upstream Repository
- **Lawnchair Project:** [https://github.com/LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair)
- **Website:** [https://lawnchair.app](https://lawnchair.app)
- **License:** GNU General Public License v3.0 / Apache License 2.0
