from tensorflow.keras import layers, Model

def build_decoder(encoded_shape):
    """Builds the image reconstruction (expansion) branch."""
    encoded_input = layers.Input(shape=encoded_shape, name="decoder_input")
    
    # Block 1
    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(encoded_input)
    x = layers.UpSampling2D((2, 2))(x)
    
    # Block 2
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.UpSampling2D((2, 2))(x)
    
    # Block 3
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.UpSampling2D((2, 2))(x)
    
    # Output Layer
    decoded = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same', name="reconstruction")(x)
    
    return Model(encoded_input, decoded, name="Decoder")