import matplotlib.pyplot as plt
import cv2
import numpy as np

def visualize_encryption_results(original_path, encrypted_path):
    """Displays original vs encrypted side-by-side with histograms."""
    orig = cv2.cvtColor(cv2.imread(original_path), cv2.COLOR_BGR2RGB)
    enc = cv2.cvtColor(cv2.imread(encrypted_path), cv2.COLOR_BGR2RGB)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Row 1: Images
    axes[0, 0].imshow(orig)
    axes[0, 0].set_title("Original (Processed)")
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(enc)
    axes[0, 1].set_title("Permutation Encrypted")
    axes[0, 1].axis('off')
    
    # Row 2: Histograms
    axes[1, 0].hist(orig.ravel(), bins=256, color='blue', alpha=0.7)
    axes[1, 0].set_title("Original Histogram")
    
    axes[1, 1].hist(enc.ravel(), bins=256, color='red', alpha=0.7)
    axes[1, 1].set_title("Encrypted Histogram")
    
    plt.tight_layout()
    plt.show()