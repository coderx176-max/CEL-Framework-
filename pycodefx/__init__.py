"""
PyCodeFX: Advanced, Extensible Media Editing Framework

Features:
- Load, decompile, edit, and recompile images/videos.
- Professional effect pipeline and plugin system.
- Metadata and edit history tracking.
- Format validation and error handling.
"""
from .media import Media, ImageMedia, VideoMedia
from .effects import Effect, BlurEffect, CustomEffect, EffectChain, SharpenEffect, BrightnessEffect
from .io import load_media, save_media, validate_format
from .decompiler import decompile_media
from .recompiler import recompile_media

__all__ = [
    "Media", "ImageMedia", "VideoMedia",
    "Effect", "BlurEffect", "CustomEffect", "EffectChain", "SharpenEffect", "BrightnessEffect",
    "load_media", "save_media", "validate_format",
    "decompile_media", "recompile_media"
]