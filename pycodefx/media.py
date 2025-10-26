import numpy as np
import cv2

class Media:
    """Base media class for images/videos. Extensible for professional workflows."""
    def __init__(self, data):
        self.data = data

    def to_binary(self):
        return self.data.tobytes()

    def to_pixels(self):
        return self.data

    def apply_effect(self, effect):
        self.data = effect.apply(self.data)

class ImageMedia(Media):
    """Image-specific media class."""
    @classmethod
    def from_file(cls, path):
        img = cv2.imread(path)
        if img is None:
            raise ValueError(f"Could not load image: {path}")
        return cls(img)

class VideoMedia(Media):
    """Video-specific media class."""
    @classmethod
    def from_file(cls, path):
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
        return cls(np.array(frames))