import pandas as pd
import json
import os

class MetricsExporter:
    @staticmethod
    def save_to_csv(data_list, path):
        df = pd.DataFrame(data_list)
        df.to_csv(path, index=False)
        
    @staticmethod
    def save_to_json(data_dict, path):
        with open(path, 'w') as f:
            json.dump(data_dict, f, indent=4)
            
    @staticmethod
    def save_to_markdown(data_list, path):
        df = pd.DataFrame(data_list)
        with open(path, 'w') as f:
            f.write("# Evaluation Summary Report\n\n")
            f.write(df.to_markdown(index=False))