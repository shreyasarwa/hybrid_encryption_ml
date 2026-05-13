import matplotlib.pyplot as plt
import cv2

def plot_sample_pairs(X, y, num_samples=3):
    fig, axes = plt.subplots(num_samples, 2, figsize=(8, 4 * num_samples))
    for i in range(num_samples):
        # Convert BGR to RGB for plotting
        axes[i, 0].imshow(cv2.cvtColor((X[i]*255).astype('uint8'), cv2.COLOR_BGR2RGB))
        axes[i, 0].set_title(f"Encrypted Input (X_{i})")
        axes[i, 1].imshow(cv2.cvtColor((y[i]*255).astype('uint8'), cv2.COLOR_BGR2RGB))
        axes[i, 1].set_title(f"Ground Truth (y_{i})")
        for ax in axes[i]: ax.axis('off')
    plt.tight_layout()
    plt.show()