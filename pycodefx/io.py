import cv2
import os
from .media import ImageMedia, VideoMedia

SUPPORTED_IMAGE_FORMATS = ["png", "jpg", "jpeg", "bmp"]
SUPPORTED_VIDEO_FORMATS = ["mp4", "avi", "mov", "mkv"]

def validate_format(path: str) -> str:
    ext = path.lower().split(".")[-1]
    if ext in SUPPORTED_IMAGE_FORMATS:
        return "image"
    elif ext in SUPPORTED_VIDEO_FORMATS:
        return "video"
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def load_media(path: str):
    typ = validate_format(path)
    if typ == "image":
        return ImageMedia.from_file(path)
    elif typ == "video":
        return VideoMedia.from_file(path)

def save_media(media, path: str, fps: int = 25, codec: str = 'mp4v'):
    typ = validate_format(path)
    data = media.to_pixels()
    ext = path.lower().split(".")[-1]

    if typ == "image":
        cv2.imwrite(path, data)
    elif typ == "video":
        if len(data.shape) == 4:
            height, width = data.shape[1:3]
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(path, fourcc, fps, (width, height))
            for frame in data:
                out.write(frame)
            out.release()
        else:
            raise ValueError("Video data must be a 4D numpy array")
    else:
        raise ValueError("Unknown file extension")