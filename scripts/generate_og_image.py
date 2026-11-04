# -*- coding: utf-8 -*-
"""
Generate a world-class 1200x630 OpenGraph & Twitter Card default image for ToolsRadar.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1200
HEIGHT = 630

# Colors
BG_COLOR = (9, 9, 12)            # #09090c
CYAN = (56, 189, 248)            # #38bdf8
EMERALD = (16, 185, 129)         # #10b981
PURPLE = (168, 85, 247)          # #a855f7
AMBER = (245, 158, 11)           # #f59e0b
TEXT_WHITE = (244, 244, 245)     # #f4f4f5
TEXT_GRAY = (161, 161, 170)      # #a1a1aa
TEXT_MUTED = (113, 113, 122)     # #71717a
BORDER_COLOR = (39, 39, 42)      # #27272a
CARD_BG = (17, 17, 21)           # #111115

def get_font(name, size):
    windir = os.environ.get("WINDIR", "C:\\Windows")
    font_path = os.path.join(windir, "Fonts", name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def create_og_image(output_path):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 1. Subtle radial glow layer
    glow_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Cyan glow around radar (center at x=980, y=315)
    radar_center = (980, 315)
    for r in range(400, 0, -10):
        alpha = int(45 * (1 - r / 400.0))
        glow_draw.ellipse(
            [radar_center[0] - r, radar_center[1] - r, radar_center[0] + r, radar_center[1] + r],
            fill=(56, 189, 248, alpha)
        )

    # Purple/blue soft glow near top-left
    for r in range(350, 0, -10):
        alpha = int(25 * (1 - r / 350.0))
        glow_draw.ellipse(
            [150 - r, 100 - r, 150 + r, 100 + r],
            fill=(168, 85, 247, alpha)
        )

    img = Image.alpha_composite(img, glow_layer)
    draw = ImageDraw.Draw(img)

    # 2. Cyber grid dots
    grid_spacing = 40
    for x in range(0, WIDTH, grid_spacing):
        for y in range(0, HEIGHT, grid_spacing):
            draw.point((x, y), fill=(255, 255, 255, 18))

    # 3. Radar Visuals (Right Side)
    # Concentric rings
    for radius in [80, 160, 240, 320]:
        box = [
            radar_center[0] - radius, radar_center[1] - radius,
            radar_center[0] + radius, radar_center[1] + radius
        ]
        draw.ellipse(box, outline=(56, 189, 248, 50), width=1)

    # Radar crosshairs
    draw.line([radar_center[0] - 340, radar_center[1], radar_center[0] + 340, radar_center[1]], fill=(56, 189, 248, 40), width=1)
    draw.line([radar_center[0], radar_center[1] - 340, radar_center[0], radar_center[1] + 340], fill=(56, 189, 248, 40), width=1)

    # Diagonal grid lines
    d = 240
    draw.line([radar_center[0] - d, radar_center[1] - d, radar_center[0] + d, radar_center[1] + d], fill=(56, 189, 248, 25), width=1)
    draw.line([radar_center[0] - d, radar_center[1] + d, radar_center[0] + d, radar_center[1] - d], fill=(56, 189, 248, 25), width=1)

    # Radar sweep sector (45 degrees wedge)
    sweep_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    sweep_draw = ImageDraw.Draw(sweep_layer)
    sweep_draw.pieslice(
        [radar_center[0] - 300, radar_center[1] - 300, radar_center[0] + 300, radar_center[1] + 300],
        start=290, end=350, fill=(56, 189, 248, 30)
    )
    img = Image.alpha_composite(img, sweep_layer)
    draw = ImageDraw.Draw(img)

    # Pinging target blips with pulse rings
    blips = [
        (radar_center[0] - 120, radar_center[1] - 90, EMERALD),
        (radar_center[0] + 140, radar_center[1] - 130, CYAN),
        (radar_center[0] - 70, radar_center[1] + 140, AMBER),
        (radar_center[0] + 90, radar_center[1] + 110, CYAN),
        (radar_center[0] - 180, radar_center[1] + 30, EMERALD),
    ]
    for bx, by, color in blips:
        # Outer ring
        draw.ellipse([bx - 12, by - 12, bx + 12, by + 12], outline=(color[0], color[1], color[2], 90), width=1)
        # Inner core
        draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=color)

    # 4. Left Content: Typography & Branding
    font_badge = get_font("segoeuib.ttf", 15)
    font_logo = get_font("segoeuib.ttf", 46)
    font_headline = get_font("segoeuib.ttf", 36)
    font_body = get_font("segoeui.ttf", 20)
    font_pills = get_font("segoeuib.ttf", 16)
    font_footer = get_font("consola.ttf", 16)

    margin_x = 75

    # Top Status Badge Pill
    badge_text = "LIVE RADAR TELEMETRY • 975+ VERIFIED TOOLS"
    badge_bbox = font_badge.getbbox(badge_text)
    badge_w = badge_bbox[2] - badge_bbox[0] + 46
    badge_h = 34
    badge_y = 65

    draw.rounded_rectangle(
        [margin_x, badge_y, margin_x + badge_w, badge_y + badge_h],
        radius=17,
        fill=(24, 24, 27, 200),
        outline=(56, 189, 248, 120),
        width=1
    )
    # Green pulse dot
    draw.ellipse([margin_x + 14, badge_y + 12, margin_x + 24, badge_y + 22], fill=EMERALD)
    draw.text((margin_x + 32, badge_y + 8), badge_text, font=font_badge, fill=TEXT_WHITE)

    # Brand Title: ToolsRadar
    logo_y = 125
    # Icon box
    icon_size = 54
    draw.rounded_rectangle(
        [margin_x, logo_y, margin_x + icon_size, logo_y + icon_size],
        radius=12,
        fill=(14, 165, 233, 40),
        outline=CYAN,
        width=2
    )
    # Mini radar icon inside
    draw.ellipse([margin_x + 12, logo_y + 12, margin_x + icon_size - 12, logo_y + icon_size - 12], outline=CYAN, width=2)
    draw.ellipse([margin_x + 22, logo_y + 22, margin_x + icon_size - 22, logo_y + icon_size - 22], fill=CYAN)

    draw.text((margin_x + icon_size + 18, logo_y + 2), "ToolsRadar", font=font_logo, fill=TEXT_WHITE)

    # Main Headline
    head_y = 210
    draw.text((margin_x, head_y), "The Intelligence Radar for", font=font_headline, fill=TEXT_WHITE)
    draw.text((margin_x, head_y + 44), "Breakthrough DevTools & AI", font=font_headline, fill=CYAN)

    # Body Description
    desc_y = 325
    desc_line1 = "Independent daily tracking of high-signal software, autonomous AI"
    desc_line2 = "agents, and privacy-first open-source alternatives."
    draw.text((margin_x, desc_y), desc_line1, font=font_body, fill=TEXT_GRAY)
    draw.text((margin_x, desc_y + 30), desc_line2, font=font_body, fill=TEXT_GRAY)

    # Feature Pills Row
    pills = [
        ("⚡ Daily Crawls", (56, 189, 248, 30), CYAN),
        ("📖 4-Chapter Dossiers", (168, 85, 247, 30), PURPLE),
        ("🔄 OSS Alternatives", (16, 185, 129, 30), EMERALD),
        ("🐳 Self-Hostable", (245, 158, 11, 30), AMBER)
    ]
    pill_x = margin_x
    pill_y = 425
    for text, bg_tint, border_c in pills:
        bbox = font_pills.getbbox(text)
        pw = bbox[2] - bbox[0] + 28
        ph = 36
        draw.rounded_rectangle(
            [pill_x, pill_y, pill_x + pw, pill_y + ph],
            radius=8,
            fill=bg_tint,
            outline=border_c,
            width=1
        )
        draw.text((pill_x + 14, pill_y + 8), text, font=font_pills, fill=TEXT_WHITE)
        pill_x += pw + 12

    # Bottom Footer Divider & Domain
    draw.line([margin_x, 520, margin_x + 650, 520], fill=(255, 255, 255, 25), width=1)
    draw.text((margin_x, 545), "https://lordorange.top", font=font_footer, fill=CYAN)
    draw.text((margin_x + 240, 545), "• Real-Time Software Intelligence Directory", font=font_footer, fill=TEXT_MUTED)

    # Subtle outer border for crisp social card framing
    draw.rectangle([0, 0, WIDTH - 1, HEIGHT - 1], outline=(56, 189, 248, 60), width=1)

    # Convert to RGB and save optimized PNG
    rgb_img = img.convert("RGB")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rgb_img.save(output_path, "PNG", optimize=True)
    print(f"Generated OpenGraph image successfully at: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "public", "og-default.png")
    create_og_image(out)
