from .mse_metric import calculate_mse
from .psnr_metric import calculate_psnr
from .ssim_metric import calculate_ssim
from src.analysis.entropy_analysis import calculate_entropy
from src.analysis.correlation_analysis import calculate_pixel_correlation

class MetricsCalculator:
    @staticmethod
    def get_all_metrics(target, reference):
        """Returns a dictionary of all relevant benchmarking metrics."""
        return {
            "MSE": calculate_mse(target, reference),
            "PSNR": calculate_psnr(target, reference),
            "SSIM": calculate_ssim(target, reference),
            "Entropy": calculate_entropy(target),
            "Correlation": calculate_pixel_correlation(target)
        }