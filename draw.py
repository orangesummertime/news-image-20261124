#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page as a 1024x1024 PNG.

Deterministic: fixed layout, fixed fonts, fixed colours, no randomness,
no network, no timestamps in the image. Run: python3 draw.py
Writes entry.png next to this script.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 42, 68)
RED = (178, 34, 34)
DARK = (20, 20, 20)
GREY = (90, 96, 104)
LIGHT = (242, 244, 247)
BORDER = (200, 205, 212)
WHITE = (255, 255, 255)

def font(path, size):
    return ImageFont.truetype(path, size)

def centred(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

STORIES = [
    ("NVIDIA", (0, 122, 80),
     "Huang returns as Nvidia chief",
     "Reinstated 11 days after stepping down; shares jump 33%"),
    ("UKRAINE", (20, 80, 160),
     "Zelensky urges four-way talks",
     "Calls for talks with Russia as strikes hit the Kyiv region"),
    ("INDIA\u2013NEPAL", (176, 96, 0),
     "New train links Ayodhya and Janakpur",
     "Modi and Nepal PM launch the Saryu-Kamala Express"),
    ("LISBON", (96, 44, 140),
     "Thousands march on living costs",
     "Protesters in Lisbon rally against rising prices"),
    ("SPORT", (178, 34, 34),
     "Verstappen wins in Las Vegas",
     "Max Verstappen takes the 2026 Las Vegas Grand Prix"),
]

def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # Top rule
    d.rectangle([0, 0, W, 10], fill=RED)
    # Masthead
    centred(d, 28, "WORLD NEWS", font(BOLD, 76), NAVY)
    centred(d, 118, "TUESDAY 24 NOVEMBER 2026", font(BOLD, 52), RED)
    centred(d, 182, "The day in one image", font(REG, 28), GREY)
    d.line([48, 224, W - 48, 224], fill=NAVY, width=4)

    # Five story panels
    y = 244
    panel_h = 132
    gap = 12
    for tag, colour, headline, detail in STORIES:
        d.rectangle([48, y, W - 48, y + panel_h], fill=LIGHT, outline=BORDER, width=2)
        d.rectangle([48, y, 64, y + panel_h], fill=colour)
        d.text((84, y + 12), tag, font=font(BOLD, 24), fill=colour)
        head_lines = wrap(d, headline, font(BOLD, 34), W - 48 - 84 - 24)
        hy = y + 42
        for line in head_lines:
            d.text((84, hy), line, font=font(BOLD, 34), fill=DARK)
            hy += 40
        d.text((84, y + 96), detail, font=font(REG, 25), fill=(50, 55, 62))
        y += panel_h + gap

    # Footer
    d.line([48, 978, W - 48, 978], fill=NAVY, width=3)
    centred(d, 990, "24 NOVEMBER 2026 \u2022 WORLD NEWS IN ONE IMAGE",
            font(BOLD, 22), NAVY)

    img.save("entry.png", format="PNG", optimize=True)

if __name__ == "__main__":
    main()
