import sys
import platform
import numpy as np
import cv2
import tensorflow as tf
from src.utils.logger import setup_logger

logger = setup_logger("EnvCheck")

def verify_environment():
    logger.info("--- Environment Verification ---")
    logger.info(f"Python Version: {sys.version}")
    logger.info(f"Platform: {platform.system()} {platform.release()}")
    logger.info(f"NumPy Version: {np.__version__}")
    logger.info(f"OpenCV Version: {cv2.__version__}")
    logger.info(f"TensorFlow Version: {tf.__version__}")
    
    gpu_devices = tf.config.list_physical_devices('GPU')
    logger.info(f"GPU Available: {len(gpu_devices) > 0}")
    if gpu_devices:
        logger.info(f"GPU Details: {gpu_devices}")
    
    return True