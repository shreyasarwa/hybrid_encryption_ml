import cv2
from src.utils.logger import setup_logger

logger = setup_logger("EncryptionUtils")

def load_image(path):
    """Loads image from path in original color space."""
    img = cv2.imread(path)
    if img is not None:
        return img
    logger.error(f"Failed to load image: {path}")
    return None

def save_encrypted_image(img_array, path):
    """Saves encrypted image array to disk."""
    try:
        cv2.imwrite(path, img_array)
        return True
    except Exception as e:
        logger.error(f"Save failed for {path}: {e}")
        return False