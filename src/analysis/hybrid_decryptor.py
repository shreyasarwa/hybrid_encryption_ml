import time
from src.decryption.reverse_chaos import reverse_chaos
from src.decryption.reverse_xor import reverse_xor
from src.decryption.reverse_permutation import reverse_permutation

class HybridDecryptor:
    def __init__(self, r_value):
        self.r = r_value

    def decrypt(self, img, p_key, x_key, x0):
        start = time.time()
        
        # Step 1: Reverse Chaos
        step1 = reverse_chaos(img, x0, self.r)
        
        # Step 2: Reverse XOR
        step2 = reverse_xor(step1, x_key)
        
        # Step 3: Reverse Permutation
        final = reverse_permutation(step2, p_key)
        
        return final, (time.time() - start)