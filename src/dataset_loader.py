import tensorflow as tf
import numpy as np
from src.utils.logger import setup_logger

logger = setup_logger("DataLoader")

def load_cifar10_data():
    """
    Loads CIFAR-10 dataset using Keras.
    Returns: (x_train, y_train), (x_test, y_test)
    """
    try:
        logger.info("Downloading/Loading CIFAR-10 dataset...")
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
        logger.info("Dataset loaded successfully.")
        return (x_train, y_train), (x_test, y_test)
    except Exception as e:
        logger.error(f"Failed to load CIFAR-10: {e}")
        raise

def print_dataset_info(x_train, y_train, x_test, y_test):
    """
    Prints technical metadata about the image arrays.
    """
    # RGB Explanation: Images are 32x32 pixels with 3 channels (Red, Green, Blue).
    # NumPy Arrays: Each image is a (32, 32, 3) matrix of uint8 integers [0-255].
    
    print("\n" + "="*30)
    print("DATASET INFORMATION")
    print("="*30)
    print(f"Training Shape: {x_train.shape}") # (50000, 32, 32, 3)
    print(f"Testing Shape:  {x_test.shape}")  # (10000, 32, 32, 3)
    print(f"Label Shape:    {y_train.shape}")
    print(f"Image Dtype:    {x_train.dtype}")
    print(f"Min Pixel Val:  {np.min(x_train)}")
    print(f"Max Pixel Val:  {np.max(x_train)}")
    print(f"Dimensions:     {x_train.shape[1]}x{x_train.shape[2]}")
    print("="*30 + "\n")