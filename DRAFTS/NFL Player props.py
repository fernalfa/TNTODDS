import time
import pyautogui
time.sleep(3)


number = 4


def deleteempty():
    pyautogui.press('home')
    pyautogui.press('end')
    pyautogui.write(', ')
    pyautogui.press('del')
    pyautogui.press('down')
    pyautogui.press('down')



count = 0

while (count < number):
    count = count + 1
    print(deleteempty())