import numpy as np
from PIL import Image
import logging

# Assuming your backend logic is in src/backend/encryption/
# from backend.encryption.engine import chaotic_shuffle, aes_encrypt

def perform_encryption(image_pil):
    """
    Middleware service to handle the hybrid encryption pipeline.
    """
    try:
        logging.info("Starting encryption pipeline...")
        
        # 1. Convert PIL to NumPy for processing
        img_array = np.array(image_pil)
        
        # 2. Placeholder for your Backend Logic 
        # (Replace these with your actual chaotic map functions)
        # encrypted_array = chaotic_shuffle(img_array)
        # final_cipher = aes_encrypt(encrypted_array)
        
        # MOCK TRANSFORMATION FOR TESTING
        # Shuffling the array to simulate encryption
        encrypted_array = np.copy(img_array)
        np.random.shuffle(encrypted_array) 
        
        logging.info("Encryption successful.")
        return Image.fromarray(encrypted_array)
        
    except Exception as e:
        logging.error(f"Encryption Service Error: {str(e)}")
        return None