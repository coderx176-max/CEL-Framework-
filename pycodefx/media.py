import numpy as np
import cv2
from typing import Callable, List, Dict, Any, Union

class Media:
    """Base media class with decompile/recompile and edit history."""
    def __init__(self, data: np.ndarray, meta: Dict[str, Any] = None):
        self.data = data
        self.meta = meta or {}
        self.history: List[str] = []

    def to_binary(self) -> bytes:
        """Return raw binary data."""
        return self.data.tobytes()

    def to_pixels(self) -> np.ndarray:
        """Return pixel array."""
        return self.data

    def apply_effect(self, effect: 'Effect'):
        self.data = effect.apply(self.data)
        self.history.append(effect.__class__.__name__)

    def apply_effects(self, effects: List['Effect']):
        for effect in effects:
            self.apply_effect(effect)

    def get_metadata(self) -> Dict[str, Any]:
        return self.meta

    def add_metadata(self, key: str, value: Any):
        self.meta[key] = value

    def get_history(self) -> List[str]:
        return self.history

class ImageMedia(Media):
    @classmethod
    def from_file(cls, path: str) -> 'ImageMedia':
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError(f"Could not load image: {path}")
        return cls(img, meta={"path": path, "type": "image"})

class VideoMedia(Media):
    @classmethod
    def from_file(cls, path: str) -> 'VideoMedia':
        cap = cv2.VideoCapture(path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        if not frames:
            raise ValueError(f"Could not load video: {path}")
        return cls(np.array(frames), meta={"path": path, "type": "video"})