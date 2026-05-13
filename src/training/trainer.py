import tensorflow as tf
from src.training.callbacks_manager import configure_callbacks

class CNNTrainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config

    def compile(self):
        opt_name = self.config["TRAIN_PARAMS"]["OPTIMIZER"].lower()
        lr = self.config["TRAIN_PARAMS"]["LEARNING_RATE"]
        
        if opt_name == "adam":
            optimizer = tf.keras.optimizers.Adam(learning_rate=lr)
        elif opt_name == "rmsprop":
            optimizer = tf.keras.optimizers.RMSprop(learning_rate=lr)
        else:
            optimizer = tf.keras.optimizers.SGD(learning_rate=lr, momentum=0.9)
            
        self.model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])

    def train(self, X_train, y_train, validation_data):
        callbacks = configure_callbacks(self.config)
        
        history = self.model.fit(
            X_train, y_train,
            epochs=self.config["TRAIN_PARAMS"]["EPOCHS"],
            batch_size=self.config["TRAIN_PARAMS"]["BATCH_SIZE"],
            validation_data=validation_data,
            callbacks=callbacks,
            shuffle=True,
            verbose=1
        )
        return history