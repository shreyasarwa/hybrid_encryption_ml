import os
import numpy as np
from PIL import Image
# Import your actual encryption logic here
# from src.encryption import chaotic_encrypt, chaotic_decrypt 

def prepare_dataset():
    raw_path = "datasets/raw"
    processed_path = "datasets/processed"
    os.makedirs(processed_path, exist_ok=True)
    
    files = [f for f in os.listdir(raw_path) if f.endswith(('.png', '.jpg'))]
    print(f"Transforming {len(files)} images into fuzzy training pairs...")

    for f in files:
        img = Image.open(os.path.join(raw_path, f)).convert('RGB').resize((64, 64))
        
        # SIMULATION: Replace this with your actual Stage 1 Decryption logic
        # For now, we simulate the "Fuzzy" output the CNN sees
        img_array = np.array(img)
        noise = np.random.normal(0, 15, img_array.shape).astype(np.uint8)
        fuzzy_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        
        fuzzy_img = Image.fromarray(fuzzy_array)
        fuzzy_img.save(os.path.join(processed_path, f))

if __name__ == "__main__":
    prepare_dataset()