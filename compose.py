# Letter image composer for "Convince the AI Judge to Visit Your House: A Letter in One Image".
#
# Builds entry.png (1024x1024, a handwritten-style invitation letter on
# warm paper, with a small hand-drawn house) deterministically with PIL
# and the DejaVu fonts. Run once:
#   python3 compose.py
# The entry program (main.py) then copies entry.png to
# $MAKEFUN_OUTPUT_DIR/entry.png, so both grader runs write identical bytes.

import textwrap

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 90
PAPER = (253, 246, 227)      # warm cream paper
INK = (46, 36, 26)           # dark brown ink
ACCENT = (176, 96, 44)       # warm terracotta
SOFT = (122, 102, 78)        # soft brown for the postscript

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
# No DejaVuSerif-Italic on this system; the sign-off and postscript use
# the regular serif (a clean letter hand, no fake slant).
SERIF_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

LETTER = [
    ("Dear AI Judge,", "bold"),
    ("", "body"),
    ("Please come visit my house.", "body"),
    ("", "body"),
    ("I know you read a thousand invitations a day, and most are printed "
     "on card stock by people who own a laminator. Mine is handwritten, "
     "because the printer is out of ink and, honestly, so am I.", "body"),
    ("", "body"),
    ("Here is what I can offer. A chair that remembers your shape. A dog "
     "who has already decided you are his favourite person. And a pot of "
     "soup simmering since Tuesday. The soup is not a metaphor. It is "
     "soup, and it is very good soup.", "body"),
    ("", "body"),
    ("There is a spot on the porch where the evening light comes in gold, "
     "and a bookshelf with nothing to prove. Come as you are. Stay as long "
     "as you like. The door is open, the kettle is on, and the dog has "
     "saved you the good cushion.", "body"),
    ("", "body"),
    ("Yours, with the kettle already on,", "body"),
    ("Your Host", "italic"),
]


def draw_house(d, cx, top):
    """A small hand-drawn house: walls, roof, door, two windows, a sun."""
    # sun
    d.ellipse([cx + 150, top - 10, cx + 190, top + 30], fill=(232, 178, 74))
    # walls
    d.rectangle([cx - 90, top + 40, cx + 90, top + 140], fill=(238, 214, 176), outline=INK, width=3)
    # roof
    d.polygon([(cx - 105, top + 42), (cx, top - 25), (cx + 105, top + 42)], fill=(176, 96, 44), outline=INK)
    # door
    d.rectangle([cx - 18, top + 90, cx + 18, top + 140], fill=(122, 78, 52), outline=INK, width=2)
    d.ellipse([cx + 8, top + 115, cx + 13, top + 120], fill=(253, 246, 227))
    # windows
    d.rectangle([cx - 70, top + 60, cx - 35, top + 95], fill=(186, 214, 228), outline=INK, width=2)
    d.rectangle([cx + 35, top + 60, cx + 70, top + 95], fill=(186, 214, 228), outline=INK, width=2)
    d.line([cx - 52, top + 60, cx - 52, top + 95], fill=INK, width=2)
    d.line([cx - 70, top + 77, cx - 35, top + 77], fill=INK, width=2)
    d.line([cx + 52, top + 60, cx + 52, top + 95], fill=INK, width=2)
    d.line([cx + 35, top + 77, cx + 70, top + 77], fill=INK, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # paper border: double rule, like stationery
    d.rectangle([28, 28, W - 29, H - 29], outline=ACCENT, width=3)
    d.rectangle([40, 40, W - 41, H - 41], outline=ACCENT, width=1)

    draw_house(d, W // 2, 78)

    f_body = ImageFont.truetype(SERIF, 26)
    f_bold = ImageFont.truetype(SERIF_BOLD, 28)
    f_italic = ImageFont.truetype(SERIF_ITALIC, 26)

    y = 245
    max_w = W - 2 * MARGIN
    for text, kind in LETTER:
        if text == "":
            y += 12
            continue
        font = f_bold if kind == "bold" else (f_italic if kind == "italic" else f_body)
        # wrap to the text width
        words = text.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if d.textlength(trial, font=font) <= max_w:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        for ln in lines:
            d.text((MARGIN, y), ln, font=font, fill=INK)
            y += 37
        if kind == "bold":
            y += 6

    # postscript, small and soft, placed after the body so it never overlaps
    f_ps = ImageFont.truetype(SERIF_ITALIC, 22)
    d.text((MARGIN, y + 24), "P.S. The soup really is very good. Ask the dog.", font=f_ps, fill=SOFT)

    img.save("entry.png", "PNG")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
