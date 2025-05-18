import streamlit as st

def main():
    st.set_page_config(page_title="AI Productivity Coach", layout="centered")
    st.title("Welcome to AI Productivity Coach 👋")
    st.markdown("Your smart assistant to boost productivity.")

    if st.button("Go to Productivity Coach"):
        st.switch_page("Coach.py")  # Requires `streamlit-extras` or `st.experimental_rerun` alternative

if __name__ == "__main__":
    main()
