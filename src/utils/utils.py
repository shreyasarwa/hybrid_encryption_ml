import os
import logging
from pathlib import Path
from src.utils.logger import setup_logger # Reusing logger from Stage 0

logger = setup_logger("Utils")

def create_folders(folder_path: str):
    """
    Safely creates directories using pathlib.
    """
    try:
        path = Path(folder_path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {folder_path}")
        else:
            logger.info(f"Directory already exists: {folder_path}")
    except Exception as e:
        logger.error(f"Error creating folder {folder_path}: {e}")
        raise