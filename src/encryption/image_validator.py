import numpy as np

def validate_image(img):
    if img is None or not isinstance(img, np.ndarray):
        return False
    if img.dtype != np.uint8:
        return False
    return True