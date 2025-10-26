import numpy as np
import cv2

class Effect:
    """Abstract base for all effects. Extend for custom/professional effects."""
    def apply(self, data: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Effect must implement the apply method.")

class BlurEffect(Effect):
    """Professional blur effect for images/videos."""
    def __init__(self, ksize=5):
        self.ksize = ksize

    def apply(self, data: np.ndarray) -> np.ndarray:
        if len(data.shape) == 3:  # Image
            return cv2.blur(data, (self.ksize, self.ksize))
        elif len(data.shape) == 4:  # Video
            return np.array([cv2.blur(frame, (self.ksize, self.ksize)) for frame in data])
        return data

class CustomEffect(Effect):
    """Custom Python-effect. Pass any function for pro-level tweaks."""
    def __init__(self, func):
        self.func = func

    def apply(self, data: np.ndarray) -> np.ndarray:
        return self.func(data)