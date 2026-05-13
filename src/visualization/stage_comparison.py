import matplotlib.pyplot as plt
import cv2

def plot_stages(original, stages):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    axes[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    
    titles = ["Permutation", "XOR", "Final (Chaos)"]
    for i, stage_img in enumerate(stages):
        axes[i+1].imshow(cv2.cvtColor(stage_img, cv2.COLOR_BGR2RGB))
        axes[i+1].set_title(titles[i])
        
    for ax in axes: ax.axis('off')
    plt.tight_layout()
    plt.show()