import numpy as np

def reverse_xor(img, x_key):
    """Standard XOR is its own inverse."""
    return np.bitwise_xor(img, x_key)