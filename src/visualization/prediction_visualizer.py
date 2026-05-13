import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

def save_reconstruction_grid(X_test, y_test, predictions, save_path, n=5):
    """Generates a side-by-side comparison grid."""
    plt.figure(figsize=(15, 3 * n))
    for i in range(n):
        # Encrypted
        plt.subplot(n, 3, i*3 + 1)
        plt.imshow(cv2.cvtColor((X_test[i]*255).astype('uint8'), cv2.COLOR_BGR2RGB))
        plt.title("Encrypted")
        plt.axis('off')
        
        # Predicted
        plt.subplot(n, 3, i*3 + 2)
        plt.imshow(cv2.cvtColor((predictions[i]*255).astype('uint8'), cv2.COLOR_BGR2RGB))
        plt.title("Reconstructed")
        plt.axis('off')
        
        # Original
        plt.subplot(n, 3, i*3 + 3)
        plt.imshow(cv2.cvtColor((y_test[i]*255).astype('uint8'), cv2.COLOR_BGR2RGB))
        plt.title("Ground Truth")
        plt.axis('off')
        
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()