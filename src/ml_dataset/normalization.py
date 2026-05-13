import numpy as np

def normalize_dataset(data):
    """Converts [0, 255] uint8 to [0.0, 1.0] float32."""
    return data.astype('float32') / 255.0

def validate_normalization(data):
    return np.min(data) >= 0.0 and np.max(data) <= 1.0