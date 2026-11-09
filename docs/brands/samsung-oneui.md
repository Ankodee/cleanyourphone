# Debloating Samsung (One UI)

## Architecture Overview
Samsung Galaxy devices (Galaxy S, Z, A, M, and F series) run **One UI** (versions 1.0 through 7.0+ on Android 9 through 15+). While One UI offers exceptional hardware integration, Samsung devices ship with redundant app ecosystems, persistent analytics, background throttling services, and preinstalled promotional suites.

Packages occupy the `com.samsung.android.*`, `com.sec.android.*`, and Microsoft partner namespaces.

---

## Key Categories Removed

1. **Bixby Assistant Suite:**
   - Packages: `com.samsung.android.bixby.agent`, `com.samsung.android.bixby.service`, `com.samsung.android.bixby.wakeup`, `com.samsung.android.bixbyvision.framework`.
   - Disables background voice listeners and hotword detection without affecting Google Assistant.
2. **Samsung Ads, Promos & Feed Junk:**
   - Packages: `com.samsung.android.app.spage` (Samsung Free / Samsung O / Bixby Home), `com.samsung.android.dynamiclock` (Glance dynamic lockscreen stories), `com.samsung.android.app.tips`, `com.samsung.android.voc` (Samsung Members).
   - Eliminates home screen minus-one page ads and lockscreen sponsored clickbait.
3. **Telemetry & Performance Throttling:**
   - Packages: `com.sec.android.diagmonagent` (Diagnostic Monitor), `com.samsung.android.rubin.app` (Runestone user profiling engine), `com.samsung.android.game.gos` (Game Optimizing Service / GOS thermal/game throttling).
   - Reclaims CPU cycles, reduces idle battery consumption, and removes artificial gaming throttles.
4. **AR Zone & Avatar Bloat:**
   - Packages: `com.samsung.android.arzone`, `com.samsung.android.aremoji`, `com.samsung.android.aremojieditor`, `com.sec.android.mimage.avatarstickers`.
   - Removes preinstalled 3D avatar studios and sticker packages.
5. **Microsoft Preloads:**
   - Packages: `com.microsoft.skydrive` (OneDrive), `com.microsoft.appmanager` (Link to Windows).

---

## Recommended Execution

```bash
# Linux / macOS
./tools/disable.sh lists/samsung/samsung-safe-debloat.txt
./tools/disable.sh lists/common/third-party-bloat.txt

# Windows (PowerShell)
.\tools\disable.ps1 -List "lists\samsung\samsung-safe-debloat.txt"
.\tools\disable.ps1 -List "lists\common\third-party-bloat.txt"
```
