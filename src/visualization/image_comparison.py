import matplotlib.pyplot as plt
import cv2
import numpy as np

def plot_results(encrypted, original, reconstructed, save_path):
    n = min(4, len(encrypted))
    plt.figure(figsize=(12, 8))
    for i in range(n):
        # Encrypted
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(cv2.cvtColor(encrypted[i], cv2.COLOR_BGR2RGB))
        plt.title("Encrypted")
        plt.axis("off")

        # Original
        ax = plt.subplot(3, n, i + 1 + n)
        plt.imshow(cv2.cvtColor(original[i], cv2.COLOR_BGR2RGB))
        plt.title("Original")
        plt.axis("off")

        # Reconstructed
        ax = plt.subplot(3, n, i + 1 + 2*n)
        plt.imshow(cv2.cvtColor(reconstructed[i], cv2.COLOR_BGR2RGB))
        plt.title("Reconstructed")
        plt.axis("off")
        
    plt.savefig(save_path)
    plt.close()