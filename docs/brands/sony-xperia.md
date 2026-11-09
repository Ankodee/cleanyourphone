# Debloating Sony (Xperia UI)

## Architecture Overview
Sony Xperia smartphones (Xperia 1, 5, 10, and Pro series) provide a clean, enthusiast-focused Android experience that adheres closely to AOSP design principles.

However, Sony preinstalls promotional portals, legacy demonstration daemons, and secondary media utilities spanning the `com.sonymobile.*`, `com.sony.*`, and `com.sonyericsson.*` namespaces.

---

## Key Categories Removed

1. **Xperia Lounge Services (`com.sonymobile.xperialounge.services`):**
   - Promotional portal that sends marketing push notifications for Sony films, games, and contests.
2. **News Suite by Sony (`com.sonyericsson.xhs`):**
   - Preloaded news reader containing sponsored article feeds and advertising banners.
3. **Sony Entrance (`com.sonymobile.entrance`, `com.sonymobile.advancedwidget.entrance`):**
   - Showcase app and widget promoting Sony digital ecosystem products.
4. **AR Effect & 3D Creator (`com.sonymobile.areffect`, `com.sonymobile.scan3d`):**
   - Auxiliary 3D modeling and augmented reality camera effect apps that consume significant system storage.
5. **Legacy Transfer & Smart Connect (`com.sonymobile.xperiatransfermobile`, `com.sony.dtv.smartconnect`):**
   - Obsolete phone-to-phone migration utilities and peripheral automation services.

---

## Safety Note: Preserving Sony Pro Media
CleanYourPhone strictly **preserves** Sony's professional imaging and audio systems:
- **Photography Pro & Cinema Pro:** Full camera hardware controls remain 100% functional.
- **Dolby Atmos & 360 Reality Audio:** Audio tuning pipelines remain intact.
- **Creator Mode & Bravia Calibration:** Display color accuracy engines are untouched.

---

## Recommended Execution

```bash
# Linux / macOS
./tools/disable.sh lists/sony/sony-safe-debloat.txt

# Windows (PowerShell)
.\tools\disable.ps1 -List "lists\sony\sony-safe-debloat.txt"
```
