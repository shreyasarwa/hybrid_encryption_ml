import numpy as np
import os

def load_training_data(dataset_path):
    """Loads X and y tensors from Stage 8."""
    X_train = np.load(os.path.join(dataset_path, "X/X_train.npy"))
    y_train = np.load(os.path.join(dataset_path, "y/y_train.npy"))
    X_test = np.load(os.path.join(dataset_path, "X/X_test.npy"))
    y_test = np.load(os.path.join(dataset_path, "y/y_test.npy"))
    
    return (X_train, y_train), (X_test, y_test)