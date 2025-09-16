import tkinter as tk
from tkinter import ttk
import threading
import time
from config import COLORS, WINDOW_TITLE, WINDOW_SIZE
from modules.facial_analysis import FacialExpressionAnalyzer
from modules.chatbot import MentalHealthChatbot
from modules.voice_processor import VoiceProcessor
from modules.ui_components import EmotionIndicator, ChatWindow, VideoFeed
from utils.helpers import format_chat_message

class MentalHealthAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=COLORS["background"])
        
        # Initialize components
        self.chatbot = MentalHealthChatbot()
        self.voice_processor = VoiceProcessor(self.handle_message)
        self.facial_analyzer = FacialExpressionAnalyzer(self.update_emotion_display)
        
        # Setup UI
        self.setup_ui()
        
        # Start services
        self.facial_analyzer.start_analysis()
        self.voice_processor.start_listening()
        
        # Welcome message
        self.add_message("assistant", "Hello! I'm your mental health assistant. How are you feeling today?")
        
    def setup_ui(self):
        # Create main panels
        main_panel = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, bg=COLORS["background"])
        main_panel.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel (video and emotion)
        left_panel = tk.Frame(main_panel, bg=COLORS["background"])
        main_panel.add(left_panel, width=400)
        
        # Video feed
        self.video_feed = VideoFeed(left_panel)
        self.video_feed.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Emotion indicator
        self.emotion_indicator = EmotionIndicator(left_panel)
        self.emotion_indicator.pack(pady=10, padx=10, fill="x")
        
        # Right panel (chat)
        right_panel = tk.Frame(main_panel, bg=COLORS["background"])
        main_panel.add(right_panel, width=800)
        
        # Chat window
        self.chat_window = ChatWindow(right_panel, self.handle_message)
        self.chat_window.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Add some decorative elements
        self.add_decorative_elements()
        
    def add_decorative_elements(self):
        # Colorful header
        header = tk.Frame(self.root, height=5, bg=COLORS["primary"])
        header.pack(fill="x", side="top")
        
        # Colorful footer
        footer = tk.Frame(self.root, height=5, bg=COLORS["secondary"])
        footer.pack(fill="x", side="bottom")
        
        # Add some accent colors to the sides
        left_accent = tk.Frame(self.root, width=5, bg=COLORS["accent1"])
        left_accent.pack(fill="y", side="left")
        
        right_accent = tk.Frame(self.root, width=5, bg=COLORS["accent2"])
        right_accent.pack(fill="y", side="right")
        
    def update_emotion_display(self, emotion, confidence, frame):
        # Update emotion indicator
        self.emotion_indicator.update_emotion(emotion, confidence)
        
        # Update video feed with the latest frame
        if frame is not None:
            from PIL import Image
            img = Image.fromarray(frame)
            self.video_feed.update_frame(img)
            
        # Occasionally respond to strong emotions
        if confidence > 0.7 and emotion != "neutral":
            # Only respond occasionally to avoid being intrusive
            import random
            if random.random() < 0.1:  # 10% chance
                response = self.chatbot.get_emotion_based_response(emotion, confidence)
                self.add_message("assistant", response)
                self.voice_processor.speak(response)
                
    def handle_message(self, message, sender_type="user_text"):
        # Add user message to chat
        if sender_type in ["user_text", "user_voice"]:
            self.add_message(sender_type, message)
            
            # Get AI response
            current_emotion = self.emotion_indicator.emotion
            response = self.chatbot.generate_response(message, current_emotion)
            
            # Add AI response to chat and speak it
            self.add_message("assistant", response)
            self.voice_processor.speak(response)
            
    def add_message(self, sender, message):
        self.chat_window.add_message(sender, message)
        
    def on_closing(self):
        self.facial_analyzer.stop_analysis()
        self.voice_processor.stop_listening()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = MentalHealthAssistant(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()