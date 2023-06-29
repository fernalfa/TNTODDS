import time
import pyautogui
time.sleep(5)
times = 0


number = 20
value = "-500"


def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    times = times + 1
    print(times)