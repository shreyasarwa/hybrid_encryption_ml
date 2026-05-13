from tensorflow.keras import layers, Model

def build_encoder(input_shape):
    """Builds the feature extraction (compression) branch."""
    inputs = layers.Input(shape=input_shape, name="encoder_input")
    
    # Block 1
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    
    # Block 2
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.MaxPooling2D((2, 2), padding='same')(x)
    
    # Block 3 (Bottleneck Preparation)
    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    encoded = layers.MaxPooling2D((2, 2), padding='same', name="bottleneck")(x)
    
    return Model(inputs, encoded, name="Encoder")