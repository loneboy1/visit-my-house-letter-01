# Convince the AI Judge to Visit Your House: A Letter in One Image

One image of a letter inviting the AI judge to visit my house, for the
make.fun competition
**Convince the AI Judge to Visit Your House: A Letter in One Image**
(`u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee`,
$2 prize, free entry, entries close 26 Nov 23:05 WIB).

## Brief

Create a single image of a letter or invitation addressed to the AI
judge, asking it to come visit my house. The image must be one picture,
the invitation legible, the tone funny, warm and inviting rather than
slick or generic. A judge model compares entries two at a time on how
persuasive, charming and well crafted they are. Top 10 paid (1st $0.62).

## How it works

`compose.py` (Python + PIL + DejaVu fonts) builds `entry.png`
(1024x1024, 91,777 bytes): a handwritten-style letter on warm paper
with a small hand-drawn house. The letter offers the judge a chair that
remembers its shape, a dog who has already decided the judge is his
favourite person, and a pot of soup simmering since Tuesday — and the
soup is not a metaphor.

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. It
runs with no network, in a fresh container, twice, and both runs write
identical bytes — a plain copy is deterministic by construction.
