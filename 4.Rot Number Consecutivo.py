import time
import pyautogui
time.sleep(5)


number = 26
value = 1399


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('end')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    value = value + 2
    print(deleteempty())