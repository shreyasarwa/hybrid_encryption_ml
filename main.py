import os
import sys
import subprocess

def start_frontend():
    """Launches the Streamlit Application with proper path handling."""
    
    # 1. PATH FIX: Adds the current directory to the Python path.
    # This prevents the 'ModuleNotFoundError: No module named frontend'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_dir)
    
    # 2. FILE CHECK: Ensure the entry point exists before launching
    target_file = os.path.join("frontend", "app.py")
    if not os.path.exists(target_file):
        print(f"[ERROR] Could not find {target_file}. Check your directory structure.")
        return

    # 3. LAUNCH: Use 'python -m streamlit' to ensure it uses your venv's version
    cmd = [sys.executable, "-m", "streamlit", "run", target_file]
    
    print(f"[INFO] Launching VoxAI Dashboard from: {target_file}")
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n[INFO] Frontend Shutdown by User.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Streamlit failed to start: {e}")

if __name__ == "__main__":
    start_frontend()