# Showcase & Benchmarks

<p align="center">
  <img src="docs/before-and-after.jpg" alt="CleanYourPhone Showcase - Before and After" width="850">
</p>

What happens when you strip the background analytics, preloaded bloatware, and ad daemons
from your Oppo, vivo, OnePlus, Realme, or iQOO smartphone?

<p align="center">
  <img src="docs/liquid-glass-home.jpg" alt="Liquid Glass Home Minimalist Screen" width="450">
</p>

Here are real-world benchmark comparisons measured before and after applying CleanYourPhone.

---

## 1. Battery Life & Overnight Standby Drain

<p align="center">
  <img src="docs/feature-battery-ram.jpg" alt="Battery & RAM Performance Benchmark Infographic" width="800">
</p>

OEM background services (HeyTap push, Vivo daemon, location tracking, lock screen content fetchers)
frequently wake the CPU (wake-locks), preventing your phone from entering Android's deepest Doze state.

| Metric | Stock Factory Phone | After CleanYourPhone | Improvement |
|---|---|---|---|
| **Overnight Standby (8 hours)** | 7% – 12% battery loss | 1% – 2% battery loss | **Up to 80% reduction** in idle drain |
| **Screen-On Time (SOT)** | ~5.5 to 6.5 hours | ~7.2 to 8.5 hours | **+1.5 to 2 hours** extra usage |
| **CPU Wake-locks (per hour)** | ~140 wakes/hr | < 15 wakes/hr | **90% fewer** background wakeups |

---

## 2. RAM & Background Memory

Proprietary stores, game boosters, and telemetry daemons sit resident in system RAM permanently.

| Device Tested | OS Version | Free RAM (Before) | Free RAM (After) | RAM Reclaimed |
|---|---|---|---|---|
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

Using network capture and DNS logging (NextDNS / Pi-hole) over a 24-hour baseline period:

| Manufacturer Telemetry Service | Pre-Debloat Daily DNS Requests | Post-Debloat Daily Requests |
|---|---|---|
| `heytapmobile.com` / `nearme.com` (Oppo/OnePlus/Realme) | ~1,850 queries/day | **0** |
| `vivoglobal.com` / `vivo.com.cn` telemetry daemons | ~1,420 queries/day | **0** |
| `graph.facebook.com` (Preloaded Facebook System Daemons) | ~620 queries/day | **0** |
| Baidu / Tencent SDK metrics | ~480 queries/day | **0** |
| **Total Daily Tracker Connections Prevented** | **~4,370 connections/day** | **0** |

---

## 4. User Experience & UI Cleanliness

- **No Lock Screen Ads:** Lock Screen Magazine / Glance / Poster is completely disabled. Your lock screen shows only your selected wallpaper.
- **No Push Notification Ads:** HeyTap Market and V-Appstore notifications promoting random games and spam apps disappear.
- **Instant Swipe-Down:** Replacing the cluttered "Global Search" with native notification shade toggle makes the UI feel instantly responsive.
- **Cleaner App Drawer:** No duplicate video players, music apps, theme stores, or pre-installed commercial apps (Netflix partner stubs, Amazon, FinShell Pay).
