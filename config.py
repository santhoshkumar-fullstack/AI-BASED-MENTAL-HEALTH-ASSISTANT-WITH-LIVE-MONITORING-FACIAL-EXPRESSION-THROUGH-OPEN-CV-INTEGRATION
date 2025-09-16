import os

# Gemini API Configuration
# Reads from environment variable if set; falls back to your provided key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCB2wmD3iXcS74JoW4yEV_XwmAvDczyLck")

# Application Settings
WINDOW_TITLE = "MindCare - Mental Health Assistant"
WINDOW_SIZE = "1200x800"

# Emotion Detection Settings
EMOTION_UPDATE_INTERVAL = 2000  # milliseconds
EMOTION_THRESHOLD = 0.6
# Number of recent frames to smooth predictions
EMOTION_SMOOTHING_WINDOW = 5

# Chat Settings
CHAT_HISTORY_LIMIT = 20

# Voice Settings
VOICE_SPEECH_RATE = 150
VOICE_VOLUME = 0.9

# UI Colors
COLORS = {
    "primary": "#6A0DAD",
    "secondary": "#FF6B6B",
    "accent1": "#4ECDC4",
    "accent2": "#FFE66D",
    "background": "#1A1A2E",
    "text": "#FFFFFF",
    "success": "#38B000",
    "warning": "#F79D65",
    "danger": "#E71D36"
}