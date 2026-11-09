#!/usr/bin/env python3
"""
CleanYourPhone - Professional Multi-Brand Lineup Banner Generator
Renders an ultra-clean, minimal, 1920x1080 studio graphic representing
all 15 supported smartphone brands and their operating systems.
"""

import os
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1920
HEIGHT = 1080

# Create base canvas with deep obsidian slate gradient
img = Image.new("RGBA", (WIDTH, HEIGHT), (11, 14, 20, 255))
draw = ImageDraw.Draw(img)

# Smooth vertical background gradient
for y in range(HEIGHT):
    factor = y / float(HEIGHT)
    r = int(9 + factor * 8)
    g = int(12 + factor * 9)
    b = int(18 + factor * 14)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

# Font loaders
FONT_DIR = "C:/Windows/Fonts"
font_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 40)
font_subtitle = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 18)
font_section = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 13)
font_badge = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 12)
font_brand = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 20)
font_os = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 13)
font_status = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 11)
font_clock = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 18)
font_date = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 9)
font_pill_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 14)
font_pill_sub = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 11)
font_footer = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 12)

# --- HEADER SECTION ---
header_tag = "UNIVERSAL OEM ARCHITECTURE  ·  15 BRANDS SUPPORTED"
bbox_tag = draw.textbbox((0, 0), header_tag, font=font_badge)
tag_w = bbox_tag[2] - bbox_tag[0]
tag_x = (WIDTH - tag_w) // 2
tag_y = 36

# Pill outline for header tag
draw.rounded_rectangle([tag_x - 16, tag_y - 4, tag_x + tag_w + 16, tag_y + 20], radius=12, fill=(255, 255, 255, 12), outline=(120, 180, 255, 75), width=1)
draw.text((tag_x, tag_y), header_tag, font=font_badge, fill=(130, 195, 255, 255))

