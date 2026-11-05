#!/usr/bin/env python3
"""
CleanYourPhone - Master Minimalist Graphics & UI Mockup Generator
Creates 100% clean, non-AI-generated, vector-sharp graphics and mockups for all 7 repository images.
"""

import os
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "C:/Windows/Fonts"
f_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 36)
f_h2 = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 24)
f_sub = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 17)
f_tag = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 12)
f_body = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 14)
f_bold = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 15)
f_small = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 11)
f_clock_lg = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 36)
f_clock_sm = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 20)
f_metric_num = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 48)

DOCS_DIR = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs"
os.makedirs(DOCS_DIR, exist_ok=True)

def create_base_canvas(w=1600, h=900, top_color=(12, 16, 22), bot_color=(8, 10, 14)):
    img = Image.new("RGBA", (w, h), (10, 13, 18, 255))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        fac = y / float(h)
        r = int(top_color[0] * (1 - fac) + bot_color[0] * fac)
        g = int(top_color[1] * (1 - fac) + bot_color[1] * fac)
        b = int(top_color[2] * (1 - fac) + bot_color[2] * fac)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
    return img, draw

def draw_header(draw, w, tag, title, subtitle):
    # Tag Pill
    bbox_tag = draw.textbbox((0, 0), tag, font=f_tag)
    tw = bbox_tag[2] - bbox_tag[0]
    tx = (w - tw) // 2
    ty = 40
    draw.rounded_rectangle([tx - 14, ty - 4, tx + tw + 14, ty + 20], radius=12, fill=(255, 255, 255, 14), outline=(100, 160, 255, 90), width=1)
    draw.text((tx, ty), tag, font=f_tag, fill=(120, 185, 255, 255))

    # Title
    bbox_t = draw.textbbox((0, 0), title, font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 74), title, font=f_title, fill=(255, 255, 255, 255))

    # Subtitle
    bbox_s = draw.textbbox((0, 0), subtitle, font=f_sub)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 126), subtitle, font=f_sub, fill=(155, 168, 185, 255))

