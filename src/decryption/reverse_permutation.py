import numpy as np

def reverse_permutation(img, p_key):
    """Uses argsort of permutation key to reverse mapping."""
    flat = img.flatten()
    # Find the inverse mapping
    inverse_idx = np.argsort(p_key)
    restored_flat = flat[inverse_idx]
    return restored_flat.reshape(img.shape)