import time
import pyautogui
time.sleep(3)


number = 50
value = 300623


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    deleteempty()
    value = value + 2
