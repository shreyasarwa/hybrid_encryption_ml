import matplotlib.pyplot as plt
import cv2

def plot_decryption_result(encrypted, decrypted):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(cv2.cvtColor(encrypted, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Encrypted Input")
    axes[1].imshow(cv2.cvtColor(decrypted, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Decrypted Output")
    for ax in axes: ax.axis('off')
    plt.show()