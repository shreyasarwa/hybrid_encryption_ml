import streamlit as st

def render_navbar():
    # Modern Horizontal Navigation
    cols = st.columns([1, 1, 1, 1, 1, 1])
    pages = ["Home", "Encryption", "Decryption", "CNN Reconstruction", "Evaluation", "Analytics"]
    
    for i, page in enumerate(pages):
        if cols[i].button(page, use_container_width=True):
            st.session_state.current_page = page
    st.markdown("<br>", unsafe_allow_html=True)