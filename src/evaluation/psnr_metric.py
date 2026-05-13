import numpy as np
from .mse_metric import calculate_mse

def calculate_psnr(img1, img2):
    """Calculates Peak Signal-to-Noise Ratio."""
    mse = calculate_mse(img1, img2)
    if mse == 0:
        return 100.0
    
    pixel_max = 255.0
    psnr = 20 * np.log10(pixel_max / np.sqrt(mse))
    return float(psnr)