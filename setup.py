#!/usr/bin/env python3
"""
Setup script for MindCare Mental Health Assistant
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements: {e}")
        return False

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    if not os.path.exists(".env"):
        if os.path.exists("env.example"):
            with open("env.example", "r") as f:
                content = f.read()
            with open(".env", "w") as f:
                f.write(content)
            print("✓ Created .env file from template")
            print("⚠️  Please edit .env file and add your Gemini API key")
        else:
            print("⚠️  env.example not found, creating basic .env file")
            with open(".env", "w") as f:
                f.write("GEMINI_API_KEY=your_api_key_here\n")
    else:
        print("✓ .env file already exists")

def check_camera():
    """Check if camera is available"""
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✓ Camera is available")
            cap.release()
            return True
        else:
            print("⚠️  Camera not available - facial analysis will not work")
            return False
    except ImportError:
        print("⚠️  OpenCV not installed yet - camera check skipped")
        return False

def check_microphone():
    """Check if microphone is available"""
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("✓ Microphone is available")
            return True
    except Exception as e:
        print(f"⚠️  Microphone check failed: {e}")
        return False

def main():
    """Main setup function"""
    print("MindCare Mental Health Assistant - Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Create environment file
    create_env_file()
    
    # Check hardware
    print("\nChecking hardware requirements...")
    check_camera()
    check_microphone()
    
    print("\n" + "=" * 50)
    print("Setup completed!")
    print("\nNext steps:")
    print("1. Edit .env file and add your Gemini API key")
    print("2. Run: python main.py")
    print("\nFor help, see README.md")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
