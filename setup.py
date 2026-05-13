from setuptools import setup, find_packages

setup(
    name="hybrid_encryption_ml",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "tensorflow",
        "pyyaml",
    ],
)