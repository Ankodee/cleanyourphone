# Debloating Lava, Karbonn & Philips Smartphones

## Architecture Overview
Entry-level and regional smartphones produced by **Lava**, **Karbonn**, and **Philips** frequently subsidize hardware costs by bundling third-party ad networks, sponsored news feeds, lockscreen content providers (such as Glance), and partner utilities.

On devices equipped with 2 GB to 4 GB of RAM, disabling these aggressive background services drastically reduces thermal throttling and frees up hundreds of megabytes of working memory.

---

## Brand-Specific Analysis

### 1. Lava Smartphones (Agni, Blaze, Yuva, Storm)
- **Namespaces:** `com.lava.*`, `com.glance.*`, `com.inmobi.*`
- **Key Bloat Removed:**
  - `com.glance.internet`: Glance lockscreen stories and wallpaper ads.
  - `com.lava.mycleaner`: Redundant RAM cleaner utility.
  - `com.lava.game`: Lava Games promotional marketplace.
  - `com.lava.customization`: Silent partner app provisioning daemon.
  - `com.inmobi.service`: Background mobile advertising SDK.

### 2. Karbonn Mobiles
- **Namespaces:** `com.karbonn.*`, `com.indus.*`, `com.mobvista.*`
- **Key Bloat Removed:**
  - `com.karbonn.appzone`: AppZone promotional downloads portal.
  - `com.karbonn.games`: Preloaded gaming portal with push notifications.
  - `com.karbonn.kstore`: K-Store third-party marketplace.
  - `com.ucmobile.intl`: Preloaded UC Browser with notification spam.

### 3. Philips Android Smartphones
- **Namespaces:** `com.philips.*`, `com.qihoo.*`
- **Key Bloat Removed:**
  - `com.philips.appstore`: Secondary application store.
  - `com.qihoo.cleansdk`: Third-party Qihoo 360 cleaner and tracking SDK.
  - `com.philips.health`: Preloaded health tracking stub.

---

## Recommended Execution

```bash
# For Lava:
./tools/disable.sh lists/lava/lava-safe-debloat.txt

# For Karbonn:
./tools/disable.sh lists/karbonn/karbonn-safe-debloat.txt

# For Philips:
./tools/disable.sh lists/philips/philips-safe-debloat.txt
```
*(On Windows PowerShell, use `.\tools\disable.ps1 -List "lists\<brand>\<brand>-safe-debloat.txt"`)*
