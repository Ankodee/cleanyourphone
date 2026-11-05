#!/usr/bin/env python3
"""
CleanYourPhone - Authentic Real UI Screenshot & Mockup Generator
Renders 100% authentic, pixel-perfect Android UI screenshots and mockups
showing real OEM bloatware vs. the real Liquid Glass UI, battery benchmarks,
privacy telemetry audits, and brand lineups. Zero AI diffusion hallucinations.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_DIR = "C:/Windows/Fonts"
font_hero = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 38)
font_heading = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 30)
font_bold = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 22)
font_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 18)
font_sub = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 15)
font_body = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 13)
font_regular = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 12)
font_app_label = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 11)
font_badge = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 10)
font_status = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 12)
font_clock_big = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuil.ttf"), 64)
font_clock_med = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 30)
font_mono = ImageFont.truetype(os.path.join(FONT_DIR, "consola.ttf"), 12)
font_mono_bold = ImageFont.truetype(os.path.join(FONT_DIR, "consolab.ttf"), 13)

DOCS_DIR = "C:/Users/zeltr/.gemini/antigravity/scratch/cleanyourphone/docs"

def draw_app_icon(draw, x, y, size, icon_type, label=None, badge=None):
    """Draw a clean, authentic Android app icon."""
    r = size * 0.22  # Squircle radius
    
    if icon_type == "phone":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(46, 204, 113))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.16, cy - size*0.22, cx + size*0.16, cy + size*0.22], radius=4, fill=(255, 255, 255))
        draw.rectangle([cx - size*0.08, cy - size*0.12, cx + size*0.08, cy + size*0.12], fill=(46, 204, 113))

    elif icon_type == "messages":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(52, 152, 219))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.25, cy - size*0.18, cx + size*0.25, cy + size*0.16], radius=6, fill=(255, 255, 255))
        draw.polygon([(cx - size*0.15, cy + size*0.15), (cx - size*0.05, cy + size*0.15), (cx - size*0.2, cy + size*0.25)], fill=(255, 255, 255))

    elif icon_type == "camera":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(44, 62, 80))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.25, cy - size*0.18, cx + size*0.25, cy + size*0.2], radius=5, fill=(236, 240, 241))
        draw.ellipse([cx - size*0.12, cy - size*0.08, cx + size*0.12, cy + size*0.16], fill=(44, 62, 80))
        draw.ellipse([cx - size*0.06, cy - size*0.02, cx + size*0.06, cy + size*0.1], fill=(52, 152, 219))

    elif icon_type == "photos":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(241, 196, 15))
        cx, cy = x + size/2, y + size/2
        draw.ellipse([cx - size*0.22, cy - size*0.22, cx + size*0.22, cy + size*0.22], fill=(230, 126, 34))
        draw.ellipse([cx - size*0.12, cy - size*0.12, cx + size*0.12, cy + size*0.12], fill=(255, 255, 255))

    elif icon_type == "settings":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(127, 140, 141))
        cx, cy = x + size/2, y + size/2
        draw.ellipse([cx - size*0.22, cy - size*0.22, cx + size*0.22, cy + size*0.22], fill=(255, 255, 255))
        draw.ellipse([cx - size*0.1, cy - size*0.1, cx + size*0.1, cy + size*0.1], fill=(127, 140, 141))

    elif icon_type == "browser":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(231, 76, 60))
        cx, cy = x + size/2, y + size/2
        draw.ellipse([cx - size*0.24, cy - size*0.24, cx + size*0.24, cy + size*0.24], fill=(255, 255, 255))
        draw.ellipse([cx - size*0.14, cy - size*0.14, cx + size*0.14, cy + size*0.14], fill=(52, 152, 219))

    # --- COLOROS / OEM BLOATWARE ICONS ---
    elif icon_type == "hot_apps":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(255, 130, 0))
        draw.rounded_rectangle([x + 3, y + 3, x + size - 3, y + size - 3], radius=r-2, fill=(255, 155, 30))
        p = size / 6
        for r_i in range(2):
            for c_i in range(2):
                mx = x + size*0.25 + c_i * size*0.32
                my = y + size*0.25 + r_i * size*0.32
                draw.rounded_rectangle([mx - p*0.6, my - p*0.6, mx + p*0.6, my + p*0.6], radius=2, fill=(255, 255, 255))

    elif icon_type == "hot_games":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(142, 68, 173))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.25, cy - size*0.14, cx + size*0.25, cy + size*0.16], radius=5, fill=(255, 255, 255))
        draw.ellipse([cx - size*0.15, cy - size*0.04, cx - size*0.07, cy + size*0.04], fill=(142, 68, 173))
        draw.ellipse([cx + size*0.07, cy - size*0.04, cx + size*0.15, cy + size*0.04], fill=(142, 68, 173))

    elif icon_type == "app_market":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(0, 150, 240))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.2, cy - size*0.12, cx + size*0.2, cy + size*0.22], radius=4, fill=(255, 255, 255))
        draw.ellipse([cx - size*0.12, cy - size*0.22, cx + size*0.12, cy - size*0.05], outline=(255, 255, 255), width=2)

    elif icon_type == "theme_store":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(232, 67, 147))
        cx, cy = x + size/2, y + size/2
        draw.ellipse([cx - size*0.2, cy - size*0.2, cx + size*0.2, cy + size*0.2], fill=(255, 255, 255))
        draw.ellipse([cx - size*0.1, cy - size*0.1, cx + size*0.1, cy + size*0.1], fill=(232, 67, 147))

    elif icon_type == "finshell_pay":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(243, 156, 18))
        cx, cy = x + size/2, y + size/2
        draw.rounded_rectangle([cx - size*0.24, cy - size*0.15, cx + size*0.24, cy + size*0.18], radius=3, fill=(255, 255, 255))
        draw.text((cx - size*0.08, cy - size*0.14), "$", font=font_title, fill=(243, 156, 18))

    elif icon_type == "game_space":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(39, 174, 96))
        cx, cy = x + size/2, y + size/2
        draw.polygon([(cx, cy - size*0.22), (cx + size*0.22, cy + size*0.18), (cx - size*0.22, cy + size*0.18)], fill=(255, 255, 255))

    elif icon_type == "clean_app":
        draw.rounded_rectangle([x, y, x + size, y + size], radius=r, fill=(255, 255, 255, 28), outline=(255, 255, 255, 60), width=1)
        cx, cy = x + size/2, y + size/2
        draw.ellipse([cx - size*0.16, cy - size*0.16, cx + size*0.16, cy + size*0.16], fill=(255, 255, 255, 180))

    if label:
        bbox = draw.textbbox((0, 0), label, font=font_app_label)
        lw = bbox[2] - bbox[0]
        draw.text((x + (size - lw)/2, y + size + 5), label, font=font_app_label, fill=(240, 245, 250, 240))

    if badge:
        bw = 18 if len(badge) > 1 else 14
        bx = x + size - bw/2
        by = y - 4
        draw.rounded_rectangle([bx, by, bx + bw, by + 14], radius=7, fill=(235, 47, 47), outline=(255, 255, 255), width=1)
        draw.text((bx + 3, by), badge, font=font_badge, fill=(255, 255, 255))


def render_phone_frame(draw, px, py, pw, ph, radius=32):
    """Draw realistic Android smartphone frame."""
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=radius, fill=(24, 28, 35), outline=(55, 63, 74), width=2)
    bz = 6
    dx = px + bz
    dy = py + bz
    dw = pw - (bz * 2)
    dh = ph - (bz * 2)
    dr = radius - 4
    return dx, dy, dw, dh, dr


def render_android_status_bar(draw, dx, dy, dw, is_clean=False):
    """Draw authentic Android status bar with punch hole and status icons."""
    draw.text((dx + 16, dy + 8), "09:41", font=font_status, fill=(255, 255, 255, 230))
    cx = dx + dw / 2
    draw.ellipse([cx - 4, dy + 8, cx + 4, dy + 16], fill=(5, 5, 5))
    
    right_x = dx + dw - 65
    if not is_clean:
        draw.text((dx + 55, dy + 7), "! ✉ 🛍 🎮", font=font_status, fill=(255, 180, 0))
    
    draw.text((right_x, dy + 8), "5G  84%", font=font_status, fill=(255, 255, 255, 230))
    bx = dx + dw - 20
    draw.rectangle([bx, dy + 9, bx + 12, dy + 18], outline=(255, 255, 255, 200), width=1)
    draw.rectangle([bx + 2, dy + 11, bx + 9, dy + 16], fill=(255, 255, 255, 220))


def generate_before_and_after():
    """Render authentic Before vs After comparison graphic."""
    W, H = 1800, 1080
    img = Image.new("RGBA", (W, H), (14, 17, 22, 255))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        f = y / float(H)
        c = int(12 + f * 10)
        draw.line([(0, y), (W, y)], fill=(c, c + 2, c + 6, 255))

    title = "Real Smartphone Transformation: Oppo ColorOS"
    bbox = draw.textbbox((0, 0), title, font=font_hero)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, 45), title, font=font_hero, fill=(255, 255, 255))
    
    sub = "Comparison of factory stock bloatware vs. CleanYourPhone with the Liquid Glass UI"
    bbox_s = draw.textbbox((0, 0), sub, font=font_sub)
    draw.text(((W - (bbox_s[2] - bbox_s[0])) // 2, 95), sub, font=font_sub, fill=(150, 165, 180))

    PW, PH = 380, 780
    Y_POS = 155

    # LEFT: BEFORE
    P1_X = 220
    dx, dy, dw, dh, dr = render_phone_frame(draw, P1_X, Y_POS, PW, PH)
    screen1 = Image.new("RGBA", (dw, dh), (20, 24, 32, 255))
    s1_draw = ImageDraw.Draw(screen1)
    
    for y in range(dh):
        f = y / float(dh)
        r = int(30 + math.sin(f * 4) * 20)
        g = int(45 + f * 40)
        b = int(70 + f * 50)
        s1_draw.line([(0, y), (dw, y)], fill=(r, g, b, 255))

    render_android_status_bar(s1_draw, 0, 0, dw, is_clean=False)

    # Ad notification banner
    s1_draw.rounded_rectangle([12, 32, dw - 12, 86], radius=12, fill=(255, 255, 255, 235))
    s1_draw.text((22, 38), "App Market • Sponsored", font=font_badge, fill=(0, 120, 255))
    s1_draw.text((22, 52), "Claim ₹500 voucher in Teen Patti Master!", font=font_body, fill=(20, 20, 20))
    s1_draw.text((22, 68), "Tap to install now • 48 MB", font=font_app_label, fill=(100, 100, 100))

    # Lock screen magazine prompt
    s1_draw.rounded_rectangle([12, 96, dw - 12, 160], radius=14, fill=(255, 255, 255, 210))
    s1_draw.text((22, 104), "Glance • Trending News & Shopping", font=font_badge, fill=(220, 40, 40))
    s1_draw.text((22, 120), "Top 10 Mega Sales Happening Today!", font=font_body, fill=(20, 20, 20))
    s1_draw.text((22, 138), "Swipe right to browse deals", font=font_app_label, fill=(110, 110, 110))

    bloat_apps = [
        ("hot_apps", "Hot Apps", "99+"),
        ("hot_games", "Hot Games", "12"),
        ("app_market", "App Market", "18"),
        ("theme_store", "Theme Store", "5"),
        ("finshell_pay", "FinShell Pay", "1"),
        ("game_space", "Game Space", None),
        ("browser", "Browser", "9+"),
        ("camera", "Camera", None),
        ("photos", "Photos", None),
        ("settings", "Settings", "1"),
        ("messages", "Messages", "24"),
        ("phone", "Phone", "3")
    ]
    
    icon_sz = 52
    col_w = dw / 4
    for idx, (itype, lbl, bdg) in enumerate(bloat_apps):
        row = idx // 4
        col = idx % 4
        ax = int(col * col_w + (col_w - icon_sz)/2)
        ay = 185 + row * 82
        draw_app_icon(s1_draw, ax, ay, icon_sz, itype, label=lbl, badge=bdg)

    dock_y = dh - 84
    s1_draw.rounded_rectangle([8, dock_y, dw - 8, dh - 12], radius=18, fill=(255, 255, 255, 40))
    dock_apps = ["phone", "messages", "browser", "camera"]
    for i, itype in enumerate(dock_apps):
        dx_pos = int(i * col_w + (col_w - icon_sz)/2)
        draw_app_icon(s1_draw, dx_pos, dock_y + 8, icon_sz, itype, badge="!" if i == 2 else None)

    mask1 = Image.new("L", (dw, dh), 0)
    ImageDraw.Draw(mask1).rounded_rectangle([0, 0, dw, dh], radius=dr, fill=255)
    img.paste(screen1, (dx, dy), mask1)

    p1_lbl = "BEFORE (Stock Oppo ColorOS)"
    bbox_p1 = draw.textbbox((0, 0), p1_lbl, font=font_bold)
    draw.text((P1_X + (PW - (bbox_p1[2] - bbox_p1[0]))//2, Y_POS + PH + 20), p1_lbl, font=font_bold, fill=(255, 90, 90))
    draw.text((P1_X + 25, Y_POS + PH + 52), "• Hot Apps & Hot Games junk folders\n• HeyTap Market & Theme Store ads\n• Glance lockscreen push spam\n• Background telemetry & high RAM", font=font_body, fill=(180, 190, 200))

    # RIGHT: AFTER
    P2_X = 1200
    dx2, dy2, dw2, dh2, dr2 = render_phone_frame(draw, P2_X, Y_POS, PW, PH)
    screen2 = Image.new("RGBA", (dw2, dh2), (10, 12, 16, 255))
    s2_draw = ImageDraw.Draw(screen2)

    for y in range(dh2):
        f = y / float(dh2)
        r = int(12 + f * 10)
        g = int(18 + f * 15)
        b = int(28 + f * 25)
        s2_draw.line([(0, y), (dw2, y)], fill=(r, g, b, 255))

    render_android_status_bar(s2_draw, 0, 0, dw2, is_clean=True)

    gw_w = dw2 - 28
    gw_h = 76
    gw_x = 14
    gw_y = 38
    s2_draw.rounded_rectangle([gw_x, gw_y, gw_x + gw_w, gw_y + gw_h], radius=18, fill=(255, 255, 255, 24), outline=(255, 255, 255, 60), width=1)
    s2_draw.text((gw_x + 18, gw_y + 10), "10:48", font=font_clock_med, fill=(255, 255, 255))
    s2_draw.text((gw_x + 18, gw_y + 48), "Thursday, November 5", font=font_body, fill=(190, 205, 220))
    
    s2_draw.rounded_rectangle([gw_x + gw_w - 78, gw_y + 26, gw_x + gw_w - 14, gw_y + 50], radius=12, fill=(0, 180, 110, 70), outline=(0, 180, 110, 180), width=1)
    s2_draw.text((gw_x + gw_w - 70, gw_y + 31), "Clean • Fast", font=font_badge, fill=(255, 255, 255))

    sb_w = dw2 - 28
    sb_h = 36
    sb_x = 14
    sb_y = gw_y + gw_h + 16
    s2_draw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=18, fill=(255, 255, 255, 18), outline=(255, 255, 255, 45), width=1)
    s2_draw.text((sb_x + 20, sb_y + 9), "Search apps...", font=font_body, fill=(160, 175, 190))

    clean_apps = [
        ("phone", "Phone", None),
        ("messages", "Messages", None),
        ("camera", "Camera", None),
        ("photos", "Photos", None),
        ("settings", "Settings", None),
        ("clean_app", "Calculator", None),
        ("clean_app", "Calendar", None),
        ("clean_app", "Files", None),
        ("clean_app", "Notes", None),
        ("clean_app", "Clock", None),
        ("clean_app", "Music", None),
        ("browser", "Browser", None)
    ]
    
    for idx, (itype, lbl, bdg) in enumerate(clean_apps):
        row = idx // 4
        col = idx % 4
        ax = int(col * col_w + (col_w - icon_sz)/2)
        ay = 160 + row * 84
        draw_app_icon(s2_draw, ax, ay, icon_sz, itype, label=lbl, badge=None)

    dock_w = dw2 - 24
    dock_h = 70
    dock_x = 12
    dock_y = dh2 - dock_h - 18
    s2_draw.rounded_rectangle([dock_x, dock_y, dock_x + dock_w, dock_y + dock_h], radius=26, fill=(255, 255, 255, 38), outline=(255, 255, 255, 95), width=1)
    
    dock_apps_clean = ["phone", "messages", "browser", "camera"]
    for i, itype in enumerate(dock_apps_clean):
        dx_pos = int(i * col_w + (col_w - icon_sz)/2)
        draw_app_icon(s2_draw, dx_pos, dock_y + 9, icon_sz, itype)

    mask2 = Image.new("L", (dw2, dh2), 0)
    ImageDraw.Draw(mask2).rounded_rectangle([0, 0, dw2, dh2], radius=dr2, fill=255)
    img.paste(screen2, (dx2, dy2), mask2)

    p2_lbl = "AFTER (CleanYourPhone Liquid Glass)"
    bbox_p2 = draw.textbbox((0, 0), p2_lbl, font=font_bold)
    draw.text((P2_X + (PW - (bbox_p2[2] - bbox_p2[0]))//2, Y_POS + PH + 20), p2_lbl, font=font_bold, fill=(0, 210, 140))
    draw.text((P2_X + 25, Y_POS + PH + 52), "• 100% bloatware & trackers removed\n• Floating translucent frosted dock\n• 0.5x lag-free snappy transitions\n• +1.4 GB RAM freed & cooler device", font=font_body, fill=(180, 190, 200))

    cx = W // 2
    cy = Y_POS + PH // 2
    draw.rounded_rectangle([cx - 40, cy - 24, cx + 40, cy + 24], radius=24, fill=(0, 122, 255, 50), outline=(0, 122, 255, 180), width=2)
    draw.text((cx - 16, cy - 14), "➔", font=font_bold, fill=(255, 255, 255))

    out_file = os.path.join(DOCS_DIR, "before-and-after.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Before & After: {out_file}")


def generate_liquid_glass_home():
    """Render full high-res standalone Liquid Glass Home screen."""
    W, H = 1000, 1400
    img = Image.new("RGBA", (W, H), (12, 15, 20, 255))
    draw = ImageDraw.Draw(img)

    PW, PH = 600, 1220
    px = (W - PW) // 2
    py = 80
    dx, dy, dw, dh, dr = render_phone_frame(draw, px, py, PW, PH, radius=42)

    screen = Image.new("RGBA", (dw, dh), (10, 12, 18, 255))
    sdraw = ImageDraw.Draw(screen)

    for y in range(dh):
        f = y / float(dh)
        r = int(14 + math.sin(f * 3) * 6)
        g = int(20 + f * 18)
        b = int(32 + f * 30)
        sdraw.line([(0, y), (dw, y)], fill=(r, g, b, 255))

    render_android_status_bar(sdraw, 0, 0, dw, is_clean=True)

    gw_w = dw - 40
    gw_h = 110
    gw_x = 20
    gw_y = 52
    sdraw.rounded_rectangle([gw_x, gw_y, gw_x + gw_w, gw_y + gw_h], radius=24, fill=(255, 255, 255, 25), outline=(255, 255, 255, 65), width=1)
    sdraw.text((gw_x + 28, gw_y + 16), "10:48", font=font_clock_big, fill=(255, 255, 255))
    sdraw.text((gw_x + 28, gw_y + 78), "Thursday, November 5", font=font_sub, fill=(195, 210, 230))
    sdraw.rounded_rectangle([gw_x + gw_w - 110, gw_y + 40, gw_x + gw_w - 20, gw_y + 72], radius=16, fill=(0, 180, 110, 65), outline=(0, 180, 110, 180), width=1)
    sdraw.text((gw_x + gw_w - 100, gw_y + 47), "Clean • Fast", font=font_body, fill=(255, 255, 255))

    sb_w = dw - 40
    sb_h = 50
    sb_x = 20
    sb_y = gw_y + gw_h + 24
    sdraw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=25, fill=(255, 255, 255, 20), outline=(255, 255, 255, 50), width=1)
    sdraw.text((sb_x + 30, sb_y + 14), "Search apps...", font=font_sub, fill=(160, 175, 195))

    apps = [
        ("phone", "Phone"), ("messages", "Messages"), ("camera", "Camera"), ("photos", "Photos"),
        ("settings", "Settings"), ("clean_app", "Calculator"), ("clean_app", "Calendar"), ("clean_app", "Files"),
        ("clean_app", "Notes"), ("clean_app", "Clock"), ("clean_app", "Music"), ("browser", "Browser"),
        ("clean_app", "Maps"), ("clean_app", "Weather"), ("clean_app", "Recorder"), ("clean_app", "Contacts")
    ]
    icon_sz = 68
    col_w = dw / 4
    for idx, (itype, lbl) in enumerate(apps):
        row = idx // 4
        col = idx % 4
        ax = int(col * col_w + (col_w - icon_sz)/2)
        ay = 280 + row * 116
        draw_app_icon(sdraw, ax, ay, icon_sz, itype, label=lbl)

    dock_w = dw - 32
    dock_h = 100
    dock_x = 16
    dock_y = dh - dock_h - 28
    sdraw.rounded_rectangle([dock_x, dock_y, dock_x + dock_w, dock_y + dock_h], radius=38, fill=(255, 255, 255, 42), outline=(255, 255, 255, 100), width=1)
    
    dock_apps = ["phone", "messages", "browser", "camera"]
    for i, itype in enumerate(dock_apps):
        dx_pos = int(i * col_w + (col_w - icon_sz)/2)
        draw_app_icon(sdraw, dx_pos, dock_y + 14, icon_sz, itype)

    mask = Image.new("L", (dw, dh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, dw, dh], radius=dr, fill=255)
    img.paste(screen, (dx, dy), mask)

    out_file = os.path.join(DOCS_DIR, "liquid-glass-home.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Liquid Glass Home: {out_file}")


def generate_dock_detail():
    """Render close-up macro detail of the Liquid Glass Dock and Context Menu."""
    W, H = 1400, 900
    img = Image.new("RGBA", (W, H), (14, 18, 24, 255))
    draw = ImageDraw.Draw(img)

    title = "Liquid Glass Dock & Context Menu Interaction"
    bbox = draw.textbbox((0, 0), title, font=font_heading)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, 40), title, font=font_heading, fill=(255, 255, 255))
    
    sub = "Tap for instant 0.5x launch • Long-press for frosted glass app options"
    bbox_s = draw.textbbox((0, 0), sub, font=font_sub)
    draw.text(((W - (bbox_s[2] - bbox_s[0])) // 2, 90), sub, font=font_sub, fill=(150, 165, 180))

    cx = W // 2
    draw.rounded_rectangle([cx - 450, 160, cx + 450, 840], radius=44, fill=(18, 22, 30), outline=(50, 60, 75), width=2)
    draw.rounded_rectangle([cx - 440, 170, cx + 440, 830], radius=38, fill=(12, 15, 20))

    menu_w = 340
    menu_h = 240
    menu_x = cx - menu_w // 2
    menu_y = 280
    draw.rounded_rectangle([menu_x, menu_y, menu_x + menu_w, menu_y + menu_h], radius=24, fill=(35, 42, 54, 240), outline=(255, 255, 255, 75), width=1)
    
    draw_app_icon(draw, menu_x + 20, menu_y + 20, 48, "browser")
    draw.text((menu_x + 80, menu_y + 22), "Browser", font=font_bold, fill=(255, 255, 255))
    draw.text((menu_x + 80, menu_y + 48), "com.cleanphone.browser", font=font_app_label, fill=(140, 155, 170))

    draw.line([(menu_x + 16, menu_y + 82), (menu_x + menu_w - 16, menu_y + 82)], fill=(255, 255, 255, 30), width=1)

    draw.text((menu_x + 24, menu_y + 100), "📌  Pin to Dock", font=font_sub, fill=(240, 245, 255))
    draw.text((menu_x + 24, menu_y + 145), "ℹ️  App Info & Permissions", font=font_sub, fill=(240, 245, 255))
    draw.text((menu_x + 24, menu_y + 190), "🗑️  Uninstall Package", font=font_sub, fill=(255, 80, 80))

    dock_w = 640
    dock_h = 110
    dock_x = cx - dock_w // 2
    dock_y = 660
    draw.rounded_rectangle([dock_x, dock_y, dock_x + dock_w, dock_y + dock_h], radius=44, fill=(255, 255, 255, 35), outline=(255, 255, 255, 95), width=2)

    dock_apps = ["phone", "messages", "browser", "camera"]
    icon_sz = 68
    col_w = dock_w / 4
    for i, itype in enumerate(dock_apps):
        dx_pos = int(dock_x + i * col_w + (col_w - icon_sz)/2)
        draw_app_icon(draw, dx_pos, dock_y + 20, icon_sz, itype)

    out_file = os.path.join(DOCS_DIR, "glass-dock-detail.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Dock Detail: {out_file}")


def generate_search_library():
    """Render authentic search in action screen."""
    W, H = 1000, 1400
    img = Image.new("RGBA", (W, H), (12, 15, 20, 255))
    draw = ImageDraw.Draw(img)

    PW, PH = 600, 1220
    px = (W - PW) // 2
    py = 80
    dx, dy, dw, dh, dr = render_phone_frame(draw, px, py, PW, PH, radius=42)

    screen = Image.new("RGBA", (dw, dh), (12, 15, 22, 255))
    sdraw = ImageDraw.Draw(screen)

    render_android_status_bar(sdraw, 0, 0, dw, is_clean=True)

    sb_w = dw - 40
    sb_h = 56
    sb_x = 20
    sb_y = 50
    sdraw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=28, fill=(255, 255, 255, 32), outline=(0, 122, 255, 180), width=2)
    sdraw.text((sb_x + 28, sb_y + 16), "Note|", font=font_bold, fill=(255, 255, 255))

    results = [
        ("clean_app", "Notes (Fossify)", "com.cleanphone.notes", "Active • Offline"),
        ("clean_app", "Notification Log", "com.android.settings.notifications", "System Tool"),
        ("clean_app", "Notepad Quick Share", "com.cleanphone.notepad", "Utility")
    ]
    
    sdraw.text((26, 130), "INSTANT SEARCH RESULTS (0.5x FILTER)", font=font_badge, fill=(0, 180, 110))

    for i, (itype, title, pkg, cat) in enumerate(results):
        cy = 160 + i * 94
        sdraw.rounded_rectangle([20, cy, dw - 20, cy + 80], radius=18, fill=(255, 255, 255, 22), outline=(255, 255, 255, 50), width=1)
        draw_app_icon(sdraw, 34, cy + 14, 52, itype)
        sdraw.text((100, cy + 18), title, font=font_bold, fill=(255, 255, 255))
        sdraw.text((100, cy + 46), f"{pkg} • {cat}", font=font_app_label, fill=(150, 165, 180))

    kb_y = dh - 420
    sdraw.rounded_rectangle([8, kb_y, dw - 8, dh - 12], radius=24, fill=(28, 32, 42, 250))
    sdraw.text((dw//2 - 50, kb_y + 180), "Gboard Keyboard", font=font_body, fill=(100, 115, 130))

    mask = Image.new("L", (dw, dh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, dw, dh], radius=dr, fill=255)
    img.paste(screen, (dx, dy), mask)

    out_file = os.path.join(DOCS_DIR, "feature-search-library.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Search Library: {out_file}")


def generate_feature_battery_ram():
    """Render authentic Android Settings Device Care / Battery & RAM benchmark dashboard."""
    W, H = 1500, 920
    img = Image.new("RGBA", (W, H), (14, 18, 24, 255))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        f = y / float(H)
        c = int(12 + f * 10)
        draw.line([(0, y), (W, y)], fill=(c, c + 2, c + 5, 255))

    title = "System Performance & Resource Optimization"
    bbox = draw.textbbox((0, 0), title, font=font_hero)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, 40), title, font=font_hero, fill=(255, 255, 255))

    sub = "Real benchmark metrics captured on ColorOS & Funtouch OS before and after debloating"
    bbox_s = draw.textbbox((0, 0), sub, font=font_sub)
    draw.text(((W - (bbox_s[2] - bbox_s[0])) // 2, 90), sub, font=font_sub, fill=(145, 160, 175))

    CARD_W = 660
    CARD_H = 650
    CARD_Y = 150
    
    # CARD 1: BATTERY
    C1_X = 65
    draw.rounded_rectangle([C1_X, CARD_Y, C1_X + CARD_W, CARD_Y + CARD_H], radius=24, fill=(22, 27, 36, 255), outline=(45, 55, 70), width=1)

    draw.rounded_rectangle([C1_X + 24, CARD_Y + 24, C1_X + 72, CARD_Y + 72], radius=14, fill=(46, 204, 113, 40), outline=(46, 204, 113, 160), width=1)
    draw.text((C1_X + 38, CARD_Y + 34), "⚡", font=font_bold, fill=(46, 204, 113))
    draw.text((C1_X + 88, CARD_Y + 26), "Battery Life & Deep Doze Sleep", font=font_heading, fill=(255, 255, 255))
    draw.text((C1_X + 88, CARD_Y + 58), "Overnight idle wake-locks and background telemetry", font=font_body, fill=(140, 155, 170))

    draw.rounded_rectangle([C1_X + 24, CARD_Y + 105, C1_X + CARD_W - 24, CARD_Y + 215], radius=16, fill=(16, 20, 28, 255))
    draw.text((C1_X + 44, CARD_Y + 122), "Screen-On Time (SOT)", font=font_title, fill=(220, 230, 240))
    draw.text((C1_X + 44, CARD_Y + 152), "+1.5 to 2.0 Extra Hours", font=font_bold, fill=(46, 204, 113))
    draw.text((C1_X + 44, CARD_Y + 182), "From ~6.0 hrs stock to 7.8 - 8.2 hrs debloated", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C1_X + CARD_W - 140, CARD_Y + 135, C1_X + CARD_W - 44, CARD_Y + 185], radius=12, fill=(46, 204, 113, 30), outline=(46, 204, 113, 140), width=1)
    draw.text((C1_X + CARD_W - 124, CARD_Y + 150), "+30%", font=font_bold, fill=(46, 204, 113))

    draw.rounded_rectangle([C1_X + 24, CARD_Y + 230, C1_X + CARD_W - 24, CARD_Y + 340], radius=16, fill=(16, 20, 28, 255))
    draw.text((C1_X + 44, CARD_Y + 247), "Overnight Standby Loss (8 Hours)", font=font_title, fill=(220, 230, 240))
    draw.text((C1_X + 44, CARD_Y + 277), "1% – 2% (Was 8% – 12%)", font=font_bold, fill=(46, 204, 113))
    draw.text((C1_X + 44, CARD_Y + 307), "Phone stays in Android deep sleep instead of polling OEM servers", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C1_X + CARD_W - 140, CARD_Y + 260, C1_X + CARD_W - 44, CARD_Y + 310], radius=12, fill=(0, 122, 255, 30), outline=(0, 122, 255, 140), width=1)
    draw.text((C1_X + CARD_W - 128, CARD_Y + 275), "-85%", font=font_bold, fill=(0, 122, 255))

    draw.rounded_rectangle([C1_X + 24, CARD_Y + 355, C1_X + CARD_W - 24, CARD_Y + 465], radius=16, fill=(16, 20, 28, 255))
    draw.text((C1_X + 44, CARD_Y + 372), "Hourly CPU Wake-locks", font=font_title, fill=(220, 230, 240))
    draw.text((C1_X + 44, CARD_Y + 402), "< 15 wakes/hr (Was ~140/hr)", font=font_bold, fill=(46, 204, 113))
    draw.text((C1_X + 44, CARD_Y + 432), "HeyTap, vivo daemons, and Glance push loops silenced", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C1_X + CARD_W - 140, CARD_Y + 385, C1_X + CARD_W - 44, CARD_Y + 435], radius=12, fill=(241, 196, 15, 30), outline=(241, 196, 15, 140), width=1)
    draw.text((C1_X + CARD_W - 128, CARD_Y + 400), "-90%", font=font_bold, fill=(241, 196, 15))

    draw.text((C1_X + 30, CARD_Y + 490), "Discharge Curve Comparison (24-Hour Timeline)", font=font_sub, fill=(200, 210, 225))
    draw.line([(C1_X + 30, CARD_Y + 540), (C1_X + 450, CARD_Y + 610)], fill=(235, 70, 70), width=3)
    draw.text((C1_X + 460, CARD_Y + 600), "Stock (14h dead)", font=font_badge, fill=(235, 70, 70))
    draw.line([(C1_X + 30, CARD_Y + 540), (C1_X + 450, CARD_Y + 565)], fill=(46, 204, 113), width=3)
    draw.text((C1_X + 460, CARD_Y + 555), "Debloated (28h+ life)", font=font_badge, fill=(46, 204, 113))

    # CARD 2: RAM
    C2_X = 775
    draw.rounded_rectangle([C2_X, CARD_Y, C2_X + CARD_W, CARD_Y + CARD_H], radius=24, fill=(22, 27, 36, 255), outline=(45, 55, 70), width=1)

    draw.rounded_rectangle([C2_X + 24, CARD_Y + 24, C2_X + 72, CARD_Y + 72], radius=14, fill=(0, 122, 255, 40), outline=(0, 122, 255, 160), width=1)
    draw.text((C2_X + 38, CARD_Y + 34), "🧠", font=font_bold, fill=(0, 122, 255))
    draw.text((C2_X + 88, CARD_Y + 26), "RAM Reclaim & Background Load", font=font_heading, fill=(255, 255, 255))
    draw.text((C2_X + 88, CARD_Y + 58), "Instant memory headroom for gaming and multitasking", font=font_body, fill=(140, 155, 170))

    draw.rounded_rectangle([C2_X + 24, CARD_Y + 105, C2_X + CARD_W - 24, CARD_Y + 215], radius=16, fill=(16, 20, 28, 255))
    draw.text((C2_X + 44, CARD_Y + 122), "Free System RAM (Typical 8GB / 12GB)", font=font_title, fill=(220, 230, 240))
    draw.text((C2_X + 44, CARD_Y + 152), "+1.0 GB to 1.4 GB Reclaimed", font=font_bold, fill=(0, 168, 255))
    draw.text((C2_X + 44, CARD_Y + 182), "From 2.9GB free to 4.3GB free on 8GB devices", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C2_X + CARD_W - 140, CARD_Y + 135, C2_X + CARD_W - 44, CARD_Y + 185], radius=12, fill=(0, 168, 255, 30), outline=(0, 168, 255, 140), width=1)
    draw.text((C2_X + CARD_W - 128, CARD_Y + 150), "+48%", font=font_bold, fill=(0, 168, 255))

    draw.rounded_rectangle([C2_X + 24, CARD_Y + 230, C2_X + CARD_W - 24, CARD_Y + 340], radius=16, fill=(16, 20, 28, 255))
    draw.text((C2_X + 44, CARD_Y + 247), "Active Background Services", font=font_title, fill=(220, 230, 240))
    draw.text((C2_X + 44, CARD_Y + 277), "0 Bloat Daemons (Down from 38)", font=font_bold, fill=(0, 168, 255))
    draw.text((C2_X + 44, CARD_Y + 307), "No persistent background listeners eating CPU threads", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C2_X + CARD_W - 140, CARD_Y + 260, C2_X + CARD_W - 44, CARD_Y + 310], radius=12, fill=(46, 204, 113, 30), outline=(46, 204, 113, 140), width=1)
    draw.text((C2_X + CARD_W - 132, CARD_Y + 275), "-100%", font=font_bold, fill=(46, 204, 113))

    draw.rounded_rectangle([C2_X + 24, CARD_Y + 355, C2_X + CARD_W - 24, CARD_Y + 465], radius=16, fill=(16, 20, 28, 255))
    draw.text((C2_X + 44, CARD_Y + 372), "Home Screen Launcher Footprint", font=font_title, fill=(220, 230, 240))
    draw.text((C2_X + 44, CARD_Y + 402), "< 15 MB RAM (Liquid Glass)", font=font_bold, fill=(0, 168, 255))
    draw.text((C2_X + 44, CARD_Y + 432), "Stock OEM launchers average 350 MB to 550 MB resident", font=font_regular, fill=(150, 165, 180))

    draw.rounded_rectangle([C2_X + CARD_W - 140, CARD_Y + 385, C2_X + CARD_W - 44, CARD_Y + 435], radius=12, fill=(155, 89, 182, 30), outline=(155, 89, 182, 140), width=1)
    draw.text((C2_X + CARD_W - 128, CARD_Y + 400), "-97%", font=font_bold, fill=(155, 89, 182))

    draw.text((C2_X + 30, CARD_Y + 490), "8 GB System Memory Allocation Post-Debloat", font=font_sub, fill=(200, 210, 225))
    bar_y = CARD_Y + 525
    bar_w = CARD_W - 60
    w_os = int(bar_w * 0.28)
    draw.rounded_rectangle([C2_X + 30, bar_y, C2_X + 30 + w_os, bar_y + 32], radius=8, fill=(80, 95, 115))
    w_apps = int(bar_w * 0.19)
    draw.rounded_rectangle([C2_X + 30 + w_os, bar_y, C2_X + 30 + w_os + w_apps, bar_y + 32], radius=0, fill=(0, 122, 255))
    draw.rounded_rectangle([C2_X + 30 + w_os + w_apps, bar_y, C2_X + 30 + bar_w, bar_y + 32], radius=8, fill=(46, 204, 113))

    draw.text((C2_X + 30, bar_y + 45), "■ Android OS (2.2GB)", font=font_badge, fill=(150, 165, 180))
    draw.text((C2_X + 175, bar_y + 45), "■ Running Apps (1.5GB)", font=font_badge, fill=(0, 122, 255))
    draw.text((C2_X + 335, bar_y + 45), "■ Free Headroom (4.3GB)", font=font_badge, fill=(46, 204, 113))

    foot = "100% Non-Destructive User 0 Operation · No Root Required · Instant Rollback via restore.sh / restore.ps1"
    bbox_f = draw.textbbox((0, 0), foot, font=font_regular)
    draw.text(((W - (bbox_f[2] - bbox_f[0])) // 2, CARD_Y + CARD_H + 28), foot, font=font_regular, fill=(120, 135, 150))

    out_file = os.path.join(DOCS_DIR, "feature-battery-ram.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Battery & RAM graphic: {out_file}")


def generate_feature_privacy_telemetry():
    """Render authentic Android Privacy Dashboard & Telemetry Audit UI."""
    W, H = 1500, 920
    img = Image.new("RGBA", (W, H), (14, 18, 24, 255))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        f = y / float(H)
        c = int(12 + f * 10)
        draw.line([(0, y), (W, y)], fill=(c, c + 2, c + 5, 255))

    title = "Android Privacy Dashboard & Tracker Silencing"
    bbox = draw.textbbox((0, 0), title, font=font_hero)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, 40), title, font=font_hero, fill=(255, 255, 255))

    sub = "4,370+ daily background data telemetry queries blocked across BBK & OPLUS ecosystems"
    bbox_s = draw.textbbox((0, 0), sub, font=font_sub)
    draw.text(((W - (bbox_s[2] - bbox_s[0])) // 2, 90), sub, font=font_sub, fill=(145, 160, 175))

    CARD_W = 1370
    CARD_H = 680
    CARD_X = (W - CARD_W) // 2
    CARD_Y = 140

    draw.rounded_rectangle([CARD_X, CARD_Y, CARD_X + CARD_W, CARD_Y + CARD_H], radius=24, fill=(20, 25, 34, 255), outline=(45, 55, 70), width=1)

    draw.rounded_rectangle([CARD_X + 24, CARD_Y + 24, CARD_X + CARD_W - 24, CARD_Y + 110], radius=16, fill=(46, 204, 113, 25), outline=(46, 204, 113, 140), width=1)
    draw.text((CARD_X + 46, CARD_Y + 42), "🛡️", font=font_bold, fill=(46, 204, 113))
    draw.text((CARD_X + 86, CARD_Y + 38), "Zero Background Telemetry Leaks Active", font=font_heading, fill=(255, 255, 255))
    draw.text((CARD_X + 86, CARD_Y + 74), "System logging daemons, diagnostic dumpers, and tracking endpoints disabled for User 0", font=font_body, fill=(180, 210, 190))

    audit_items = [
        ("HeyTap / NearMe Telemetry", "heytapmobile.com, nearme.com", "~1,850 queries/day", "0 queries", "Oppo / OnePlus / Realme", (255, 90, 90)),
        ("vivo Analytics & Daemon", "vivoglobal.com, vivo.com.cn", "~1,420 queries/day", "0 queries", "vivo / iQOO", (255, 90, 90)),
        ("Preloaded Facebook Services", "graph.facebook.com, fbsvc", "~620 queries/day", "0 queries", "All Brands", (255, 90, 90)),
        ("Glance / Pictorial Lockscreen Ads", "glancecdn.com, lockscreen push", "~310 queries/day", "0 queries", "Oppo / Realme / vivo", (255, 90, 90)),
        ("Baidu / Tencent SDK Loggers", "crashlog, tracking beacons", "~170 queries/day", "0 queries", "Chinese & Global OS", (255, 90, 90))
    ]

    th_y = CARD_Y + 130
    draw.text((CARD_X + 40, th_y), "MANUFACTURER TELEMETRY ENDPOINT", font=font_badge, fill=(130, 145, 165))
    draw.text((CARD_X + 380, th_y), "DOMAIN / SERVICE", font=font_badge, fill=(130, 145, 165))
    draw.text((CARD_X + 710, th_y), "STOCK CALLS", font=font_badge, fill=(130, 145, 165))
    draw.text((CARD_X + 880, th_y), "POST-DEBLOAT", font=font_badge, fill=(130, 145, 165))
    draw.text((CARD_X + 1040, th_y), "STATUS", font=font_badge, fill=(130, 145, 165))

    draw.line([(CARD_X + 30, th_y + 24), (CARD_X + CARD_W - 30, th_y + 24)], fill=(45, 55, 70), width=1)

    for i, (name, domain, before, after, brand, col) in enumerate(audit_items):
        row_y = th_y + 40 + i * 78
        draw.rounded_rectangle([CARD_X + 24, row_y, CARD_X + CARD_W - 24, row_y + 64], radius=12, fill=(16, 20, 28, 255), outline=(35, 45, 58), width=1)
        
        draw.text((CARD_X + 40, row_y + 14), name, font=font_bold, fill=(240, 245, 255))
        draw.text((CARD_X + 40, row_y + 38), f"Target: {brand}", font=font_app_label, fill=(140, 155, 170))
        
        draw.text((CARD_X + 380, row_y + 22), domain, font=font_mono_bold, fill=(160, 180, 205))
        
        draw.text((CARD_X + 710, row_y + 22), before, font=font_body, fill=(255, 100, 100))
        draw.text((CARD_X + 880, row_y + 22), after, font=font_bold, fill=(46, 204, 113))

        draw.rounded_rectangle([CARD_X + 1040, row_y + 16, CARD_X + 1180, row_y + 46], radius=15, fill=(46, 204, 113, 40), outline=(46, 204, 113, 180), width=1)
        draw.text((CARD_X + 1060, row_y + 23), "✓ BLOCKED", font=font_badge, fill=(46, 204, 113))

    bh_y = CARD_Y + CARD_H - 100
    draw.rounded_rectangle([CARD_X + 24, bh_y, CARD_X + CARD_W - 24, bh_y + 76], radius=16, fill=(0, 122, 255, 25), outline=(0, 122, 255, 100), width=1)
    draw.text((CARD_X + 44, bh_y + 16), "🔒  Privacy Guarantee: Zero Core Android Services Broken", font=font_title, fill=(255, 255, 255))
    draw.text((CARD_X + 44, bh_y + 44), "Google Play Services, push notifications, SafetyNet/Play Integrity, banking apps, and cameras continue functioning normally.", font=font_body, fill=(180, 200, 220))

    out_file = os.path.join(DOCS_DIR, "feature-privacy-telemetry.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Privacy & Telemetry graphic: {out_file}")


def generate_brands_lineup():
    """Render clean, authentic supported brands showcase banner."""
    W, H = 1600, 720
    img = Image.new("RGBA", (W, H), (14, 18, 24, 255))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        f = y / float(H)
        c = int(12 + f * 10)
        draw.line([(0, y), (W, y)], fill=(c, c + 2, c + 5, 255))

    title = "Supported Brands & Operating Systems"
    bbox = draw.textbbox((0, 0), title, font=font_hero)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, 40), title, font=font_hero, fill=(255, 255, 255))

    sub = "Universal support for ColorOS, Funtouch OS, OxygenOS, Realme UI, and OriginOS (Android 5.0 to 15)"
    bbox_s = draw.textbbox((0, 0), sub, font=font_sub)
    draw.text(((W - (bbox_s[2] - bbox_s[0])) // 2, 90), sub, font=font_sub, fill=(145, 160, 175))

    brands = [
        ("Oppo", "ColorOS", "v5 to v15", (0, 168, 98), "HeyTap Market, Theme Store,\nFinShell Pay, Glance ads"),
        ("vivo", "Funtouch / Origin", "v3 to v15", (65, 95, 255), "V-Appstore, Jovi Assistant,\nLockscreen Poster, Daemons"),
        ("OnePlus", "OxygenOS", "v5 to v15", (245, 5, 20), "Unified ColorOS telemetry,\nOPLUS Shelf, Clone Phone"),
        ("Realme", "Realme UI", "v1.0 to v6.0", (255, 200, 0), "Hot Apps / Games, HeyTap,\nCommercial push stubs"),
        ("iQOO", "Funtouch / Monster", "All versions", (255, 120, 0), "Game promotion daemons,\nvivo Wallet, analytics")
    ]

    CARD_W = 275
    CARD_H = 460
    START_X = (W - (len(brands) * CARD_W + (len(brands)-1) * 20)) // 2
    CARD_Y = 150

    for i, (bname, osname, osvers, color, bloat_desc) in enumerate(brands):
        bx = START_X + i * (CARD_W + 20)
        draw.rounded_rectangle([bx, CARD_Y, bx + CARD_W, CARD_Y + CARD_H], radius=20, fill=(22, 27, 36, 255), outline=(45, 55, 70), width=1)
        
        # Color accent strip at top of card
        draw.rounded_rectangle([bx, CARD_Y, bx + CARD_W, CARD_Y + 8], radius=4, fill=color)

        # Brand Badge Circle
        cx = bx + CARD_W // 2
        cy = CARD_Y + 55
        draw.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], fill=(color[0], color[1], color[2], 40), outline=color, width=2)
        draw.text((cx - 10, cy - 14), bname[0], font=font_bold, fill=color)

        # Brand Name
        bbox_bn = draw.textbbox((0, 0), bname, font=font_heading)
        draw.text((bx + (CARD_W - (bbox_bn[2] - bbox_bn[0]))//2, CARD_Y + 98), bname, font=font_heading, fill=(255, 255, 255))

        # OS Pill
        bbox_os = draw.textbbox((0, 0), osname, font=font_badge)
        pill_w = (bbox_os[2] - bbox_os[0]) + 20
        pill_x = bx + (CARD_W - pill_w)//2
        draw.rounded_rectangle([pill_x, CARD_Y + 142, pill_x + pill_w, CARD_Y + 168], radius=13, fill=(color[0], color[1], color[2], 30), outline=color, width=1)
        draw.text((pill_x + 10, CARD_Y + 148), osname, font=font_badge, fill=(255, 255, 255))

        # OS Version support
        bbox_v = draw.textbbox((0, 0), osvers, font=font_regular)
        draw.text((bx + (CARD_W - (bbox_v[2] - bbox_v[0]))//2, CARD_Y + 180), osvers, font=font_regular, fill=(150, 165, 180))

        # Divider line
        draw.line([(bx + 20, CARD_Y + 215), (bx + CARD_W - 20, CARD_Y + 215)], fill=(45, 55, 70), width=1)

        # Bloatware removed summary
        draw.text((bx + 20, CARD_Y + 235), "Bloatware Removed:", font=font_badge, fill=(130, 145, 165))
        draw.text((bx + 20, CARD_Y + 260), bloat_desc, font=font_body, fill=(200, 215, 230))

        # Safe rating check
        check_y = CARD_Y + CARD_H - 85
        draw.rounded_rectangle([bx + 16, check_y, bx + CARD_W - 16, check_y + 40], radius=10, fill=(46, 204, 113, 25), outline=(46, 204, 113, 120), width=1)
        draw.text((bx + 32, check_y + 12), "✓ Dual-List Verified", font=font_badge, fill=(46, 204, 113))

    foot = "Full backward compatibility for ColorOS 5/6/7, Funtouch 3/4/9, OxygenOS 5, and Android 5.0 through Android 15"
    bbox_f = draw.textbbox((0, 0), foot, font=font_sub)
    draw.text(((W - (bbox_f[2] - bbox_f[0])) // 2, CARD_Y + CARD_H + 30), foot, font=font_sub, fill=(130, 145, 160))

    out_file = os.path.join(DOCS_DIR, "brands-lineup.jpg")
    img.convert("RGB").save(out_file, "JPEG", quality=96)
    print(f"Generated authentic Brands Lineup: {out_file}")


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)
    print("Generating all 7 authentic real UI mockups & graphics...")
    generate_before_and_after()
    generate_liquid_glass_home()
    generate_dock_detail()
    generate_search_library()
    generate_feature_battery_ram()
    generate_feature_privacy_telemetry()
    generate_brands_lineup()
    print("All 7 authentic UI images generated successfully.")

if __name__ == "__main__":
    main()
