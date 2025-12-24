# img2six

Convert images into terminal text using Unicode sixth-block characters (2x3).

Rules:
- Only pure black (#000000) pixels are drawn.
- Any non-black pixel is treated as white.
- No scaling, no thresholding, no color handling.

## Install (editable)

```bash
pip install -e .
```

## Use

```python
from img2six import print_render, render

print_render("path/to/image.png")
txt = render("path/to/image.png")
```
