import matplotlib.pyplot as plt

def compare_histograms(orig, chaos, title="Histogram Comparison"):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(orig.ravel(), bins=256, color='blue', alpha=0.6)
    axes[0].set_title("Input Histogram")
    axes[1].hist(chaos.ravel(), bins=256, color='red', alpha=0.6)
    axes[1].set_title("Chaos Encrypted Histogram")
    plt.show()