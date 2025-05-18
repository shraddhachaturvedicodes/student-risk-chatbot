# File: frontend/pages/Coach_Chat.py

import streamlit as st
import sys
import os

#parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from utils import get_chat_response, capture_microphone_input, speak_text

st.set_page_config(page_title="Coach Chat", layout="centered")
st.title("🧠 Talk to your AI Coach")

#  Navigation
st.page_link("Home.py", label="🏠 Back to Home", icon="🏠")
st.page_link("pages/Dropout_Predict.py", label="📊 Go to Dropout Predictor")

# 🔘 Input method selector
mode = st.radio("Choose Input Mode", ["Text", "Live Voice"])

# ✏️ Text mode
if mode == "Text":
    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        if user_input.strip():
            response = get_chat_response(user_input)
            st.success(f"Coach: {response}")
        else:
            st.warning("Please enter a message.")

# 🎙️ Live voice mode
elif mode == "Live Voice":
    if st.button("🎤 Speak Now"):
        transcript = capture_microphone_input()
        st.info(f"You said: {transcript}")
        response = get_chat_response(transcript)
        st.success(f"Coach: {response}")
        speak_text(response)  # ✅ Speak only in voice mode