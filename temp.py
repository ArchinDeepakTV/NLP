# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib

gmail_id = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('SENDER_EMAIL_PASSWORD')


myName = 'Jarvis'
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour<=12:
        speak("Good Morning Sir!!")
    elif hour>12 and hour<16:
        speak("Good Afternoon Sir!!")
    else:
        speak("Good Evening Sir!!")
    speak('How VIVA, can help you!!')
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_id, gmail_password)
    server.sendmail('archindeepakad.ad@gmail.com', to, content)
    server.close()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio=r.listen(source,phrase_time_limit=5)
        
    try:
        
        query = r.recognize_google(audio,language='en-in')
        print('Sir you said!!',query)
        
    except Exception:
        return 'None'
    return query
if __name__ == "__main__":
    greet()
    query="None"
    while "vivah of" not in query:
        
        query=takecommand().lower()
        
        
        if "open notepad" in query:
            tasktarget = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(tasktarget)
            
        elif "open google chrome" in query:
            tasktarget = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(tasktarget)
            
        elif "open terminal" in query:
            os.system("start cmd")
            
        elif "open browser" in query:
            tasktarget = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(tasktarget)
            
        elif "open pdf reader" in query:
            tasktarget = "C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\FoxitReader.exe"
            os.startfile(tasktarget)
        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "vivah of" in query:
            speak("Adios. Turning off")    
        elif 'email to john' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "aporwal2207@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")     
        print(query)
        
