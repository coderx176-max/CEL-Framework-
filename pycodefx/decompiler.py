"""
Decompiler: Convert media into editable code, pixel arrays, and metadata.
"""
import numpy as np
from .media import Media

def decompile_media(media: Media):
    """
    Decompile media into code (pixel array), metadata, and binary.
    Returns a dict with 'pixels', 'binary', 'metadata'.
    """
    return {
        "pixels": media.to_pixels(),
        "binary": media.to_binary(),
        "metadata": media.get_metadata(),
        "history": media.get_history()
    }