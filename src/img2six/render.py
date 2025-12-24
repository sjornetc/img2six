from __future__ import annotations

from pathlib import Path
from typing import Union

from PIL import Image

# Index 0..63, each value represents a 2x3 "sixth block" bitmask.
BLOCK_CHARS = [
    " ", "🬀", "🬁", "🬂", "🬃", "🬄", "🬅", "🬆",
    "🬇", "🬈", "🬉", "🬊", "🬋", "🬌", "🬍", "🬎",
    "🬏", "🬐", "🬑", "🬒", "🬓", "▌", "🬔", "🬕",
    "🬖", "🬗", "🬘", "🬙", "🬚", "🬛", "🬜", "🬝",
    "🬞", "🬟", "🬠", "🬡", "🬢", "🬣", "🬤", "🬥",
    "🬦", "🬧", "▐", "🬨", "🬩", "🬪", "🬫", "🬬",
    "🬭", "🬮", "🬯", "🬰", "🬱", "🬲", "🬳", "🬴",
    "🬵", "🬶", "🬷", "🬸", "🬹", "🬺", "🬻", "█",
]


PathLike = Union[str, Path]


def render(path: PathLike) -> str:
    """
    Render an image as text using 2x3 'sixth block' Unicode characters.

    Rules:
    - Only pixels that are exactly #000000 are considered "on" (drawn).
    - Any non-black pixel is treated as white (not drawn).
    - No scaling, no thresholding, no color processing.
    - Image is cropped to multiples of 2 (width) and 3 (height).
    """
    img = Image.open(path).convert("RGB")
    width, height = img.size
    pixels = img.load()

    out_lines: list[str] = []

    usable_width = width - (width % 2)
    usable_height = height - (height % 3)

    for y in range(0, usable_height, 3):
        line_chars: list[str] = []
        for x in range(0, usable_width, 2):
            value = 0
            bit = 0

            # Bit order: row-major within the 2x3 block (top->bottom, left->right)
            for dy in range(3):
                for dx in range(2):
                    if pixels[x + dx, y + dy] == (0, 0, 0):
                        value |= (1 << bit)
                    bit += 1

            line_chars.append(BLOCK_CHARS[value])
        out_lines.append("".join(line_chars))

    return "\n".join(out_lines)


def print_render(path: PathLike) -> None:
    """Convenience wrapper that prints the rendered text to stdout."""
    print(render(path))
