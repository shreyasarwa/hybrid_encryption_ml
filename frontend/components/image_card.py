import streamlit as st

def display_image_card(image, title, key_val=None):
    """UI card for images."""
    st.markdown(f"### {title}")
    st.image(image, use_container_width=True)
    if key_val:
        st.info(f"Key: `{key_val}`")

def display_image_comparison(original, processed, title_orig="Input", title_proc="Output"):
    col1, col2 = st.columns(2)
    with col1:
        st.caption(title_orig)
        st.image(original, use_container_width=True)
    with col2:
        st.caption(title_proc)
        st.image(processed, use_container_width=True)