import time
import pyautogui
with open('../0.INFO', 'r', encoding='utf-8', errors='replace') as file:
    value = file.read().upper()


def enterleague():

    pyautogui.hotkey('alt', 'tab')
    pyautogui.keyDown('ctrl')
    pyautogui.press('e')
    pyautogui.keyUp('ctrl')


def searchleague():
    pyautogui.write(value)


enterleague()
searchleague()
