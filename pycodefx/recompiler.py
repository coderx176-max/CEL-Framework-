"""
Recompiler: Convert code/pixels/metadata back into media objects.
"""
import numpy as np
from .media import ImageMedia, VideoMedia

def recompile_media(pixels, media_type='image', meta=None):
    """
    Recompile pixel data into a Media object.
    """
    if media_type == 'image':
        return ImageMedia(pixels, meta)
    elif media_type == 'video':
        return VideoMedia(pixels, meta)
    else:
        raise ValueError("Unsupported media type for recompilation")