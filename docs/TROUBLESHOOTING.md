# Troubleshooting & FAQ

Encountering an issue while connecting or debloating? Here are tested solutions across all 15 supported smartphone ecosystems.

---

## 1. ADB Connection Issues

### `adb devices` shows nothing
- **Fix:**
  1. Ensure **USB Debugging** is toggled ON under `Settings > Developer Options`.
  2. If using a cable, try another USB cable or a different USB port on your PC (prefer USB 2.0 or direct motherboard ports).
  3. Ensure USB Mode is set to **File Transfer / MTP** rather than "Charge only".
  4. **Samsung:** Ensure official Samsung USB drivers are installed on Windows (or use platform-tools default).
  5. **Xiaomi / POCO:** In Developer Options, enable **USB debugging**, and toggle **Install via USB** and **USB debugging (Security settings)**. Note: Xiaomi requires a SIM card inserted to toggle Security settings.
  6. **Oppo / OnePlus / Realme:** Enable **Disable Permission Monitoring** if available under Developer Options.
  7. **Transsion (Infinix / Tecno / itel):** Set Default USB Configuration to "File Transfer".

### `device unauthorized`
- **Fix:**
  - Unlock your phone screen.
  - A pop-up dialog will ask: *"Allow USB debugging from this computer?"*.
  - Check **Always allow from this computer** and tap **Allow**.
  - If the prompt doesn't appear, run `adb kill-server && adb start-server`, then disconnect and reconnect the cable.

### Wireless Debugging disconnects
- Android rotates the pairing port each time Wireless Debugging is toggled. Check `Settings > Developer Options > Wireless Debugging` to see the current port number.
- Ensure phone and PC are connected to the exact same Wi-Fi subnet (disable PC VPNs during pairing).

---

## 2. Package Management Errors

### `Failure [DELETE_FAILED_INTERNAL_ERROR]`
- **Cause:**
  - Modern ColorOS, Realme UI, One UI, and HyperOS prevent `pm uninstall` on certain packages without root.
- **Solution:**
  - Use `pm disable-user --user 0 <pkg>`. This achieves the exact same result: 0 RAM, 0 CPU usage, no background services, and the app icon is removed.
  - `disable.sh` and `disable.ps1` handle this fallback automatically.

### `SecurityException: Permission Denial`
- **Cause:**
  - On Xiaomi/POCO (MIUI / HyperOS), ADB commands to modify packages are blocked unless "USB debugging (Security settings)" is turned on.
  - On vivo (Funtouch OS / OriginOS 14), BBK security policies block modifying certain protected system packages via standard ADB.
- **Solution:**
  - **POCO / Xiaomi:** Turn ON **USB debugging (Security settings)** under Developer options.
  - **vivo / iQOO:** Look for **Verify apps over USB** and toggle it. If a specific framework package is hard-locked by vivo ROM, skip it.

---

## 3. Google Stock Launcher Tips

### Gesture navigation feels stiff or reverts to 3-button
- On certain heavy OEM skins (e.g. older MIUI, HiOS, or Funtouch OS), third-party launcher gesture navigation is mediated by Android's QuickStep API.
- If full-screen gestures encounter glitches, toggle system navigation to **Gestures** in `Settings > System > Navigation bar`, or use 3-button navigation.
- Running CleanYourPhone's installer sets animation speeds to **0.5x**, ensuring fluid launches and zero dropped frames.

### How do I return to the stock factory launcher?
- If you ever wish to return to your manufacturer launcher:
  - Samsung: `adb shell pm enable com.sec.android.app.launcher`
  - Xiaomi/POCO: `adb shell pm enable com.miui.home` (or `com.mi.android.globallauncher`)
  - Oppo: `adb shell pm enable com.oppo.launcher`
  - vivo: `adb shell pm enable com.bbk.launcher2`
  - Transsion: `adb shell pm enable com.transsion.hilauncher` (or `com.transsion.XOSLauncher`)
  - Motorola: `adb shell pm enable com.motorola.launcher3`
- Or go to `Settings > Apps > Default Apps > Home app` and select your OEM launcher.

---

## 4. Post-Debloat Fixes

### "I accidentally disabled an app I need. How do I get it back?"
- **Solution:**
  - If you know the package name:
    ```bash
    adb shell pm enable <package.name>
    adb shell cmd package install-existing <package.name>
    ```
  - Or run the automatic rollback script generated during your session:
    ```bash
    # Linux / macOS
    ./restore_last_session.sh

    # Windows PowerShell
    .\restore_last_session.ps1
    ```

### "Can I still receive OTA system updates?"
- **Yes.**
  - Because debloating via ADB only uninstalls or disables apps for **User 0**, the `/system` partition is untouched and dm-verity cryptographic checksums remain valid. Official over-the-air updates will install normally.
