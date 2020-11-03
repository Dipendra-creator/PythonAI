import smtplib
import webbrowser as wb
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import timeit

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
    r = sr.()
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
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'hello' in query:
            speak("Hello! What's your Good Name")
            name = takeCommand()
            speak("Hello "+name+" Welcome to our AI, we are continuously working on it. Hope You like it!")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia!")
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
                print('google think you said:\n' + text + '.com')
                wb.get(chrome_path).open(text + '.com')
            except Exception as e:
                print(e)
        # elif 'how is the weather' and 'weather' in query:
        #
        #         url = 'https://api.openweathermap.org/'  # Open api link here
        #
        #         res = requests.get(url)
        #
        #         data = res.json()
        #
        #         weather = data['weather'][0]['main']
        #         temp = data['main']['temp']
        #         wind_speed = data['wind']['speed']
        #
        #         latitude = data['coord']['lat']
        #         longitude = data['coord']['lon']
        #
        #         description = data['weather'][0]['description']
        #         speak('Temperature : {} degree celcius'.format(temp))
        #         print('Wind Speed : {} m/s'.format(wind_speed))
        #         print('Latitude : {}'.format(latitude))
        #         print('Longitude : {}'.format(longitude))
        #         print('Description : {}'.format(description))
        #         print('weather is: {} '.format(weather))
        #         speak('weather is : {} '.format(weather))

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
        elif 'open music' in query:
            music_dir = 'https://www.youtube.com/watch?v=JGwWNGJdvx8&list=RDJGwWNGJdvx8&start_radio=1'
            wb.get(chrome_path).open(music_dir)
        elif 'get lost' or 'exit' in query:
            speak('OK! Stay Home, Stay Safe')
            break
