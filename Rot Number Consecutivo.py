import time
import pyautogui
time.sleep(3)


number = 2
value = 537


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('home')
    pyautogui.press('del')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())