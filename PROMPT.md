# The Prompt for AI Coding Assistants

Paste this prompt into Claude Code, Antigravity CLI, Gemini CLI, Cursor, or any AI assistant with terminal/shell access on your computer.

Works for **Oppo (ColorOS)**, **vivo (Funtouch OS / OriginOS)**, **OnePlus (OxygenOS)**, **Realme (Realme UI)**, and **iQOO** smartphones.

---

### Before You Start (On Your Phone):
1. **Enable Developer Options:**
   - Go to `Settings > About device > Version`.
   - Tap `Build number` 7 times until you see *"You are now in developer mode!"*.
2. **Enable USB Debugging (or Wireless Debugging):**
   - Go to `Settings > System / Additional settings > Developer options`.
   - Turn ON **USB debugging**.
   - If connecting without a cable on Android 11+, turn ON **Wireless debugging** (see [docs/WIRELESS-ADB.md](docs/WIRELESS-ADB.md)).
3. Connect your phone to your computer via USB (select "File Transfer" mode) or pair via Wireless ADB.

---

### Copy and Paste Everything Below This Line:

```text
I want to debloat my Android smartphone, remove background trackers and ads, and optimize battery life.
My phone model and OS are: <ENTER PHONE MODEL & BRAND HERE, e.g., OnePlus 12 / Oppo Reno 10 / vivo V29 / Realme GT / iQOO Neo 9>.
Work on the real device step-by-step using ADB. Verify everything you do and ask me before touching anything that depends on my preferences.

Follow these strict operating procedures:

1. Connect & Device Recon
- Check for connected devices using `adb devices -l`.
- If no device is detected, instruct me on checking the USB connection, allowing the "Always allow from this computer" prompt on the screen, or pairing via Wireless Debugging (`adb pair` / `adb connect`).
- Probe the exact device properties:
  `adb shell getprop ro.product.brand`
  `adb shell getprop ro.product.model`
  `adb shell getprop ro.build.version.release`
  `adb shell getprop ro.build.version.security_patch`
- Run `python tools/phone.py --info` to print a clean summary.

2. Back Up First
- Before altering or disabling ANY package on my phone, create a full backup snapshot:
  - Save all installed packages: `adb shell pm list packages -f > backups/installed_packages.txt`
  - Save currently disabled packages: `adb shell pm list packages -d > backups/disabled_packages.txt`
  - Save system properties: `adb shell getprop > backups/getprop.txt`
- Generate an instant restore script (`restore_last_session.sh` / `restore_last_session.ps1`) that can re-enable and re-install every touched package.

3. Enforce the Dual-List Safety Consensus
- Cross-reference packages against the repository lists in `lists/<brand>/` and the upstream databases (Universal Android Debloater and MuntashirAkon Android Debloat List).
- Never touch core Android framework packages:
  `android`, `com.android.systemui`, `com.android.phone`, `com.android.dialer`, `com.android.settings`,
  `com.google.android.permissioncontroller`, `com.android.packageinstaller`, `com.android.keyguard`.
- Follow the conservative consensus:
  - If a package is rated in both lists, the more cautious rating wins.
  - If in only one list, remove it only if rated 100% fully safe (Recommended).
  - If in neither list, leave it alone.
  - Remove only for User 0 (`pm disable-user --user 0` or `pm uninstall -k --user 0`). Never perform destructive root actions.

4. Interactive Checklist (Ask My Preferences)
- Before executing, present a grouped summary of discovered bloatware on my phone:
  - Brand App Stores & Theme Stores (HeyTap Market, V-Appstore, Theme Stores)
  - Lock Screen Magazine / Glance / Global Search
  - Brand Cloud & Push Services (HeyTap Cloud, vivo Cloud, Push Service)
  - Game Centers & Game Boosters
  - Voice Assistant (Breeno / Jovi / Google Assistant)
  - Duplicate Media Apps (Stock browser, music player, video player)
  - Preinstalled Commercial Bloat (Facebook daemons, Netflix stubs, Amazon)
- Ask me if there are any specific stock apps I wish to keep.

5. Execute Debloat
- Run the appropriate brand script:
  `tools/disable.sh lists/<brand>/<brand>-safe-debloat.txt`
  (or `.\tools\disable.ps1` on Windows).
- If uninstallation throws `DELETE_FAILED_INTERNAL_ERROR` or `SecurityException`, gracefully fall back to `pm disable-user --user 0`.

6. Post-Debloat Verification
- Verify that cellular signal, Wi-Fi, SMS, camera, biometrics, and phone settings function properly.
- Show me how many packages were disabled and verify that the restore script is ready.
- Offer recommendations from `themes/PRIVATE-DNS.md` for zero-app system-level ad blocking.
- Remind me to toggle OFF USB Debugging / Wireless Debugging for security.
```
