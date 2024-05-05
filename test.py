# import os
#
# flag = 0
#
#
# def myDrive():
#     drives = []
#     for x in range(65, 91):
#         if os.path.exists(chr(x) + ":"):
#             drives.append(chr(x))
#     print("The drives present in the pc =\n", drives)
#     return drives
#
#
# def myPath(drives, file):
#     print("Initialising search....")
#     print("Searching in all locations...")
#     global flag
#     for d in drives:
#         drv = d + ":\\"
#         for root, dirs, files in os.listdir(drv):
#             for name in files:
#                 if name==file:
#                     print(os.path.abspath(os.path.join(root, name)))
#                     flag = 1
#     return flag
#
#
# d = myDrive()
# print("Be careful it is case sensitive search!. ")
# file = input("Enter the file name to be searched = ")
# flag = myPath(d, file)
# if flag == 0:
#     print("File not found")
import keyboard
import pyautogui


def pressandrel(key, times):
    while times > 0:
        keyboard.press_and_release(key)
        pyautogui.sleep(.35)
        times -= 1


def search(filename):
    pyautogui.hotkey('win', 's')
    pyautogui.sleep(1)
    keyboard.write("file explorer")
    keyboard.press_and_release('enter')
    pyautogui.sleep(.20)
    pressandrel('tab', 3)
    keyboard.press_and_release('enter')
    pyautogui.sleep(1)
    keyboard.write("This pc")
    pyautogui.sleep(1)
    pressandrel('enter', 1)
    pressandrel('tab', 6)
    pyautogui.sleep(1)
    keyboard.write(filename)
    pyautogui.sleep(1)
    keyboard.press_and_release('enter')


search("games")
