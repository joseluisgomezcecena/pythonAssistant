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
engine.setProperty('voice', 'spanish')
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
        speak("Hola!, Buenas noches")
        print("Hi!, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language = 'en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            if statement == "":
                print ('nothing was said')
                return statement
            else:
                speak("Sorry, i couldn't understand that")
                return "None"
                return statement

print("Loading AI Assistant G-one")
speak("Loading AI Assistant")
wishMe()


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

        if "ok assistant" in statement or "ok martech" in statement or "okay assistant" in statement:
            time.sleep(3)
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

            elif 'youtube' in statement:
                statement = statement.replace("youtube", "")
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+statement)
                speak("youtubing "+statement)
                time.sleep(5)    

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open hour by hour' in statement:
                webbrowser.open_new_tab("http://mxmtsvrandon1/horaxhora/")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'what is the efficiency' in statement:
                speak("Plant one, two or three?")
                planta = takeCommand()
                webbrowser.open_new_tab("mxmtsvrandon1/horaxhora/reportes?planta="+planta)
                time.sleep(5)

            elif "weather" in statement:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                else:
                    speak(" City Not Found ")



            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Bora")
                print("I was built by Bora")

            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")

            elif 'juve news' in statement:
                news = webbrowser.open_new_tab("https://news.google.com/search?q=juventus&hl=en-US&gl=US&ceid=US%3Aen")
                speak('Here are some headlines')
                time.sleep(6)

            
            #elif "camera" in statement or "take a photo" in statement:
            #    ec.capture(0,"robo camera","img.jpg")

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question=takeCommand()
                app_id="93GVVG-7KJ83QUQVY"
                client = wolframalpha.Client('93GVVG-7KJ83QUQVY')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)


            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

time.sleep(3)    
