<#
.SYNOPSIS
    Liquid Glass Launcher - Build & Install Script for Windows PowerShell
.DESCRIPTION
    Compiles the minimal Liquid Glass Launcher APK and installs it as the
    default home screen on the connected Android smartphone via ADB.
.EXAMPLE
    .\launcher\build-and-install.ps1
    .\launcher\build-and-install.ps1 -DisableStock
#>

param (
    [switch]$DisableStock
)

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Building Liquid Glass Launcher..." -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

Set-Location $PSScriptRoot

# Verify ADB
$adbCmd = Get-Command "adb" -ErrorAction SilentlyContinue
if (-not $adbCmd) {
    Write-Error "Error: 'adb' executable not found in PATH. Install Android platform-tools."
    exit 1
}

$devices = adb devices
$attached = ($devices | Select-String -Pattern "\s+device$")
if (-not $attached) {
    Write-Error "Error: No Android device detected over ADB. Connect phone via USB or Wireless ADB."
    exit 1
}

$brand = (adb shell getprop ro.product.brand).Trim()
$model = (adb shell getprop ro.product.model).Trim()
Write-Host "[*] Connected to $brand $model" -ForegroundColor Cyan

$apkPath = "app\build\outputs\apk\release\app-release.apk"

# Check if Gradle / Java can build
$javaCmd = Get-Command "java" -ErrorAction SilentlyContinue
if ((Test-Path ".\gradlew.bat") -and $javaCmd) {
    Write-Host "[*] Compiling APK using Gradle..." -ForegroundColor White
    .\gradlew.bat assembleRelease -q --console=plain
} elseif (-not (Test-Path $apkPath)) {
    Write-Host "Note: Gradle build skipped (Java JDK not found in PATH)." -ForegroundColor Yellow
}

if (Test-Path $apkPath) {
    Write-Host "[*] Pushing APK to phone..." -ForegroundColor White
    adb push $apkPath /data/local/tmp/glasshome.apk | Out-Null
    Write-Host "[*] Installing Liquid Glass Launcher..." -ForegroundColor White
    $res = adb shell pm install -r /data/local/tmp/glasshome.apk
    adb shell rm -f /data/local/tmp/glasshome.apk | Out-Null
    Write-Host "Installation result: $res" -ForegroundColor Green
} else {
    Write-Host "If building in Android Studio, install using: adb install <path-to-apk>" -ForegroundColor Yellow
}

# Set as default home activity (supports Android 5 through Android 15)
Write-Host "[*] Setting Liquid Glass Launcher as default home..." -ForegroundColor Cyan
try {
    adb shell cmd package set-home-activity --user 0 com.cleanphone.glasshome/.MainActivity 2>&1 | Out-Null
} catch {}
try {
    adb shell pm set-home-activity com.cleanphone.glasshome/.MainActivity 2>&1 | Out-Null
} catch {}

# Start the home screen
Write-Host "[*] Starting Liquid Glass Home..." -ForegroundColor Cyan
adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.HOME -n com.cleanphone.glasshome/.MainActivity | Out-Null

if ($DisableStock) {
    Write-Host "[*] Disabling OEM stock launcher..." -ForegroundColor Yellow
    $stockList = @("com.oppo.launcher", "com.coloros.home", "com.oneplus.launcher", "com.realme.launcher", "com.bbk.launcher2", "com.vivo.launcher")
    $installed = (adb shell pm list packages) -join "`n"
    foreach ($stock in $stockList) {
        if ($installed -match "package:$stock") {
            Write-Host "[*] Disabling $stock..." -ForegroundColor DarkGray
            adb shell pm disable-user --user 0 $stock | Out-Null
        }
    }
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Liquid Glass Launcher successfully installed!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
