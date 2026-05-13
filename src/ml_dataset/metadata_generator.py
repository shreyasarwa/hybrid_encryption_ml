from datetime import datetime
import numpy as np

def generate_ml_metadata(X_train, X_test, y_train, y_test, config):
    return {
        "timestamp": datetime.now().isoformat(),
        "config": config,
        "dataset_stats": {
            "total_pairs": len(X_train) + len(X_test),
            "train_count": len(X_train),
            "test_count": len(X_test),
            "X_train_shape": X_train.shape,
            "y_train_shape": y_train.shape,
            "dtype": str(X_train.dtype),
            "pixel_range": [float(np.min(X_train)), float(np.max(X_train))]
        }
    }