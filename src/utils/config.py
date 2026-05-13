import os
from pathlib import Path

CONFIG = {
    "PATHS": {
        "ORIGINAL": "datasets/processed/",
        "ENCRYPTED": "datasets/final_encrypted/",
        "DECRYPTED": "datasets/decrypted/",
        "RECONSTRUCTED": "datasets/reconstructed/",
        "OUTPUT_BASE": "outputs/evaluations/"
    },
    "SUBDIRS": [
        "comparison_images",
        "plots",
        "reports",
        "tables",
        "metrics_json"
    ],
    "METRICS": {
        "SSIM_WIN_SIZE": 3,
        "DPI": 300,
        "IMG_SIZE": (64, 64)
    }
}

def get_eval_path(subfolder):
    path = Path(CONFIG["PATHS"]["OUTPUT_BASE"]) / subfolder
    path.mkdir(parents=True, exist_ok=True)
    return path