import os
import time
from tqdm import tqdm
from src.preprocess.pre_helpers import ensure_dir, get_stats 
from src.preprocess.image_loader import load_image, get_image_list
from src.preprocess.resize_images import resize_image
from src.preprocess.normalize_images import normalize_image
from src.utils.logger import setup_logger

logger = setup_logger("Pipeline")

class PreprocessPipeline:
    def __init__(self, config):
        self.config = config
        ensure_dir(config['output_folder'])
        self.success_count = 0
        self.fail_count = 0

    def process_single_image(self, img_path):
        """Full pipeline for a single image."""
        try:
            filename = os.path.basename(img_path)
            
            # 1. Load
            img = load_image(img_path)
            if img is None: return None
            
            # 2. Resize
            img_resized = resize_image(img, self.config['image_size'])
            if img_resized is None: return None
            
            # 3. Normalize (Returning this for the return list)
            img_norm = normalize_image(img_resized)
            
            # 4. Save Processed (for visual verification and Stage 3 input)
            # Use OpenCV to save. Note: load_image converts BGR->RGB, 
            # so we must convert back to BGR for imwrite to save colors correctly.
            import cv2
            out_path = os.path.join(self.config['output_folder'], filename)
            save_status = cv2.imwrite(out_path, cv2.cvtColor(img_resized, cv2.COLOR_RGB2BGR))
            
            if save_status:
                self.success_count += 1
                return img_norm
            else:
                self.fail_count += 1
                return None
        except Exception as e:
            logger.error(f"Error processing {img_path}: {e}")
            self.fail_count += 1
            return None

    def run(self):
        """The missing method that executes the batch processing."""
        start_time = time.time()
        images = get_image_list(self.config['input_folder'], self.config['formats'])
        
        logger.info(f"Found {len(images)} images in {self.config['input_folder']}")
        
        processed_data = []
        for path in tqdm(images, desc="Processing Images"):
            result = self.process_single_image(path)
            if result is not None:
                processed_data.append(result)
        
        get_stats(len(images), self.success_count, self.fail_count, start_time, time.time())
        return processed_data