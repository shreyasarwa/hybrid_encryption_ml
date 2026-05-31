# Machine Learning Analysis of Hybrid Image Encryption and Decryption System

---

(https://hybridencryptionml.streamlit.app)

---

An advanced, production-ready cybersecurity and deep learning pipeline designed to protect digital imagery using layered cryptographic primitives, followed by neural network-driven image restoration. 

This project implements a multi-stage approach combining classical permutation-diffusion architectures with Modern Convolutional Autoencoders to analyze, encrypt, decrypt, and visually reconstruct high-resolution images.

---

##  Project Architecture & Complete Stage Breakdown

The system is engineered as a sequential pipeline divided into distinct operational modules. Each stage handles a dedicated layer of data processing, security enforcement, or machine learning evaluation.

[Input Image] ──> (Stage 1: Preprocessing) ──> (Stage 2: Permutation)
                                                      │
(Stage 5: Autoencoder) <── (Stage 4: Decryption) <── (Stage 3: XOR Diffusion)
         │
         └──> (Stage 6: Evaluation & Metrics) ──> [Streamlit Dashboard]

### Stage 1: Image Preprocessing System
Before any cryptographic transformations occur, images must be normalized to ensure deterministic matrix math operations and stable neural network convergence.
* **Dimensions & Alignment:** Standardizes input imagery into consistent spatial dimensions (e.g., $256 \times 256$ pixels).
* **Channel Management:** Handles multi-channel color arrays (RGB) as well as single-channel grayscale transformations.
* **Data Normalization:** Scales pixel intensity values from integer boundaries $[0, 255]$ into floating-point tensors mapped across $[0, 1]$ or $[-1, 1]$.

### Stage 2: Permutation Encryption Layer
The first layer of defense breaks the strong spatial correlation naturally present between neighboring pixels in an ordinary image.
* **Matrix Scrambling:** Rearranges the spatial coordinates $(x, y)$ of pixels across the image matrix based on chaotic maps or pseudo-random index arrays.
* **Information Dissipation:** While the total histogram count of colors remains identical, the recognizable features of the original image are completely scrambled into visual noise.

### Stage 3: XOR Diffusion Layer (Hybridization)
Permutation alone is vulnerable to plain-text attacks. The diffusion layer modifies the actual pixel values themselves to maximize security.
* **Bitwise Manipulation:** Executes high-speed, element-wise XOR ($\oplus$) math operations across the scrambled pixel matrices using dynamically generated security keys.
* **Avalanche Effect:** Altering a single bit in the original image or key causes a cascading, radical change throughout the entire encrypted output image file.

### Stage 4: Cryptographic Decryption Layer
The exact mirror inverse of the encryption modules, responsible for processing incoming secured cipher-images back into readable arrays.
* **Inverse Diffusion:** Strips the bitwise keys by applying the reverse XOR operations.
* **Inverse Permutation:** Unscrambles the spatial coordinate map back into its original geometry using the corresponding structural security tokens.

### Stage 5: CNN Autoencoder Reconstruction
Even with exact keys, cryptographic decryption over unshielded channels can suffer from transmission noise, data loss, or compression artifacts. This system introduces deep learning to reconstruct and clean the output.
* **Encoder Network:** Compresses the decrypted image down into a low-dimensional bottleneck (latent space representation), capturing only the core structural features.
* **Decoder Network:** Reconstructs the image back to its original shape, filtering out cryptographic high-frequency noise and structural artifacts.
* **Optimization:** Trained via Backpropagation minimizing Mean Squared Error ($MSE$) to guarantee pristine pixel-level accuracy.

### Stage 6: Advanced Evaluation Metrics
Quantifiable performance benchmarks are automatically executed to mathematically evaluate both security strength and machine learning reconstruction fidelity.
* **Security Metrics:** Calculates Information Entropy ($H \approx 8$ for perfect randomness), Correlation Coefficients (aiming for $0$ between adjacent pixels), and Pixel Change Rate ($NPCR$ / $UACI$).
* **Reconstruction Metrics:** Computes Peak Signal-to-Noise Ratio ($PSNR$) and Structural Similarity Index ($SSIM$) to verify structural perfection.

### Stage 7: Streamlit Frontend & Analytical Visualization
A modern, web-based graphical interface that abstracts the underlying python execution scripts into an interactive dashboard.
* **Real-time Processing:** Drag-and-drop raw image files to view live encryption, decryption, and model output pipelines side-by-side.
* **Visual Analytics:** Interactive plotting of structural image histograms, training loss curves, and evaluation tables.

---

##  Installation & Workspace Setup

### Prerequisites
* **Operating System:** Windows 10/11, macOS, or Linux
* **Python Runtime:** Python 3.10 or higher installed on your system path
* **Hardware Accelerator (Optional):** NVIDIA GPU with CUDA support for accelerated model training

### Step-by-Step Environment Deployment
Open your terminal or command prompt, navigate to your desired directory workspace, and run the following commands:

```bash
# 1. Clone or create the project folder and step inside
mkdir machine_learning_project
cd machine_learning_project

# 2. Create an isolated virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Upgrade core package installer tools
python -m pip install --upgrade pip

# 5. Install all foundational framework requirements
pip install -r requirements.txt
