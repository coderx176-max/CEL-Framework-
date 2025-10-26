from pycodefx import load_media, save_media, BlurEffect, CustomEffect

# Load an image or video
media = load_media("input.png")  # Or "input.jpg", "input.mp4", etc.

# Apply a professional blur effect
media.apply_effect(BlurEffect(ksize=10))

# Apply a custom effect (invert colors + noise)
def crazy_effect(data):
    import numpy as np
    noise = np.random.randint(0, 50, data.shape, dtype=data.dtype)
    return np.clip(255 - data + noise, 0, 255)

media.apply_effect(CustomEffect(crazy_effect))

# Save to PNG, JPG, MP4, etc. as needed
save_media(media, "output.png")