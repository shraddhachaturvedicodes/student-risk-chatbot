import requests
from gpt4all import GPT4All

# You can change this path to wherever your model actually lives
gpt_model_path = "mistral-7b-instruct-v0.1.Q4_0.gguf"

def logic_from_op(text):
    # This function decides wheter to call backend or use GPT4All for chat
    if "performance" in text.lower() or "at risk" in text.lower():
        try:
            student_data = {
                'quiz_score': 55,
                'video_watch_time': 100,
                'assignments_submitted': 2,
                'forum_posts': 1,
                'exam_score': 60,
                'login_frequency': 8,
                'study_hours_per_day': 1.5,
                'self_reported_mood': 3,
                'stress_level': 8,
                'focus_rating': 4
            }
            response = requests.post("http://127.0.0.1:5000/predict", json=student_data)
            result = response.json()
            if result["at_risk"]:
                message = "⚠️ You are currently at risk.\n"
            else:
                message = "✅ You’re doing well! Keep it up.\n"
            message += "\n".join(result["suggestions"])
            return message
        except Exception as e:
            return f"❌ Could not connect to backend: {e}"

    # GPT4All for general chat
    try:
        model = GPT4All(gpt_model_path)
        with model.chat_session():
            return model.generate(text, max_tokens=250)
    except Exception as e:
        return f"❌ GPT4All error: {e}"

def logic_from_lp(text):
    return f"📘 Learning logic says: {text}"

def logic_from_op1(text):
    return f"⚙️ Optimization logic says: {text}"

def process_input(user_text):
    if "learn" in user_text.lower():
        return logic_from_lp(user_text)
    elif "optimize" in user_text.lower():
        return logic_from_op1(user_text)
    else:
        return logic_from_op(user_text)