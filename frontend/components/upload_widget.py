import streamlit as st

# Add 'label' as a parameter with a default value
def render_upload_widget(label="Upload Image"):
    uploaded_file = st.file_uploader(label, type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        return uploaded_file
    return None