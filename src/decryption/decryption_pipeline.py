# This file serves as a wrapper for batch processing if needed by main.py
from src.decryption.hybrid_decryptor import HybridDecryptor

class DecryptionPipeline:
    def __init__(self, config):
        self.decryptor = HybridDecryptor(r_value=config.get("LOGISTIC_R", 3.99))
    
    def run(self, encrypted_img, p_key, x_key, x0):
        return self.decryptor.decrypt(encrypted_img, p_key, x_key, x0)