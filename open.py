import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


def pressandrel(key, times):
    while times > 0:
        keyboard.press_and_release(key)
        pyautogui.sleep(.50)
        times -= 1


def execute(query):
    query=str(query).lower()

    if "visit" in query :
        query=query.replace("visit","")
        nameOfWeb=query.strip()
        link="https://www.bing.com/search?q="+nameOfWeb
        webbrowser.open(link)
        # keyboard.write(nameOfWeb)
        # pyautogui.sleep(25)
        # keyboard.press_and_release('enter')

    elif "open" in query :
        query=query.replace("open","")
        Name=query.strip()
        pyautogui.hotkey('win','s')
        pyautogui.sleep(1)
        keyboard.write(Name)
        keyboard.press('enter')
        sleep(.5)

    elif "search" in query :
        query = query.replace("search", "")
        Name = query.strip()
        pyautogui.hotkey('win', 's')
        pyautogui.sleep(1)
        keyboard.write("file explorer")
        keyboard.press_and_release('enter')
        pyautogui.sleep(.30)
        pressandrel('tab', 3)
        keyboard.press_and_release('enter')
        pyautogui.sleep(1)
        keyboard.write("This pc")
        pyautogui.sleep(1)
        pressandrel('enter', 1)
        pressandrel('tab', 6)
        pyautogui.sleep(1)
        keyboard.write(Name)
        pyautogui.sleep(1)
        keyboard.press_and_release('enter')

    return True

#execute("visit todays ipl match")