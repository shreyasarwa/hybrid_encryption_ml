import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

def render_reconstruction():
    st.header("CNN Reconstruction Stage")
    
    if 'chaos_decrypted_img' not in st.session_state:
        st.warning("Complete Decryption first.")
        return

    if st.button("Recover Original Features", use_container_width=True):
        try:
            # compile=False avoids indexing errors
            model = tf.keras.models.load_model('models/saved_models/final_autoencoder.h5', compile=False)
            
            # Prepare image for CNN
            img = st.session_state['chaos_decrypted_img'].resize((64, 64))
            img_array = np.array(img).astype('float32') / 255.0
            img_batch = np.expand_dims(img_array, axis=0) # (1, 64, 64, 3)
            
            # Predict
            pred = model.predict(img_batch)[0]
            final_img = Image.fromarray((pred * 255).astype('uint8'))
            
            # Save for Evaluation
            st.session_state['ml_reconstructed_img'] = final_img
            
            st.image(final_img, caption="Cleaned Output", width=450)
            st.success("Reconstruction success! Check Evaluation tab for PSNR.")
        except Exception as e:
            st.error(f"Reconstruction Error: {e}")