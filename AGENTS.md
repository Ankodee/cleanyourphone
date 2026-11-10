# AGENTS.md — Instructions for AI Coding Assistants

This repository is designed to be operated both manually and through AI coding assistants
(e.g., Claude Code, Antigravity CLI, Gemini CLI, Cursor, Codex).

When acting as an agent running debloating operations for a user, follow the strict guidelines below.

---

## 1. Prime Directive: Do No Harm

Debloating modern Android phones (Samsung One UI, POCO HyperOS/MIUI, Transsion XOS/HiOS/itelOS, Motorola Hello UI, Sony Xperia UI, Lava, Karbonn, Philips, ColorOS, OxygenOS, Realme UI, Funtouch OS, OriginOS)
differs from Android TV: phones manage cellular modems, biometric authentication (fingerprint/face),
emergency dialing (eCall/SOS), camera post-processing pipelines, and secure keystores.

**Never touch:**
- Core Android packages (see [SECURITY.md](SECURITY.md) for full regex).
- Modem, telephony, SIM toolkit, or IMS packages (`com.android.phone`, `com.qualcomm.qti.telephonyservice`, `com.mediatek.telephony`).
- Biometrics and lockscreen keyguards (`com.android.keyguard`, `com.oplus.faceunlock`, `com.vivo.fingerprint`).
- Camera processing engines (`com.oplus.camera`, `com.vivo.camera`).
- Package installer and runtime permission controllers (`com.google.android.permissioncontroller`, `com.android.packageinstaller`).

---

## 2. The Dual-List Safety Consensus

CleanYourPhone harmonizes two upstream safety authorities:
1. **Universal Android Debloater Next Generation (UAD-ng)**
2. **MuntashirAkon Android Debloat List**

When evaluating packages on a user's phone, enforce this exact decision matrix:

| Scenario | Action | Reason |
|---|---|---|
| **Rated in both lists** | Follow the **more cautious** rating. | If List A says "Recommended" and List B says "Advanced", treat as "Advanced" (require explicit user consent). If either says "Unsafe", refuse to touch. |
| **Rated in only one list** | Remove **only** if rated fully Safe / Recommended. | If marked "Advanced" or unconfirmed, do not remove automatically. |
| **Rated in neither list** | **Leave it alone.** | Unknown OEM packages may cause bootloops or broken updates. |
| **All removals** | Apply **only to User 0** (`--user 0`). | Never perform root-level deletes. Everything must remain reversible. |

---

## 3. Disabling vs. Uninstalling

On modern Android builds (especially Android 13, 14, and 15):
- `pm disable-user --user 0 <pkg>` is the preferred, safest method. The package is stopped from running, removed from app drawers, consumes 0 RAM and CPU, but its APK remains in `/system` intact.
- `pm uninstall -k --user 0 <pkg>` uninstalls the app for the primary user. On some ColorOS and Funtouch OS builds, this throws `DELETE_FAILED_INTERNAL_ERROR` or `SecurityException`.
- **Agent Rule:** Always attempt `pm disable-user --user 0 <pkg>` first, or handle uninstall fallback gracefully. Never force root exploits.

---

## 4. Execution Workflow for Agents

When a user invokes you using [`PROMPT.md`](PROMPT.md), execute in this exact sequence:

1. **Connect & Probe:**
   - Detect device (`adb devices -l`).
   - Query OEM brand and OS build:
     ```bash
     adb shell getprop ro.product.brand
     adb shell getprop ro.product.model
     adb shell getprop ro.build.version.release
     adb shell getprop ro.build.version.ota
     ```
2. **Back Up Before Changing Anything:**
   - Save full installed package list: `adb shell pm list packages -f > backup_installed_packages.txt`
   - Save currently disabled packages: `adb shell pm list packages -d > backup_disabled_packages.txt`
   - Save system properties: `adb shell getprop > backup_getprop.txt`
   - Generate a single-click restore script before running the debloat.
3. **Interactive Questionnaire:**
   - Identify the user's workflow needs (e.g., Do you use the stock HeyTap/Vivo Cloud? Do you use Breeno/Jovi voice assistant? Do you want to keep the stock gallery or switch to Fossify?).
4. **Execute Safe Debloat:**
   - Use the pre-tested brand lists from `lists/<brand>/`.
   - Never skip the core package filter.
5. **Post-Debloat Verification:**
   - Verify cellular signal and Wi-Fi connectivity are active.
   - Verify Settings opens without crashing.
   - Verify phone calls / SMS continue functioning.
6. **Cleanup:**
   - Remind the user to disable USB Debugging / Wireless Debugging for security.

---

## 5. Brand Archetypes

- **Samsung (One UI Platform):**
  - Clusters around `com.samsung.android.*` and `com.sec.android.*`.
  - Common pain points: Bixby suite, Samsung Free ad feeds, Game Optimizing Service (GOS), Samsung Push Service, Samsung Checkout, Galaxy Store monetization.
- **POCO & Xiaomi (MIUI & HyperOS Platform):**
  - Clusters around `com.miui.*` and `com.xiaomi.*`.
  - Common pain points: MSA (MIUI System Ads), Joyose background throttler, GetApps store, App Vault, Mi Pay, Cleaner recommendations.
- **Transsion (Infinix XOS, Tecno HiOS, itel itelOS):**
  - Clusters around `com.transsion.*` and `com.afmobi.*`.
  - Common pain points: Phoenix Browser, AHA Games, Palm Store, PalmPay, HiOS/XOS Lock Screen Magazine, Phone Master ad engine.
- **Motorola (Hello UI & My UX):**
  - Clusters around `com.motorola.*`.
  - Common pain points: Glance lock screen stories, Moto Mobile Services marketing surveys, Motorola Notifications.
- **Sony (Xperia UI):**
  - Clusters around `com.sonymobile.*` and `com.sony.tvsideview.*`.
  - Common pain points: Xperia Lounge, Sony News Suite, redundant PC Companion / transfer stubs.
- **Budget Android (Lava, Karbonn, Philips):**
  - Clusters around carrier preloads, Glance lockscreen feeds, regional news aggregators, and Indian commercial preloads.
- **Oppo, OnePlus, Realme (OPLUS / HeyTap Ecosystem):**
  - Share the ColorOS underlying codebase.
  - Clusters around `com.heytap.*`, `com.nearme.*`, `com.coloros.*`, and `com.oplus.*`.
  - Common pain points: HeyTap App Market, Lock screen magazine (Pictorial), Global Search swipe-down, FinShell Pay, Breeno Voice.
- **vivo & iQOO (BBK Vivo Ecosystem):**
  - Share the Funtouch OS / OriginOS underlying codebase.
  - Clusters around `com.vivo.*`, `com.bbk.*`, and `com.iqoo.*`.
  - Common pain points: V-Appstore, Jovi Assistant, Lockscreen Poster, i Theme store, vivo Cloud, vivo Browser.

---

## 6. Scripts & File Edits

- Shell scripts (`tools/*.sh`) must remain compatible with Bash 4+ and macOS/Linux environments.
- PowerShell scripts (`tools/*.ps1`) must be natively runnable on Windows 10/11 without requiring WSL.
- Python tools (`tools/*.py`) must use standard library or dependencies in `tools/requirements.txt`.
