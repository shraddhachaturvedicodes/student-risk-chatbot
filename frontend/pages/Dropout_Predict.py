import streamlit as st
import requests
from gpt4all import GPT4All

class ProductivityCoachApp:
    def __init__(self):
        self.backend_url = 'http://127.0.0.1:5000/predict_dropout'
        self.gpt_model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

    def get_dropout_prediction(self, student_data):
        response = requests.post(self.backend_url, json=student_data)
        response.raise_for_status()
        return response.json()

    def generate_gpt_prompt(self, dropout_prob):
        if dropout_prob > 0.5:
            return (f"The student has a dropout risk probability of {dropout_prob:.2f}. "
                    "Please provide empathetic coaching advice and ask if they want suggestions to improve.")
        else:
            return (f"The student has a low dropout risk probability of {dropout_prob:.2f}. "
                    "Congratulate them and ask if they want tips to improve their learning.")

    def get_gpt_response(self, prompt):
        with self.gpt_model.chat_session():
            return self.gpt_model.generate(prompt)

    def run(self):
        st.title("🤖 AI Productivity Coach")

        with st.form("student_form"):
            st.header("🎓 Student Profile Input")
            student_data = {
                'Age': int(st.text_input("Age", "22")),
                'Gender': st.selectbox("Gender", ['Male', 'Female', 'Other']),
                'Education_Level': st.selectbox("Education Level", ['High School', 'Undergraduate', 'Postgraduate']),
                'Time_Spent_on_Videos': float(st.text_input("Time Spent on Videos (mins)", "120")),
                'Quiz_Attempts': int(st.text_input("Quiz Attempts", "3")),
                'Quiz_Scores': float(st.text_input("Quiz Score (%)", "65")),
                'Assignment_Completion_Rate': float(st.text_input("Assignment Completion (%)", "70")),
                'Engagement_Level': st.selectbox("Engagement Level", ['Low', 'Medium', 'High']),
                'Final_Exam_Score': float(st.text_input("Final Exam Score (%)", "75")),  # ✅ NEW
                'Learning_Style': st.selectbox("Learning Style", ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic']),  # ✅ NEW
                'Feedback_Score': int(st.text_input("Feedback Score (1-5)", "4"))  # ✅ NEW
            }
            submit = st.form_submit_button("Analyze and Ask Coach")

        if submit:
            try:
                prediction = self.get_dropout_prediction(student_data)
                prob = prediction['dropout_probability']
                pred = prediction['dropout_prediction']

                st.success(f"Dropout Risk Probability: {prob:.2f}, Prediction: {'Yes' if pred else 'No'}")

                prompt = self.generate_gpt_prompt(prob)
                gpt_response = self.get_gpt_response(prompt)
                st.markdown(f"🤖 Coach says: {gpt_response}")

                if "suggestions" in gpt_response.lower():
                    if st.button("Yes, show me suggestions"):
                        suggestion_prompt = (
                            f"Suggest 3 practical ways for a student with dropout risk probability {prob:.2f} to improve."
                        )
                        suggestion_response = self.get_gpt_response(suggestion_prompt)
                        st.info(suggestion_response)

            except requests.HTTPError as http_err:
                st.error(f"HTTP error occurred: {http_err}")
            except Exception as err:
                st.error(f"An error occurred: {err}")

if __name__ == "__main__":
    app = ProductivityCoachApp()
    app.run()