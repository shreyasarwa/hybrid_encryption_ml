import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from PIL import Image

# 1. ARCHITECTURE WITH SKIP CONNECTIONS
def build_unet(input_shape=(64, 64, 3)):
    inputs = layers.Input(input_shape)
    # Encoder
    c1 = layers.Conv2D(64, 3, activation='relu', padding='same')(inputs)
    p1 = layers.MaxPooling2D()(c1)
    c2 = layers.Conv2D(128, 3, activation='relu', padding='same')(p1)
    p2 = layers.MaxPooling2D()(c2)

    # Bottleneck
    b = layers.Conv2D(256, 3, activation='relu', padding='same')(p2)

    # Decoder
    u1 = layers.UpSampling2D()(b)
    m1 = layers.Concatenate()([u1, c2])
    c3 = layers.Conv2D(128, 3, activation='relu', padding='same')(m1)
    u2 = layers.UpSampling2D()(c3)
    m2 = layers.Concatenate()([u2, c1])
    c4 = layers.Conv2D(64, 3, activation='relu', padding='same')(m2)

    outputs = layers.Conv2D(3, 3, activation='tanh', padding='same')(c4)
    return models.Model(inputs, outputs)

# 2. SSIM-BASED LOSS FUNCTION
def ssim_loss(y_true, y_pred):
    return 1 - tf.reduce_mean(tf.image.ssim(y_true, y_pred, max_val=2.0))

# 3. DATA LOADER
def load_paired_data():
    raw_files = sorted(os.listdir("datasets/raw"))
    x_list, y_list = [], []
    
    for f in raw_files:
        if not f.endswith(('.png', '.jpg')): continue
        # Target: Clean image [-1, 1]
        y_img = Image.open(f"datasets/raw/{f}").convert('RGB').resize((64, 64))
        y_list.append((np.array(y_img) / 127.5) - 1.0)
        # Input: Fuzzy image [-1, 1]
        x_img = Image.open(f"datasets/processed/{f}").convert('RGB').resize((64, 64))
        x_list.append((np.array(x_img) / 127.5) - 1.0)
        
    return np.array(x_list), np.array(y_list)

# 4. START TRAINING
if __name__ == "__main__":
    X, Y = load_paired_data()
    model = build_unet()
    model.compile(optimizer='adam', loss=ssim_loss, metrics=['mae'])
    
    # Save the best model automatically
    checkpoint = callbacks.ModelCheckpoint(
        "models/saved_models/final_autoencoder.h5", 
        monitor='loss', save_best_only=True
    )

    print("🏋️ Training U-Net to reach SSIM > 0.80...")
    model.fit(X, Y, epochs=100, batch_size=16, callbacks=[checkpoint])