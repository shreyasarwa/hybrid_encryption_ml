import streamlit as st
import sys
import os

# Absolute path fixing for modular imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from ui.styles import apply_pastel_theme
from ui.sidebar import render_sidebar
from ui.display import render_home, render_encryption_ui, render_decryption_ui
from utils.session_manager import init_session

# ... rest of your main() function