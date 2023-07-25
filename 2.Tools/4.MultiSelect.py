import time
import pyautogui
time.sleep(4)
times = 0

number = 300

def deleteempty():
    pyautogui.press('tab')
    pyautogui.press('space')

count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    times = times + 1
    print(times)