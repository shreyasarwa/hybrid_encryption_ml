import os
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger("PermutationUtils")

def ensure_directory(path: str):
    """Ensures a directory exists."""
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(f"Directory creation failed for {path}: {e}")
        raise

def get_image_paths(folder: str, formats: tuple):
    """Retrieves list of images with specific formats."""
    path = Path(folder)
    return [str(p) for p in path.iterdir() if p.suffix.lower() in formats]

def validate_image_array(img_array):
    """Validates properties of the image array."""
    if img_array is None or img_array.size == 0:
        return False
    return True