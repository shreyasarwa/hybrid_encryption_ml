import os
import tensorflow as tf
import numpy as np

def verify_system():
    print("\n" + "="*40)
    print("🚀 FINAL SYSTEM READINESS CHECK")
    print("="*40)

    model_path = "models/saved_models/final_autoencoder.h5"
    
    if os.path.exists(model_path):
        print(f"✅ FILE: Weights found at {model_path}")
        try:
            model = tf.keras.models.load_model(model_path, compile=False)
            print(f"✅ LOAD: Model is valid. Input shape: {model.input_shape}")
            
            if model.input_shape[1:3] == (64, 64):
                print("✅ SHAPE: Matches expected 64x64 dimensions.")
            else:
                print(f"⚠️ SHAPE: Unexpected dimensions {model.input_shape[1:3]}")
                
        except Exception as e:
            print(f"❌ LOAD FAILED: {e}")
    else:
        print("❌ FILE NOT FOUND: Check 'models/saved_models/' folder.")

    print("="*40 + "\n")

if __name__ == "__main__":
    verify_system()