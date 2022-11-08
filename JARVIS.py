import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <= 12:
        speak("Good morning")
    elif hour >= 13 and hour <= 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("It's Momo sir. How may I help you?")


def takeCommand():

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=5, timeout=1)
            query = r.recognize_google(audio)
            print(f"Recognized: {query}\n")  
    except Exception as e:  
        print("Say that again please...") 
        return 'none'
    return query
  

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir,")
            print(results)
            speak(results)

        elif "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open messenger" in query:
            webbrowser.open("facebook.com/messages")

        elif "play music" in query:
            music_dir = "C:\\Users\\legen\\Music\\Playlists"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))
