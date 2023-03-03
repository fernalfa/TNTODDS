import time
import pyautogui
time.sleep(3)


number = 61


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())