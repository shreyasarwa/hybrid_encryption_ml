import matplotlib.pyplot as plt
import cv2
import numpy as np

def plot_sample_pairs(X, y, num_samples=3):
    """
    Plots pairs of encrypted and original images for verification.
    """
    # Ensure we don't try to plot more samples than we have
    num_samples = min(num_samples, len(X))
    
    fig, axes = plt.subplots(num_samples, 2, figsize=(10, 4 * num_samples))
    
    # Handle the case of a single sample (axes is not a 2D array)
    if num_samples == 1:
        axes = np.expand_dims(axes, axis=0)

    for i in range(num_samples):
        # Convert BGR to RGB for correct Matplotlib display
        img_x = cv2.cvtColor((X[i] * 255).astype('uint8'), cv2.COLOR_BGR2RGB)
        img_y = cv2.cvtColor((y[i] * 255).astype('uint8'), cv2.COLOR_BGR2RGB)
        
        axes[i, 0].imshow(img_x)
        axes[i, 0].set_title(f"Encrypted Input (X[{i}])")
        axes[i, 0].axis('off')
        
        axes[i, 1].imshow(img_y)
        axes[i, 1].set_title(f"Ground Truth (y[{i}])")
        axes[i, 1].axis('off')
        
    plt.tight_layout()
    plt.show()