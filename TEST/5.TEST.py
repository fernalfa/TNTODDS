import time
import pyautogui
time.sleep(4)
times = 0

number = 12

def deleteempty():
    pyautogui.press('F2')

    pyautogui.press('backspace', presses = 20)
    pyautogui.press('enter')

count = 0

while (count < number):
    count = count + 1
    deleteempty()
    times = times + 1
    print(times)