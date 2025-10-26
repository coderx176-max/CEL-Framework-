import cv2
from .media import ImageMedia, VideoMedia

def load_media(path: str):
    ext = path.lower().split(".")[-1]
    if ext in ["png", "jpg", "jpeg", "bmp"]:
        return ImageMedia.from_file(path)
    elif ext in ["mp4", "avi", "mov", "mkv"]:
        return VideoMedia.from_file(path)
    else:
        raise ValueError("Unsupported file type")

def save_media(media, path: str):
    data = media.to_pixels()
    ext = path.lower().split(".")[-1]
    # Image
    if ext in ["png", "jpg", "jpeg", "bmp"]:
        cv2.imwrite(path, data)
    # Video
    elif ext in ["mp4", "avi", "mov", "mkv"]:
        if len(data.shape) == 4:
            height, width = data.shape[1:3]
            fps = 25
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(path, fourcc, fps, (width, height))
            for frame in data:
                out.write(frame)
            out.release()
    else:
        raise ValueError("Unknown file extension")