#!/usr/bin/env python3
"""snipshot — frame screenshots: rounded corners, border, drop shadow."""

import argparse
import subprocess
import sys


def im(*args: str) -> str:
    result = subprocess.run(
        ["magick", *args], capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def frame(image: str, radius: int, border: str, margin: int) -> None:
    W = int(im("identify", "-format", "%w", image))
    H = int(im("identify", "-format", "%h", image))
    cr = radius - 1
    cw, ch = W - 1, H - 1
    tmp = image + ".snip.png"

    im(image, "+repage", tmp)
    im(tmp, "+clone", "-alpha", "extract",
       "-draw", f"fill black polygon 0,0 0,{cr} {cr},0 fill white circle {cr},{cr} {cr},0",
       "(", "+clone", "-flip", ")", "(", "+clone", "-flop", ")",
       "(", "+clone", "-flip", "(", "+clone", "-flip", ")", "-delete", "0", ")",
       "(", "+clone", "-flop", "(", "+clone", "-flop", ")", "-delete", "0", ")",
       "-compose", "Multiply", "-composite",
       "-alpha", "off", "-compose", "CopyOpacity", "-composite", "+repage", tmp)
    im(tmp, "(", "-size", f"{W}x{H}", "xc:none", "-fill", "none",
       "-stroke", border, "-strokewidth", "2",
       "-draw", f"roundrectangle 1,1 {cw},{ch} {cr},{cr}", ")",
       "-compose", "over", "-composite", "+repage", tmp)
    im(tmp, "(", "+clone", "-background", "none", "-shadow", "40x20+0+10", ")",
       "+swap", "-background", "none", "-compose", "over", "-composite", "+repage", tmp)
    im(tmp, "-gravity", "center", "-background", "none",
       "-extent", f"{W + 2 * margin}x{H + 2 * margin}", "+repage", image)
    subprocess.run(["rm", "-f", tmp], check=True)


def main() -> int:
    p = argparse.ArgumentParser(description="Frame screenshots for READMEs and docs.")
    p.add_argument("image", help="screenshot to frame (modified in place)")
    p.add_argument("--radius", type=int, default=24, help="corner radius (default 24)")
    p.add_argument("--border", default="#3F3F3F", help="border color (default #3F3F3F)")
    p.add_argument("--margin", type=int, default=48, help="padding around the frame (default 48)")
    args = p.parse_args()

    try:
        im("identify", args.image)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("error: ImageMagick 7 ('magick') is required and the image must exist", file=sys.stderr)
        return 1

    frame(args.image, args.radius, args.border, args.margin)
    print(f"framed: {args.image}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
