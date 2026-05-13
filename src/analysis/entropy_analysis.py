import numpy as np
import cv2
from scipy.stats import entropy

def calculate_entropy(image):
    """Calculates the Shannon Entropy of an image."""
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.sum()
    return float(entropy(hist_norm, base=2))