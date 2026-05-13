from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
import os

def get_callbacks(config):
    return [
        ModelCheckpoint(
            filepath=os.path.join(config["DIRS"]["CHECKPOINTS"], "best_model.h5"),
            save_best_only=True,
            monitor='val_loss'
        ),
        EarlyStopping(monitor='val_loss', patience=config["EARLY_STOPPING_PATIENCE"]),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=config["REDUCE_LR_PATIENCE"]),
        TensorBoard(log_dir=config["DIRS"]["LOGS"])
    ]