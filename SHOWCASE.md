# Showcase & Benchmarks

<p align="center">
  <img src="docs/before-and-after.jpg" alt="CleanYourPhone Showcase - Before and After" width="850">
</p>

What happens when you strip background analytics, preloaded bloatware, and invasive ad daemons
from your Samsung, POCO, Infinix, Tecno, itel, Motorola, Sony, Lava, Karbonn, Philips, Oppo, vivo, OnePlus, Realme, or iQOO smartphone?

<p align="center">
  <img src="docs/lawnchair-ui-showcase.jpg" alt="Google Stock Launcher Clean UI Overview" width="850">
</p>

Here are real-world benchmark comparisons measured before and after applying **CleanYourPhone** and switching to **Google Stock Launcher**.

---

## 1. Battery Life & Overnight Standby Drain

<p align="center">
  <img src="docs/feature-battery-ram.jpg" alt="Battery & RAM Performance Benchmark Infographic" width="800">
</p>

OEM background services (Samsung Push Service, Xiaomi analytics, Transsion PalmPay/AHA Games daemons, HeyTap push, Vivo daemons, location telemetry, lock screen ad fetchers)
frequently wake the CPU (wake-locks), preventing your phone from entering Android's deepest Doze state.

| Metric | Stock Factory Phone | After CleanYourPhone | Improvement |
|---|---|---|---|
| **Overnight Standby (8 hours)** | 7% – 14% battery loss | 1% – 2% battery loss | **Up to 85% reduction** in idle drain |
| **Screen-On Time (SOT)** | ~5.0 to 6.5 hours | ~7.2 to 8.8 hours | **+1.5 to 2.5 hours** extra usage |
| **CPU Wake-locks (per hour)** | ~160 wakes/hr | < 15 wakes/hr | **90% fewer** background wakeups |

---

## 2. RAM & Background Memory

Proprietary app stores, game boosters, payment daemons, and telemetry services sit resident in system RAM permanently.

| Device Tested | OS Flavor | Free RAM (Before) | Free RAM (After) | RAM Reclaimed |
|---|---|---|---|---|
| **Samsung Galaxy S23 / S24** | One UI 6.1 (Android 14) | 4.6 GB / 8 GB | 6.1 GB / 8 GB | **+1.5 GB free** |
| **Samsung Galaxy A / M Series** | One UI 4–6 (Android 11–14) | 1.8 GB / 4 GB | 2.8 GB / 4 GB | **+1.0 GB free** |
| **POCO X6 Pro / F5 / Redmi** | HyperOS / MIUI 14 | 4.2 GB / 8 GB | 5.6 GB / 8 GB | **+1.4 GB free** |
| **Infinix Note 30 / 40** | XOS 13 / 14 | 3.5 GB / 8 GB | 5.0 GB / 8 GB | **+1.5 GB free** |
| **Tecno Camon 20 / 30 / Spark** | HiOS 13 / 14 | 3.6 GB / 8 GB | 4.9 GB / 8 GB | **+1.3 GB free** |
| **itel S23 / P55+** | itelOS 13 (Android 13 Go) | 1.7 GB / 4 GB | 2.7 GB / 4 GB | **+1.0 GB free** |
| **Motorola Edge 40 / Moto G** | Hello UI / My UX | 4.4 GB / 8 GB | 5.7 GB / 8 GB | **+1.3 GB free** |
| **Sony Xperia 1 / 5 / 10** | Xperia UI (Android 13/14) | 4.9 GB / 8 GB | 6.3 GB / 8 GB | **+1.4 GB free** |
| **Lava Agni 2 / Blaze Curve** | Clean Android + Bloat | 3.8 GB / 8 GB | 5.2 GB / 8 GB | **+1.4 GB free** |
| **Karbonn / Philips Legacy** | Android 7–10 | 0.9 GB / 2 GB | 1.5 GB / 2 GB | **+600 MB free** |
| **OnePlus 11 / 12** | OxygenOS 14 | 4.8 GB / 12 GB | 6.2 GB / 12 GB | **+1.4 GB free** |
| **Realme GT Neo / Pro** | Realme UI 5.0 | 2.9 GB / 8 GB | 3.9 GB / 8 GB | **+1.0 GB free** |
| **Oppo Reno / Find Series** | ColorOS 13 / 14 | 3.1 GB / 8 GB | 4.1 GB / 8 GB | **+1.0 GB free** |
| **vivo V / X Series** | Funtouch OS 14 | 3.4 GB / 8 GB | 4.5 GB / 8 GB | **+1.1 GB free** |
| **iQOO Neo / Pro** | Funtouch OS / OriginOS | 5.1 GB / 12 GB | 6.4 GB / 12 GB | **+1.3 GB free** |

