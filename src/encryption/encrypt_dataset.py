import os
import cv2
import time
from tqdm import tqdm
from src.encryption.permutation import encrypt_image
from src.encryption.key_generator import generate_permutation_key, save_key
from src.encryption.permutation_utils import ensure_directory, get_image_paths, validate_image_array
from src.utils.logger import setup_logger

logger = setup_logger("DatasetEncryptor")

def encrypt_dataset(config):
    """Batch encrypts images from processed folder to encrypted folder."""
    ensure_directory(config['OUTPUT_FOLDER'])
    ensure_directory(config['KEY_FOLDER'])
    
    img_paths = get_image_paths(config['INPUT_FOLDER'], config['SUPPORTED_FORMATS'])
    total_imgs = len(img_paths)
    success = 0
    failed = 0
    
    start_time = time.time()
    
    for path in tqdm(img_paths, desc="Encrypting Dataset"):
        try:
            filename = os.path.basename(path)
            img = cv2.imread(path)
            
            if not validate_image_array(img):
                failed += 1
                continue
                
            # Create a unique key/seed per image or use fixed seed per project
            # Here we use fixed seed to simplify for Stage 3, but allow scalability
            img_size_flat = img.size
            key = generate_permutation_key(img_size_flat, config['RANDOM_SEED'])
            
            # Encrypt
            encrypted_img = encrypt_image(img, key)
            
            if encrypted_img is not None:
                # Save Encrypted Image
                out_path = os.path.join(config['OUTPUT_FOLDER'], filename)
                cv2.imwrite(out_path, encrypted_img)
                
                # Save Key for this image
                key_name = f"{os.path.splitext(filename)[0]}_key.npy"
                save_key(key, os.path.join(config['KEY_FOLDER'], key_name))
                
                success += 1
            else:
                failed += 1
                
        except Exception as e:
            logger.error(f"Error encrypting {path}: {e}")
            failed += 1
            
    end_time = time.time()
    
    logger.info(f"Encryption Complete: {success} Success, {failed} Failed.")
    logger.info(f"Total Time Taken: {round(end_time - start_time, 2)}s")