# Debloating POCO (MIUI & HyperOS for POCO)

## Architecture Overview
POCO smartphones (F, X, M, and C series) run **MIUI for POCO** and modern **Xiaomi HyperOS**. Although marketed for power users and gamers, POCO devices are notorious for preinstalled advertising daemons (MSA), background analytics, push-notification-heavy stock apps, and the controversial Joyose background service.

Packages primarily span the `com.miui.*` and `com.xiaomi.*` namespaces.

---

## Key Categories Removed

1. **MIUI System Ads (MSA - `com.miui.msa.global`):**
   - The primary advertising daemon in Xiaomi's software stack. Removing this eliminates in-system ad banners and sponsored recommendations.
2. **Joyose (`com.xiaomi.joyose`):**
   - Xiaomi's background throttling daemon that artificially limits frame rates in games and collects behavioral telemetry.
3. **GetApps App Store (`com.xiaomi.mipicks`):**
   - Redundant secondary app store that sends multiple unsolicited push notifications daily.
4. **App Vault & Minus-One Feed (`com.mi.android.globalminusscreen`):**
   - Replaces the clean Google Discover feed with commercial widgets, sponsored shortcuts, and ad carousels.
5. **Ad-Supported Media Players (`com.miui.videoplayer`, `com.miui.player`):**
   - Preloaded players that inject sponsored streaming banners, popups, and notification spam into basic local playback.
6. **Cheetah Mobile Cleaner Engine (`com.miui.cleanmaster`):**
   - Embedded cleaner daemon that constantly monitors storage and surfaces interstitial ads.

---

## Recommended Execution

```bash
# Linux / macOS
./tools/disable.sh lists/poco/poco-safe-debloat.txt
./tools/disable.sh lists/common/facebook-bloat.txt
./tools/disable.sh lists/common/third-party-bloat.txt

# Windows (PowerShell)
.\tools\disable.ps1 -List "lists\poco\poco-safe-debloat.txt"
.\tools\disable.ps1 -List "lists\common\facebook-bloat.txt"
.\tools\disable.ps1 -List "lists\common\third-party-bloat.txt"
```
