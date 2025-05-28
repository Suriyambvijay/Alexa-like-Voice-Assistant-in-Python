import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

# Initialize the engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi! I’m your Python Alexa. How can I help you today?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def run_alexa():
    wish_user()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            topic = command.replace("wikipedia", "").strip()
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on that.")
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        
        elif 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open('https://youtube.com')

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open('https://google.com')

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        elif command:
            speak("I didn’t understand that. Can you repeat?")

# Run the assistant
run_alexa()