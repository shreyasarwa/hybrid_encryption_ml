import numpy as np
import os

def export_numpy_arrays(path, name, data):
    np_path = os.path.join(path, f"{name}.npy")
    np.save(np_path, data)
    return np_path