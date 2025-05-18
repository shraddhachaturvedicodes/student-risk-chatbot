import streamlit as st
from utils import get_chat_response, transcribe_audio

st.title("🧠 Productivity Coach")

mode = st.radio("Choose Input Mode:", ["Text", "Voice"])

if mode == "Text":
    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        response = get_chat_response(user_input)
        st.success(f"Coach: {response}")

elif mode == "Voice":
    audio_file = st.file_uploader("Upload a voice clip (wav format)")
    if audio_file and st.button("Send"):
        transcript = transcribe_audio(audio_file)
        st.info(f"You said: {transcript}")
        response = get_chat_response(transcript)
        st.success(f"Coach: {response}")
