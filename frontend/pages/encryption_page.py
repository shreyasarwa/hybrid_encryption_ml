import streamlit as st
from PIL import Image
from src.hybrid_crypto import chaotic_encrypt

def render_encryption():
    with st.container():
        st.subheader("Upload & Secure")
        
        uploaded = st.file_uploader("Drop your image here", type=['png', 'jpg', 'jpeg'])
        
        if uploaded:
            # Model needs 64x64
            img = Image.open(uploaded).convert("RGB").resize((64, 64))
            st.session_state['original_img'] = img
            
            c1, c2 = st.columns(2)
            with c1:
                st.image(img, caption="Original Input", width=400)
            
            with c2:
                key = st.number_input("Chaos Key (Seed)", value=0.357123, format="%.6f")
                st.session_state['hybrid_key'] = key
                
                if st.button("Execute Encryption", use_container_width=True):
                    enc = chaotic_encrypt(img, key, 15.0)
                    st.session_state['chaos_encrypted_img'] = enc
                    st.success("Image Encrypted Successfully!")
            
            if 'chaos_encrypted_img' in st.session_state:
                st.image(st.session_state['chaos_encrypted_img'], caption="Encrypted Result", width=400)