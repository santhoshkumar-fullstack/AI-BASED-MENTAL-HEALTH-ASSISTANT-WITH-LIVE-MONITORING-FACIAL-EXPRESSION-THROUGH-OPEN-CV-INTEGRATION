#!/usr/bin/env python3
"""
Launcher script for MindCare Mental Health Assistant
"""

import sys
import os
import subprocess

def check_requirements():
    """Check if all requirements are met"""
    try:
        # Try to import main modules
        import tkinter
        import cv2
        import numpy
        from PIL import Image
        import pygame
        import speech_recognition
        import pyttsx3
        import google.generativeai
        return True
    except ImportError as e:
        print(f"Missing requirement: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_config():
    """Check if configuration is set up"""
    try:
        from config import GEMINI_API_KEY
        if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
            print("⚠️  Warning: Gemini API key not configured")
            print("Please edit config.py and add your API key")
            return False
        return True
    except Exception as e:
        print(f"Config error: {e}")
        return False

def main():
    """Main launcher function"""
    print("MindCare Mental Health Assistant")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Requirements not met. Please install dependencies first.")
        return False
    
    # Check configuration
    if not check_config():
        print("\n⚠️  Configuration issues detected.")
        response = input("Continue anyway? (y/N): ").lower()
        if response != 'y':
            return False
    
    print("\n🚀 Starting MindCare...")
    print("Press Ctrl+C to stop the application")
    print("-" * 40)
    
    try:
        # Import and run the main application
        from main import main as app_main
        app_main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Take care of your mental health.")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
