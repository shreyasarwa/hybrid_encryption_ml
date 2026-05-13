import numpy as np
from src.encryption.logistic_map import generate_logistic_sequence

def apply_chaos(img, x0, r):
    seq = generate_logistic_sequence(x0, r, img.size)
    mask = (seq * 255).astype(np.uint8).reshape(img.shape)
    return np.bitwise_xor(img, mask), mask