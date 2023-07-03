import time
import pyautogui
time.sleep(5)
times = 0


number = 40
value = "-115"


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