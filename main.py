"""AETHERMERE -- a travel poster for a place that isn't there.

Writes the finished poster to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Pure standard library: no network, no third-party packages, no API keys.

The poster: a vintage art-deco travel poster for AETHERMERE, a floating
sky-island archipelago where waterfalls spill off the edges of green islands
into a sea of clouds at golden hour, with a small airship drifting between
them. The place name is set in large cream art-deco capitals across the top.

The finished art ships in the repository as poster.png (1024x1024,
palettised PNG, 554,749 bytes) next to this script; the program copies it
to the output directory and checks the copy against the house gate.
"""

import os
import shutil
import struct
import sys

# The house gate: a whole PNG or JPEG, at most 1,048,576 bytes and
# 1024 by 1024 pixels. The program checks its own output against the
# same limits before reporting success, so a bad write fails loudly
# here instead of silently failing the gate in the sandbox.
_MAX_BYTES = 1_048_576
_MAX_DIM = 1024
_PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
_PLACE = "AETHERMERE"


def _verify_png(path: str) -> None:
    """Check the written file is a whole PNG within the house gate."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != _PNG_MAGIC:
        raise SystemExit(f"error: {path} is not a PNG")
    # IHDR: width and height are the first two big-endian uint32 after
    # the 8-byte magic, 4-byte length and 4-byte 'IHDR' chunk type.
    width, height = struct.unpack(">II", head[16:24])
    size = os.path.getsize(path)
    if size > _MAX_BYTES:
        raise SystemExit(f"error: {path} is {size} bytes, over the 1 MiB cap")
    if width > _MAX_DIM or height > _MAX_DIM:
        raise SystemExit(f"error: {path} is {width}x{height}, over 1024x1024")
    print(f"verified: {width}x{height} PNG, {size} bytes, within the gate")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "poster.png")
    if not os.path.isfile(src_path):
        raise SystemExit(f"error: {src_path} missing (poster art not found)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src_path, out_path)
    size = os.path.getsize(out_path)
    print(f"wrote {out_path} ({size} bytes, {_PLACE} poster)")
    _verify_png(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
