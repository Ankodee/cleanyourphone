# Liquid Glass Home (iOS-Style Minimalist Launcher)

<p align="center">
  <img src="../docs/liquid-glass-home.jpg" alt="Liquid Glass Home UI" width="450">
</p>

An ultra-clean, minimal, lag-free **iOS-style home screen launcher** featuring true liquid glass effects over your live background wallpaper.
Engineered with horizontal left-to-right SpringBoard paging, an iOS Smart Stack widget, a floating liquid glass dock, Spotlight search, and an iOS App Library—all running in under 15 MB of RAM with 0.5x snappy responsiveness.

<p align="center">
  <img src="../docs/glass-dock-detail.jpg" alt="Liquid Glass Dock Detail" width="650">
</p>

---

## Key Features

- **iOS 17/18 SpringBoard Left-to-Right Paging:** Horizontal paginated app pages that swipe smoothly left to right with silky 120Hz snap physics and animated iOS page indicator dots (`• • •`).
- **Live Wallpaper Liquid Glass Effect:** Real optical frosted glass refraction over your live system wallpaper with specular edge highlights, light dispersion, and real-time wallpaper blur pass-through.
- **iOS Smart Widget (Home Page):** Authentic frosted glass card on Page 1 displaying Apple-style live clock, day, date, and live battery level.
- **Floating Liquid Glass Dock:** Floating translucent glass island at the bottom housing your 4 primary apps (Phone, Messages, Browser, Camera) that stays anchored while pages swipe above.
- **iOS Spotlight "Search" Pill:** Floating glass pill (`🔍 Search`) right above the dock that smoothly opens the Spotlight search overlay for instant, real-time app filtering.

<p align="center">
  <img src="../docs/feature-search-library.jpg" alt="Liquid Glass 0.5x Search in Action" width="550">
</p>

- **iOS App Library (Last Page):** Swiping to the rightmost page reveals the iOS App Library with 2x2 frosted glass category folders (Suggestions, Utilities, Communication, Media) and quick search.
- **Haptic Context Menu:** Long-press any app icon to pin/unpin from the dock, view system app permissions, or uninstall.
- **Extreme Speed & Efficiency:**
  - 0.5x duration animations (instant launch, zero lag).
  - Uses less than 15 MB of RAM (compared to OEM launchers taking 350 MB–600 MB).
  - 100% offline, zero ads, zero telemetry, no tracking.

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
