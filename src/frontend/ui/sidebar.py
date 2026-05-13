import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: #6d6d6d;'>🛡️ VoxAI</h1>", unsafe_allow_html=True)
        st.markdown("---")
        selection = st.radio(
            "Navigation",
            ["Home", "Encrypt", "Decrypt", "ML Reconstruction", "Metrics"]
        )
        return selection