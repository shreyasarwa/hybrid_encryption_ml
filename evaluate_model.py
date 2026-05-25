import os
import numpy as np
import tensorflow as tf
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def run_eval():
    model_path = "models/saved_models/final_autoencoder.h5"
    input_dir = "datasets/raw" # Based on your sidebar
    
    if not os.path.exists(model_path):
        print(f"❌ Model missing at {model_path}")
        return

    files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if not files:
        print(f"❌ No images found in {input_dir}. Please add a file there.")
        return
        
    sample_path = os.path.join(input_dir, files[0])
    print(f"🔍 Evaluating: {sample_path}")

    model = tf.keras.models.load_model(model_path, compile=False)
    
    # 1. Process Input
    img = Image.open(sample_path).convert('RGB').resize((64, 64))
    img_arr = np.array(img).astype(np.float32)
    norm_input = (img_arr / 127.5) - 1.0  # Normalized to [-1, 1]
    
    # 2. Predict
    recon = model.predict(np.expand_dims(norm_input, axis=0), verbose=0)[0]
    
    # 3. Post-Process for Metrics (Scale both back to 0-1 range for SSIM/PSNR)
    gt_eval = img_arr / 255.0
    recon_eval = (recon + 1.0) / 2.0
    recon_eval = np.clip(recon_eval, 0, 1)
    
    # 4. Calculate
    s = ssim(gt_eval, recon_eval, channel_axis=2, data_range=1.0)
    p = psnr(gt_eval, recon_eval, data_range=1.0)
    
    print("\n" + "="*30)
    print(f"📊 SSIM: {s:.4f}")
    print(f"📊 PSNR: {p:.2f} dB")
    print("="*30)

    # Save visual result for inspection
    debug_img = (recon_eval * 255).astype(np.uint8)
    Image.fromarray(debug_img).save("debug_eval_output.png")
    print("✅ Visual result saved as 'debug_eval_output.png'")

if __name__ == "__main__":
    run_eval()