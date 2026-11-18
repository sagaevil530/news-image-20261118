#!/usr/bin/env python3
"""Compose the 18 November 2026 one-day news image (1024x1024 PNG).

Newspaper front page: masthead with the date, a lead story (Trump welcomed
by Marcos in Manila), and four further stories (APEC opens in Shenzhen,
US strike on Qeshm Island, Cyclone Akvan, new Knesset speaker). Base
illustrations were generated with no text; all lettering is rendered here
with PIL so it stays crisp and legible.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

W = H = 1024
PAPER = (250, 246, 238)
INK = (18, 18, 18)
NAVY = (27, 58, 95)
RED = (178, 34, 34)
GREY = (90, 88, 82)
RULE = (18, 18, 18)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def fit_image(path, tw, th):
    img = Image.open(path).convert("RGB")
    return ImageOps.fit(img, (tw, th), Image.LANCZOS)


def draw_cyclone(draw, x, y, w, h):
    """Spiral storm pictogram on a pale sky panel."""
    draw.rectangle([x, y, x + w, y + h], fill=(214, 231, 240))
    cx, cy = x + w // 2, y + h // 2
    rmax = min(w, h) * 0.46
    for k in range(3):
        pts = []
        for t in range(0, 541, 5):
            ang = math.radians(t + k * 42)
            r = rmax * (1 - t / 600.0)
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        draw.line(pts, fill=(27, 58, 95), width=8)
    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(250, 246, 238),
                 outline=(27, 58, 95), width=3)


def draw_parliament(draw, x, y, w, h):
    """Simple parliament building pictogram on a pale panel."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 228, 216))
    bx0, bx1 = x + w * 0.18, x + w * 0.82
    base = y + h - 18
    # steps: three thin slabs
    for i, sw in enumerate((0.60, 0.68, 0.76)):
        draw.rectangle([x + w * (1 - sw) / 2, base - 6 - i * 6,
                        x + w * (1 + sw) / 2, base - i * 6], fill=(140, 130, 114))
    # columns
    top = y + h * 0.42
    n = 5
    for i in range(n):
        cx = bx0 + (bx1 - bx0) * (i + 0.5) / n
        draw.rectangle([cx - 10, top, cx + 10, base - 18], fill=(250, 246, 238),
                       outline=(27, 58, 95), width=2)
    # entablature + pediment
    draw.rectangle([bx0 - 10, top - 12, bx1 + 10, top], fill=(27, 58, 95))
    draw.polygon([(bx0 - 16, top - 12), (bx1 + 16, top - 12),
                  ((bx0 + bx1) / 2, y + h * 0.10)], fill=(178, 34, 34))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=1)

    # ---- Masthead ----
    f_kicker = font(SANS_B, 20)
    centered(d, 30, "T H E   W O R L D   I N   O N E   D A Y", f_kicker, NAVY)
    f_date = font(SERIF_B, 56)
    centered(d, 56, "18 NOVEMBER 2026", f_date, INK)
    f_sub = font(SANS, 19)
    centered(d, 122, "Wednesday  ·  The day's world news in one page", f_sub, GREY)
    d.line([(28, 152), (W - 28, 152)], fill=RULE, width=3)
    d.line([(28, 158), (W - 28, 158)], fill=RULE, width=1)

    # ---- Lead story: hero image ----
    hero = fit_image("assets/media-generation-hero-manila-0-e262ef91-fcf5-401f-8fbf-deed6f708ab9.png",
                     968, 268)
    img.paste(hero, (28, 168))
    d.rectangle([28, 168, 28 + 968, 168 + 268], outline=INK, width=2)
    f_head = font(SERIF_B, 40)
    head_text = "TRUMP GETS MARCOS WELCOME IN MANILA"
    while d.textlength(head_text, font=f_head) > 968 and f_head.size > 20:
        f_head = font(SERIF_B, f_head.size - 1)
    centered(d, 448, head_text, f_head, INK)
    f_deck = font(SANS, 20)
    deck = ("Full military honours at Malacañang and a state banquet — then on to "
            "Shenzhen, as Asia's leaders gather for APEC.")
    for i, line in enumerate(wrap(d, deck, f_deck, 940)):
        centered(d, 498 + i * 26, line, f_deck, GREY)
    d.line([(28, 556), (W - 28, 556)], fill=RULE, width=2)

    # ---- Four story panels, 2 x 2 ----
    panels = [
        ("assets/media-generation-apec-shenzhen-0-aa3c9c97-1519-440c-a3dd-2b5466d79858.png",
         "APEC OPENS IN SHENZHEN",
         "Leaders meet 18–19 Nov; Trump, Xi and Putin "
         "to hold nuclear talks on Thursday."),
        ("assets/media-generation-gulf-strait-0-9051313b-1480-4080-b407-7eaabbbb3132.png",
         "US HITS IRAN MISSILE SITE",
         "Strike on Qeshm Island follows Iranian drones "
         "aimed at a US radar in Bahrain; tankers hit in the Strait."),
        (None, "CYCLONE AKVAN BEARS DOWN",
         "Severe storm in the Bay of Bengal; heavy rain "
         "on India's east coast, landfall due Friday."),
        (None, "NEW SPEAKER TAKES CHARGE",
         "Kahana, an Eisenkot ally, takes the Knesset "
         "chair after a 66–52 vote — a blow to Netanyahu."),
    ]
    f_ph = font(SERIF_B, 25)
    f_pb = font(SANS, 17)
    px = [28, 524]
    py = [572, 776]
    pw, ph = 472, 188
    for idx, (art, head, body) in enumerate(panels):
        x = px[idx % 2]
        y = py[idx // 2]
        if art:
            thumb = fit_image(art, pw, 108)
            img.paste(thumb, (x, y))
            d.rectangle([x, y, x + pw, y + 108], outline=INK, width=1)
        elif idx == 2:
            draw_cyclone(d, x, y, pw, 108)
            d.rectangle([x, y, x + pw, y + 108], outline=INK, width=1)
        else:
            draw_parliament(d, x, y, pw, 108)
            d.rectangle([x, y, x + pw, y + 108], outline=INK, width=1)
        d.text((x + 2, y + 114), head, font=f_ph, fill=INK)
        lines = wrap(d, body, f_pb, pw - 4)
        for i, line in enumerate(lines[:2]):
            d.text((x + 2, y + 146 + i * 21), line, font=f_pb, fill=GREY)

    # ---- Footer ticker ----
    d.line([(28, 972), (W - 28, 972)], fill=RULE, width=2)
    f_foot = font(SANS_B, 16)
    centered(d, 982, "ALSO TODAY:  US House briefing on the Nvidia affair  ·  APEC leaders meet in Shenzhen",
             f_foot, NAVY)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
