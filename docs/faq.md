# Frequently Asked Questions (FAQ)

### 1. Does debloating void my phone's warranty?
**No.** Debloating via ADB does not unlock the bootloader, alter the `/boot` or `/recovery` partitions, or trip any hardware fuses (like Samsung Knox). It is completely recognized as standard Android user configuration.

### 2. Does this break banking and UPI apps (Google Pay, PhonePe, Paytm)?
**No.** Because the bootloader remains locked and the device is not rooted, Google Play Integrity and SafetyNet pass with flying colors. All banking apps continue working seamlessly.

### 3. Which phone brands and OS versions are supported?
CleanYourPhone supports 15 major smartphone ecosystems:
- **Samsung:** One UI (v1 to v7+) & TouchWiz
- **POCO / Xiaomi:** MIUI & HyperOS
- **Infinix:** XOS (v3 to v14+)
- **Tecno:** HiOS (v3 to v14+)
- **itel:** itelOS (Full & Go editions)
- **Motorola:** Hello UI & My UX
- **Sony:** Xperia UI
- **Lava:** Agni, Blaze & Star OS
- **Karbonn & Philips:** Budget Indian & Global Android builds
- **Oppo:** ColorOS (v5 to v15+)
- **vivo & iQOO:** Funtouch OS (v3 to v15+) & OriginOS
- **OnePlus:** OxygenOS (v5 to v15+)
- **Realme:** Realme UI (v1 to v6+)

### 4. What is Google Stock Launcher in Stage 2?
Google Stock Launcher is CleanYourPhone's integrated Pixel-style home screen replacement powered by the upstream Lawnchair / AOSP Launcher3 open-source base. It features:
- Micro-memory footprint (<18 MB RAM vs 350MB–600MB OEM launchers)
- Zero ads, zero recommendations, and zero telemetry
- Silky 0.5x transition physics and half-duration app launches
- Dynamic Android Material You wallpaper theming
- It is completely optional: you can keep your existing home screen or install Google Stock Launcher at any time.

### 5. Will I still receive Android OS and security updates?
**Yes.** Standard over-the-air (OTA) updates download and install normally. System partitions remain intact.
*Note:* A major Android OS upgrade (e.g. from Android 14 to Android 15) may re-install or re-enable some OEM bloatware. You can simply re-run CleanYourPhone after the update.

### 6. What is the difference between disabling and uninstalling?
- **Disabling (`pm disable-user --user 0`):** Freezes the application completely. It consumes 0 bytes of RAM, 0% CPU, and is hidden from app drawers and launchers.
- **Uninstalling (`pm uninstall -k --user 0`):** Removes the package from the active user environment. The APK remains stored in the read-only `/system` partition and can be brought back instantly with `cmd package install-existing`.
Both achieve identical privacy, speed, and battery benefits.

### 7. What if I make a mistake or want an app back?
Run `./restore_last_session.sh` (or `.\restore_last_session.ps1` on Windows) to immediately reverse every modification made in that session. You can also re-enable individual apps using `adb shell pm enable <package.name>`.
