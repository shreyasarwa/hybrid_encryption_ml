import numpy as np

def apply_permutation(img, seed):
    flat = img.flatten()
    np.random.seed(seed)
    idx = np.random.permutation(len(flat))
    permuted = flat[idx]
    return permuted.reshape(img.shape), idx