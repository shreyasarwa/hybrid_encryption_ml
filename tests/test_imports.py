import pytest

def test_critical_imports():
    try:
        import numpy
        import cv2
        import tensorflow
        import sklearn
        import streamlit
        import yaml
    except ImportError as e:
        pytest.fail(f"Critical import failed: {e}")

def test_local_imports():
    try:
        from src.utils.logger import setup_logger
        from src.utils.config_loader import load_config
    except ImportError as e:
        pytest.fail(f"Local module import failed: {e}")