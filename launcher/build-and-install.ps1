<#
.SYNOPSIS
    Lawnchair Launcher - Installer & Setup Script for Windows PowerShell
.DESCRIPTION
    Installs Lawnchair Launcher (the modern open-source Pixel-style launcher
    based on AOSP Launcher3) as the default home screen via ADB.
    Upstream repository: https://github.com/LawnchairLauncher/lawnchair
.EXAMPLE
    .\launcher\build-and-install.ps1
    .\launcher\build-and-install.ps1 -DisableStock
#>

param (
    [string]$ApkPath = "",
    [switch]$DisableStock
)

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Lawnchair Launcher Installer (CleanYourPhone)" -ForegroundColor Green
Write-Host " Upstream: https://github.com/LawnchairLauncher/lawnchair" -ForegroundColor DarkGray
Write-Host "==========================================================" -ForegroundColor Cyan

Set-Location $PSScriptRoot

# 1. Verify ADB connection
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
$sdkRaw = (adb shell getprop ro.build.version.sdk).Trim() -replace '\D'
$sdk = [int]$sdkRaw

Write-Host "[*] Connected device: $brand $model (Android SDK $sdk)" -ForegroundColor Cyan

# 2. Select matching Lawnchair version and component
$pkgName = "app.lawnchair"
$launcherActivity = "app.lawnchair/app.lawnchair.LawnchairLauncher"
$downloadUrl = ""
$versionLabel = ""

if ($sdk -ge 34) {
    # Android 14 & 15
    $versionLabel = "Lawnchair 15 (Beta 3.0)"
    $downloadUrl = "https://github.com/LawnchairLauncher/lawnchair/releases/download/v15.0.0-beta3.0/Lawnchair.15.0.0.Beta.3.0.apk"
} elseif ($sdk -ge 29) {
    # Android 10, 11, 12, 13
    $versionLabel = "Lawnchair 14 (Beta 3)"
    $downloadUrl = "https://github.com/LawnchairLauncher/lawnchair/releases/download/v14.0.0-beta3/Lawnchair.14.0.0.Beta.3.apk"
} else {
    # Legacy Android 5 through 9 (ColorOS 5, older Oppo/Vivo/Xiaomi)
    $versionLabel = "Lawnchair 2.0 (Legacy)"
    $downloadUrl = "https://github.com/LawnchairLauncher/lawnchair/releases/download/2.0.2589/Lawnchair.2.0.2589.apk"
    $pkgName = "ch.deletescape.lawnchair.plah"
    $launcherActivity = "ch.deletescape.lawnchair.plah/ch.deletescape.lawnchair.plah.Launcher"
}

Write-Host "[*] Target launcher release: $versionLabel" -ForegroundColor White

# 3. Locate or download APK
$targetApk = ""
if ($ApkPath -and (Test-Path $ApkPath)) {
    $targetApk = $ApkPath
} elseif (Test-Path ".\Lawnchair.apk") {
    $targetApk = ".\Lawnchair.apk"
} else {
    # Check if user compiled inside lawnchair submodule
    $submoduleBuild = Get-ChildItem -Path ".\lawnchair" -Recurse -Filter "*.apk" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($submoduleBuild) {
        $targetApk = $submoduleBuild.FullName
    }
}

if (-not $targetApk -or -not (Test-Path $targetApk)) {
    Write-Host "[*] Fetching official release from Lawnchair GitHub..." -ForegroundColor Cyan
    Write-Host "    Source: $downloadUrl" -ForegroundColor DarkGray
    $targetApk = ".\Lawnchair.apk"
    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $downloadUrl -OutFile $targetApk -UseBasicParsing
        Write-Host "[*] Download completed successfully." -ForegroundColor Green
    } catch {
        Write-Error "Failed to download Lawnchair APK: $_"
        exit 1
    }
}

# 4. Install Lawnchair APK via ADB
Write-Host "[*] Installing $versionLabel on $brand $model..." -ForegroundColor White
$installOut = adb install -r -d $targetApk 2>&1
Write-Host "ADB install status: $installOut" -ForegroundColor Green

# 5. Set as default home activity
Write-Host "[*] Setting Lawnchair as default home screen..." -ForegroundColor Cyan
try {
    adb shell cmd package set-home-activity --user 0 $launcherActivity 2>&1 | Out-Null
} catch {}
try {
    adb shell pm set-home-activity $launcherActivity 2>&1 | Out-Null
} catch {}

# 6. Configure 0.5x transition speed
Write-Host "[*] Setting transition speed to 0.5x for snappy, lag-free experience..." -ForegroundColor Cyan
try {
    adb shell settings put global window_animation_scale 0.5 2>&1 | Out-Null
    adb shell settings put global transition_animation_scale 0.5 2>&1 | Out-Null
    adb shell settings put global animator_duration_scale 0.5 2>&1 | Out-Null
} catch {}

# 7. Start Lawnchair home screen
Write-Host "[*] Starting Lawnchair Launcher..." -ForegroundColor Cyan
adb shell am start -W -a android.intent.action.MAIN -c android.intent.category.HOME -n $launcherActivity | Out-Null

# 8. Optionally disable OEM bloatware launcher
if ($DisableStock) {
    Write-Host "[*] Disabling OEM stock launcher..." -ForegroundColor Yellow
    $stockList = @(
        "com.oppo.launcher", "com.coloros.home",
        "com.oneplus.launcher", "com.realme.launcher",
        "com.bbk.launcher2", "com.vivo.launcher",
        "com.miui.home", "com.sec.android.app.launcher",
        "com.transsion.hilauncher", "com.transsion.XOSLauncher"
    )
    $installed = (adb shell pm list packages) -join "`n"
    foreach ($stock in $stockList) {
        if ($installed -match "package:$stock") {
            Write-Host "[*] Disabling $stock..." -ForegroundColor DarkGray
            adb shell pm disable-user --user 0 $stock 2>&1 | Out-Null
        }
    }
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Lawnchair Launcher successfully installed and running!" -ForegroundColor Green
Write-Host " Experience: Pixel-style AOSP launcher, Material You, 0.5x speed" -ForegroundColor White
Write-Host "==========================================================" -ForegroundColor Cyan
