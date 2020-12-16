import speech_recognition as sr
import pyttsx3 #text to speech  conversion :)
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec #images from webcam instalar primero numpy si falla y tambien pip517
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5') #sapi5 microsoft voice recognition
voices = engine.getProperty('voices') #voice id 0 = hombre, id 1 = mujer
engine.setProperty('voice', voices[1].id)


#function speak,  converti texto a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()#esperar y hacer queue


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hi, Good Morning")
        print("Hi!, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hi!, Good Afternoon")
        print("Hi!, Good Afternoon")
    else:
        speak("Hi!, Good Evening")
        print("Hi!, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        if audio != 0:
            try:
                statement = r.recognize_google(audio, language = 'en-in')
                print(f"user said:{statement}\n")

            except Exception:
                speak("Sorry, i couldn't understand that")
                return "None"
            return statement

#print("Loading AI Assistant G-one")
#speak("Loading AI Assistant")
#wishMe()


if __name__=='__main__':
    

    while True:
        #speak("How can i help?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "shut down now" in statement:
            speak('AI Assistant is shutting down, Good bye')
            print('AI Assistant is shutting down, Good bye')
            break

        if "ok assistant" in statement or "okay assistant" in statement or "martech" in statement or "assistant" in statement:
            speak('How can i help?')
            statement = takeCommand().lower()
            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

time.sleep(3)    
