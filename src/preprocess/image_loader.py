import cv2
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger("ImageLoader")

def load_image(image_path: str):
    """Loads an image and converts from BGR to RGB."""
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Could not read image at {image_path}")
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except Exception as e:
        logger.error(f"Error loading {image_path}: {e}")
        return None

def get_image_list(folder_path: str, supported_formats: tuple):
    """Returns a list of image paths with supported extensions."""
    path = Path(folder_path)
    return [str(p) for p in path.iterdir() if p.suffix.lower() in supported_formats]