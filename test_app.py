#!/usr/bin/env python3
"""
Test script for MindCare Mental Health Assistant
"""

import sys
import os
import importlib.util

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    required_modules = [
        "tkinter",
        "cv2",
        "numpy",
        "PIL",
        "pygame",
        "speech_recognition",
        "pyttsx3",
        "google.generativeai"
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            if module == "cv2":
                import cv2
            elif module == "PIL":
                from PIL import Image, ImageTk
            elif module == "google.generativeai":
                import google.generativeai as genai
            else:
                __import__(module)
            print(f"✓ {module}")
        except ImportError as e:
            print(f"✗ {module}: {e}")
            failed_imports.append(module)
    
    return len(failed_imports) == 0

def test_config():
    """Test if config file is valid"""
    print("\nTesting configuration...")
    
    try:
        from config import GEMINI_API_KEY, COLORS, WINDOW_TITLE
        print("✓ Config file loaded successfully")
        
        if GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here":
            print("✓ API key is configured")
        else:
            print("⚠️  API key needs to be configured")
        
        return True
    except Exception as e:
        print(f"✗ Config error: {e}")
        return False

def test_modules():
    """Test if custom modules can be imported"""
    print("\nTesting custom modules...")
    
    modules_to_test = [
        "modules.chatbot",
        "modules.facial_analysis", 
        "modules.ui_components",
        "modules.voice_processor",
        "utils.constants",
        "utils.helpers"
    ]
    
    failed_modules = []
    
    for module in modules_to_test:
        try:
            spec = importlib.util.find_spec(module)
            if spec is None:
                print(f"✗ {module}: Module not found")
                failed_modules.append(module)
            else:
                print(f"✓ {module}")
        except Exception as e:
            print(f"✗ {module}: {e}")
            failed_modules.append(module)
    
    return len(failed_modules) == 0

def test_assets():
    """Test if asset files exist"""
    print("\nTesting assets...")
    
    required_assets = [
        "assets/icons/happy.png",
        "assets/icons/neutral.png", 
        "assets/icons/sad.png",
        "assets/icons/voice.png",
        "assets/sounds/notification.mp3",
        "assets/sounds/voice_start.mp3"
    ]
    
    missing_assets = []
    
    for asset in required_assets:
        if os.path.exists(asset):
            print(f"✓ {asset}")
        else:
            print(f"⚠️  {asset}: File not found")
            missing_assets.append(asset)
    
    return len(missing_assets) == 0

def main():
    """Main test function"""
    print("MindCare Mental Health Assistant - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Config Test", test_config),
        ("Module Test", test_modules),
        ("Asset Test", test_assets)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 20)
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    all_passed = True
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! The application should work correctly.")
    else:
        print("\n⚠️  Some tests failed. Please check the issues above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
