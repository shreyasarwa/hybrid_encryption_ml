import os
import time
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger("PreprocessHelpers")

def ensure_dir(path: str):
    """Ensures that a directory exists."""
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(f"Failed to create directory {path}: {e}")
        raise

def get_stats(total, success, failed, start_time, end_time):
    """Prints processing statistics."""
    duration = round(end_time - start_time, 2)
    print("\n" + "="*40)
    print("PROCESSING STATISTICS")
    print("="*40)
    print(f"Total Images Found: {total}")
    print(f"Successfully Processed: {success}")
    print(f"Failed: {failed}")
    print(f"Total Time: {duration} seconds")
    print("="*40 + "\n")