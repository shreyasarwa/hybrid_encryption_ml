import os
import json
from pathlib import Path

def ensure_directories(dirs_dict):
    for path in dirs_dict.values():
        Path(path).mkdir(parents=True, exist_ok=True)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)