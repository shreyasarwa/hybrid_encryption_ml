import numpy as np
from scipy.stats import entropy

def calculate_entropy(img_array):
    """Calculates the Shannon entropy of an image."""
    marg = np.histogram(img_array, bins=256, range=(0, 255), density=True)[0]
    return entropy(marg, base=2)