from gpt4all import GPT4All
import requests  
#import openai
import speech_recognition as sr
import pyttsx3
import smtplib
from playsound import playsound
import webbrowser
import os
import datetime

model_name = "mistral-7b-instruct-v0.1.Q4_0.gguf"  #specifies which GPT4All model to load
gpt4all_model = GPT4All(model_name)

# Initialize text-to-speech engine
engine = pyttsx3.init() # init() is to load the reference of pyttsx3 library is in engine 

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait() #used to process

#user choice for input mode
def input_mode():
    print("\nChoose input method:")
    print("1. Speak")
    print("2. Type")
    choice = input("Enter 1 or 2: ").strip()
    return choice

# Function to recognize speech
def listen():
    choice=input_mode()
    if choice=="2":
        return input("Type command: ").lower()
    
    recognizer = sr.Recognizer() #recognises audio input
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

# Function to send email
def send_email(to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-email-password')  
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail('your-email@gmail.com', to, message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Failed to send email: {e}")

# Function to play music
def play_music():
    music_dir = 'path-to-your-music-directory'  
    songs = os.listdir(music_dir)
    if songs:
        playsound(os.path.join(music_dir, songs[0]))
    else:
        speak("No music found in the directory.")

# Function to open a website
def open_website(url):
    webbrowser.open(url)

# Function to tell time and date
def tell_time_date():
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%H:%M')} and the date is {now.strftime('%Y-%m-%d')}")

# Function to search for files
def search_files(query):
    results = []
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if query in file:
                results.append(os.path.join(root, file))
    if results:
        speak(f"Found {len(results)} files matching your query.")
        for result in results:
            print(result)
    else:
        speak("No files found matching your query.")

#new function added
def check_performance():
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

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=student_data)
        result = response.json()

        if result['at_risk']:
            speak("Warning: You are currently at risk.")
        else:
            speak("You're doing well! Keep it up!")

        speak("Here are some suggestions for you:")
        for suggestion in result['suggestions']:
            speak(suggestion)

    except Exception as e:
        speak("Sorry, I couldn't connect to the productivity server.")
        print("Error:", e)

def handle_command(command):
    # Specific known commands
    if 'email' in command:
        speak("Who should I send the email to?")
        to = listen()
        speak("What is the subject?")
        subject = listen()
        speak("What should I say in the body?")
        body = listen()
        send_email(to, subject, body)

    elif 'play music' in command:
        play_music()

    elif 'open website' in command:
        speak("Which website should I open?")
        url = listen()
        if url:
            open_website(f"https://{url}")

    elif 'check my performance' in command:
        check_performance()

    elif command and command.strip() in ['exit', 'stop', 'go to sleep', 'quit']:
        speak("Goodbye!")
        exit()

    # Only respond to date/time if it's a short command
    elif command and command.lower() in ['what time is it', 'tell me the time', 'what is the date']:
        tell_time_date()

    # Otherwise, use AI (GPT)
    elif command:
        try:
            with gpt4all_model.chat_session():
                response = gpt4all_model.generate(
                    command,
                    max_tokens=250,
                    temp=0.7,
                    top_k=40, 
                    top_p=0.9,
                    repeat_penalty=1.1
                )
                print("AI:", response)
                speak(response)
        except Exception as e:
            print("Error with GPT4All:", e)
            speak("Sorry, I can't process that request right now.")

# Introduction
speak("Hello, I am JARVIS, your personal assistant. How can I help you today?")

# Main loop
while True:
    command = listen()
    if command:
        handle_command(command)