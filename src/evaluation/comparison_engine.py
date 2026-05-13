import numpy as np
import cv2
from .metrics_calculator import MetricsCalculator

class ComparisonEngine:
    def __init__(self, logger):
        self.logger = logger
        self.calculator = MetricsCalculator()

    def run_comparison(self, img_sets):
        """
        img_sets keys: 'orig', 'enc', 'dec', 'rec'
        """
        results = {}
        
        # Original vs Encrypted (Encryption Strength)
        results['encryption'] = self.calculator.get_all_metrics(
            img_sets['enc'], img_sets['orig']
        )
        
        # Original vs Decrypted (Reversibility)
        results['decryption'] = self.calculator.get_all_metrics(
            img_sets['dec'], img_sets['orig']
        )
        
        # Original vs Reconstructed (ML Performance)
        results['reconstruction'] = self.calculator.get_all_metrics(
            img_sets['rec'], img_sets['orig']
        )
        
        return results