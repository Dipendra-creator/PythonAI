import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 <= hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Night!")
    speak("My Name is Friday, I am Your Personal Assistant")


# wishMe()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()


def lighton():
    driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe')  # add the location of the chrome Drivers
    driver.get("https://Add here.000webhostapp.com/main.html")  # Add the webhost name
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()


def monthname(x):
    if x == 1:
        monthName = 'January'
    elif x == 2:
        monthName = 'February'
    elif x == 3:
        monthName = 'March'
    elif x == 4:
        monthName = 'April'
    elif x == 5:
        monthName = 'May'
    elif x == 6:
        monthName = 'June'
    elif x == 7:
        monthName = 'July'
    elif x == 8:
        monthName = 'August'
    elif x == 9:
        monthName = 'September'
    elif x == 10:
        monthName = 'October'
    elif x == 11:
        monthName = 'November'
    else:
        monthName = 'December'
    return monthName


def lightoff():
    driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
    driver.get("https://Add here.000webhostapp.com/main.html")  # Add the webhost name
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # Add the Location of the chrome browser

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                if 'open music' in text:
                    text = 'https://www.youtube.com/watch?v=JGwWNGJdvx8&list=RDJGwWNGJdvx8&start_radio=1'
                    speak('Opening Youtube Music List')
                    wb.get(chrome_path).open(text)
                else:
                    print('google think you said:\n' + text + '.com')
                    wb.get(chrome_path).open(text + '.com')
            except Exception as e:
                print(e)

        elif 'how is the weather' and 'weather' in query:
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            city = input('City Name :')
            url = api_address + city
            json_data = requests.get(url).json()
            format_add = json_data['base']
            print(format_add)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(monthname(month))
            speak(year)
            
        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ReciversEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'open code' in query:
            codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open', '')))


        elif 'turn on lights' in query:
            speak("OK,sir turning on the Lights")
            lighton()
            speak("Lights are on")

        elif 'turn off lights' in query:
            speak("OK,sir turning off the Lights")
            lightoff()
            speak("Lights are off")

        elif 'dance' in query:
            speak("Get Lost! Otherwise i wil kick your ASS.")

        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
