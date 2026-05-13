import numpy as np
from src.encryption.logistic_map import generate_logistic_sequence
from src.utils.logger import setup_logger

logger = setup_logger("MaskGenerator")

def generate_chaotic_mask(shape, x0, r):
    """Converts a logistic sequence into a uint8 mask matching image shape."""
    try:
        length = np.prod(shape)
        sequence = generate_logistic_sequence(x0, r, length)
        
        # Normalize and scale to [0, 255]
        mask = (sequence * 255).astype(np.uint8)
        return mask.reshape(shape)
    except Exception as e:
        logger.error(f"Mask generation error: {e}")
        return None