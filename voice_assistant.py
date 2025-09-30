import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")
    print(f"Current Time: {time}")

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please specify")
    except wikipedia.exceptions.PageError:
        speak("No Results Found")

def process_command(command):
    if "time" in command:
        get_time()
    elif "wikipedia" in command:
        speak("What do you want to search on Wikipedia?")
        query = recognize_speech()
        if query:
            search_wikipedia(query)
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()
    else:
        speak("Sorry, I dont understand that command")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return None
    except sr.RequestError:
        print("Could not connect to Google Speech Recognition.")
        return None

def start_voice_assistant():
    speak("hello! I am your voice assistant. How can I help you?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)

start_voice_assistant()
