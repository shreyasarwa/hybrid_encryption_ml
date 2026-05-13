from tensorflow.keras.callbacks import (
    EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TensorBoard, CSVLogger
)
import os

def configure_callbacks(config):
    """Initializes standard training monitoring callbacks."""
    checkpoint_path = os.path.join(config["DIRS"]["CHECKPOINTS"], "best_model.h5")
    log_dir = config["DIRS"]["LOGS"]
    csv_path = os.path.join(config["DIRS"]["HISTORY"], "training_log.csv")
    
    return [
        EarlyStopping(monitor='val_loss', patience=12, restore_best_weights=True, verbose=1),
        ModelCheckpoint(filepath=checkpoint_path, monitor='val_loss', save_best_only=True, verbose=1),
        ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-6, verbose=1),
        TensorBoard(log_dir=log_dir, histogram_freq=1, write_images=True),
        CSVLogger(csv_path)
    ]