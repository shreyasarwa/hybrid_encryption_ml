import tensorflow as tf
from tensorflow.keras import layers, models

def build_skip_connection_autoencoder(input_shape=(64, 64, 3)):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    e1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    p1 = layers.MaxPooling2D((2, 2), padding='same')(e1) # 32x32
    
    e2 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(p1)
    p2 = layers.MaxPooling2D((2, 2), padding='same')(e2) # 16x16

    # Decoder with SKIP CONNECTIONS
    d1 = layers.UpSampling2D((2, 2))(p2) # 32x32
    concat1 = layers.Concatenate()([d1, e2]) # Combines fuzzy and sharp data
    
    d2 = layers.UpSampling2D((2, 2))(concat1) # 64x64
    concat2 = layers.Concatenate()([d2, e1]) # The 'fix' for blurring

    outputs = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(concat2)
    
    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mse')
    return model