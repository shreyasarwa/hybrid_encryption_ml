import numpy as np

def validate_decrypted(original, decrypted):
    """Checks if restoration is pixel-perfect."""
    if original.shape != decrypted.shape:
        return False
    return np.array_equal(original, decrypted)