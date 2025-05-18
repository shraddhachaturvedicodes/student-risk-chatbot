# File: frontend/Home.py
import streamlit as st

st.set_page_config(page_title="AI Productivity Coach", layout="centered")
st.title("🏠 Welcome to AI Productivity Coach")

st.markdown("""
A smart assistant to help students improve their focus, reduce dropout risks, and achieve their goals.
""")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/Dropout_Predict.py", label="🎓 Go to Dropout & Score Prediction")

with col2:
    st.page_link("pages/Coach_Chat.py", label="🧠 Chat with Coach")