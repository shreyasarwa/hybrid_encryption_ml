import numpy as np
import hashlib
import os

def save_hybrid_keys(path, name, p_key, x_key, chaos_params):
    np.save(os.path.join(path, f"{name}_p_key.npy"), p_key)
    np.save(os.path.join(path, f"{name}_x_key.npy"), x_key)
    # Simple hash for integrity check
    key_hash = hashlib.sha256(p_key.tobytes()).hexdigest()
    return key_hash