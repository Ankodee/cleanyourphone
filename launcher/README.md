# Lawnchair Launcher (CleanYourPhone Integration)

[![Lawnchair Upstream](https://img.shields.io/badge/Upstream-LawnchairLauncher%2Flawnchair-blue?logo=github)](https://github.com/LawnchairLauncher/lawnchair)
[![License: GPL-3.0 / Apache-2.0](https://img.shields.io/badge/License-GPL--3.0%20%2F%20Apache--2.0-green.svg)](https://github.com/LawnchairLauncher/lawnchair/blob/15-beta/LICENSE.txt)
[![Android Compatibility](https://img.shields.io/badge/Android-5.0%20to%2015.0+-brightgreen.svg)](#supported-android-versions)

**CleanYourPhone** integrates **[Lawnchair Launcher](https://github.com/LawnchairLauncher/lawnchair)**—the legendary free and open-source Android home screen replacement based on AOSP Launcher3. It brings the pure Google Pixel launcher experience to any device, enriched with deep customization, dynamic Material You theming, and an uncompromising commitment to privacy and zero bloat.

The upstream Lawnchair source tree is integrated directly as a Git submodule at [`launcher/lawnchair`](https://github.com/LawnchairLauncher/lawnchair) pinned to official releases.

---

## Why Lawnchair?

* **Pixel-Pure Experience:** Clean, fluid home screen and app drawer directly derived from the Android Open Source Project (AOSP Launcher3).
* **Material You Dynamic Theming:** Full Android 12+ Monet color extraction adapting seamlessly to your active wallpaper.
* **Smart "At a Glance" & Quick Search:** Clean weather, date, calendar integration, and fast offline application indexing.
* **Deep Customization:** Grid layout customization (4x4, 4x5, 5x5, 6x6), custom icon pack support, dock configuration, and drawer folders.
* **0.5x Lag-Free Transition Speeds:** Automated system animation scaling (`window_animation_scale 0.5`, `transition_animation_scale 0.5`, `animator_duration_scale 0.5`) for an instantaneous response on both flagship and budget hardware.
* **Privacy-First & Zero Bloat:** 100% open-source, zero advertising, zero OEM telemetry, and zero tracking. Consumes a fraction of the RAM used by stock launchers (ColorOS Home, MIUI Launcher, or Funtouch Launcher).

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
