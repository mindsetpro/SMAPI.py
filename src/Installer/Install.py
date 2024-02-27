# Install.py

import subprocess

def install_dependencies():
    print("Installing required Python modules...")
    try:
        subprocess.run(["pip", "install", "harmony"])
        # Add more dependencies as needed
        print("Dependencies installed successfully!")
    except Exception as e:
        print(f"Error installing dependencies: {e}")

if __name__ == "__main__":
    install_dependencies()