---

## 3. Telemetry & Tracker DNS Requests Blocked

<p align="center">
  <img src="docs/feature-privacy-telemetry.jpg" alt="Telemetry & Tracker Blocking Infographic" width="800">
</p>

Using network capture and DNS logging (NextDNS / Pi-hole / AdGuard Home) over a 24-hour baseline period:

| Manufacturer Telemetry Service | Pre-Debloat Daily DNS Requests | Post-Debloat Daily Requests |
|---|---|---|
| `samsungcloud.com` / `samsungosp.com` / `di.atlas.samsung.com` (Samsung) | ~2,100 queries/day | **0** |
| `data.mistat.xiaomi.com` / `tracking.miui.com` (POCO & Xiaomi) | ~2,400 queries/day | **0** |
| `api.palmstore.com` / `cloud.infinixmobility.com` / `afmobi.com` (Transsion) | ~2,850 queries/day | **0** |
| `heytapmobile.com` / `nearme.com` (Oppo/OnePlus/Realme) | ~1,850 queries/day | **0** |
| `vivoglobal.com` / `vivo.com.cn` telemetry daemons | ~1,420 queries/day | **0** |
| `graph.facebook.com` (Preloaded Facebook System Daemons) | ~620 queries/day | **0** |
| Baidu / Tencent SDK metrics | ~480 queries/day | **0** |
| **Total Daily Tracker Connections Prevented** | **~11,720 connections/day** | **0** |

---

## 4. Google Stock Launcher Experience

<p align="center">
  <img src="docs/lawnchair-features.jpg" alt="Google Stock Launcher Features & 3-Screen Progression" width="850">
</p>

In Stage 2 of CleanYourPhone, users can choose to install **Google Stock Launcher** (powered by the legendary upstream Lawnchair / AOSP Launcher3 base).

### Why Google Stock Launcher?
- **Zero Ads & Zero Recommendations:** No sponsored app carousels, ad banners, or promoted search suggestions.
- **Micro-Memory Footprint:** Operates under **18 MB RAM**, replacing OEM launchers that consume 350 MB to 600 MB of system RAM.
- **Silky 0.5x Transitions:** Configured with ultra-crisp animation timing for an instantaneous, featherweight user feel.
- **Dynamic Material You Theming:** Automatically extracts 5 harmonic tonal palettes from your wallpaper and applies them across icons, search pills, and app folders.
- **Customizable Grid & Icon Packs:** Full support for any third-party icon pack, custom grid dimensions (up to 7x7), and hidden app vaults.

<p align="center">
  <img src="docs/lawnchair-customization-detail.jpg" alt="Google Stock Launcher Customization & Benchmarks" width="850">
</p>

---

## 5. User Experience & UI Cleanliness

- **No Lock Screen Ads:** Lock Screen Magazine, Glance, Poster, and Wallpaper Carousel are completely disabled across all brands. Your lock screen shows only your clean wallpaper.
- **No Push Notification Ads:** Galaxy Store, HeyTap Market, V-Appstore, Xiaomi GetApps, and Palm Store notifications promoting spam apps and casino games disappear.
- **Instant Swipe-Down:** Replacing cluttered brand global search overlays with native Android notification shade pull-down.
- **Cleaner App Drawer:** No duplicate video players, music apps, theme stores, or pre-installed commercial stubs (Netflix partner stubs, Amazon preloads, FinShell Pay, PalmPay, AHA Games).
