import streamlit as st

def apply_glassmorphism():
    st.markdown("""
        <style>
        /* Global Background */
        .stApp {
            background-color: #F8F9FA;
        }

        /* Glassmorphism Containers */
        .glass-card {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 2.5rem;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }

        /* Pastel Buttons */
        .stButton>button {
            border-radius: 8px;
            border: none;
            background-color: #E9ECEF;
            color: #495057;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .stButton>button:hover {
            background-color: #BDE0FE !important;
            color: white !important;
            transform: scale(1.02);
        }

        /* Status Box */
        .metric-box {
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-size: 0.9rem;
            font-weight: 600;
            color: white;
        }

        /* Animations */
        .fade-in { animation: fadeIn 1s; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        </style>
    """, unsafe_allow_html=True)