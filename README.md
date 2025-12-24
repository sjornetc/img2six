# img2six

Render images as plain text in the terminal using Unicode *sixth-block* characters (2×3).

This module is intentionally minimal:
- it only cares about **pure black pixels**
- any other pixel value is **not represented**
- no scaling, no thresholding, no color handling

If you need preprocessing, do it **before** calling this module.

## ⚠️ Project status

**Still debugging n stufffffffffff...** 🙄

This project is usable but not considered stable yet.
APIs may change and edge cases are still being tested.

## Installation

### Normal installation (recommended for production)

Install directly from GitHub:

```bash
pip install git+https://github.com/sjornetc/img2six.git
```

Or, if you cloned the repository:

```bash
pip install .
```

### Development installation (editable)

```bash
pip install -e .
```

## Usage

### As a Python module

```python
from img2six import render, print_render

print_render("image.png")

text = render("image.png")
```

- `render(path)` → returns a string
- `print_render(path)` → prints directly to stdout

---

### Standalone (command line)

```bash
python -m img2six image.png
```

This prints the rendered image to the terminal.

## Rendering rules (important)

- Only pixels that are **exactly black** (`#000000`) are rendered
- Any other pixel value is **not represented**
- The image is **not scaled**
- The image is cropped to multiples of:
  - 2 pixels (width)
  - 3 pixels (height)
- Each 2×3 block is mapped to a Unicode sixth-block character

If your output looks wrong, fix the image — not this module 😌

## What this module does NOT do

By design, this module does **not**:
- apply thresholds (only pure black pixels are printed)
- invert colors
- handle grayscale or color conversion
- apply any ANSI formatting (colors, styles, etc.)
- resize or scale images

Those responsibilities belong to the calling code.

## Requirements

- Python ≥ 3.10
- Pillow

## License

This project is licensed under the **GNU General Public License v3.0**.
See the `LICENSE` file for details.
