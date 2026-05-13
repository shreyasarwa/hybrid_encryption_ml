import numpy as np

def generate_logistic_sequence(x0, r, length):
    x = np.zeros(length)
    x[0] = x0
    for i in range(1, length):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def reverse_chaos(img, x0, r):
    """Re-generates mask and XORs to reverse."""
    seq = generate_logistic_sequence(x0, r, img.size)
    mask = (seq * 255).astype(np.uint8).reshape(img.shape)
    return np.bitwise_xor(img, mask)