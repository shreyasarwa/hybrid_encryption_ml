from skimage.metrics import structural_similarity as ssim
import cv2

def calculate_ssim(img1, img2):
    """Calculates Structural Similarity Index."""
    # SSIM requires grayscale or channel_axis specification
    multichannel = len(img1.shape) == 3
    
    score, _ = ssim(
        img1, img2, 
        full=True, 
        channel_axis=2 if multichannel else None,
        data_range=255
    )
    return float(score)