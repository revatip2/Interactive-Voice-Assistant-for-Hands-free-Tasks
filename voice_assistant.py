!pip install pyttsx3
!pip install SpeechRecognition
!pip install wikipedia
!pip install py-espeak-ng
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning,what should we do today?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon,how can i help you today?")

    else:
        speak("Good Evening,how may i be of service today?")



def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo
     server.starttls()
     server.login('email.com','password')
     server.sendmail('email.com',to,content)
     server.close



def takeCommand():
    #It takes microphone input from the user and returns string output.

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")


    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
         query = takeCommand().lower()
# logic for executing task based on query.
         if 'wikipedia' in query:
             speak('Searching Wikipedia')
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:

            webbrowser.open("https://www.youtube.com/")

         elif 'open google' in query:

            webbrowser.open("https://www.google.com/")

         elif 'play music' in query:
            music_dir="C:path"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H hours and %M minutes")
            speak(f"The time is{strTime}")

         elif 'open code' in query:
             codePath = "C:\path"
             os.startfile(codePath)


         elif 'send mail' in query:
             try:
                 speak("What do you want the email to convey?")
                 content=takeCommand()
                 to='email.com'
                 sendEmail(to,content)
                 speak('Email has been sent')
             except Exception as e:
                 print(e)
                 speak('Sorry i am currently unable to send the email')

         elif 'bye' in query:
             speak('See you soon')
             sys.exit()

         elif 'navigate' in query:
             webbrowser.open("https://www.google.com/maps")

         elif 'shopping' in query:
             webbrowser.open("https://www.flipkart.com/")

         elif "check mail" in query:
             webbrowser.open("https://mail.google.com")

         elif "my computer" in query:
             codePath=('C:\path')
             os.startfile(codePath)
