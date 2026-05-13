import matplotlib.pyplot as plt
import numpy as np

def plot_logistic_sequence(sequence, title="Logistic Map Sequence"):
    """Visualizes the chaotic nature of the sequence."""
    plt.figure(figsize=(10, 4))
    plt.plot(sequence[:100], marker='o', linestyle='-', markersize=2)
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()