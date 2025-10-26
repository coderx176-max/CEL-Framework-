import numpy as np
import cv2
from typing import Callable, List

class Effect:
    """Abstract base for all effects."""
    def apply(self, data: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Effect must implement the apply method.")

class BlurEffect(Effect):
    """Professional blur effect."""
    def __init__(self, ksize: int = 5):
        self.ksize = ksize

    def apply(self, data: np.ndarray) -> np.ndarray:
        if len(data.shape) == 3:  # Image
            return cv2.blur(data, (self.ksize, self.ksize))
        elif len(data.shape) == 4:  # Video
            return np.array([cv2.blur(frame, (self.ksize, self.ksize)) for frame in data])
        return data

class SharpenEffect(Effect):
    """Sharpening filter."""
    def apply(self, data: np.ndarray) -> np.ndarray:
        kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
        if len(data.shape) == 3:
            return cv2.filter2D(data, -1, kernel)
        elif len(data.shape) == 4:
            return np.array([cv2.filter2D(frame, -1, kernel) for frame in data])
        return data

class BrightnessEffect(Effect):
    """Adjust brightness."""
    def __init__(self, value: int = 30):
        self.value = value

    def apply(self, data: np.ndarray) -> np.ndarray:
        return np.clip(data + self.value, 0, 255)

class CustomEffect(Effect):
    """Custom Python effect."""
    def __init__(self, func: Callable[[np.ndarray], np.ndarray], name: str = 'CustomEffect'):
        self.func = func
        self.name = name

    def apply(self, data: np.ndarray) -> np.ndarray:
        return self.func(data)

class EffectChain(Effect):
    """Chain multiple effects together."""
    def __init__(self, effects: List[Effect]):
        self.effects = effects

    def apply(self, data: np.ndarray) -> np.ndarray:
        for effect in self.effects:
            data = effect.apply(data)
        return data