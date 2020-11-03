import smtplib
import webbrowser as wb
import pyttsx3
import speech_recognition as sr
import datetime
import requests
import os
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 <= hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Night!")
    speak("My Name is Friday, I am Your Personal Assistant")
    speak("If You Want some Help then please say Friday Help!")


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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


if __name__ == "__main__":
    count = 0
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wake up friday' in query:
            if count >= 1:
                speak('What next?')
            else:
                speak('Always there for you Sir! How can I help You?')
            count += 1

        elif 'wikipedia' in query:
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

        elif 'dance' in query:
            speak("Get Lost! Otherwise i wil kick your ASS.")

        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
