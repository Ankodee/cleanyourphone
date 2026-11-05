# Contributing to CleanYourPhone

Thank you for helping make Android smartphones cleaner, faster, and more private!

We welcome package additions, brand profiles, bug reports, and documentation improvements.
Because this project modifies system services, all contributions must adhere to strict safety standards.

---

## The Rule of Safety First

Every package included in `lists/` must follow our **Dual-List Consensus**:

1. **Verify against UAD-ng & MuntashirAkon:**
   - Look up the package in [UAD-ng](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) and [MuntashirAkon/android-debloat-list](https://github.com/MuntashirAkon/android-debloat-list).
   - If both rate it Safe / Recommended, it belongs in `<brand>-safe-debloat.txt`.
   - If either rates it Advanced / Depends / Caution, place it in `<brand>-optional-debloat.txt`.
   - If either rates it Unsafe, **do not include it**.
2. **Hardware Testing:**
   - Test the change on real hardware (Oppo, OnePlus, Realme, vivo, or iQOO).
   - Verify that calls, SMS, camera, biometrics, Bluetooth, and Google Play Store continue working after a full phone reboot.

---

## File Format Standards for Lists

Package lists inside `lists/<brand>/` must adhere to these rules:

- **One package per line.**
- Use comments `#` to describe what the package does and why it was removed.
- Never include core Android packages (checked automatically by CI).
- Files must be encoded in **UTF-8 with LF line endings** (no Windows CRLF or UTF-8 BOM).

### Example Format:
```text
# HeyTap App Market (Oppo / Realme proprietary app store)
com.heytap.market

# Lock Screen Magazine ads & wallpapers
com.heytap.pictorial
```

---

## Adding a New Device or Brand

If you are adding a new profile or testing on a newer OS (e.g. ColorOS 15, OriginOS 5):

1. Export your installed packages:
   ```bash
   adb shell pm list packages -f > installed_packages.txt
   ```
2. Identify non-AOSP manufacturer packages (`com.oplus.*`, `com.vivo.*`, `com.heytap.*`, etc.).
3. Cross-reference each package with `tools/audit_packages.py`.
4. Submit a Pull Request with the updated list and test results.

---

## Running CI Tests Locally

Before submitting a Pull Request:

```bash
# Validate package list syntax and safety rules
python tools/check.py lists/oppo/coloros-safe-debloat.txt
python tools/check.py lists/vivo/funtouchos-safe-debloat.txt
```
