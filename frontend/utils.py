import sys
import os

# ✅ Add parent directory to path first
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Now import from backend
from backend.chat_logic import process_input
import speech_recognition as sr
import pyttsx3

# Convert audio to text using microphone
def capture_microphone_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError as e:
        return f"Speech recognition error: {e}"

# Speak out the response
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Text input chat logic
def get_chat_response(text):
    return process_input(text)