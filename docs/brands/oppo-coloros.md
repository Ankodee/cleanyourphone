# Debloating Oppo (ColorOS)

## Architecture Overview
ColorOS serves as the foundation for the broader OPLUS ecosystem (powering Oppo, Realme, and modern OnePlus).
Bloatware packages primarily occupy the `com.heytap.*`, `com.coloros.*`, and `com.oplus.*` namespaces.

---

## Key Categories Removed

1. **HeyTap App Market (`com.heytap.market`):**
   - Replaced by Google Play Store or F-Droid.
   - Eliminates spammy push notifications promoting sponsored utility tools.
2. **Lock Screen Pictorial (`com.heytap.pictorial`):**
   - Eliminates dynamic lockscreen wallpaper clickbait and commercial ads.
3. **Global Search (`com.heytap.quicksearchbox`):**
   - Disables the intrusive swipe-down search bar on the home screen.
4. **FinShell Pay & Wallet (`com.finshell.wallet`):**
   - Pre-installed loan, insurance, and financial marketing services.
5. **LogKit & DeepThinker (`com.oplus.logkit`, `com.oplus.deepthinker`):**
   - Telemetry collection daemons that track app usage sequences and upload crash metrics.

---

## Recommended Execution

```bash
# Recommended safe debloat
./tools/disable.sh lists/oppo/coloros-safe-debloat.txt

# Remove preinstalled commercial bloat
./tools/disable.sh lists/common/facebook-bloat.txt
./tools/disable.sh lists/common/third-party-bloat.txt
```
