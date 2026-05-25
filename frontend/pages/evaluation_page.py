import streamlit as st
import numpy as np
from PIL import Image

def calculate_metrics(img1, img2):
    im1 = np.array(img1).astype(np.float64)
    im2 = np.array(img2).astype(np.float64)
    mse = np.mean((im1 - im2) ** 2)
    if mse == 0: return 100, 1.0
    psnr = 20 * np.log10(255.0 / np.sqrt(mse))
    # Simple accuracy mapping based on PSNR thresholds
    accuracy = min(100, (psnr / 35) * 100) 
    return psnr, accuracy

def render_evaluation():
    st.markdown("<div class='glass-card'><h2>⚖️ Integrity Evaluation</h2></div>", unsafe_allow_html=True)

    if 'ml_reconstructed_img' not in st.session_state:
        st.warning("⚠️ No data found. Please run the 'CNN Reconstruction' stage first.")
        return

    orig = st.session_state['original_img']
    recon = st.session_state['ml_reconstructed_img']

    psnr_val, acc_val = calculate_metrics(orig, recon)

    # Modern Metric Cards
    m1, m2, m3 = st.columns(3)
    m1.metric("PSNR Score", f"{psnr_val:.2f} dB", delta="Target: >30dB")
    m2.metric("Reconstruction Accuracy", f"{acc_val:.1f}%", delta="High Fidelity")
    m3.metric("MSE (Error)", f"{np.mean((np.array(orig)-np.array(recon))**2):.2f}", delta_color="inverse")

    st.markdown("### Visual Side-by-Side Comparison")
    st.image([orig, recon], caption=["Original", "AI Reconstructed"], width=350)