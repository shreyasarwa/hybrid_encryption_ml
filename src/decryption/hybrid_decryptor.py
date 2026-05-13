import time
import numpy as np
from src.decryption.reverse_chaos import reverse_chaos
from src.decryption.reverse_xor import reverse_xor
from src.decryption.reverse_permutation import reverse_permutation

class HybridDecryptor:
    def __init__(self, r_value=3.99):
        self.r = r_value

    def decrypt(self, img, p_key, x_key, x0):
        """
        Executes decryption in exact reverse order of encryption:
        Chaos Masking -> XOR -> Permutation
        """
        start_time = time.time()
        
        # Step 1: Reverse Chaos (Masking)
        step1 = reverse_chaos(img, x0, self.r)
        
        # Step 2: Reverse XOR Encryption
        step2 = reverse_xor(step1, x_key)
        
        # Step 3: Reverse Permutation (Pixel shuffling)
        decrypted_img = reverse_permutation(step2, p_key)
        
        duration = time.time() - start_time
        return decrypted_img, duration