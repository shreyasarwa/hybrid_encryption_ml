import streamlit as st
from PIL import Image
import io
import os
import numpy as np
from src.hybrid_crypto.py import generate_key_and_map

def render_home():
    st.markdown("<div class='glass-card'><h2>Stage 0: Secure Upload & Key Generation</h2><p>Provide the original image to begin the secure hybrid encryption sequence.</p></div>", unsafe_allow_html=True)
    
    # 1. Upload Widget
    uploaded_file = st.file_uploader("Choose a raw image file...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        # Store essential data for the entire session
        st.session_state['original_img'] = image
        st.session_state['image_data'] = np.array(image)
        
        # 2. Automatically Generate Key and Chaotic Map
        key, map_data = generate_key_and_map()
        st.session_state['hybrid_key'] = key
        st.session_state['chaotic_map'] = map_data
        
        st.success(f"Image Uploaded! A 256-bit Secure Key has been generated for this session.")
        st.markdown("Please proceed to **Stage 1: Encryption** from the sidebar.")