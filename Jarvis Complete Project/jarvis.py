import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr.Harsh !")

    elif hour>=12 and hour<16:
        speak(" Good Afternoon Mr.Harsh !")

    elif hour>=16 and hour<20:
        speak("Good Evening Mr Harsh  ! ")

    else:
        speak("Good Night Mr Harsh ! ")
    
    speak(" I am Genisis  Sir, Please tell me how may I help you")

def takeCommand():
    # It takes microphone input fron the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e) 
        print("Say that again please...")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=4)
    speak("According to Wikipedia")
    print(results)
    speak(results)

elif'open google'in query:
    webbrowser.open("google.com")

elif'open youtube'in query:
    webbrowser.open("youtube.com")

elif'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, The time is {strTime}")

elif 'open vs code' in query:
    codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif'open intellij idea' in query:
    codePath =  "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.4\\bin\\idea64.exe"
    os.startfile(codePath)

elif 'play music' in query:
    music_dir = 'C:\\Users\\DELL\\Music\\kalu'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[0]))
   
    










