import streamlit as st
from ui.uploader import render_uploader

def render_home():  # Ensure no typos here
    st.markdown("""
        <div class="glass-card">
            <h1 style='text-align: center;'>✨ VoxAI Dashboard</h1>
            <p style='text-align: center;'>Hybrid Encryption & ML Reconstruction Suite</p>
            <hr>
            <p>Welcome, Shreya. Select a module from the sidebar to begin.</p>
        </div>
    """, unsafe_allow_html=True)

def render_encryption_ui():
    st.markdown("<div class='glass-card'><h3>🔒 Encryption Module</h3></div>", unsafe_allow_html=True)
    img = render_uploader()
    if img:
        st.image(img, caption="Original Stream", width=400)
        if st.button("Generate Ciphertext"):
            st.success("Processing...")

def render_decryption_ui():
    st.markdown("<div class='glass-card'><h3>🔓 Decryption Module</h3></div>", unsafe_allow_html=True)
    st.info("Awaiting encrypted data...")