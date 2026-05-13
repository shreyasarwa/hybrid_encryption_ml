from src.encryption.permutation import permutation_encrypt_image
from src.encryption.xor_encryption import xor_encrypt_image
from src.utils.logger import setup_logger

logger = setup_logger("HybridEncryptor")

def hybrid_encrypt_image(img_array, p_key, x_key):
    """Executes the Two-Step Hybrid Workflow."""
    
    # Step 1: Permutation (Confusion)
    permuted_img = permutation_encrypt_image(img_array, p_key)
    if permuted_img is None: return None
    
    # Step 2: XOR (Diffusion)
    hybrid_img = xor_encrypt_image(permuted_img, x_key)
    
    return hybrid_img, permuted_img