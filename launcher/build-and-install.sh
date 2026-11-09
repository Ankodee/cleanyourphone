#!/usr/bin/env bash
#
# CleanYourPhone - Lawnchair Launcher Installer & Setup
# Upstream repository: https://github.com/LawnchairLauncher/lawnchair
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DISABLE_STOCK=0
APK_PATH=""

for arg in "$@"; do
  case "$arg" in
    --disable-stock)
      DISABLE_STOCK=1
      ;;
    *.apk)
      APK_PATH="$arg"
      ;;
  esac
done

echo "=========================================================="
echo " Lawnchair Launcher Installer (CleanYourPhone)"
echo " Upstream: https://github.com/LawnchairLauncher/lawnchair"
echo "=========================================================="

if ! command -v adb >/dev/null 2>&1; then
  echo "Error: 'adb' executable not found in PATH. Install Android platform-tools." >&2
  exit 1
fi

if ! adb devices | grep -E '\s+device$' >/dev/null 2>&1; then
  echo "Error: No Android device detected over ADB. Connect phone via USB or Wireless ADB." >&2
  exit 1
fi

BRAND=$(adb shell getprop ro.product.brand 2>/dev/null | tr -d '\r')
MODEL=$(adb shell getprop ro.product.model 2>/dev/null | tr -d '\r')
SDK_RAW=$(adb shell getprop ro.build.version.sdk 2>/dev/null | tr -d '\r' | tr -cd '0-9')
SDK=${SDK_RAW:-30}

echo "[*] Connected device: $BRAND $MODEL (Android SDK $SDK)"

# Select matching Lawnchair version and component
PKG_NAME="app.lawnchair"
LAUNCHER_ACTIVITY="app.lawnchair/app.lawnchair.LawnchairLauncher"
DOWNLOAD_URL=""
VERSION_LABEL=""

if [ "$SDK" -ge 34 ]; then
  # Android 14 & 15
  VERSION_LABEL="Lawnchair 15 (Beta 3.0)"
  DOWNLOAD_URL="https://github.com/LawnchairLauncher/lawnchair/releases/download/v15.0.0-beta3.0/Lawnchair.15.0.0.Beta.3.0.apk"
elif [ "$SDK" -ge 29 ]; then
  # Android 10, 11, 12, 13
  VERSION_LABEL="Lawnchair 14 (Beta 3)"
  DOWNLOAD_URL="https://github.com/LawnchairLauncher/lawnchair/releases/download/v14.0.0-beta3/Lawnchair.14.0.0.Beta.3.apk"
else
  # Legacy Android 5 through 9 (ColorOS 5, older Oppo/Vivo/Xiaomi)
  VERSION_LABEL="Lawnchair 2.0 (Legacy)"
  DOWNLOAD_URL="https://github.com/LawnchairLauncher/lawnchair/releases/download/2.0.2589/Lawnchair.2.0.2589.apk"
  PKG_NAME="ch.deletescape.lawnchair.plah"
  LAUNCHER_ACTIVITY="ch.deletescape.lawnchair.plah/ch.deletescape.lawnchair.plah.Launcher"
fi

echo "[*] Target launcher release: $VERSION_LABEL"

TARGET_APK=""
if [ -n "$APK_PATH" ] && [ -f "$APK_PATH" ]; then
  TARGET_APK="$APK_PATH"
elif [ -f "Lawnchair.apk" ]; then
  TARGET_APK="Lawnchair.apk"
else
  # Check for compiled build in submodule
  COMPILED=$(find lawnchair -name "*.apk" 2>/dev/null | head -n 1 || true)
  if [ -n "$COMPILED" ] && [ -f "$COMPILED" ]; then
    TARGET_APK="$COMPILED"
  fi
fi

if [ -z "$TARGET_APK" ] || [ ! -f "$TARGET_APK" ]; then
  echo "[*] Fetching official release from Lawnchair GitHub..."
  echo "    Source: $DOWNLOAD_URL"
  TARGET_APK="Lawnchair.apk"
  if command -v curl >/dev/null 2>&1; then
    curl -fL -o "$TARGET_APK" "$DOWNLOAD_URL"
  elif command -v wget >/dev/null 2>&1; then
    wget -O "$TARGET_APK" "$DOWNLOAD_URL"
  else
    echo "Error: curl or wget required to download APK." >&2
    exit 1
  fi
  echo "[*] Download completed successfully."
fi

# Install Lawnchair via ADB
echo "[*] Installing $VERSION_LABEL on $BRAND $MODEL..."
adb install -r -d "$TARGET_APK"

# Set as default home activity
echo "[*] Setting Lawnchair as default home screen..."
adb shell cmd package set-home-activity --user 0 "$LAUNCHER_ACTIVITY" 2>/dev/null || \
adb shell pm set-home-activity "$LAUNCHER_ACTIVITY" 2>/dev/null || true

# Configure 0.5x transition speed
echo "[*] Setting transition speed to 0.5x for snappy, lag-free experience..."
adb shell settings put global window_animation_scale 0.5 2>/dev/null || true
adb shell settings put global transition_animation_scale 0.5 2>/dev/null || true
adb shell settings put global animator_duration_scale 0.5 2>/dev/null || true

# Start Lawnchair
echo "[*] Starting Lawnchair Launcher..."
adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.HOME -n "$LAUNCHER_ACTIVITY"

# Optionally disable OEM stock launcher
if [ "$DISABLE_STOCK" -eq 1 ]; then
  echo "[*] Disabling OEM stock launcher..."
  for stock in \
    com.oppo.launcher com.coloros.home \
    com.oneplus.launcher com.realme.launcher \
    com.bbk.launcher2 com.vivo.launcher \
    com.miui.home com.sec.android.app.launcher \
    com.transsion.hilauncher com.transsion.XOSLauncher; do
    if adb shell pm list packages | grep -qx "package:$stock"; then
      echo "[*] Disabling $stock..."
      adb shell pm disable-user --user 0 "$stock" 2>/dev/null || true
    fi
  done
fi

echo "=========================================================="
echo " Lawnchair Launcher successfully installed and running!"
echo " Experience: Pixel-style AOSP launcher, Material You, 0.5x speed"
echo "=========================================================="
