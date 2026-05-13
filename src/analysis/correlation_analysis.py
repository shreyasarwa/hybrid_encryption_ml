import numpy as np

def calculate_pixel_correlation(image):
    """Calculates horizontal pixel correlation (Randomness Test)."""
    if len(image.shape) == 3:
        image = image[:,:,0] # Use one channel for correlation
        
    x = image[:, :-1].flatten().astype(np.float64)
    y = image[:, 1:].flatten().astype(np.float64)
    
    correlation_matrix = np.corrcoef(x, y)
    return float(correlation_matrix[0, 1])