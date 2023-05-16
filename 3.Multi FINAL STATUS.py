import time
import pyautogui

time.sleep(3)

number = 10


def deleteempty():
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f')
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)


count = 0

while (count < number):
    count = count + 1
    print(count)
    print(deleteempty())
