import numpy as np

def calculate_mse(img1, img2):
    """Mean Squared Error."""
    return np.mean((img1.astype(float) - img2.astype(float)) ** 2)
