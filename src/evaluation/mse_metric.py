import numpy as np

def calculate_mse(img1, img2):
    """Calculates Mean Squared Error between two images."""
    if img1.shape != img2.shape:
        raise ValueError("Images must have identical dimensions for MSE.")
    
    # Ensure float precision
    i1 = img1.astype(np.float64)
    i2 = img2.astype(np.float64)
    
    mse = np.mean((i1 - i2) ** 2)
    return float(mse)