import time
import pyautogui
time.sleep(3)


number = 5
value = 91
value2 = 99


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('home')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
    pyautogui.press('enter')
    pyautogui.press('home')
    pyautogui.typewrite(str(value2))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 5)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())