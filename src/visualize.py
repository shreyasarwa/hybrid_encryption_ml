import matplotlib.pyplot as plt
from src.save_images import CLASS_NAMES

def visualize_samples(x_data, y_data, num_samples=9):
    """
    Displays a grid of images with their corresponding labels.
    """
    plt.figure(figsize=(10, 10))
    for i in range(num_samples):
        plt.subplot(3, 3, i + 1)
        plt.imshow(x_data[i])
        label_idx = y_data[i][0]
        plt.title(CLASS_NAMES[label_idx])
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()