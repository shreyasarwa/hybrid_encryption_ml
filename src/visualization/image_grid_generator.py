import matplotlib.pyplot as plt
import numpy as np

def generate_comparison_grid(img_dict, save_path):
    """Generates a publication-ready comparison grid."""
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    titles = [
        "Original", "Encrypted (Hybrid)", 
        "Decrypted (AES/Chaos)", "ML Reconstruction"
    ]
    keys = ['orig', 'enc', 'dec', 'rec']
    
    for i, key in enumerate(keys):
        axes[i].imshow(img_dict[key])
        axes[i].set_title(titles[i], fontsize=14, fontweight='bold')
        axes[i].axis('off')
        
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()