import numpy as np
from scipy.stats import entropy

def calculate_entropy(img):
    hist = np.histogram(img, bins=256, range=(0, 256), density=True)[0]
    return entropy(hist, base=2)