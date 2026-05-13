import os
import cv2
from pathlib import Path
from src.utils.config import CONFIG, get_eval_path
from .comparison_engine import ComparisonEngine
from src.visualization.image_grid_generator import generate_comparison_grid
from src.visualization.histogram_visualizer import plot_histogram_comparison
from .metrics_exporter import MetricsExporter

class EvaluationPipeline:
    def __init__(self, logger):
        self.logger = logger
        self.engine = ComparisonEngine(logger)
        self.exporter = MetricsExporter()
        self.master_records = []

    def load_image_set(self, filename):
        paths = {
            'orig': Path(CONFIG["PATHS"]["ORIGINAL"]) / filename,
            'enc': Path(CONFIG["PATHS"]["ENCRYPTED"]) / filename,
            'dec': Path(CONFIG["PATHS"]["DECRYPTED"]) / filename,
            'rec': Path(CONFIG["PATHS"]["RECONSTRUCTED"]) / filename
        }
        
        imgs = {}
        for key, path in paths.items():
            if not path.exists():
                raise FileNotFoundError(f"Missing {key} image: {path}")
            img = cv2.imread(str(path))
            imgs[key] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return imgs

    def process_all(self):
        self.logger.info("Starting Evaluation Pipeline Stage 11...")
        image_files = [f for f in os.listdir(CONFIG["PATHS"]["ORIGINAL"]) if f.endswith(('.png', '.jpg'))]
        
        total = len(image_files)
        for idx, filename in enumerate(image_files):
            try:
                progress = ((idx + 1) / total) * 100
                self.logger.info(f"[{progress:.1f}%] Evaluating: {filename}")
                
                imgs = self.load_image_set(filename)
                metrics = self.engine.run_comparison(imgs)
                
                # Store for CSV
                record = {"image": filename}
                for category, values in metrics.items():
                    for metric_name, val in values.items():
                        record[f"{category}_{metric_name}"] = round(val, 4)
                self.master_records.append(record)

                # Individual JSON
                json_path = get_eval_path("metrics_json") / f"{filename}.json"
                self.exporter.save_to_json(metrics, json_path)

                # Visualizations
                grid_path = get_eval_path("comparison_images") / f"grid_{filename}"
                generate_comparison_grid(imgs, grid_path)
                
                hist_path = get_eval_path("plots") / f"hist_{filename}"
                plot_histogram_comparison(imgs, hist_path)

            except Exception as e:
                self.logger.error(f"Failed to process {filename}: {str(e)}")

        self.export_final_reports()

    def export_final_reports(self):
        table_path = get_eval_path("tables") / "master_metrics.csv"
        self.exporter.save_to_csv(self.master_records, table_path)
        
        summary_path = get_eval_path("reports") / "evaluation_summary.md"
        self.exporter.save_to_markdown(self.master_records, summary_path)
        self.logger.info(f"Stage 11 complete. Reports saved to {CONFIG['PATHS']['OUTPUT_BASE']}")