import streamlit as st
from PIL import Image

def render_home():
    st.title("🏠 Hybrid Image Cryptosystem")
    st.write("Upload an image to begin the three-stage protection process.")
    
    uploaded = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = Image.open(uploaded).convert("RGB").resize((64, 64))
        st.session_state['original_img'] = img
        st.image(img, caption="Ready for Processing", width=200)