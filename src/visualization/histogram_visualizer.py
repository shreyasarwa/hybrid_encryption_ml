import matplotlib.pyplot as plt
import seaborn as sns
import cv2

def plot_histogram_comparison(img_dict, save_path):
    """Plots pixel intensity distribution for statistical analysis."""
    plt.figure(figsize=(15, 6))
    colors = ['blue', 'red', 'green', 'purple']
    keys = ['orig', 'enc', 'dec', 'rec']
    labels = ['Original', 'Encrypted', 'Decrypted', 'Reconstructed']
    
    for i, key in enumerate(keys):
        img = img_dict[key]
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        sns.kdeplot(img.flatten(), label=labels[i], color=colors[i], fill=True)
        
    plt.title("Pixel Intensity Distribution Comparison", fontsize=16)
    plt.xlabel("Pixel Value (0-255)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig(save_path, dpi=300)
    plt.close()