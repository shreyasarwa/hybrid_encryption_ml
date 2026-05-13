import numpy as np
import os

def load_keys(base_path, filename):
    """Loads npy keys for permutation and XOR."""
    p_key_path = os.path.join(base_path, f"{filename}_p_key.npy")
    x_key_path = os.path.join(base_path, f"{filename}_x_key.npy")
    
    if not os.path.exists(p_key_path) or not os.path.exists(x_key_path):
        return None, None
        
    return np.load(p_key_path), np.load(x_key_path)