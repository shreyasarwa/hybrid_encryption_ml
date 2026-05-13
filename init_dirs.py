import os
from pathlib import Path

def create_structure():
    dirs = [
        "app", "config", "docs", "logs", "notebooks", "tests",
        "datasets/raw", "datasets/processed", "datasets/encrypted", 
        "datasets/decrypted", "datasets/train", "datasets/test", "datasets/validation",
        "outputs/images", "outputs/models", "outputs/metrics", "outputs/reports",
        "src/encryption", "src/decryption", "src/ml_models", 
        "src/preprocessing", "src/utils", "src/evaluation", "src/visualization"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(d, "__init__.py")).touch() if "src" in d or "tests" in d else None
    print("✅ Project structure initialized.")

if __name__ == "__main__":
    create_structure()