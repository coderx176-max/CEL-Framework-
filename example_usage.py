from pycodefx import (
    load_media, save_media, decompile_media, recompile_media,
    BlurEffect, SharpenEffect, BrightnessEffect, CustomEffect, EffectChain
)

# Load an image
media = load_media("input.png")

# Decompile: get code, pixels, metadata
decomp = decompile_media(media)
pixels = decomp["pixels"]
meta = decomp["metadata"]

# Apply chained effects (pro pipeline)
effects = [
    BlurEffect(ksize=10),
    SharpenEffect(),
    BrightnessEffect(value=50),
    CustomEffect(lambda d: 255 - d, name="InvertColors"),
]
chain = EffectChain(effects)
media.apply_effect(chain)

# Recompile (optionally, you could recompile a modified pixel array)
new_media = recompile_media(media.to_pixels(), media_type=meta.get("type", "image"), meta=meta)

# Save to PNG, JPG, MP4, etc.
save_media(new_media, "output.png")