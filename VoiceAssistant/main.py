
# this is a voiceassistant


import speech_recognition as sr
import pyttsx3
import datetime
import urllib.parse
import os
import subprocess

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Function to speak text
def speak(text):
    print("🤖 Vox:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-US").lower()
        print("📝 You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is down.")
        return ""

# Function to open URL using Safari
def open_in_safari(url):
    os.system(f"open -a Safari '{url}'")

# Function to open YouTube app on Mac (if installed via App Store)
def open_youtube_app():
    try:
        subprocess.run(["open", "-a", "YouTube"])
    except Exception as e:
        speak("YouTube app is not installed. Opening in Safari instead.")
        open_in_safari("https://www.youtube.com")

# Run Vox Assistant
def run_vox():
    speak("Hello Sayed! I’m Vox. How can I help you?")
    while True:
        command = listen()

        if "open google" in command or "google" in command:
            speak("Opening Google.")
            open_in_safari("https://www.google.com")

        elif "youtube" in command:
            speak("Opening YouTube App.")
            open_youtube_app()


        elif "time" in command:

            current_time = datetime.datetime.now().strftime("%I:%M %p")

            speak("The current time is " + current_time)


        elif "stop" in command or "exit" in command or "goodbye" in command:

            speak("Goodbye, see you later!")

            break


        else:

            speak("Let me search that on Google.")

            query = urllib.parse.quote_plus(command)

            open_in_safari(f"https://www.google.com/search?q={query}")


# Start the assistant
run_vox()
