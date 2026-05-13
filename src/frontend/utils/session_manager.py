import streamlit as st

def init_session():
    """Persists data across different navigation pages."""
    keys = ['original_img', 'enc_img', 'dec_img', 'recon_img', 'metrics']
    for key in keys:
        if key not in st.session_state:
            st.session_state[key] = None