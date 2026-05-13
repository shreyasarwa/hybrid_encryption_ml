import numpy as np
import os

def load_dataset(dataset_path):
    """Loads and validates NumPy datasets for training."""
    try:
        # Match the structure seen in image_2a6c9e.jpg exactly
        X_train = np.load(os.path.join(dataset_path, "X", "X_train.npy")).astype('float32')
        y_train = np.load(os.path.join(dataset_path, "y", "y_train.npy")).astype('float32')
        X_test = np.load(os.path.join(dataset_path, "X", "X_test.npy")).astype('float32')
        y_test = np.load(os.path.join(dataset_path, "y", "y_test.npy")).astype('float32')
        
        # Ensure data is in [0, 1] range
        if X_train.max() > 1.0:
            X_train /= 255.0
            y_train /= 255.0
            X_test /= 255.0
            y_test /= 255.0
            
        return (X_train, y_train), (X_test, y_test)
    except Exception as e:
        raise IOError(f"Failed to load datasets. Check if files exist in {dataset_path}: {e}")