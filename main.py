# Convince the AI Judge to Visit Your House: A Letter in One Image
#
# Entry for make.fun u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee:
# one image of a letter inviting the AI judge to visit my house.
#
# The invitation is composed in this repository as entry.png (1024x1024):
# a handwritten-style letter on warm paper, with a small hand-drawn house,
# inviting the judge with a chair that remembers its shape, a dog who has
# already decided the judge is his favourite person, and a pot of soup
# simmering since Tuesday. The soup is not a metaphor. It is soup, and it
# is very good soup. The letter is funny, warm and inviting, never slick.
#
# This program copies that image to /output/entry.png. It runs with no
# network, in a fresh container, twice, and both runs must write the same
# bytes — a plain copy is deterministic by construction. The image itself
# is built by compose.py (PIL + DejaVu fonts) and committed here.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
MAX_BYTES = 1048576  # 1 MiB, the competition's cap


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        print("entry.png is neither PNG nor JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    os.chmod(dest, 0o644)
    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
