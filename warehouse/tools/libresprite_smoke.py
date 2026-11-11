#!/usr/bin/env python3
"""Minimal LibreSprite integration smoke test. No Bearframe user art is included."""
from __future__ import annotations
import json, struct, sys, zlib
from pathlib import Path

W = H = 32

def write_png(path: str) -> None:
    rows = []
    for y in range(H):
        row = bytearray([0])  # PNG filter 0
        for x in range(W):
            # Deliberately plain reference block; LibreSprite JS must edit it.
            rgba = (48, 53, 69, 255) if (12 <= x <= 20 and 12 <= y <= 20) else (0, 0, 0, 0)
            row.extend(rgba)
        rows.append(bytes(row))
    def chunk(tag: bytes, content: bytes) -> bytes:
        return struct.pack(">I", len(content)) + tag + content + struct.pack(">I", zlib.crc32(tag + content) & 0xffffffff)
    data = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 6, 0, 0, 0))
    data += chunk(b"IDAT", zlib.compress(b"".join(rows), 9)) + chunk(b"IEND", b"")
    Path(path).write_bytes(data)

def verify() -> None:
    from PIL import Image
    a = Image.open("smoke_input.png").convert("RGBA")
    b = Image.open("smoke_output.png").convert("RGBA")
    assert a.size == b.size == (W, H)
    assert a.getpixel((16, 16)) == (48, 53, 69, 255), a.getpixel((16, 16))
    assert b.getpixel((16, 16)) == (171, 91, 240, 255), b.getpixel((16, 16))
    assert b.getpixel((17, 16)) == (134, 72, 210, 255), b.getpixel((17, 16))
    assert b.getpixel((0, 0))[3] == 0
    report = {"tool": "LibreSprite 1.3", "test": "JS modified RGBA pixels in headless real editor", "dimensions": [W, H], "passed": True, "source_pixel": list(a.getpixel((16, 16))), "edited_pixel": list(b.getpixel((16, 16))), "transparent_corners": True, "notes": "Integration smoke test only; not artwork or a quality claim."}
    Path("smoke_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "init":
        write_png("smoke_input.png")
        print("Created reference 32x32 RGBA PNG.")
    elif mode == "verify":
        verify()
    else:
        raise SystemExit("Usage: libresprite_smoke.py init|verify")
