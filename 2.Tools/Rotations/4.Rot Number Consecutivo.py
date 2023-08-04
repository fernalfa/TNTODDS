import time
import pyautogui
time.sleep(5)


number = 150
value = 6601001


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    print(count)
    deleteempty()
    value = value + 2
