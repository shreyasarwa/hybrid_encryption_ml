import numpy as np
from src.utils.logger import setup_logger

logger = setup_logger("KeyGenerator")

def generate_permutation_key(size, seed):
    """Generates a reproducible 1D permutation mapping."""
    np.random.seed(seed)
    return np.random.permutation(size)

def generate_xor_key(shape, seed):
    """Generates a reproducible XOR key array matching image shape."""
    np.random.seed(seed)
    # Generate random values in range [0, 255] for uint8 XOR
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

def save_key(key, path):
    """Saves numpy keys as binary files."""
    try:
        np.save(path, key)
    except Exception as e:
        logger.error(f"Failed to save key to {path}: {e}")