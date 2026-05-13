import numpy as np
from src.utils.logger import setup_logger

logger = setup_logger("NormalizeModule")

def normalize_image(image_array):
    """Normalizes pixel values from [0, 255] to [0, 1]."""
    try:
        # Convert to float32 and scale
        normalized = image_array.astype(np.float32) / 255.0
        return normalized
    except Exception as e:
        logger.error(f"Normalization failed: {e}")
        return None

def validate_array(image_array):
    """Returns metadata about the processed numpy array."""
    return {
        "shape": image_array.shape,
        "dtype": image_array.dtype,
        "min": np.min(image_array),
        "max": np.max(image_array)
    }