from __future__ import annotations

import argparse
import sys

from .render import render


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m img2six",
        description="Render an image to terminal text using Unicode sixth-block characters (2x3).",
    )
    parser.add_argument("path", help="Path to the input image file")
    args = parser.parse_args(argv)

    try:
        sys.stdout.write(render(args.path))
        sys.stdout.write("\n")
        return 0
    except FileNotFoundError:
        sys.stderr.write(f"error: file not found: {args.path}\n")
        return 2
    except Exception as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
