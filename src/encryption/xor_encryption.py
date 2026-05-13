import numpy as np

def apply_xor(img, seed):
    np.random.seed(seed)
    key = np.random.randint(0, 256, img.shape, dtype=np.uint8)
    return np.bitwise_xor(img, key), key