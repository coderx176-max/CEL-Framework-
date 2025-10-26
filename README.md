# PyCodeFX

**Production-ready Programmable Photo & Video Editing Framework for Python**

## Features
- Load images and videos.
- Edit at pixel or binary level.
- Apply built-in and custom Python effects.
- Export to PNG, MP4, etc.
- Modular, professional, and extensible for any workflow.

## Quick Start
```python
from pycodefx import load_media, save_media, BlurEffect, CustomEffect

media = load_media("input.png")
media.apply_effect(BlurEffect(ksize=7))

def invert(data):
    return 255 - data
media.apply_effect(CustomEffect(invert))

save_media(media, "edited.png")
```

## Extending
Add new effects by subclassing `Effect` and implementing `apply` for unlimited creativity.

## Supported Formats
- Images: PNG, JPG, JPEG, BMP
- Videos: MP4, AVI, MOV, MKV

## Requirements
- Python 3.8+
- numpy
- opencv-python

Install dependencies:
```bash
pip install numpy opencv-python
```

## Demo
See `example_usage.py` for a full demo.

---

**PyCodeFX is designed for professional workflows and rapid creative coding. Unmatched flexibility—better than CapCut for Python devs!**