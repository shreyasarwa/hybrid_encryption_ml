from datetime import datetime
from src.utils.file_handler import save_json

def generate_metadata(filename, shape, entropy, time_taken, config):
    meta = {
        "filename": filename,
        "timestamp": datetime.now().isoformat(),
        "shape": list(shape),
        "entropy": float(entropy),
        "processing_time": time_taken,
        "parameters": config
    }
    return meta