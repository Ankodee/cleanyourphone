#!/usr/bin/env bash
# ==============================================================================
# CleanYourPhone - Liquid Glass Launcher Build & Install Script (Bash)
# Builds the lightweight APK and installs it as the default home screen via ADB.
# ==============================================================================

set -euo pipefail
cd "$(dirname "$0")"

DISABLE_STOCK=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --disable-stock)
      DISABLE_STOCK=1
      shift
      ;;
    *)
      shift
      ;;
  esac
done

echo "=========================================================="
echo " Building Liquid Glass Launcher..."
echo "=========================================================="

# Build APK if gradlew is available
if [ -f "./gradlew" ] && command -v java >/dev/null 2>&1; then
  chmod +x ./gradlew
  ./gradlew assembleRelease -q --console=plain
  APK_PATH="app/build/outputs/apk/release/app-release.apk"
else
  # Check if pre-built APK exists
  APK_PATH="app/build/outputs/apk/release/app-release.apk"
  if [ ! -f "$APK_PATH" ]; then
    echo "Warning: Gradle/Java not found. Looking for existing APK..."
  fi
fi

if ! command -v adb >/dev/null 2>&1; then
  echo "Error: adb not found in PATH." >&2
  exit 1
fi

DEVICE_COUNT=$(adb devices | grep -v "List of devices" | grep "device$" | wc -l | tr -d ' ')
if [ "$DEVICE_COUNT" -eq 0 ]; then
  echo "Error: No Android device detected over ADB." >&2
  exit 1
fi

BRAND=$(adb shell getprop ro.product.brand | tr -d '\r')
MODEL=$(adb shell getprop ro.product.model | tr -d '\r')
echo "[*] Connected to $BRAND $MODEL"

if [ -f "$APK_PATH" ]; then
  echo "[*] Pushing APK to device..."
  adb push "$APK_PATH" /data/local/tmp/glasshome.apk
  echo "[*] Installing Liquid Glass Launcher..."
  adb shell pm install -r /data/local/tmp/glasshome.apk
  adb shell rm -f /data/local/tmp/glasshome.apk
else
  echo "Note: If compiling standalone, install the APK with: adb install app-release.apk"
fi

# Set default home activity (supports Android 5 through Android 15)
echo "[*] Setting Liquid Glass Launcher as default home screen..."
adb shell cmd package set-home-activity --user 0 com.cleanphone.glasshome/.MainActivity 2>/dev/null || \
adb shell pm set-home-activity com.cleanphone.glasshome/.MainActivity 2>/dev/null || true

# Configure 0.5x transition speed for lag-free, ultra-responsive experience
echo "[*] Setting transition speed to 0.5x for snappy, lag-free experience..."
adb shell settings put global window_animation_scale 0.5 2>/dev/null || true
adb shell settings put global transition_animation_scale 0.5 2>/dev/null || true
adb shell settings put global animator_duration_scale 0.5 2>/dev/null || true

# Start the new homescreen
echo "[*] Starting Liquid Glass Home..."
adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.HOME -n com.cleanphone.glasshome/.MainActivity

# Check if user requested disabling stock launcher
if [ "$DISABLE_STOCK" -eq 1 ]; then
  echo "[*] Detecting and disabling stock OEM launcher..."
  for stock in com.oppo.launcher com.coloros.home com.oneplus.launcher com.realme.launcher com.bbk.launcher2 com.vivo.launcher; do
    if adb shell pm list packages | grep -qx "package:$stock"; then
      echo "[*] Disabling $stock..."
      adb shell pm disable-user --user 0 "$stock" || true
    fi
  done
fi

echo "=========================================================="
echo " Liquid Glass Launcher successfully installed and running!"
echo "=========================================================="
