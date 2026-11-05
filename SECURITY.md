# Security Policy

## Core Android Protection & Safety Rules

Debloating an Android smartphone removes unwanted telemetry and battery drain,
but modifying system-level packages carries inherent risks if critical framework
services are touched.

CleanYourPhone enforces hardcoded, fail-safe guardrails in every script (`disable.sh`, `disable.ps1`, `phone.py`).

---

## 1. Protected Core Packages (The Untouchable List)

The debloat scripts will **refuse to run** if any package in your debloat list matches
the core package blacklist pattern:

```regex
^(android|android\.ext\.(services|shared)|com\.android\.sdksandbox|com\.android\.location\.fused|com\.android\.systemui|com\.android\.shell|com\.android\.phone|com\.android\.dialer|com\.android\.server\.telecom|com\.android\.settings|com\.android\.keyguard|com\.(google\.)?android\.(permissioncontroller|packageinstaller|ext\.services|ext\.shared|modulemetadata)|com\.google\.android\.overlay\.modules.*|com\.android\.providers\.(telephony|media|downloads|settings)|com\.qualcomm\.qti\.telephonyservice|com\.mediatek\.telephony)$
```

### Critical Packages Explained

| Package | Purpose | Disabling Consequence |
|---|---|---|
| `android` | Android OS Core Framework | Immediate bootloop / hard brick |
| `com.android.systemui` | Status bar, navigation, recent apps, notifications | Infinite crash loop; screen goes black |
| `com.android.phone` / `telephony` | Cellular modem, radio interface, SIM stack | Loss of cellular connection, no 911/emergency calls |
| `permissioncontroller` | Grants/revokes runtime app permissions | All apps crash when asking for permissions |
| `packageinstaller` | Allows APK installation and updates | Cannot install or update any app |
| `com.android.keyguard` | PIN, password, pattern, fingerprint lockscreen | Cannot unlock phone |
| `com.android.settings` | System settings app | Settings crashes; cannot access Wi-Fi or Bluetooth |

---

## 2. Safety Rules & Rating Consensus

CleanYourPhone cross-references every package against:
1. **[Universal Android Debloater Next Generation (UAD-ng)](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation)**
2. **[MuntashirAkon Android Debloat List](https://github.com/MuntashirAkon/android-debloat-list)**

### The Consensus Decision Matrix

- **Rule 1 (Conservative Override):** If a package is rated in both lists, the more cautious rating always wins.
  - *Example:* If List A rates a package "Recommended" (Safe) but List B rates it "Advanced" (Needs caution), CleanYourPhone moves it to the Optional list and warns the user.
  - If either list rates it "Unsafe", it is blacklisted and never removed.
- **Rule 2 (Single-List Validation):** If a package appears in only one list, it is removed only if that list rates it 100% fully safe (Recommended).
- **Rule 3 (Zero Unknown Removal):** If a package appears in neither list, it is left completely untouched.
- **Rule 4 (User 0 Isolation):** All removals are executed using `pm disable-user --user 0` or `pm uninstall -k --user 0`.
  - The actual APK remains preserved in `/system` or `/vendor`.
  - No root access is ever required.
  - Any app can be restored instantly via `cmd package install-existing <pkg>` or `pm enable <pkg>`.

---

## 3. ADB & Network Hygiene

When connecting your phone via ADB:

- **Turn off USB / Wireless Debugging** immediately after completing the debloat.
- Leaving Network ADB (port 5555) open on public or shared Wi-Fi networks exposes your device shell to unauthorized LAN connections.
- Revoke USB debugging authorizations in `Developer Options` when you are done.

---

## 4. Reporting Security Vulnerabilities

If you discover a package in our safe lists that causes a bootloop, prevents emergency calls, breaks Play Integrity, or leads to system instability:

1. Open an issue with the tag `[SAFETY CRITICAL]`.
2. Include the phone brand, model, OS build (`ro.build.display.id`), and logcat output if available.
3. The package will be pulled immediately from default safe lists into the protected blacklist.
