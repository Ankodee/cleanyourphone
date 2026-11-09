# Debloating Motorola (My UX & Hello UI)

## Architecture Overview
Motorola smartphones (Moto G, Edge, Razr, and ThinkPhone series) feature a near-stock Android user interface formerly branded as **My UX** and recently updated to **Hello UI**.

While Motorola maintains clean Android core behavior without aggressive custom skins, modern Motorola builds ship with preloaded partner installation agents, lock screen stories, and marketing feedback services located in the `com.motorola.*` namespace.

---

## Key Categories Removed

1. **Glance on Moto Lockscreen (`com.motorola.glance`):**
   - Sponsored lockscreen wallpapers, news headlines, and commercial click-through stories.
2. **Motorola Mobile Services (`com.motorola.mobileservices`, `com.motorola.brapps`):**
   - Silent background application delivery engines that install partner bloatware and sponsored games over Wi-Fi after initial setup or OS updates.
3. **Motorola Marketing & Surveys (`com.motorola.ccc.notification`):**
   - Telemetry service responsible for pushing satisfaction surveys and Motorola service promotional banners to the notification shade.
4. **Moto Suggestions / Genie (`com.motorola.genie`):**
   - Contextual recommendation prompts that suggest Motorola features and partner utilities.
5. **Retail Demo Mode (`com.motorola.demomode`):**
   - Leftover carrier/retail store display demo service.

---

## Safety Note: Preserving Moto Experiences
CleanYourPhone strictly **preserves** Motorola's celebrated signature features:
- **Moto Actions & Gestures:** Quick capture chop-for-flashlight and twist-for-camera remain 100% functional.
- **Moto Display:** Peek display and ambient notifications remain intact.

---

## Recommended Execution

```bash
# Linux / macOS
./tools/disable.sh lists/motorola/motorola-safe-debloat.txt

# Windows (PowerShell)
.\tools\disable.ps1 -List "lists\motorola\motorola-safe-debloat.txt"
```
