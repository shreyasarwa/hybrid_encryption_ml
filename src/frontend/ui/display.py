import streamlit as st
from ui.uploader import render_uploader

def render_home():
    st.markdown("""
        <div class="glass-card">
            <h1 style='text-align: center;'>✨ VoxAI Dashboard</h1>
            <p style='text-align: center;'>Welcome to the Hybrid Encryption & ML Reconstruction Suite.</p>
            <hr>
            <p>Select a module from the sidebar to begin processing your image data.</p>
        </div>
    """, unsafe_allow_html=True)

def render_encryption_ui():
    st.markdown("<div class='glass-card'><h3>🔒 Encryption Module</h3></div>", unsafe_allow_html=True)
    img = render_uploader()
    if img:
        st.image(img, caption="Ready for Encryption", width=400)
        if st.button("Start Hybrid Encryption"):
            st.success("Encryption Process Started...")

def render_decryption_ui():
    st.markdown("<div class='glass-card'><h3>🔓 Decryption Module</h3></div>", unsafe_allow_html=True)
    st.info("Upload an encrypted .bin or image file to restore.")