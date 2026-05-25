import numpy as np
from PIL import Image

def chaotic_encrypt(img, key, noise_intensity=15.0):
    """
    Stage 1: Hybrid Encryption
    Combines a structural permutation with a controlled chaos noise layer.
    """
    # 1. Convert image to numpy array for processing
    img_array = np.array(img).astype(np.float32)
    
    # 2. Structural Scrambling (Permutation)
    # This rearranges pixels so the image is unrecognizable
    permuted = np.flipud(img_array)
    
    # 3. Controlled Chaos Noise (Diffusion)
    # Using a float for noise_intensity fixes the 'dict' TypeError
    np.random.seed(int(key * 1000000))
    noise = np.random.normal(0, noise_intensity, img_array.shape)
    
    # 4. Final Ciphertext Generation
    # We clip values to 0-255 to keep it a valid image
    diffused = np.clip(permuted + noise, 0, 255).astype(np.uint8)
    
    return Image.fromarray(diffused)

def chaotic_decrypt(encrypted_img, key, noise_intensity=15.0):
    """
    Stage 2: Chaotic Decryption
    Removes the chaos layer to produce a 'Fuzzy' image ready for the CNN.
    """
    enc_array = np.array(encrypted_img).astype(np.float32)
    
    # Generate the exact same noise pattern using the key
    np.random.seed(int(key * 1000000))
    noise = np.random.normal(0, noise_intensity, enc_array.shape)
    
    # 1. Inverse Diffusion (Remove Noise)
    # This leaves a 'Fuzzy' result that the CNN will clean up
    decrypted_array = np.clip(enc_array - noise, 0, 255).astype(np.uint8)
    
    # 2. Inverse Permutation (Restore Structure)
    original_structure = np.flipud(decrypted_array)
    
    return Image.fromarray(original_structure)