title_text = "Supported Brands & Operating Systems"
bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
title_w = bbox_title[2] - bbox_title[0]
draw.text(((WIDTH - title_w) // 2, 68), title_text, font=font_title, fill=(255, 255, 255, 255))

sub_text = "Verified zero-root debloating, background telemetry removal, and Lawnchair Launcher across 15 smartphone ecosystems"
bbox_sub = draw.textbbox((0, 0), sub_text, font=font_subtitle)
sub_w = bbox_sub[2] - bbox_sub[0]
draw.text(((WIDTH - sub_w) // 2, 118), sub_text, font=font_subtitle, fill=(155, 170, 190, 255))

# --- 6 HERO SMARTPHONES (Representative Ecosystems) ---
HERO_PHONES = [
    {
        "name": "Samsung",
        "os": "One UI 1.0 – 7.0+",
        "accent": (45, 125, 245),
        "bg_top": (10, 28, 55),
        "bg_bot": (6, 15, 30)
    },
    {
        "name": "POCO / Xiaomi",
        "os": "HyperOS & MIUI",
        "accent": (255, 200, 20),
        "bg_top": (45, 36, 12),
        "bg_bot": (22, 18, 6)
    },
    {
        "name": "OnePlus",
        "os": "OxygenOS 5 – 15",
        "accent": (245, 50, 65),
        "bg_top": (48, 16, 22),
        "bg_bot": (24, 8, 12)
    },
    {
        "name": "Motorola",
        "os": "Hello UI / My UX",
        "accent": (0, 195, 245),
        "bg_top": (8, 38, 50),
        "bg_bot": (4, 18, 26)
    },
    {
        "name": "Infinix / Tecno",
        "os": "XOS & HiOS 14",
        "accent": (0, 210, 125),
        "bg_top": (10, 42, 28),
        "bg_bot": (5, 20, 14)
    },
    {
        "name": "Sony",
        "os": "Xperia UI",
        "accent": (165, 100, 255),
        "bg_top": (35, 20, 55),
        "bg_bot": (18, 10, 28)
    }
]

PHONE_W = 215
PHONE_H = 425
CORNER = 28
START_Y = 168
TOTAL_PHONES_W = len(HERO_PHONES) * PHONE_W
SPACING = (WIDTH - 160 - TOTAL_PHONES_W) // (len(HERO_PHONES) - 1)
START_X = 80

for i, b in enumerate(HERO_PHONES):
    px = START_X + i * (PHONE_W + SPACING)
    py = START_Y

    # Soft ambient glow behind chassis
    glow_color = (*b["accent"], 26)
    draw.rounded_rectangle([px - 4, py - 4, px + PHONE_W + 4, py + PHONE_H + 4], radius=CORNER + 4, fill=glow_color)

    # Phone chassis outer border (aluminum/titanium frame)
    draw.rounded_rectangle([px, py, px + PHONE_W, py + PHONE_H], radius=CORNER, fill=(26, 30, 38, 255), outline=(70, 80, 95, 255), width=2)

    # Phone screen bezel
    BEZEL = 6
    sx = px + BEZEL
    sy = py + BEZEL
    sw = PHONE_W - (BEZEL * 2)
    sh = PHONE_H - (BEZEL * 2)
    sc = CORNER - 6

    # Draw screen wallpaper gradient
    screen_img = Image.new("RGBA", (sw, sh), (*b["bg_bot"], 255))
    sdraw = ImageDraw.Draw(screen_img)
    for yline in range(sh):
        factor = yline / float(sh)
        sr = int(b["bg_top"][0] * (1 - factor) + b["bg_bot"][0] * factor)
        sg = int(b["bg_top"][1] * (1 - factor) + b["bg_bot"][1] * factor)
        sb = int(b["bg_top"][2] * (1 - factor) + b["bg_bot"][2] * factor)
        sdraw.line([(0, yline), (sw, yline)], fill=(sr, sg, sb, 255))

    # Mask screen to rounded rect
    mask = Image.new("L", (sw, sh), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, sw, sh], radius=sc, fill=255)
    img.paste(screen_img, (sx, sy), mask)

    # Re-draw screen border
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=sc, outline=(255, 255, 255, 25), width=1)

    # Centered punch-hole selfie camera
    cam_x = px + (PHONE_W // 2)
    cam_y = sy + 12
    draw.ellipse([cam_x - 4, cam_y - 4, cam_x + 4, cam_y + 4], fill=(8, 10, 14, 255), outline=(40, 45, 55, 255), width=1)

    # Screen UI: Lawnchair "At a Glance" Card
    gw_w = sw - 24
    gw_h = 54
    gw_x = sx + 12
    gw_y = sy + 32
    draw.rounded_rectangle([gw_x, gw_y, gw_x + gw_w, gw_y + gw_h], radius=14, fill=(255, 255, 255, 24), outline=(255, 255, 255, 60), width=1)
    draw.text((gw_x + 14, gw_y + 8), "10:48", font=font_clock, fill=(255, 255, 255, 255))
    draw.text((gw_x + 14, gw_y + 32), "Thursday, Nov 9 · 24°C", font=font_date, fill=(200, 215, 230, 220))

    # Clean small status pill in widget
    draw.rounded_rectangle([gw_x + gw_w - 52, gw_y + 16, gw_x + gw_w - 10, gw_y + 36], radius=9, fill=(*b["accent"], 60), outline=(*b["accent"], 180), width=1)
    draw.text((gw_x + gw_w - 45, gw_y + 20), "SAFE", font=font_status, fill=(255, 255, 255, 255))

    # Frosted Search Capsule Pill (Lawnchair style)
    sb_w = sw - 24
    sb_h = 30
    sb_x = sx + 12
    sb_y = gw_y + gw_h + 14
    draw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=15, fill=(255, 255, 255, 20), outline=(255, 255, 255, 50), width=1)
    draw.text((sb_x + 14, sb_y + 8), "Search apps & web...", font=font_date, fill=(160, 175, 195, 180))

    # Clean 4x3 App Grid Dots/Squircles (Material You Clean Style)
    grid_y_start = sb_y + sb_h + 20
    for row in range(3):
        for col in range(4):
            app_size = 26
            gap_x = (sw - 24 - (4 * app_size)) // 3
            ax = sx + 12 + col * (app_size + gap_x)
            ay = grid_y_start + row * (app_size + 20)
            tint = (*b["accent"], 85) if (row + col) % 3 == 0 else (255, 255, 255, 35)
            draw.rounded_rectangle([ax, ay, ax + app_size, ay + app_size], radius=8, fill=tint, outline=(255, 255, 255, 50), width=1)
            draw.line([(ax + 4, ay + app_size + 5), (ax + app_size - 4, ay + app_size + 5)], fill=(255, 255, 255, 80), width=2)

    # Floating Lawnchair Dock Pill at Bottom
    dock_w = sw - 20
    dock_h = 46
    dock_x = sx + 10
    dock_y = sy + sh - dock_h - 12
    draw.rounded_rectangle([dock_x, dock_y, dock_x + dock_w, dock_y + dock_h], radius=18, fill=(255, 255, 255, 36), outline=(255, 255, 255, 85), width=1)
    d_icon_size = 26
    d_gap = (dock_w - (4 * d_icon_size)) // 5
    for di in range(4):
        dix = dock_x + d_gap + di * (d_icon_size + d_gap)
        diy = dock_y + (dock_h - d_icon_size) // 2
        d_tint = (*b["accent"], 125) if di == 0 else (255, 255, 255, 55)
        draw.rounded_rectangle([dix, diy, dix + d_icon_size, diy + d_icon_size], radius=8, fill=d_tint, outline=(255, 255, 255, 75), width=1)

    # --- BELOW PHONE LABELS & BRANDING ---
    label_y = py + PHONE_H + 18

    # Brand Name (Bold, large, pristine)
    bbox_b = draw.textbbox((0, 0), b["name"], font=font_brand)
    bw = bbox_b[2] - bbox_b[0]
    bx = px + (PHONE_W - bw) // 2
    draw.text((bx, label_y), b["name"], font=font_brand, fill=(255, 255, 255, 255))

    # OS Badge Pill
    bbox_os = draw.textbbox((0, 0), b["os"], font=font_os)
    osw = bbox_os[2] - bbox_os[0]
    osx = px + (PHONE_W - osw) // 2
    osy = label_y + 30

    draw.rounded_rectangle([osx - 10, osy - 3, osx + osw + 10, osy + 20], radius=10, fill=(255, 255, 255, 14), outline=(*b["accent"], 120), width=1)
    draw.text((osx, osy), b["os"], font=font_os, fill=(210, 222, 238, 255))

    # Safe status indicator with colored dot
    stat_text = "Verified Safe"
    bbox_st = draw.textbbox((0, 0), stat_text, font=font_status)
    stw = bbox_st[2] - bbox_st[0]
    stx = px + (PHONE_W - stw) // 2 + 5
    sty = osy + 28

    dot_x = stx - 9
    dot_y = sty + 6
    draw.ellipse([dot_x - 3, dot_y - 3, dot_x + 3, dot_y + 3], fill=(*b["accent"], 255))
    draw.text((stx, sty), stat_text, font=font_status, fill=(160, 175, 195, 220))

# --- ALL 15 SUPPORTED BRANDS MATRIX (Bottom Grid) ---
sec_y = START_Y + PHONE_H + 115
sec_title = "COMPREHENSIVE 15-BRAND DEBLOAT MATRIX"
bbox_sec = draw.textbbox((0, 0), sec_title, font=font_section)
sec_w = bbox_sec[2] - bbox_sec[0]
draw.text(((WIDTH - sec_w) // 2, sec_y), sec_title, font=font_section, fill=(120, 170, 240, 240))

ALL_15_BRANDS = [
    # Row 1
    {"name": "Samsung", "os": "One UI 1.0–7.0+", "color": (45, 125, 245)},
    {"name": "POCO", "os": "MIUI & HyperOS", "color": (255, 200, 20)},
    {"name": "Infinix", "os": "XOS v3–v14+", "color": (0, 210, 125)},
    {"name": "Tecno", "os": "HiOS v3–v14+", "color": (0, 195, 160)},
    {"name": "itel", "os": "itelOS (Go/Full)", "color": (255, 60, 80)},

    # Row 2
    {"name": "Motorola", "os": "Hello UI / My UX", "color": (0, 195, 245)},
    {"name": "Sony", "os": "Xperia UI (1/5/10)", "color": (165, 100, 255)},
    {"name": "Lava", "os": "Star OS / Agni", "color": (240, 70, 45)},
    {"name": "Karbonn", "os": "Karbonn Platform", "color": (255, 145, 30)},
    {"name": "Philips", "os": "Philips Android", "color": (15, 135, 240)},

    # Row 3
    {"name": "OPPO", "os": "ColorOS 5–15", "color": (0, 190, 115)},
    {"name": "vivo", "os": "Funtouch / OriginOS", "color": (65, 115, 255)},
    {"name": "OnePlus", "os": "OxygenOS 5–15", "color": (245, 50, 65)},
    {"name": "realme", "os": "Realme UI 1.0–6.0", "color": (255, 185, 25)},
    {"name": "iQOO", "os": "Monster / OriginOS", "color": (255, 115, 20)},
]

PILL_W = 328
PILL_H = 40
PILL_START_Y = sec_y + 24
COLS = 5
GAP_X = 20
GAP_Y = 10
TOTAL_GRID_W = (COLS * PILL_W) + ((COLS - 1) * GAP_X)
GRID_START_X = (WIDTH - TOTAL_GRID_W) // 2

for idx, b in enumerate(ALL_15_BRANDS):
    row = idx // COLS
    col = idx % COLS
    bx = GRID_START_X + col * (PILL_W + GAP_X)
    by = PILL_START_Y + row * (PILL_H + GAP_Y)

    # Frosted pill background
    draw.rounded_rectangle([bx, by, bx + PILL_W, by + PILL_H], radius=10, fill=(255, 255, 255, 10), outline=(255, 255, 255, 28), width=1)

    # Colored indicator dot
    dot_cx = bx + 18
    dot_cy = by + (PILL_H // 2)
    draw.ellipse([dot_cx - 4, dot_cy - 4, dot_cx + 4, dot_cy + 4], fill=(*b["color"], 255))

    # Brand text
    draw.text((bx + 30, by + 10), b["name"], font=font_pill_title, fill=(255, 255, 255, 255))

    # OS Subtitle
    draw.text((bx + 115, by + 13), b["os"], font=font_pill_sub, fill=(155, 170, 190, 240))

    # Green checkmark badge
    draw.text((bx + PILL_W - 54, by + 13), "✓ SAFE", font=font_status, fill=(*b["color"], 255))

# --- FOOTER BANNER ---
foot_text = "Universal Android 5.0 to 15.0+ Support  ·  No Root Required  ·  100% User 0 Safe  ·  One-Command Instant Restore"
bbox_ft = draw.textbbox((0, 0), foot_text, font=font_footer)
ft_w = bbox_ft[2] - bbox_ft[0]
ft_x = (WIDTH - ft_w) // 2
ft_y = 1040
draw.text((ft_x, ft_y), foot_text, font=font_footer, fill=(130, 145, 165, 220))

# Save output to docs/brands-lineup.jpg
output_path = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs/brands-lineup.jpg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
img.convert("RGB").save(output_path, "JPEG", quality=95)
print(f"Generated updated brands lineup banner: {output_path}")
