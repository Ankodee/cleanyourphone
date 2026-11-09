# Debloating Transsion Devices (Infinix XOS, Tecno HiOS & itel itelOS)

## Architecture Overview
Transsion Holdings is the manufacturer behind **Infinix**, **Tecno**, and **itel**, dominating emerging markets across Africa, South Asia, Southeast Asia, and Latin America.

Across all three brands, the underlying operating systems (**XOS**, **HiOS**, and **itelOS**) share a unified Transsion software stack rooted in the `com.transsion.*` and `com.afmobi.*` namespaces. Out of the box, Transsion devices are notoriously burdened with preloaded adware, aggressive browser notifications, lock screen wallpaper stories, and intrusive cleaning utilities.

On entry-level devices with 1 GB to 3 GB of RAM, debloating Transsion bloatware can reduce background memory usage by up to **400 MB–700 MB**, dramatically accelerating responsiveness.

---

## Shared Transsion Bloatware Stack

1. **Phoenix Browser (`com.transsion.phoenix`):**
   - High-priority target: Continuously pushes clickbait news headlines, sponsored ads, and lockscreen overlays.
2. **AHA Games (`com.transsion.ahagames`):**
   - Preinstalled gaming marketplace that persistently generates notification spam for downloadable APKs.
3. **Boomplay Music (`com.afmobi.boomplayer`):**
   - Preloaded music streaming app with continuous promotional notifications and background telemetry.
4. **Phone Master (`com.transsion.phonemanager`):**
   - Aggressive RAM cleaner utility that displays full-screen interstitial ads after system tasks.
5. **Scooper News & Vskit (`com.transsion.scooper`, `com.transsion.vskit`):**
   - Background aggregators for short video feeds and commercial news feeds.
6. **Lock Screen Magazine (`com.transsion.magazineservice`):**
   - Dynamic lockscreen service displaying sponsored wallpapers and commercial links.

---

## Recommended Execution by Brand

### For Infinix (XOS):
```bash
./tools/disable.sh lists/infinix/xos-safe-debloat.txt
```

### For Tecno (HiOS):
```bash
./tools/disable.sh lists/tecno/hios-safe-debloat.txt
```

### For itel (itelOS):
```bash
./tools/disable.sh lists/itel/itelos-safe-debloat.txt
```

*Note: For Windows PowerShell, replace `./tools/disable.sh <path>` with `.\tools\disable.ps1 -List "<path>"`. After debloating, installing **Lawnchair Launcher** completely replaces the ad-laden stock Transsion launchers (`XOSLauncher`, `hilauncher`, `itellauncher`).*
