from open import execute
import pyttsx3
from datetime import datetime
import speech_recognition as sr
from googletrans import Translator
import httpcore

setattr(httpcore, 'SyncHTTPTransport', 'AsyncHTTPProxy')


def internetConnectionChecker():
    import subprocess
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False


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
        query = input("Enter index no. :")
        return query
    if c == "1":
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Speak now')
            audio = r.listen(source)

            try:
                voice_data = r.recognize_google(audio, language="en-In")
            except:
                del voice_data
                takeCommand()
            return voice_data.lower()

    else:
        print("Wrong choice")
        takeCommand()


def takeQuestion():
    print("Choose type of input form 1. For speech 2. For text")
    c = input()
    if c == "2":
        query = input("Give your input :")
        return query
    if c == "1":
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Speak now ')
            audio = r.listen(source)

            try:
                voice_data = r.recognize_google(audio, language="en-In")
                if internetConnectionChecker():
                    voice_data=Translation(voice_data)
            except:
                takeQuestion()
            return voice_data.lower()

    else:
        print("Wrong choice")
        takeCommand()


def Translation(text):
    l = str(text)
    translate = Translator()
    result = translate.translate(l)
    data = result.text
    # print(f"you :{data}.")
    return data


if __name__ == '__main__':
    print("pycharm")
    d, t = dateTime()
    # speak("Hello i am Hector , Your Virtual Assistant")
    # speak(f"current date is {d}")
    # speak(f"and current time is {t}")
    # speak(
    #     "I can also suggest medicines and remedies for basic health issues to enable this mode please enter M in input Thankyou! ")
    print("As a prototype currently i can assist you in the following categories of tasks :")

    while True:
        print("\n\n1.For solving study related problems (problems of class 10-12 level).*(Requires Internet connection)*\n"
              "2.Launch any application present in your System.\n"
              "3.Find you the location of any virtual object that is present in your system.\n"
              "4.Perform a web search on a given query.*(Requires Internet connection)*\n"
              "5.Predict a disease based on given symptoms using ML.\n"
              "6.Provide some known remedies for a particular given disease.*(Requires Internet connection for new search)*\n"
              "7.Chat randomly.*(Requires Internet connection for new search)*\n"
              "8. to exit!.\n"
              "***************\n"
              "Please input the given Index number for respective operations that you want me to perform except normal chat\n"
              "Please give instructions in English only in case of offline System\n"
              "***************\n")
        try:
            out = takeCommand()
            if internetConnectionChecker():
                out = Translation(out)
            dLen = len(out)
            print(f"You : {out}")
        except Exception as e:
            print(f"Error!{e}. Please kindly retry! ")
            continue

        if out == '8' or out == 'eight':
            speak("Thank you.")
            break

        elif out == '1' or out == 'one':
            try:
                question = takeQuestion().lower()
                quesLen = len(question)

                if quesLen <= 3:
                    pass

                from questionanswer import replyques

                replyques(question)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '2' or out == 'two':
            try:
                ip = takeQuestion()
                execute("open" + ip)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '3' or out == 'three':
            try:
                ip = takeQuestion()
                execute("search" + ip)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '4' or out == 'four':
            try:
                ip = takeQuestion()
                execute("visit" + ip)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '5' or out == 'five':
            print("Please enter 2 symptoms \n")
            s1 = takeQuestion()
            s2 = takeQuestion()
            # s3=takeQuestion()
            d = s1 + "," + s2  # + "," + s3
            try:
                from diseasPredic import takeD

                takeD(d)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '6' or out == 'six':
            try:
                from medBrain import take

                print("Please enter symptoms (MAx 2)\n")
                ip = takeQuestion()
                take(ip)
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        elif out == '7' or out == 'seven':
            try:
                ip = takeQuestion()
                from Brain import reply
                print(reply(ip))
            except Exception as e:
                print(f"Error!{e}. Please kindly retry! ")

        else:
            print("You have chosen a wrong option.")

        # if 'what' in out.lower():
        # resp = reply(out.lower)
        # speak("Here is what i found ")
        # print(f"AI : {resp}")
