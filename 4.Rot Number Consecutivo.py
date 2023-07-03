import time
import pyautogui
time.sleep(3)


number = 214
value = 7257001


def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    value = value + 2
    print(deleteempty())