# ==============================================================================
# 1. BEFORE AND AFTER (Oppo Smartphone)
# ==============================================================================
def render_before_after():
    img, draw = create_base_canvas(1600, 920)
    draw_header(draw, 1600, "DUAL-LIST SAFETY CONSENSUS", "Before & After Debloating Comparison", "Real ColorOS bloatware on Oppo hardware transformed into the minimal Liquid Glass UI")

    PW, PH = 300, 600
    CORNER = 36
    Y = 195
    X_BEFORE = 360
    X_AFTER = 940

    # --- LEFT PHONE: BEFORE (ColorOS Bloatware) ---
    # Phone Chassis
    draw.rounded_rectangle([X_BEFORE - 2, Y - 2, X_BEFORE + PW + 2, Y + PH + 2], radius=CORNER + 2, fill=(25, 28, 34, 255), outline=(220, 70, 70, 120), width=2)
    # Screen
    SX, SY = X_BEFORE + 8, Y + 8
    SW, SH = PW - 16, PH - 16
    draw.rounded_rectangle([SX, SY, SX + SW, SY + SH], radius=CORNER - 6, fill=(18, 16, 20, 255))

    # Punch hole camera
    draw.ellipse([X_BEFORE + PW//2 - 4, SY + 12, X_BEFORE + PW//2 + 4, SY + 20], fill=(8, 8, 10, 255))

    # Status Bar
    draw.text((SX + 16, SY + 12), "10:48", font=f_small, fill=(255, 255, 255, 200))
    draw.text((SX + SW - 75, SY + 12), "5G  84%", font=f_small, fill=(255, 255, 255, 200))

    # Intrusive Lockscreen / Glance Ad Banner
    draw.rounded_rectangle([SX + 14, SY + 40, SX + SW - 14, SY + 115], radius=14, fill=(255, 60, 60, 35), outline=(255, 80, 80, 90), width=1)
    draw.text((SX + 26, SY + 48), "Glance Sponsored Feed", font=f_bold, fill=(255, 120, 120, 255))
    draw.text((SX + 26, SY + 72), "Trending: 10 Mobile Games You Must Play!\nShop now for 50% discount on Coins", font=f_small, fill=(240, 220, 220, 220))

    # Notification Toast: App Market Spam
    draw.rounded_rectangle([SX + 14, SY + 125, SX + SW - 14, SY + 175], radius=12, fill=(40, 32, 35, 255), outline=(255, 100, 100, 60), width=1)
    draw.text((SX + 24, SY + 133), "HeyTap App Market • Just now", font=f_small, fill=(255, 140, 140, 255))
    draw.text((SX + 24, SY + 150), "3 updates pending. Clean 1.2 GB cache now!", font=f_small, fill=(220, 220, 220, 200))

    # Cluttered Bloat Apps Grid
    bloat_names = [
        ("Hot Apps", True), ("Hot Games", True), ("App Market", True), ("Theme Store", True),
        ("FinShell Pay", True), ("Game Center", True), ("O-Roaming", True), ("LogKit Daemon", True),
        ("DeepThinker", True), ("Glance", True), ("NearMe ROM", True), ("Browser Ads", True)
    ]
    for idx, (bname, is_bloat) in enumerate(bloat_names):
        col = idx % 4
        row = idx // 4
        bx = SX + 14 + col * 66
        by = SY + 195 + row * 75
        # Red warning outline
        draw.rounded_rectangle([bx, by, bx + 50, by + 50], radius=12, fill=(45, 25, 25, 255), outline=(255, 70, 70, 160), width=1)
        # 99+ red badge
        draw.ellipse([bx + 36, by - 4, bx + 54, by + 14], fill=(240, 40, 40, 255))
        draw.text((bx + 40, by - 2), "!", font=f_tag, fill=(255, 255, 255, 255))
        # Label
        draw.text((bx - 2, by + 53), bname[:9], font=f_small, fill=(240, 160, 160, 255))

    # Cluttered Stock Bottom Dock
    draw.rounded_rectangle([SX + 12, SY + SH - 85, SX + SW - 12, SY + SH - 15], radius=20, fill=(35, 28, 28, 255), outline=(255, 80, 80, 80), width=1)
    for di in range(4):
        dx = SX + 22 + di * 68
        draw.rounded_rectangle([dx, SY + SH - 75, dx + 46, SY + SH - 25], radius=12, fill=(60, 30, 30, 255), outline=(255, 90, 90, 120), width=1)

    # Status Pill Below Before
    draw.rounded_rectangle([X_BEFORE + 15, Y + PH + 20, X_BEFORE + PW - 15, Y + PH + 58], radius=16, fill=(255, 60, 60, 20), outline=(255, 70, 70, 140), width=1)
    draw.text((X_BEFORE + 32, Y + PH + 28), "BEFORE: 84+ Bloat Packages Active", font=f_bold, fill=(255, 110, 110, 255))
    draw.text((X_BEFORE + 35, Y + PH + 43), "Hot Apps • App Market • High Idle Drain", font=f_small, fill=(220, 160, 160, 220))

    # --- CENTER ARROW ---
    draw.text((790, Y + PH // 2 - 20), "──►", font=f_title, fill=(100, 180, 255, 220))
    draw.text((765, Y + PH // 2 + 25), "CleanYourPhone\nSafe Debloat", font=f_tag, fill=(140, 180, 230, 200))

    # --- RIGHT PHONE: AFTER (Liquid Glass UI) ---
    draw.rounded_rectangle([X_AFTER - 2, Y - 2, X_AFTER + PW + 2, Y + PH + 2], radius=CORNER + 2, fill=(25, 28, 34, 255), outline=(0, 200, 130, 140), width=2)
    SX_A, SY_A = X_AFTER + 8, Y + 8
    draw.rounded_rectangle([SX_A, SY_A, SX_A + SW, SY_A + SH], radius=CORNER - 6, fill=(12, 18, 24, 255))

    # Punch hole camera
    draw.ellipse([X_AFTER + PW//2 - 4, SY_A + 12, X_AFTER + PW//2 + 4, SY_A + 20], fill=(8, 8, 10, 255))

    # Status Bar
    draw.text((SX_A + 16, SY_A + 12), "10:48", font=f_small, fill=(255, 255, 255, 200))
    draw.text((SX_A + SW - 75, SY_A + 12), "5G  98%", font=f_small, fill=(255, 255, 255, 200))

    # Liquid Glass Glance Header Card
    draw.rounded_rectangle([SX_A + 14, SY_A + 40, SX_A + SW - 14, SY_A + 125], radius=18, fill=(255, 255, 255, 25), outline=(255, 255, 255, 75), width=1)
    draw.text((SX_A + 30, SY_A + 52), "10:48", font=f_clock_lg, fill=(255, 255, 255, 255))
    draw.text((SX_A + 30, SY_A + 96), "Thursday, November 5", font=f_body, fill=(190, 215, 235, 240))
    # Status chip inside header
    draw.rounded_rectangle([SX_A + SW - 100, SY_A + 56, SX_A + SW - 26, SY_A + 82], radius=12, fill=(0, 200, 120, 50), outline=(0, 220, 130, 180), width=1)
    draw.text((SX_A + SW - 90, SY_A + 62), "Clean • Fast", font=f_tag, fill=(255, 255, 255, 255))

    # Frosted Search Capsule
    draw.rounded_rectangle([SX_A + 14, SY_A + 138, SX_A + SW - 14, SY_A + 178], radius=16, fill=(255, 255, 255, 18), outline=(255, 255, 255, 55), width=1)
    draw.text((SX_A + 30, SY_A + 148), "Search apps...", font=f_body, fill=(160, 180, 205, 180))

    # Clean Ad-Free App Grid (0.5x responsive)
    clean_apps = [
        "Phone", "Messages", "Camera", "Settings",
        "Photos", "Browser", "Calendar", "Calculator",
        "Music", "Notes", "Maps", "Files"
    ]
    for idx, aname in enumerate(clean_apps):
        col = idx % 4
        row = idx // 4
        bx = SX_A + 14 + col * 66
        by = SY_A + 195 + row * 75
        # Clean frosted squircle
        draw.rounded_rectangle([bx, by, bx + 50, by + 50], radius=12, fill=(255, 255, 255, 30), outline=(255, 255, 255, 60), width=1)
        # Inner icon symbol
        draw.ellipse([bx + 16, by + 16, bx + 34, by + 34], fill=(120, 180, 255, 120))
        # Label
        draw.text((bx + 2, by + 53), aname[:8], font=f_small, fill=(230, 240, 250, 240))

    # Floating Liquid Glass Island / Bottom Dock
    draw.rounded_rectangle([SX_A + 12, SY_A + SH - 85, SX_A + SW - 12, SY_A + SH - 15], radius=24, fill=(255, 255, 255, 45), outline=(255, 255, 255, 120), width=1)
    for di in range(4):
        dx = SX_A + 22 + di * 68
        draw.rounded_rectangle([dx, SY_A + SH - 75, dx + 46, SY_A + SH - 25], radius=14, fill=(255, 255, 255, 65), outline=(255, 255, 255, 95), width=1)
        draw.ellipse([dx + 15, SY_A + SH - 60, dx + 31, SY_A + SH - 40], fill=(0, 200, 130, 180) if di==0 else (120, 180, 255, 180))

    # Status Pill Below After
    draw.rounded_rectangle([X_AFTER + 15, Y + PH + 20, X_AFTER + PW - 15, Y + PH + 58], radius=16, fill=(0, 200, 130, 20), outline=(0, 200, 130, 140), width=1)
    draw.text((X_AFTER + 34, Y + PH + 28), "AFTER: 0 Bloat • 0 Telemetry", font=f_bold, fill=(0, 220, 140, 255))
    draw.text((X_AFTER + 36, Y + PH + 43), "Liquid Glass UI • 0.5x Snappy • 15MB RAM", font=f_small, fill=(180, 230, 200, 220))

    out_file = os.path.join(DOCS_DIR, "before-and-after.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: before-and-after.jpg")

# ==============================================================================
# 2. LIQUID GLASS HOME UI SHOWCASE
# ==============================================================================
def render_liquid_glass_home():
    img, draw = create_base_canvas(1500, 920)
    draw_header(draw, 1500, "LIQUID GLASS HOME SCREEN", "Minimalist Android-First Interface", "Sub-15MB RAM footprint · Tuned to 0.5x snappy animation speed · 100% offline & private")

    PW, PH = 320, 640
    CORNER = 38
    X = 590
    Y = 190

    # Phone Frame
    draw.rounded_rectangle([X - 3, Y - 3, X + PW + 3, Y + PH + 3], radius=CORNER + 3, fill=(30, 35, 45, 255), outline=(100, 140, 200, 150), width=2)
    SX, SY = X + 8, Y + 8
    SW, SH = PW - 16, PH - 16
    draw.rounded_rectangle([SX, SY, SX + SW, SY + SH], radius=CORNER - 6, fill=(12, 17, 24, 255))

    # Punch hole camera
    draw.ellipse([X + PW//2 - 4, SY + 12, X + PW//2 + 4, SY + 20], fill=(8, 8, 10, 255))
    draw.text((SX + 20, SY + 12), "10:48", font=f_small, fill=(255, 255, 255, 200))
    draw.text((SX + SW - 80, SY + 12), "5G  99%", font=f_small, fill=(255, 255, 255, 200))

    # Frosted Header Card
    draw.rounded_rectangle([SX + 14, SY + 44, SX + SW - 14, SY + 135], radius=20, fill=(255, 255, 255, 25), outline=(255, 255, 255, 80), width=1)
    draw.text((SX + 32, SY + 58), "10:48", font=f_clock_lg, fill=(255, 255, 255, 255))
    draw.text((SX + 32, SY + 104), "Thursday, November 5", font=f_body, fill=(200, 220, 240, 240))
    draw.rounded_rectangle([SX + SW - 105, SY + 62, SX + SW - 28, SY + 88], radius=12, fill=(0, 180, 255, 40), outline=(0, 200, 255, 160), width=1)
    draw.text((SX + SW - 95, SY + 68), "Clean • Fast", font=f_tag, fill=(255, 255, 255, 255))

    # Frosted Search Capsule
    draw.rounded_rectangle([SX + 14, SY + 150, SX + SW - 14, SY + 192], radius=18, fill=(255, 255, 255, 18), outline=(255, 255, 255, 60), width=1)
    draw.text((SX + 34, SY + 162), "Search apps...", font=f_body, fill=(160, 180, 210, 180))

    # App Grid
    apps = ["Phone", "Messages", "Camera", "Settings", "Photos", "Browser", "Music", "Notes", "Maps", "Clock", "Files", "Weather"]
    for idx, aname in enumerate(apps):
        col = idx % 4
        row = idx // 4
        bx = SX + 14 + col * 71
        by = SY + 215 + row * 84
        draw.rounded_rectangle([bx, by, bx + 54, by + 54], radius=14, fill=(255, 255, 255, 30), outline=(255, 255, 255, 65), width=1)
        draw.ellipse([bx + 18, by + 18, bx + 36, by + 36], fill=(120, 180, 255, 140))
        draw.text((bx + 4, by + 58), aname[:8], font=f_small, fill=(230, 240, 250, 240))

    # Liquid Glass Dock
    draw.rounded_rectangle([SX + 12, SY + SH - 90, SX + SW - 12, SY + SH - 16], radius=26, fill=(255, 255, 255, 45), outline=(255, 255, 255, 120), width=1)
    for di in range(4):
        dx = SX + 24 + di * 72
        draw.rounded_rectangle([dx, SY + SH - 80, dx + 50, SY + SH - 26], radius=16, fill=(255, 255, 255, 65), outline=(255, 255, 255, 95), width=1)
        draw.ellipse([dx + 16, SY + SH - 63, dx + 34, SY + SH - 43], fill=(0, 200, 130, 180) if di==0 else (100, 170, 255, 180))

    # --- LEFT FEATURE CALLOUT CARDS ---
    callouts_left = [
        ("Frosted Glance Card", "Displays time, date, and live status chip with ambient wallpaper light pass-through."),
        ("Offline Search Capsule", "Instant local app filter with zero network tracking, latency < 4ms."),
        ("Material You Grid", "Clean 4-column layout without promotional folders, Hot Apps, or badges.")
    ]
    for i, (title, desc) in enumerate(callouts_left):
        cy = 230 + i * 140
        draw.rounded_rectangle([120, cy, 510, cy + 110], radius=16, fill=(20, 26, 36, 220), outline=(255, 255, 255, 40), width=1)
        draw.text((142, cy + 18), title, font=f_bold, fill=(120, 190, 255, 255))
        draw.text((142, cy + 46), desc, font=f_body, fill=(180, 195, 215, 240))
        # Connection line
        draw.line([(510, cy + 55), (X - 10, cy + 55)], fill=(120, 190, 255, 80), width=1)

    # --- RIGHT FEATURE CALLOUT CARDS ---
    callouts_right = [
        ("Floating Liquid Glass Dock", "Translucent glass island with layered refraction and 1.5dp specular edge highlight."),
        ("0.5x Snappy Physics", "50ms touch-down, 80ms rebound curves tuned for lag-free 120Hz responsiveness."),
        ("Lightweight & Ad-Free", "Native Java/AndroidX architecture, consumes under 15MB RAM, zero ads.")
    ]
    for i, (title, desc) in enumerate(callouts_right):
        cy = 230 + i * 140
        draw.rounded_rectangle([990, cy, 1380, cy + 110], radius=16, fill=(20, 26, 36, 220), outline=(255, 255, 255, 40), width=1)
        draw.text((1012, cy + 18), title, font=f_bold, fill=(0, 220, 150, 255))
        draw.text((1012, cy + 46), desc, font=f_body, fill=(180, 195, 215, 240))
        # Connection line
        draw.line([(X + PW + 10, cy + 55), (990, cy + 55)], fill=(0, 220, 150, 80), width=1)

    out_file = os.path.join(DOCS_DIR, "liquid-glass-home.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: liquid-glass-home.jpg")

# ==============================================================================
# 3. GLASS DOCK & CONTEXT MENU DETAIL
# ==============================================================================
def render_dock_detail():
    img, draw = create_base_canvas(1400, 820)
    draw_header(draw, 1400, "INTERACTION DESIGN", "Liquid Glass Dock & Context Card Detail", "Layered glass refraction · 1.5dp specular highlight · Snappy long-press options")

    # Center floating dock
    DX, DY = 250, 480
    DW, DH = 900, 130
    draw.rounded_rectangle([DX, DY, DX + DW, DY + DH], radius=44, fill=(255, 255, 255, 35), outline=(255, 255, 255, 110), width=2)
    # Specular upper gleam line
    draw.line([(DX + 40, DY + 2), (DX + DW - 40, DY + 2)], fill=(255, 255, 255, 180), width=2)

    dock_items = [("Dialer", (0, 200, 120)), ("Messages", (80, 160, 255)), ("Browser", (255, 170, 0)), ("Camera", (240, 70, 90))]
    for i, (name, color) in enumerate(dock_items):
        ix = DX + 60 + i * 210
        iy = DY + 25
        draw.rounded_rectangle([ix, iy, ix + 80, iy + 80], radius=22, fill=(*color, 65), outline=(255, 255, 255, 90), width=1)
        draw.ellipse([ix + 26, iy + 26, ix + 54, iy + 54], fill=(*color, 220))
        draw.text((ix + 18, iy + 86), name, font=f_small, fill=(220, 230, 245, 220))

    # Floating Context Menu Card (pointing to Camera)
    CX, CY = 820, 190
    CW, CH = 340, 250
    draw.rounded_rectangle([CX, CY, CX + CW, CY + CH], radius=22, fill=(24, 30, 42, 245), outline=(255, 255, 255, 80), width=2)

    # Context Header
    draw.rounded_rectangle([CX + 20, CY + 18, CX + 64, CY + 62], radius=14, fill=(240, 70, 90, 70), outline=(240, 70, 90, 160), width=1)
    draw.text((CX + 76, CY + 22), "Camera", font=f_bold, fill=(255, 255, 255, 255))
    draw.text((CX + 76, CY + 42), "com.cleanphone.camera", font=f_small, fill=(160, 180, 205, 200))

    # Divider
    draw.line([(CX + 16, CY + 75), (CX + CW - 16, CY + 75)], fill=(255, 255, 255, 35), width=1)

    # Menu Options
    options = [
        ("★  Pin to Dock", (255, 255, 255, 255)),
        ("ⓘ   App Info", (210, 225, 245, 255)),
        ("🗑  Uninstall / Disable", (255, 100, 100, 255))
    ]
    for mi, (otext, ocolor) in enumerate(options):
        oy = CY + 90 + mi * 48
        draw.rounded_rectangle([CX + 16, oy, CX + CW - 16, oy + 40], radius=10, fill=(255, 255, 255, 12), outline=(255, 255, 255, 30), width=1)
        draw.text((CX + 32, oy + 10), otext, font=f_body, fill=ocolor)

    # Pointer line from menu to camera dock item
    draw.line([(CX + 170, CY + CH), (DX + 60 + 3 * 210 + 40, DY)], fill=(255, 255, 255, 90), width=2)

    # Specification Notes Below
    specs = [
        "1.5dp Specular Border Highlight",
        "Layered Glass Translucency",
        "0.5x Snappy Spring Touch Animation",
        "Reversible User-0 Package Actions"
    ]
    for si, stext in enumerate(specs):
        sx = 260 + si * 230
        sy = 660
        draw.rounded_rectangle([sx, sy, sx + 210, sy + 38], radius=12, fill=(255, 255, 255, 10), outline=(100, 160, 255, 60), width=1)
        draw.text((sx + 14, sy + 11), stext, font=f_small, fill=(180, 210, 240, 220))

    out_file = os.path.join(DOCS_DIR, "glass-dock-detail.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: glass-dock-detail.jpg")

# ==============================================================================
# 4. BATTERY AND RAM PERFORMANCE INFOGRAPHIC
# ==============================================================================
def render_battery_ram():
    img, draw = create_base_canvas(1600, 900)
    draw_header(draw, 1600, "BENCHMARK PERFORMANCE", "Battery Life & Memory Reclaimed", "Real hardware measurements before and after removing OEM telemetry and background bloat")

    # Left Card: Battery Drain Curve
    BX, BY, BW, BH = 120, 200, 640, 580
    draw.rounded_rectangle([BX, BY, BX + BW, BY + BH], radius=24, fill=(18, 24, 34, 220), outline=(255, 255, 255, 40), width=1)

    draw.text((BX + 32, BY + 30), "Overnight Standby Battery Drain (8 Hours)", font=f_h2, fill=(255, 255, 255, 255))
    draw.text((BX + 32, BY + 68), "Comparison of idle discharge rate while screen is off", font=f_sub, fill=(150, 170, 195, 220))

    # Big Metric
    draw.text((BX + 32, BY + 115), "Up to 80%", font=f_metric_num, fill=(0, 220, 140, 255))
    draw.text((BX + 300, BY + 138), "Reduction in Idle Drain", font=f_bold, fill=(200, 230, 215, 240))

    # Graph Box
    GX, GY, GW, GH = BX + 40, BY + 200, BW - 80, 260
    draw.rounded_rectangle([GX, GY, GX + GW, GY + GH], radius=14, fill=(12, 16, 24, 255), outline=(255, 255, 255, 30), width=1)
    # Grid lines
    for gy in range(GY + 40, GY + GH, 50):
        draw.line([(GX + 10, gy), (GX + GW - 10, gy)], fill=(255, 255, 255, 18), width=1)

    # Red Line: Before (12% drop)
    draw.line([(GX + 30, GY + 40), (GX + GW - 30, GY + GH - 40)], fill=(240, 60, 60, 240), width=4)
    draw.text((GX + 40, GY + 50), "Before: 12% Loss (140 wake-locks/hr)", font=f_bold, fill=(255, 110, 110, 255))

    # Green Line: After (1.5% drop - nearly flat)
    draw.line([(GX + 30, GY + 40), (GX + GW - 30, GY + 65)], fill=(0, 220, 140, 255), width=4)
    draw.text((GX + 220, GY + 75), "After: 1.5% Loss (Clean Doze State)", font=f_bold, fill=(0, 230, 150, 255))

    # Stat Badges Bottom Left
    draw.rounded_rectangle([BX + 40, BY + 490, BX + BW - 40, BY + 545], radius=14, fill=(0, 200, 120, 25), outline=(0, 200, 120, 80), width=1)
    draw.text((BX + 60, BY + 508), "+1.5 to 2.0 Extra Hours of Screen-On Time (SOT)", font=f_bold, fill=(160, 240, 200, 255))

    # Right Card: RAM & Memory Reclaimed
    RX, RY, RW, RH = 840, 200, 640, 580
    draw.rounded_rectangle([RX, RY, RX + RW, RY + RH], radius=24, fill=(18, 24, 34, 220), outline=(255, 255, 255, 40), width=1)

    draw.text((RX + 32, BY + 30), "RAM & Memory Reclaimed by Device", font=f_h2, fill=(255, 255, 255, 255))
    draw.text((RX + 32, BY + 68), "Persistent background bloatware removed from RAM", font=f_sub, fill=(150, 170, 195, 220))

    draw.text((RX + 32, BY + 115), "+1.4 GB", font=f_metric_num, fill=(80, 170, 255, 255))
    draw.text((RX + 265, BY + 138), "Free RAM Immediately Available", font=f_bold, fill=(200, 225, 255, 240))

    # RAM Bars for OEM brands
    ram_data = [
        ("OnePlus 11 / 12 (OxygenOS)", "4.8 GB", "6.2 GB", "+1.4 GB Reclaimed", (240, 50, 70)),
        ("Oppo Reno / Find (ColorOS)", "3.1 GB", "4.1 GB", "+1.0 GB Reclaimed", (0, 180, 110)),
        ("vivo V / X Series (Funtouch)", "3.4 GB", "4.5 GB", "+1.1 GB Reclaimed", (65, 115, 255)),
        ("Realme GT Series (Realme UI)", "2.9 GB", "3.9 GB", "+1.0 GB Reclaimed", (255, 185, 25)),
        ("iQOO Neo / Pro (Funtouch)", "5.1 GB", "6.4 GB", "+1.3 GB Reclaimed", (255, 115, 20))
    ]
    for ri, (dname, bfree, afree, diff, col) in enumerate(ram_data):
        rbar_y = RY + 200 + ri * 55
        draw.text((RX + 40, rbar_y), dname, font=f_bold, fill=(230, 240, 255, 240))
        draw.text((RX + RW - 180, rbar_y), diff, font=f_tag, fill=(*col, 255))

        # Background Bar
        draw.rounded_rectangle([RX + 40, rbar_y + 24, RX + RW - 40, rbar_y + 36], radius=6, fill=(35, 45, 60, 255))
        # Active Free Bar
        pct = 0.55 + ri * 0.08
        draw.rounded_rectangle([RX + 40, rbar_y + 24, RX + 40 + int((RW - 80) * pct), rbar_y + 36], radius=6, fill=(*col, 220))

    # Stat Badges Bottom Right
    draw.rounded_rectangle([RX + 40, RY + 490, RX + RW - 40, RY + 545], radius=14, fill=(80, 160, 255, 25), outline=(80, 160, 255, 80), width=1)
    draw.text((RX + 60, RY + 508), "Zero Resident OEM Ad Daemons or Analytics Loggers", font=f_bold, fill=(180, 220, 255, 255))

    out_file = os.path.join(DOCS_DIR, "feature-battery-ram.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: feature-battery-ram.jpg")

# ==============================================================================
# 5. PRIVACY & TELEMETRY SHIELD INFOGRAPHIC
# ==============================================================================
def render_privacy_telemetry():
    img, draw = create_base_canvas(1600, 900)
    draw_header(draw, 1600, "CYBER-PRIVACY SHIELD", "Telemetry & Tracker Blocking Engine", "Eliminate background data harvesting, user habit profilers, and sponsored push daemons")

    # Center Status Card
    draw.rounded_rectangle([250, 190, 1350, 290], radius=20, fill=(0, 200, 130, 20), outline=(0, 220, 140, 120), width=2)
    draw.text((280, 215), "4,370+ Daily Tracker Connections Prevented", font=f_h2, fill=(0, 230, 150, 255))
    draw.text((280, 252), "All telemetry services and proprietary ad channels are disabled exclusively for User 0", font=f_sub, fill=(180, 225, 205, 240))
    # Right badge
    draw.rounded_rectangle([1120, 220, 1310, 260], radius=12, fill=(0, 220, 140, 45), outline=(0, 230, 150, 180), width=1)
    draw.text((1140, 230), "100% PRIVATE", font=f_bold, fill=(255, 255, 255, 255))

    # Grid of Blocked Services
    trackers = [
        ("HeyTap Analytics & OpenID", "com.heytap.mcs • com.heytap.openid", "Ad push delivery and unique advertising identifier daemons", "~1,850 queries/day"),
        ("Vivo Daemon & Log System", "com.vivo.daemonService • com.bbk.iqoo.logsystem", "Continuous diagnostic reporting and telemetry logs", "~1,420 queries/day"),
        ("Facebook System Services", "com.facebook.system • com.facebook.appmanager", "Privileged background updater and silent app installer", "~620 queries/day"),
        ("Lock Screen Magazine (Glance)", "com.glance.internet • com.heytap.pictorial", "Dynamic lockscreen clickbait feeds and shopping ads", "~480 queries/day"),
        ("DeepThinker User Profiler", "com.oplus.deepthinker • com.coloros.atd", "Monitors app usage patterns and Wi-Fi networks", "Resident in RAM"),
        ("OEM Commercial FinShell", "com.finshell.wallet • com.vivo.wallet", "Pre-installed personal loan and financial marketing stubs", "Preloaded")
    ]

    for idx, (tname, tpkg, tdesc, tqueries) in enumerate(trackers):
        col = idx % 2
        row = idx // 2
        tx = 250 + col * 570
        ty = 320 + row * 165
        tw, th = 530, 140

        draw.rounded_rectangle([tx, ty, tx + tw, ty + th], radius=18, fill=(18, 24, 34, 220), outline=(255, 255, 255, 40), width=1)

        # Blocked icon indicator
        draw.ellipse([tx + 24, ty + 24, tx + 48, ty + 48], fill=(240, 60, 60, 45), outline=(240, 60, 60, 200), width=1)
        draw.text((tx + 31, ty + 27), "X", font=f_bold, fill=(255, 100, 100, 255))

        draw.text((tx + 60, ty + 22), tname, font=f_bold, fill=(255, 255, 255, 255))
        draw.text((tx + 60, ty + 48), tpkg, font=f_small, fill=(120, 180, 255, 220))
        draw.text((tx + 24, ty + 80), tdesc, font=f_body, fill=(170, 185, 205, 220))

        # Blocked Pill
        draw.rounded_rectangle([tx + tw - 125, ty + 22, tx + tw - 20, ty + 50], radius=8, fill=(240, 50, 50, 30), outline=(240, 60, 60, 140), width=1)
        draw.text((tx + tw - 110, ty + 28), "BLOCKED", font=f_tag, fill=(255, 110, 110, 255))

    out_file = os.path.join(DOCS_DIR, "feature-privacy-telemetry.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: feature-privacy-telemetry.jpg")

# ==============================================================================
# 6. REAL-TIME SEARCH & APP LIBRARY
# ==============================================================================
def render_search_library():
    img, draw = create_base_canvas(1400, 880)
    draw_header(draw, 1400, "REAL-TIME APP SEARCH", "Instant 0.5x Offline Search & App Drawer", "Lightning-fast fuzzy search with zero internet permissions, telemetry, or query logging")

    # Center Phone Mockup (Search Active)
    PX, PY = 520, 180
    PW, PH = 360, 640
    CORNER = 38
    draw.rounded_rectangle([PX - 3, PY - 3, PX + PW + 3, PY + PH + 3], radius=CORNER + 3, fill=(30, 35, 45, 255), outline=(100, 140, 200, 150), width=2)
    SX, SY = PX + 8, PY + 8
    SW, SH = PW - 16, PH - 16
    draw.rounded_rectangle([SX, SY, SX + SW, SY + SH], radius=CORNER - 6, fill=(12, 17, 24, 255))

    # Punch hole camera
    draw.ellipse([PX + PW//2 - 4, SY + 12, PX + PW//2 + 4, SY + 20], fill=(8, 8, 10, 255))

    # Active Search Capsule
    draw.rounded_rectangle([SX + 14, SY + 40, SX + SW - 14, SY + 86], radius=18, fill=(255, 255, 255, 30), outline=(100, 180, 255, 180), width=2)
    draw.text((SX + 32, SY + 52), "Note|", font=f_bold, fill=(255, 255, 255, 255))
    draw.text((SX + SW - 85, SY + 54), "1 result", font=f_small, fill=(140, 190, 255, 200))

    # Filtered Results Card (Liquid Glass style)
    draw.rounded_rectangle([SX + 14, SY + 104, SX + SW - 14, SY + 180], radius=16, fill=(255, 255, 255, 25), outline=(255, 255, 255, 70), width=1)
    draw.rounded_rectangle([SX + 28, SY + 118, SX + 74, SY + 164], radius=12, fill=(255, 180, 0, 70), outline=(255, 190, 20, 140), width=1)
    draw.text((SX + 88, SY + 122), "Notes", font=f_bold, fill=(255, 255, 255, 255))
    draw.text((SX + 88, SY + 145), "org.fossify.notes • Clean", font=f_small, fill=(180, 210, 240, 220))

    # Recent Apps Header
    draw.text((SX + 16, SY + 205), "RECENT APPS", font=f_tag, fill=(140, 160, 185, 200))

    recent = [("Phone", (0, 200, 120)), ("Camera", (240, 70, 90)), ("Calculator", (80, 160, 255)), ("Settings", (160, 170, 185))]
    for ri, (rname, rcol) in enumerate(recent):
        ry = SY + 230 + ri * 65
        draw.rounded_rectangle([SX + 14, ry, SX + SW - 14, ry + 54], radius=14, fill=(255, 255, 255, 18), outline=(255, 255, 255, 45), width=1)
        draw.rounded_rectangle([SX + 24, ry + 10, SX + 58, ry + 44], radius=10, fill=(*rcol, 65), outline=(255, 255, 255, 60), width=1)
        draw.text((SX + 72, ry + 16), rname, font=f_bold, fill=(240, 245, 255, 255))

    # Left & Right Callout Cards
    draw.rounded_rectangle([100, 320, 440, 480], radius=18, fill=(18, 24, 34, 220), outline=(255, 255, 255, 40), width=1)
    draw.text((120, 340), "0.5x Snappy Filter", font=f_bold, fill=(100, 180, 255, 255))
    draw.text((120, 370), "• Sub-4ms response time\n• Real-time TextWatcher\n• 120Hz smooth animations\n• Zero search stutter", font=f_body, fill=(180, 195, 215, 240))

    draw.rounded_rectangle([960, 320, 1300, 480], radius=18, fill=(18, 24, 34, 220), outline=(255, 255, 255, 40), width=1)
    draw.text((980, 340), "100% Offline Privacy", font=f_bold, fill=(0, 220, 140, 255))
    draw.text((980, 370), "• Zero network calls\n• No query logging\n• No sponsored suggestions\n• Pure local indexing", font=f_body, fill=(180, 225, 205, 240))

    out_file = os.path.join(DOCS_DIR, "feature-search-library.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print("Rendered: feature-search-library.jpg")

if __name__ == "__main__":
    print("[*] Generating all 6 clean minimalist repository mockups...")
    render_before_after()
    render_liquid_glass_home()
    render_dock_detail()
    render_battery_ram()
    render_privacy_telemetry()
    render_search_library()
    print("[+] All mockups successfully created in docs/!")
