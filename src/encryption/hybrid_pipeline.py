import time
from src.encryption.permutation import apply_permutation
from src.encryption.xor_encryption import apply_xor
from src.encryption.chaos import apply_chaos
from src.analysis.entropy_analysis import calculate_entropy

class HybridPipeline:
    def __init__(self, config):
        self.config = config

    def encrypt(self, img):
        start = time.time()
        
        # 1. Permutation
        img_p, p_key = apply_permutation(img, self.config['RANDOM_SEED'])
        
        # 2. XOR
        img_x, x_key = apply_xor(img_p, self.config['RANDOM_SEED'] + 1)
        
        # 3. Chaos
        img_final, c_mask = apply_chaos(img_x, self.config['CHAOS_X0'], self.config['CHAOS_R'])
        
        end = time.time()
        
        return {
            "image": img_final,
            "stages": [img_p, img_x, img_final],
            "keys": {"p": p_key, "x": x_key},
            "entropy": calculate_entropy(img_final),
            "time": end - start
        }