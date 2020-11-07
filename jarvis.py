# Importing All Necessery Module
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver

# Setup Voice from Machine

engine = pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
#print(voice [0].id/[1].id)
engine.setProperty('voice', voice[0].id)

#Make Machine Talk

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

#Function to Wish After Program start
def wishMe():
    hour= int (datetime.datetime.now().hour)
    if hour>=0 and hour<6:
         speak("Good Night Mr. Rayhan, Peaced be Upon You")
    elif hour>=6 and hour<12:
         speak("Good Morning Mr. Rayhan, Peaced be Upon You")     
    elif hour>=12 and hour<16:
         speak("Good Noon Mr. Rayhan, Peaced be Upon You")
    elif hour>=16 and hour<18:
         speak("Good Evening Mr. Rayhan, Peaced be Upon You") 
    else:
         speak("Heloo Mr. Rayhan, Peaced be Upon You, What do you want from me at this late night") 

    speak("This is Jarvis, Your AI Partner...Waiting for Your Command")                   



def takeCommand ():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Waiting For Your Command....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Voice Matching to Owner")
        query=r.recognize_google(audio,language='en-in')
        print("Sir You told me\t",query)    

    except Exception as e:
        print (e)
        print ("Please Sir, Say that again")
        return "none"     
    return query


if __name__ == "__main__":
    wishMe ()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'open email' in query:
            webbrowser.open("gmail.com")
       
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\SM. Nibir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'How are you' in query:
            speak (f"I am fine, What's about You")

        elif 'Thanks' in query:
            speak (f"Welcome")
            

        elif 'Play Song From Youtube' in query:
            driver = webdriver.Chrome(executable_path="E:\\Soft & Apps\\chromedriver_win32\\chromedriver.exe")
            driver.get('Youtube.com')
            searchbox=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            searchbox.send_keys(query)
            searchButton=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
            searchButton.click()

            


        
        else:
            print ("Sorry to let you down sir")    
       
 