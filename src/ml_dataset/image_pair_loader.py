import os
import cv2
import numpy as np
from tqdm import tqdm

class ImagePairLoader:
    def __init__(self, config):
        self.config = config

    def load_pairs(self):
        X, y, filenames = [], [], []
        enc_folder = self.config["DIRS"]["ENCRYPTED"]
        org_folder = self.config["DIRS"]["ORIGINAL"]
        
        enc_files = [f for f in os.listdir(enc_folder) if f.lower().endswith(self.config["SUPPORTED_FORMATS"])]
        
        for fname in tqdm(enc_files, desc="Loading Pairs"):
            org_path = os.path.join(org_folder, fname)
            enc_path = os.path.join(enc_folder, fname)
            
            if os.path.exists(org_path):
                img_org = cv2.imread(org_path)
                img_enc = cv2.imread(enc_path)
                
                if img_org is not None and img_enc is not None:
                    # Ensure size consistency
                    img_org = cv2.resize(img_org, self.config["IMAGE_SIZE"])
                    img_enc = cv2.resize(img_enc, self.config["IMAGE_SIZE"])
                    
                    X.append(img_enc)
                    y.append(img_org)
                    filenames.append(fname)
                    
        return np.array(X), np.array(y), filenames