import streamlit as st

def apply_pastel_theme():
    """Applies modern pastel glassmorphism CSS for the Hybrid Encryption project."""
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #FAD0C4 0%, #FFD1FF 100%);
            }
            .glass-card {
                background: rgba(255, 255, 255, 0.4);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 25px;
                border: 1px solid rgba(255, 255, 255, 0.3);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
                margin-bottom: 20px;
                color: #4A4A4A;
            }
            .stButton>button {
                background-color: #BDE0FE;
                color: #4A4A4A;
                border-radius: 12px;
                border: none;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #A2D2FF;
                transform: translateY(-2px);
            }
        </style>
    """, unsafe_allow_html=True)