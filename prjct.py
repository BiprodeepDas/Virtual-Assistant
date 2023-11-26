import pyttsx3

from datetime import datetime
import webbrowser
import speech_recognition as sr
from googletrans import Translator
import httpcore

setattr(httpcore, 'SyncHTTPTransport', 'AsyncHTTPProxy')


def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"A I : {text}")
    print("")
    engine.say(text)
    engine.runAndWait()


def dateTime():
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string_date = now.strftime("%m/%d/%Y")
    dt_string_time = now.strftime("%H:%M:%S")
    print("Time and date =", dt_string_time, dt_string_date)
    return dt_string_date, dt_string_time


def takeCommand():
    print("Choose type of command 1. For speech 2. For text")
    c = input()
    if c == "2":
        query = input("Enter task :")
        return query
    if c == "1":
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Say somthing')
            audio = r.listen(source)

            voice_data = r.recognize_google(audio, language="en-In")
            return voice_data

    else:
        print("Wrong choice")


def Translation(text):
    l = str(text)
    translate = Translator()
    result = translate.translate(l)
    data = result.text
    print(f"you :{data}.")
    return data


if __name__ == '__main__':
    print("pycharm")
    d, t = dateTime()
    speak("Hello i am Hector A  I")
    speak(f"current date is {d}")
    speak(f"and current time is {t}")
    while True:
        out = takeCommand().lower()
        # out = Translation(text)

        if 'exit' in out:
            speak("Thank you.")
            exit()

        elif 'youtube' in out:
            speak("Opening youtube for you..")
            webbrowser.open("https://youtube.com")
        elif 'facebook' in out:
            speak("Opening face book for you..")
            webbrowser.open("https://facebook.com")
        elif 'wikipedia' in out:
            speak("Opening wiki pedia for you..")
            webbrowser.open("https://wikipedia.com")
        elif 'blogger' in out:
            speak("Opening blogger for you..")
            webbrowser.open("https://blogger.com")
        elif 'linkedin' in out:
            speak("Opening linkdin for you..")
            webbrowser.open("https://linkedin.com")
        elif 'play music' in out:
            from playsound import playsound

            # n=input("Enter name of song in download folder : ")
            print("Playing your  music")
            playsound('habibi.mp3')

        else:
            from Brain import reply
            print(reply(out))

        # if 'what' in out.lower():
        # resp = reply(out.lower)
        # speak("Here is what i found ")
        # print(f"AI : {resp}")
