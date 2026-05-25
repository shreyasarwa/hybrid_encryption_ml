import streamlit as st
import sys
import os

# Root path fix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from frontend.pages.encryption_page import render_encryption
from frontend.pages.decryption_page import render_decryption
from frontend.pages.reconstruction_page import render_reconstruction
from frontend.pages.evaluation_page import render_evaluation

def main():
    st.set_page_config(page_title="Hybrid Crypto AI", layout="wide")
    
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
        .nav-container { display: flex; justify-content: center; gap: 10px; margin-bottom: 25px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("Advanced Hybrid Cryptosystem")

    # Navigation Logic
    if 'page' not in st.session_state: st.session_state.page = "Encryption"
    
    cols = st.columns(4)
    if cols[0].button("Encryption", use_container_width=True): st.session_state.page = "Encryption"
    if cols[1].button("Decryption", use_container_width=True): st.session_state.page = "Decryption"
    if cols[2].button("AI Reconstruction", use_container_width=True): st.session_state.page = "Reconstruction"
    if cols[3].button("Evaluation", use_container_width=True): st.session_state.page = "Evaluation"

    if st.session_state.page == "Encryption": render_encryption()
    elif st.session_state.page == "Decryption": render_decryption()
    elif st.session_state.page == "Reconstruction": render_reconstruction()
    elif st.session_state.page == "Evaluation": render_evaluation()

if __name__ == "__main__":
    main()