import os
from pathlib import Path
from src.utils.logger import setup_logger 

logger = setup_logger("Helpers")

def create_folders(folder_path: str):
    try:
        path = Path(folder_path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {folder_path}")
    except Exception as e:
        logger.error(f"Error creating folder: {e}")