import os
from PIL import Image
from tqdm import tqdm
from src.utils.logger import setup_logger

logger = setup_logger("ImageSaver")

# CIFAR-10 Class names mapping
CLASS_NAMES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer', 
    'dog', 'frog', 'horse', 'ship', 'truck'
]

def save_images_to_disk(x_data, y_data, output_folder="datasets/raw", num_images=100, img_format="png"):
    """
    Saves NumPy arrays as physical image files.
    Format: classname_index.png
    """
    try:
        logger.info(f"Saving {num_images} images to {output_folder}...")
        
        for i in tqdm(range(min(num_images, len(x_data))), desc="Saving Images"):
            # Extract image and label index
            img_array = x_data[i]
            label_idx = y_data[i][0]
            class_name = CLASS_NAMES[label_idx]
            
            # Construct filename
            file_name = f"{class_name}_{i}.{img_format}"
            file_path = os.path.join(output_folder, file_name)
            
            # Convert NumPy array (uint8) to PIL Image
            img = Image.fromarray(img_array)
            img.save(file_path)
            
        logger.info(f"Successfully saved {num_images} images.")
    except Exception as e:
        logger.error(f"Error while saving images: {e}")
        raise