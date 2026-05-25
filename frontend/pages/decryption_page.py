import streamlit as st
from src.hybrid_crypto import chaotic_decrypt

def render_decryption():
    st.header("Chaotic Decryption")
    if 'chaos_encrypted_img' not in st.session_state:
        st.warning("Please upload and encrypt an image first.")
        return

    if st.button("Decrypt"):
        key = st.session_state['hybrid_key']
        encrypted = st.session_state['chaos_encrypted_img']
        decrypted = chaotic_decrypt(encrypted, key, 15.0)
        st.session_state['chaos_decrypted_img'] = decrypted
        st.image(decrypted, caption="Decrypted Image", width=400)