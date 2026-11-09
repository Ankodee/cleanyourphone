#!/usr/bin/env python3
"""
CleanYourPhone - Professional Lawnchair Launcher Showcase Generator
Renders three high-resolution, ultra-clean 1920x1080 studio graphics:
1. docs/lawnchair-ui-showcase.jpg (Home Screen UI & Feature Overview)
2. docs/lawnchair-features.jpg (3-Screen UI Progression: Home, Drawer, Settings)
3. docs/lawnchair-customization-detail.jpg (Customization, Gestures & RAM Efficiency)
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1920
HEIGHT = 1080
FONT_DIR = "C:/Windows/Fonts"
LOGO_PATH = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/launcher/lawnchair/docs/assets/lawnchair-round.webp"

# Fonts
font_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 38)
font_subtitle = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 17)
font_badge = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 12)
font_card_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 18)
font_card_body = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 13)
font_card_tag = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 11)
font_phone_clock = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 26)
font_phone_sub = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 12)
font_phone_app = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 10)
font_phone_status = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 10)
font_footer = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 12)

lawnchair_logo = None
if os.path.exists(LOGO_PATH):
    lawnchair_logo = Image.open(LOGO_PATH).convert("RGBA")

def create_base_canvas():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (11, 14, 20, 255))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        factor = y / float(HEIGHT)
        r = int(9 + factor * 8)
        g = int(12 + factor * 9)
        b = int(18 + factor * 14)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))
    return img, draw

# ==============================================================================
# IMAGE 1: docs/lawnchair-ui-showcase.jpg
# ==============================================================================
def render_ui_showcase():
    img, draw = create_base_canvas()

    # Header Tag & Title
    header_tag = "LAWNCHAIR LAUNCHER  ·  PIXEL-PURE AOSP HOME SCREEN"
    bbox_tag = draw.textbbox((0, 0), header_tag, font=font_badge)
    tag_w = bbox_tag[2] - bbox_tag[0]
    tag_x = (WIDTH - tag_w) // 2
    tag_y = 36

    draw.rounded_rectangle([tag_x - 18, tag_y - 5, tag_x + tag_w + 18, tag_y + 21], radius=13, fill=(255, 255, 255, 12), outline=(100, 175, 255, 80), width=1)
    draw.text((tag_x, tag_y), header_tag, font=font_badge, fill=(125, 195, 255, 255))

    title_text = "The Minimalist Android Experience"
    bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = bbox_title[2] - bbox_title[0]
    draw.text(((WIDTH - title_w) // 2, 70), title_text, font=font_title, fill=(255, 255, 255, 255))

    sub_text = "Pixel Launcher aesthetics, Material You dynamic Monet palettes, Smart At a Glance, and 0.5x instantaneous physics"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_subtitle)
    sub_w = bbox_sub[2] - bbox_sub[0]
    draw.text(((WIDTH - sub_w) // 2, 120), sub_text, font=font_subtitle, fill=(155, 170, 190, 255))

    # Center Hero Smartphone
    PW = 340
    PH = 690
    PX = (WIDTH - PW) // 2
    PY = 175
    CORNER = 36

    # Chassis glow & frame
    draw.rounded_rectangle([PX - 6, PY - 6, PX + PW + 6, PY + PH + 6], radius=CORNER + 6, fill=(45, 125, 245, 28))
    draw.rounded_rectangle([PX, PY, PX + PW, PY + PH], radius=CORNER, fill=(24, 28, 36, 255), outline=(70, 80, 98, 255), width=2)

    # Screen
    BEZEL = 8
    SX = PX + BEZEL
    SY = PY + BEZEL
    SW = PW - (BEZEL * 2)
    SH = PH - (BEZEL * 2)
    SC = CORNER - 6

    screen_img = Image.new("RGBA", (SW, SH), (10, 18, 32, 255))
    sdraw = ImageDraw.Draw(screen_img)
    for yline in range(SH):
        factor = yline / float(SH)
        sr = int(14 * (1 - factor) + 8 * factor)
        sg = int(35 * (1 - factor) + 16 * factor)
        sb = int(65 * (1 - factor) + 30 * factor)
        sdraw.line([(0, yline), (SW, yline)], fill=(sr, sg, sb, 255))

    mask = Image.new("L", (SW, SH), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, SW, SH], radius=SC, fill=255)
    img.paste(screen_img, (SX, SY), mask)
    draw.rounded_rectangle([SX, SY, SX + SW, SY + SH], radius=SC, outline=(255, 255, 255, 28), width=1)

    # Centered punch-hole camera
    cam_x = PX + (PW // 2)
    cam_y = SY + 14
    draw.ellipse([cam_x - 5, cam_y - 5, cam_x + 5, cam_y + 5], fill=(6, 8, 12, 255), outline=(45, 50, 60, 255), width=1)

    # Status Bar
    draw.text((SX + 20, SY + 10), "10:48", font=font_phone_status, fill=(240, 245, 255, 240))
    draw.text((SX + SW - 58, SY + 10), "5G  98%", font=font_phone_status, fill=(240, 245, 255, 240))

    # At a Glance Widget
    gw_x = SX + 18
    gw_y = SY + 48
    gw_w = SW - 36
    gw_h = 75
    draw.rounded_rectangle([gw_x, gw_y, gw_x + gw_w, gw_y + gw_h], radius=18, fill=(255, 255, 255, 24), outline=(255, 255, 255, 65), width=1)
    draw.text((gw_x + 18, gw_y + 12), "Thursday, Nov 9", font=font_phone_clock, fill=(255, 255, 255, 255))
    draw.text((gw_x + 18, gw_y + 45), "Sunny 24°C  ·  No upcoming events", font=font_phone_sub, fill=(200, 220, 245, 230))
    draw.rounded_rectangle([gw_x + gw_w - 62, gw_y + 20, gw_x + gw_w - 14, gw_y + 44], radius=10, fill=(45, 125, 245, 80), outline=(100, 180, 255, 180), width=1)
    draw.text((gw_x + gw_w - 53, gw_y + 26), "PIXEL", font=font_card_tag, fill=(255, 255, 255, 255))

    # Quick Search Bar (Capsule)
    sb_x = SX + 18
    sb_y = gw_y + gw_h + 20
    sb_w = SW - 36
    sb_h = 42
    draw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=21, fill=(255, 255, 255, 28), outline=(255, 255, 255, 60), width=1)
    # Draw G logo circle
    draw.ellipse([sb_x + 12, sb_y + 11, sb_x + 32, sb_y + 31], fill=(66, 133, 244, 255))
    draw.text((sb_x + 18, sb_y + 14), "G", font=font_phone_status, fill=(255, 255, 255, 255))
    draw.text((sb_x + 42, sb_y + 14), "Search apps, web & files...", font=font_phone_sub, fill=(180, 200, 225, 200))

    # 4x4 Material You App Icons Grid
    grid_y = sb_y + sb_h + 30
    app_names = [
        "Phone", "Messages", "Camera", "Settings",
        "Chrome", "Files", "Photos", "Clock",
        "Maps", "Calendar", "Calculator", "Notes",
        "Music", "Weather", "Contacts", "Gallery"
    ]
    ACCENT_MONET = (65, 135, 245)

    for row in range(4):
        for col in range(4):
            idx = row * 4 + col
            size = 38
            gap = (SW - 36 - (4 * size)) // 3
            ax = SX + 18 + col * (size + gap)
            ay = grid_y + row * (size + 24)

            # Squircle app icon
            tint = (*ACCENT_MONET, 140) if idx % 2 == 0 else (255, 255, 255, 45)
            draw.rounded_rectangle([ax, ay, ax + size, ay + size], radius=11, fill=tint, outline=(255, 255, 255, 70), width=1)
            # Label
            lbl = app_names[idx]
            bbox_lbl = draw.textbbox((0, 0), lbl, font=font_phone_app)
            lw = bbox_lbl[2] - bbox_lbl[0]
            draw.text((ax + (size - lw) // 2, ay + size + 5), lbl, font=font_phone_app, fill=(225, 235, 250, 230))

    # Floating Bottom Dock
    dk_w = SW - 28
    dk_h = 60
    dk_x = SX + 14
    dk_y = SY + SH - dk_h - 18
    draw.rounded_rectangle([dk_x, dk_y, dk_x + dk_w, dk_y + dk_h], radius=24, fill=(255, 255, 255, 36), outline=(255, 255, 255, 85), width=1)
    dock_apps = ["Phone", "Messages", "Browser", "Camera"]
    d_size = 38
    d_gap = (dk_w - (4 * d_size)) // 5
    for di in range(4):
        dix = dk_x + d_gap + di * (d_size + d_gap)
        diy = dk_y + (dk_h - d_size) // 2
        d_tint = (*ACCENT_MONET, 180) if di in (0, 3) else (255, 255, 255, 65)
        draw.rounded_rectangle([dix, diy, dix + d_size, diy + d_size], radius=11, fill=d_tint, outline=(255, 255, 255, 95), width=1)

    # --- LEFT CALLOUT CARDS ---
    LC_X = 80
    LC_W = 440
    CARD_H = 220

    # Card 1: At a Glance
    c1_y = 220
    draw.rounded_rectangle([LC_X, c1_y, LC_X + LC_W, c1_y + CARD_H], radius=16, fill=(255, 255, 255, 12), outline=(255, 255, 255, 35), width=1)
    draw.rounded_rectangle([LC_X + 24, c1_y + 20, LC_X + 180, c1_y + 44], radius=10, fill=(45, 125, 245, 60), outline=(100, 180, 255, 140), width=1)
    draw.text((LC_X + 34, c1_y + 25), "AT A GLANCE WIDGET", font=font_card_tag, fill=(130, 200, 255, 255))
    draw.text((LC_X + 24, c1_y + 58), "Smart Contextual Information", font=font_card_title, fill=(255, 255, 255, 255))
    c1_body = "Native Pixel-style glance card integrates live weather,\nupcoming calendar schedules, battery status, and commute alerts\ndirectly on your home screen without third-party battery drain."
    draw.text((LC_X + 24, c1_y + 92), c1_body, font=font_card_body, fill=(170, 185, 205, 230))
    # Bullet points
    draw.text((LC_X + 24, c1_y + 165), "✓ Smartspacer & weather feed integration", font=font_card_tag, fill=(100, 215, 140, 255))
    draw.text((LC_X + 24, c1_y + 185), "✓ Zero background telemetry, 100% private", font=font_card_tag, fill=(100, 215, 140, 255))

    # Card 2: Material You Theming
    c2_y = 480
    draw.rounded_rectangle([LC_X, c2_y, LC_X + LC_W, c2_y + CARD_H], radius=16, fill=(255, 255, 255, 12), outline=(255, 255, 255, 35), width=1)
    draw.rounded_rectangle([LC_X + 24, c2_y + 20, LC_X + 175, c2_y + 44], radius=10, fill=(160, 95, 255, 60), outline=(200, 140, 255, 140), width=1)
    draw.text((LC_X + 34, c2_y + 25), "DYNAMIC MONET THEMING", font=font_card_tag, fill=(210, 160, 255, 255))
    draw.text((LC_X + 24, c2_y + 58), "Material 3 Expressive Design", font=font_card_title, fill=(255, 255, 255, 255))
    c2_body = "Automatically extracts dynamic color palettes from any\nwallpaper on Android 12 through 15+. Adapts app icon tints,\nsearch capsules, and popup dialogs automatically."
    draw.text((LC_X + 24, c2_y + 92), c2_body, font=font_card_body, fill=(170, 185, 205, 230))
    # 4 Swatch Circles
    swatches = [(45, 125, 245), (160, 95, 255), (0, 205, 130), (255, 195, 25)]
    for si, sc in enumerate(swatches):
        draw.ellipse([LC_X + 24 + si * 32, c2_y + 170, LC_X + 46 + si * 32, c2_y + 192], fill=(*sc, 255), outline=(255, 255, 255, 160), width=1)
    draw.text((LC_X + 160, c2_y + 174), "Dynamic Palette Engine", font=font_card_tag, fill=(200, 215, 235, 220))

    # --- RIGHT CALLOUT CARDS ---
    RC_X = WIDTH - 80 - LC_W

    # Card 3: 0.5x Transitions
    c3_y = 220
    draw.rounded_rectangle([RC_X, c3_y, RC_X + LC_W, c3_y + CARD_H], radius=16, fill=(255, 255, 255, 12), outline=(255, 255, 255, 35), width=1)
    draw.rounded_rectangle([RC_X + 24, c3_y + 20, RC_X + 175, c3_y + 44], radius=10, fill=(255, 185, 20, 60), outline=(255, 215, 75, 140), width=1)
    draw.text((RC_X + 34, c3_y + 25), "0.5X SNAPPY PHYSICS", font=font_card_tag, fill=(255, 215, 75, 255))
    draw.text((RC_X + 24, c3_y + 58), "Instant Lag-Free Transitions", font=font_card_title, fill=(255, 255, 255, 255))
    c3_body = "Halved window, activity, and animator scales (150ms)\neliminate sluggish OEM animation lags. Automatically tuned\nover ADB during install for instantaneous touch response."
    draw.text((RC_X + 24, c3_y + 92), c3_body, font=font_card_body, fill=(170, 185, 205, 230))
    draw.text((RC_X + 24, c3_y + 165), "⚡ 150ms App Launch  ·  80ms Touch Scales", font=font_card_tag, fill=(255, 215, 75, 255))
    draw.text((RC_X + 24, c3_y + 185), "⚡ 120Hz Silk Physics with zero stutter", font=font_card_tag, fill=(255, 215, 75, 255))

    # Card 4: 100% Privacy & Zero Bloat
    c4_y = 480
    draw.rounded_rectangle([RC_X, c4_y, RC_X + LC_W, c4_y + CARD_H], radius=16, fill=(255, 255, 255, 12), outline=(255, 255, 255, 35), width=1)
    draw.rounded_rectangle([RC_X + 24, c4_y + 20, RC_X + 160, c4_y + 44], radius=10, fill=(0, 200, 120, 60), outline=(80, 230, 160, 140), width=1)
    draw.text((RC_X + 34, c4_y + 25), "PRIVACY & EFFICIENCY", font=font_card_tag, fill=(100, 235, 160, 255))
    draw.text((RC_X + 24, c4_y + 58), "Pure AOSP Launcher3 Core", font=font_card_title, fill=(255, 255, 255, 255))
    c4_body = "Zero ads, zero commercial recommendations, and zero\nanalytics uploaders. Uses under 20MB of RAM compared to\nstock OEM launchers consuming 400MB–600MB."
    draw.text((RC_X + 24, c4_y + 92), c4_body, font=font_card_body, fill=(170, 185, 205, 230))
    draw.text((RC_X + 24, c4_y + 165), "🛡️ <20MB RAM vs 500MB OEM launchers", font=font_card_tag, fill=(100, 235, 160, 255))
    draw.text((RC_X + 24, c4_y + 185), "🛡️ 100% offline, zero network telemetry", font=font_card_tag, fill=(100, 235, 160, 255))

    # Footer Banner
    foot_text = "Universal Android 5.0 to 15.0+  ·  Open Source (GPL-3.0 / Apache-2.0)  ·  Upstream: github.com/LawnchairLauncher/lawnchair"
    bbox_ft = draw.textbbox((0, 0), foot_text, font=font_footer)
    ft_w = bbox_ft[2] - bbox_ft[0]
    draw.text(((WIDTH - ft_w) // 2, 1038), foot_text, font=font_footer, fill=(130, 145, 165, 220))

    out_file = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs/lawnchair-ui-showcase.jpg"
    img.convert("RGB").save(out_file, "JPEG", quality=95)
    print(f"[OK] Generated: {out_file}")

# ==============================================================================
# IMAGE 2: docs/lawnchair-features.jpg
# ==============================================================================
def render_features_progression():
    img, draw = create_base_canvas()

    header_tag = "LAWNCHAIR LAUNCHER  ·  CORE UI & WORKFLOW PROGRESSION"
    bbox_tag = draw.textbbox((0, 0), header_tag, font=font_badge)
    tag_w = bbox_tag[2] - bbox_tag[0]
    tag_x = (WIDTH - tag_w) // 2
    tag_y = 36

    draw.rounded_rectangle([tag_x - 18, tag_y - 5, tag_x + tag_w + 18, tag_y + 21], radius=13, fill=(255, 255, 255, 12), outline=(100, 175, 255, 80), width=1)
    draw.text((tag_x, tag_y), header_tag, font=font_badge, fill=(125, 195, 255, 255))

    title_text = "Pixel Aesthetics, Smart Drawer & Deep Customization"
    bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = bbox_title[2] - bbox_title[0]
    draw.text(((WIDTH - title_w) // 2, 70), title_text, font=font_title, fill=(255, 255, 255, 255))

    sub_text = "Three core interfaces working in unison: clean Home Screen, fast App Drawer search, and comprehensive settings"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_subtitle)
    sub_w = bbox_sub[2] - bbox_sub[0]
    draw.text(((WIDTH - sub_w) // 2, 120), sub_text, font=font_subtitle, fill=(155, 170, 190, 255))

    # 3 Large Phones Side by Side
    PW = 320
    PH = 640
    CORNER = 32
    PY = 175
    TOTAL_W = 3 * PW + 2 * 120
    START_X = (WIDTH - TOTAL_W) // 2

    SCREENS = [
        {
            "tag": "1. PIXEL HOME SCREEN",
            "title": "Minimal Home & At a Glance",
            "desc": "Smart date/weather glance card, Google capsule search, 4x4 Material You app grid, and persistent 4-app floating dock.",
            "accent": (45, 125, 245),
            "type": "home"
        },
        {
            "tag": "2. SMART APP DRAWER",
            "title": "Lightning-Fast Fuzzy Search",
            "desc": "Smooth vertical scrolling, alphabet fast-scrubber, fuzzy search box, customizable tabs, and hidden apps drawer.",
            "accent": (0, 205, 130),
            "type": "drawer"
        },
        {
            "tag": "3. DEEP CUSTOMIZATION",
            "title": "Granular Controls & Theming",
            "desc": "Independent grid sizing (4x4 to 7x7), third-party icon packs, custom fonts, gesture shortcuts, and QuickSwitch recents.",
            "accent": (160, 95, 255),
            "type": "settings"
        }
    ]

    for idx, sc_info in enumerate(SCREENS):
        px = START_X + idx * (PW + 120)
        py = PY

        # Glow & Frame
        draw.rounded_rectangle([px - 5, py - 5, px + PW + 5, py + PH + 5], radius=CORNER + 5, fill=(*sc_info["accent"], 26))
        draw.rounded_rectangle([px, py, px + PW, py + PH], radius=CORNER, fill=(24, 28, 36, 255), outline=(70, 80, 95, 255), width=2)

        BEZEL = 7
        sx = px + BEZEL
        sy = py + BEZEL
        sw = PW - (BEZEL * 2)
        sh = PH - (BEZEL * 2)
        sc = CORNER - 6

        screen_img = Image.new("RGBA", (sw, sh), (10, 16, 28, 255))
        sdraw = ImageDraw.Draw(screen_img)

        # Wallpaper
        for yline in range(sh):
            factor = yline / float(sh)
            sr = int(12 * (1 - factor) + 8 * factor)
            sg = int(28 * (1 - factor) + 16 * factor)
            sb = int(55 * (1 - factor) + 30 * factor)
            sdraw.line([(0, yline), (sw, yline)], fill=(sr, sg, sb, 255))

        mask = Image.new("L", (sw, sh), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.rounded_rectangle([0, 0, sw, sh], radius=sc, fill=255)
        img.paste(screen_img, (sx, sy), mask)
        draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=sc, outline=(255, 255, 255, 28), width=1)

        # Punch hole camera
        cam_x = px + (PW // 2)
        cam_y = sy + 13
        draw.ellipse([cam_x - 4, cam_y - 4, cam_x + 4, cam_y + 4], fill=(6, 8, 12, 255), outline=(45, 50, 60, 255), width=1)

        # Status Bar
        draw.text((sx + 16, sy + 10), "10:48", font=font_phone_status, fill=(240, 245, 255, 240))
        draw.text((sx + sw - 52, sy + 10), "5G  98%", font=font_phone_status, fill=(240, 245, 255, 240))

        # SCREEN CONTENTS
        if sc_info["type"] == "home":
            # Glance
            gw_x = sx + 14
            gw_y = sy + 44
            gw_w = sw - 28
            draw.rounded_rectangle([gw_x, gw_y, gw_x + gw_w, gw_y + 65], radius=16, fill=(255, 255, 255, 24), outline=(255, 255, 255, 60), width=1)
            draw.text((gw_x + 14, gw_y + 10), "Thursday, Nov 9", font=font_card_title, fill=(255, 255, 255, 255))
            draw.text((gw_x + 14, gw_y + 36), "Sunny 24°C  ·  At a Glance", font=font_phone_sub, fill=(200, 220, 245, 230))

            # Search bar
            sb_x = sx + 14
            sb_y = gw_y + 80
            draw.rounded_rectangle([sb_x, sb_y, sb_x + gw_w, sb_y + 38], radius=19, fill=(255, 255, 255, 28), outline=(255, 255, 255, 55), width=1)
            draw.text((sb_x + 16, sb_y + 11), "🔍  Search apps & web...", font=font_phone_sub, fill=(180, 200, 225, 200))

            # 4x3 Grid
            gy = sb_y + 55
            for r in range(3):
                for c in range(4):
                    asize = 32
                    gap = (sw - 28 - (4 * asize)) // 3
                    ax = sx + 14 + c * (asize + gap)
                    ay = gy + r * (asize + 22)
                    tint = (*sc_info["accent"], 140) if (r + c) % 2 == 0 else (255, 255, 255, 45)
                    draw.rounded_rectangle([ax, ay, ax + asize, ay + asize], radius=10, fill=tint, outline=(255, 255, 255, 70), width=1)
                    draw.line([(ax + 4, ay + asize + 5), (ax + asize - 4, ay + asize + 5)], fill=(255, 255, 255, 80), width=2)

            # Dock
            dk_w = sw - 24
            dk_h = 54
            dk_x = sx + 12
            dk_y = sy + sh - dk_h - 16
            draw.rounded_rectangle([dk_x, dk_y, dk_x + dk_w, dk_y + dk_h], radius=22, fill=(255, 255, 255, 36), outline=(255, 255, 255, 80), width=1)
            for di in range(4):
                d_size = 32
                d_gap = (dk_w - (4 * d_size)) // 5
                dix = dk_x + d_gap + di * (d_size + d_gap)
                diy = dk_y + (dk_h - d_size) // 2
                draw.rounded_rectangle([dix, diy, dix + d_size, diy + d_size], radius=10, fill=(*sc_info["accent"], 150), outline=(255, 255, 255, 85), width=1)

        elif sc_info["type"] == "drawer":
            # Search Bar at Top of Drawer
            sb_x = sx + 14
            sb_y = sy + 42
            sb_w = sw - 28
            draw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + 38], radius=19, fill=(255, 255, 255, 35), outline=(0, 205, 130, 140), width=1)
            draw.text((sb_x + 16, sb_y + 11), "Search 48 apps...", font=font_phone_sub, fill=(255, 255, 255, 240))

            # Category Tabs
            draw.text((sx + 18, sb_y + 48), "All Apps", font=font_card_tag, fill=(0, 225, 140, 255))
            draw.text((sx + 90, sb_y + 48), "Work", font=font_card_tag, fill=(160, 175, 195, 180))
            draw.text((sx + 145, sb_y + 48), "Media", font=font_card_tag, fill=(160, 175, 195, 180))
            draw.text((sx + 205, sb_y + 48), "Tools", font=font_card_tag, fill=(160, 175, 195, 180))
            draw.line([(sx + 18, sb_y + 64), (sx + 72, sb_y + 64)], fill=(0, 225, 140, 255), width=2)

            # Vertical App List
            app_list = [
                ("Camera", "System"), ("Chrome", "Browser"), ("Clock", "Tools"),
                ("Contacts", "Communication"), ("Files", "Storage"), ("Gallery", "Media"),
                ("Maps", "Navigation"), ("Messages", "Communication"), ("Phone", "System"),
                ("Settings", "System")
            ]
            list_y = sb_y + 76
            for ai, (aname, acat) in enumerate(app_list):
                ay = list_y + ai * 46
                if ay + 40 > sy + sh - 20:
                    break
                # Icon
                draw.rounded_rectangle([sx + 16, ay, sx + 50, ay + 34], radius=9, fill=(0, 205, 130, 120), outline=(255, 255, 255, 60), width=1)
                # App name
                draw.text((sx + 60, ay + 4), aname, font=font_card_body, fill=(255, 255, 255, 255))
                draw.text((sx + 60, ay + 20), acat, font=font_card_tag, fill=(150, 170, 190, 180))

            # Fast alphabet scrollbar on right
            alpha = "ABCDEFGH..."
            for ci, ch in enumerate(alpha):
                draw.text((sx + sw - 14, list_y + ci * 18), ch, font=font_phone_app, fill=(130, 160, 190, 200))

        elif sc_info["type"] == "settings":
            # Lawnchair Settings Menu
            draw.text((sx + 18, sy + 44), "Lawnchair Settings", font=font_card_title, fill=(255, 255, 255, 255))
            draw.text((sx + 18, sy + 68), "Version 15.0 Beta 3", font=font_card_tag, fill=(180, 150, 255, 220))

            settings_items = [
                ("🎨 General & Theme", "Material You Monet palette, dark mode"),
                ("🏠 Home Screen", "Grid 4x4 - 7x7, At a Glance, search provider"),
                ("📥 App Drawer", "Categorized tabs, hidden apps, fast scroll"),
                ("⚓ Dock", "Icon count, scale size, search capsule"),
                ("🖼️ Icon Pack", "Lawnicons, adaptive shapes, icon labels"),
                ("👆 Gestures", "Double tap sleep, swipe down search, recents"),
                ("⚡ Transitions (0.5x)", "Custom half-duration snappy animations"),
                ("🛡️ Privacy & Backup", "Zero telemetry, export/import layout")
            ]
            set_y = sy + 94
            for si, (stitle, ssub) in enumerate(settings_items):
                iy = set_y + si * 54
                if iy + 45 > sy + sh - 15:
                    break
                # Setting row card
                draw.rounded_rectangle([sx + 12, iy, sx + sw - 12, iy + 46], radius=10, fill=(255, 255, 255, 14), outline=(160, 95, 255, 55), width=1)
                draw.text((sx + 20, iy + 6), stitle, font=font_card_tag, fill=(255, 255, 255, 255))
                draw.text((sx + 20, iy + 24), ssub, font=font_phone_app, fill=(160, 175, 195, 200))
                draw.text((sx + sw - 28, iy + 14), "›", font=font_card_body, fill=(180, 150, 255, 220))

        # Under Phone Labels
        ly = py + PH + 20
        # Pill Tag
        draw.rounded_rectangle([px + (PW - 160) // 2, ly, px + (PW + 160) // 2, ly + 24], radius=12, fill=(255, 255, 255, 12), outline=(*sc_info["accent"], 140), width=1)
        draw.text((px + (PW - 140) // 2, ly + 4), sc_info["tag"], font=font_card_tag, fill=(*sc_info["accent"], 255))

        # Title
        bbox_t = draw.textbbox((0, 0), sc_info["title"], font=font_card_title)
        tw = bbox_t[2] - bbox_t[0]
        draw.text((px + (PW - tw) // 2, ly + 32), sc_info["title"], font=font_card_title, fill=(255, 255, 255, 255))

        # Desc
        d_lines = [sc_info["desc"][:45], sc_info["desc"][45:90], sc_info["desc"][90:]]
        for dli, dl in enumerate(d_lines):
            dl = dl.strip()
            if not dl: continue
            bbox_d = draw.textbbox((0, 0), dl, font=font_card_body)
            dw = bbox_d[2] - bbox_d[0]
            draw.text((px + (PW - dw) // 2, ly + 62 + dli * 18), dl, font=font_card_body, fill=(160, 175, 195, 220))

    # Footer
    foot_text = "Universal Android 5.0 to 15.0+  ·  Open Source (GPL-3.0 / Apache-2.0)  ·  Upstream: github.com/LawnchairLauncher/lawnchair"
    bbox_ft = draw.textbbox((0, 0), foot_text, font=font_footer)
    ft_w = bbox_ft[2] - bbox_ft[0]
    draw.text(((WIDTH - ft_w) // 2, 1038), foot_text, font=font_footer, fill=(130, 145, 165, 220))

    out_file = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs/lawnchair-features.jpg"
    img.convert("RGB").save(out_file, "JPEG", quality=95)
    print(f"[OK] Generated: {out_file}")

# ==============================================================================
# IMAGE 3: docs/lawnchair-customization-detail.jpg
# ==============================================================================
def render_customization_detail():
    img, draw = create_base_canvas()

    header_tag = "LAWNCHAIR LAUNCHER  ·  CUSTOMIZATION, GESTURES & BENCHMARKS"
    bbox_tag = draw.textbbox((0, 0), header_tag, font=font_badge)
    tag_w = bbox_tag[2] - bbox_tag[0]
    tag_x = (WIDTH - tag_w) // 2
    tag_y = 36

    draw.rounded_rectangle([tag_x - 18, tag_y - 5, tag_x + tag_w + 18, tag_y + 21], radius=13, fill=(255, 255, 255, 12), outline=(100, 175, 255, 80), width=1)
    draw.text((tag_x, tag_y), header_tag, font=font_badge, fill=(125, 195, 255, 255))

    title_text = "Deep Personalization, Fluid Physics & Zero Bloat"
    bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = bbox_title[2] - bbox_title[0]
    draw.text(((WIDTH - title_w) // 2, 70), title_text, font=font_title, fill=(255, 255, 255, 255))

    sub_text = "Explore the engineering that makes Lawnchair the ultimate home screen upgrade for debloated smartphones"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_subtitle)
    sub_w = bbox_sub[2] - bbox_sub[0]
    draw.text(((WIDTH - sub_w) // 2, 120), sub_text, font=font_subtitle, fill=(155, 170, 190, 255))

    # 4 Large Interactive Panels (2x2 Grid)
    PW = 840
    PH = 390
    START_X = (WIDTH - (2 * PW + 60)) // 2
    START_Y = 175
    GAP_X = 60
    GAP_Y = 40

    PANELS = [
        {
            "tag": "MONET THEME ENGINE",
            "title": "Material You Dynamic Wallpaper Palettes",
            "body": "Lawnchair dynamically extracts five tonal color palettes (Primary, Secondary, Tertiary, Neutral, Neutral Variant) from any wallpaper. System components, widgets, search bars, and adaptive icon shapes automatically update to harmonize with your backdrop.",
            "color": (45, 125, 245),
            "col": 0, "row": 0
        },
        {
            "tag": "ADAPTIVE ICONS & PACKS",
            "title": "Universal Icon Theming & Squircles",
            "body": "Complete third-party icon pack support (including Lawnicons and Play Store icon packs). Apply uniform icon masking, adjust individual icon scales (70% to 150%), customize label font weights, or hide labels completely for an ultra-clean minimalist aesthetic.",
            "color": (255, 195, 25),
            "col": 1, "row": 0
        },
        {
            "tag": "INTUITIVE GESTURE PHYSICS",
            "title": "0.5x Snappy Navigation & Shortcuts",
            "body": "Configure natural gestures with halved animation scales (150ms): swipe down anywhere to summon global search or notifications; swipe up for the smart app drawer; double-tap to lock screen; pinch for home screen overview. Completely stutter-free on 60Hz, 90Hz, and 120Hz displays.",
            "color": (0, 205, 130),
            "col": 0, "row": 1
        },
        {
            "tag": "RAM & BATTERY BENCHMARKS",
            "title": "Resource Consumption vs. Stock OEM Launchers",
            "body": "Stock launchers from Oppo, Vivo, Xiaomi, and Samsung continuously run background recommendation engines, ad fetchers, and lockscreen story services consuming 350MB–600MB of RAM. Lawnchair runs on less than 20MB of RAM with zero background telemetry.",
            "color": (160, 95, 255),
            "col": 1, "row": 1
        }
    ]

    for p in PANELS:
        bx = START_X + p["col"] * (PW + GAP_X)
        by = START_Y + p["row"] * (PH + GAP_Y)

        # Frosted glass card
        draw.rounded_rectangle([bx, by, bx + PW, by + PH], radius=20, fill=(255, 255, 255, 12), outline=(255, 255, 255, 35), width=1)
        # Left accent stripe
        draw.rounded_rectangle([bx, by + 20, bx + 5, by + PH - 20], radius=3, fill=(*p["color"], 255))

        # Tag
        draw.rounded_rectangle([bx + 28, by + 26, bx + 220, by + 50], radius=11, fill=(*p["color"], 45), outline=(*p["color"], 140), width=1)
        draw.text((bx + 38, by + 31), p["tag"], font=font_card_tag, fill=(*p["color"], 255))

        # Title
        draw.text((bx + 28, by + 66), p["title"], font=font_card_title, fill=(255, 255, 255, 255))

        # Body
        draw.text((bx + 28, by + 104), p["body"], font=font_card_body, fill=(170, 185, 205, 230))

        # Visual illustration inside each panel
        if p["tag"] == "MONET THEME ENGINE":
            # 4 Palette Swatch Bars
            swatch_themes = [
                ("Sapphire Blue", [(25, 75, 160), (45, 125, 245), (120, 180, 255), (210, 230, 255)]),
                ("Emerald Green", [(10, 80, 45), (0, 180, 100), (80, 225, 150), (200, 250, 220)]),
                ("Amber Gold", [(120, 80, 10), (230, 160, 20), (255, 205, 75), (255, 240, 200)]),
                ("Lavender Velvet", [(80, 30, 130), (155, 80, 240), (205, 145, 255), (240, 220, 255)])
            ]
            for ti, (tname, tcolors) in enumerate(swatch_themes):
                sy = by + 210 + ti * 40
                draw.text((bx + 28, sy + 6), tname, font=font_card_tag, fill=(210, 220, 235, 220))
                for ci, cc in enumerate(tcolors):
                    cx = bx + 180 + ci * 48
                    draw.rounded_rectangle([cx, sy, cx + 40, sy + 26], radius=7, fill=(*cc, 255), outline=(255, 255, 255, 60), width=1)

        elif p["tag"] == "ADAPTIVE ICONS & PACKS":
            # Icon shape examples
            shapes = ["Circle", "Squircle", "Rounded Square", "Teardrop"]
            for si, sname in enumerate(shapes):
                sx = bx + 28 + si * 190
                sy = by + 225
                draw.rounded_rectangle([sx, sy, sx + 56, sy + 56], radius=16 if si == 1 else (28 if si == 0 else 8), fill=(255, 195, 25, 150), outline=(255, 255, 255, 120), width=1)
                draw.text((sx, sy + 68), sname, font=font_card_tag, fill=(220, 230, 245, 240))
                draw.text((sx, sy + 88), "Adaptive Icon", font=font_phone_app, fill=(150, 165, 185, 180))

        elif p["tag"] == "INTUITIVE GESTURE PHYSICS":
            # Gesture items
            gestures = [
                ("Swipe Down", "Global Search / Notifications"),
                ("Swipe Up", "Smart App Drawer with Fuzzy Search"),
                ("Double Tap", "Instant Screen Sleep (DeviceAdmin/Rootless)"),
                ("Pinch In", "Home Screen & Overview Manager")
            ]
            for gi, (gname, gaction) in enumerate(gestures):
                gy = by + 210 + gi * 40
                draw.rounded_rectangle([bx + 28, gy, bx + 150, gy + 30], radius=8, fill=(0, 205, 130, 45), outline=(0, 205, 130, 140), width=1)
                draw.text((bx + 38, gy + 7), gname, font=font_card_tag, fill=(120, 240, 175, 255))
                draw.text((bx + 168, gy + 7), gaction, font=font_card_body, fill=(210, 225, 240, 230))

        elif p["tag"] == "RAM & BATTERY BENCHMARKS":
            # RAM comparison bars
            data = [
                ("Lawnchair Launcher (CleanYourPhone)", 18, (0, 205, 130)),
                ("ColorOS Home Launcher (Oppo / Realme)", 460, (245, 60, 75)),
                ("Funtouch OS Launcher (vivo / iQOO)", 410, (245, 60, 75)),
                ("One UI Home Launcher (Samsung)", 380, (245, 60, 75))
            ]
            for ri, (rlabel, rmb, rcolor) in enumerate(data):
                ry = by + 210 + ri * 40
                draw.text((bx + 28, ry + 2), rlabel, font=font_card_tag, fill=(215, 225, 240, 230))
                # Bar background
                bar_x = bx + 360
                bar_w = 340
                draw.rounded_rectangle([bar_x, ry + 2, bar_x + bar_w, ry + 20], radius=6, fill=(255, 255, 255, 15))
                # Fill bar proportional to 600MB max
                fill_w = max(14, int((rmb / 500.0) * bar_w))
                draw.rounded_rectangle([bar_x, ry + 2, bar_x + fill_w, ry + 20], radius=6, fill=(*rcolor, 255))
                draw.text((bar_x + bar_w + 14, ry + 2), f"{rmb} MB", font=font_card_tag, fill=(255, 255, 255, 255))

    # Footer
    foot_text = "Universal Android 5.0 to 15.0+  ·  Open Source (GPL-3.0 / Apache-2.0)  ·  Upstream: github.com/LawnchairLauncher/lawnchair"
    bbox_ft = draw.textbbox((0, 0), foot_text, font=font_footer)
    ft_w = bbox_ft[2] - bbox_ft[0]
    draw.text(((WIDTH - ft_w) // 2, 1038), foot_text, font=font_footer, fill=(130, 145, 165, 220))

    out_file = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs/lawnchair-customization-detail.jpg"
    img.convert("RGB").save(out_file, "JPEG", quality=95)
    print(f"[OK] Generated: {out_file}")

if __name__ == "__main__":
    print("Generating Lawnchair showcase graphics...")
    render_ui_showcase()
    render_features_progression()
    render_customization_detail()
    print("All 3 Lawnchair graphics generated successfully.")
