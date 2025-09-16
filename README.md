# MindCare - Mental Health Assistant

A comprehensive mental health assistant application that combines facial expression analysis, voice processing, and AI-powered chat to provide emotional support and guidance.

## Features

- **Facial Expression Analysis**: Real-time emotion detection using computer vision
- **Voice Processing**: Speech-to-text and text-to-speech capabilities
- **AI Chatbot**: Powered by Google's Gemini AI for empathetic conversations
- **Modern UI**: Clean, colorful interface with emotion indicators
- **Real-time Feedback**: Immediate responses to emotional states

## Requirements

- Python 3.8 or higher
- Webcam for facial analysis
- Microphone for voice input
- Internet connection for AI responses

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mental-health-assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your Gemini API key
```

5. Run the application:
```bash
python main.py
```

## Configuration

### API Keys
- **Gemini API**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Add your API key to the `.env` file or directly in `config.py`

### Customization
- Modify colors and UI settings in `config.py`
- Adjust emotion detection sensitivity in the facial analysis module
- Customize AI prompts in `utils/constants.py`

## Usage

1. **Start the Application**: Run `python main.py`
2. **Allow Camera Access**: Grant permission for webcam access
3. **Allow Microphone Access**: Grant permission for microphone access
4. **Interact**: 
   - Type messages in the chat window
   - Use the microphone button for voice input
   - The app will analyze your facial expressions and respond accordingly

## Project Structure

```
mental-health-assistant/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── modules/
│   ├── chatbot.py        # AI chatbot implementation
│   ├── facial_analysis.py # Facial expression detection
│   ├── ui_components.py  # UI components and widgets
│   └── voice_processor.py # Voice input/output processing
├── utils/
│   ├── constants.py      # Application constants
│   └── helpers.py        # Utility functions
├── assets/
│   ├── icons/           # Emotion icons
│   └── sounds/          # Audio files
└── README.md            # This file
```

## Features in Detail

### Facial Expression Analysis
- Detects 7 basic emotions: happy, sad, angry, surprised, fearful, disgusted, neutral
- Real-time confidence scoring
- Visual feedback with emotion indicators

### Voice Processing
- Continuous speech recognition
- Text-to-speech responses
- Audio feedback for interactions

### AI Chatbot
- Context-aware responses based on current emotional state
- Empathetic and supportive conversation style
- Fallback responses for offline scenarios

## Troubleshooting

### Common Issues

1. **Camera not working**: Ensure your webcam is not being used by another application
2. **Microphone issues**: Check microphone permissions in your system settings
3. **API errors**: Verify your Gemini API key is correct and has sufficient quota
4. **Import errors**: Make sure all dependencies are installed correctly

### Performance Tips

- Close other applications using the camera/microphone
- Ensure good lighting for facial analysis
- Use a quiet environment for voice recognition

## Privacy and Security

- All processing is done locally except for AI responses
- No personal data is stored permanently
- Camera and microphone access is only used during active sessions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational and supportive purposes only. It is not a substitute for professional mental health care. If you're experiencing a mental health crisis, please contact a qualified healthcare provider or emergency services.

## Support

For support, please open an issue on GitHub or contact the development team.
