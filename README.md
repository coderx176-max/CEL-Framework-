# PyCodeFX

**Advanced Programmable Photo & Video Editing Framework for Python**

## Features
- Load, decompile, and recompile images/videos.
- Edit at pixel or binary level with full Python power.
- Chain effects for pro workflows (batch, complex pipelines).
- Built-in effects: blur, sharpen, brightness, invert, custom.
- Metadata and edit history tracking.
- Export to PNG, JPG, MP4, MOV, etc.
- Modular and extensible for plugins, AI, and more.

## Quick Start

```python
from pycodefx import (
    load_media, save_media, decompile_media, recompile_media,
    BlurEffect, SharpenEffect, BrightnessEffect, CustomEffect, EffectChain
)
media = load_media("input.png")
decomp = decompile_media(media)
effects = [
    BlurEffect(ksize=7),
    SharpenEffect(),
    BrightnessEffect(value=30),
    CustomEffect(lambda data: 255 - data, name="InvertColors")
]
media.apply_effect(EffectChain(effects))
new_media = recompile_media(media.to_pixels(), media_type="image", meta=decomp["metadata"])
save_media(new_media, "edited.png")
```

## Extending

Add new effects by subclassing `Effect` and implementing `apply`. You can chain any number of effects with `EffectChain`.

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

See `example_usage.py` for a full demo and pro workflow.

---

**PyCodeFX gives you pro-grade, developer-focused editing power—fast, flexible, and creative. Outperforms CapCut for code-driven workflows.**
