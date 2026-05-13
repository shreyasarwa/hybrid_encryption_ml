import cv2
from src.utils.logger import setup_logger

logger = setup_logger("ResizeModule")

def resize_image(image_array, size=(64, 64)):
    """Resizes image to target dimensions (width, height)."""
    try:
        resized = cv2.resize(image_array, size, interpolation=cv2.INTER_AREA)
        return resized
    except Exception as e:
        logger.error(f"Resize failed: {e}")
        return None