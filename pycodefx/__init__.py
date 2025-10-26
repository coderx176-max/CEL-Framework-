"""
PyCodeFX: Programmable Photo & Video Editing Framework

Production-ready, extensible, and high-performance.

Features:
- Load images and videos.
- Edit content at pixel or binary level.
- Apply built-in and custom effects.
- Easy export to common formats (PNG, MP4, etc.).
- Professional API and modular design.
"""

from .media import Media, ImageMedia, VideoMedia
from .effects import Effect, BlurEffect, CustomEffect
from .io import load_media, save_media

__all__ = [
    "Media", "ImageMedia", "VideoMedia",
    "Effect", "BlurEffect", "CustomEffect",
    "load_media", "save_media"
]