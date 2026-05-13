import streamlit as st
from PIL import Image

def render_uploader():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        return Image.open(uploaded_file)
    return None