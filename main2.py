import time
import pyautogui
value = 0
time.sleep(3)

number = 16


def deleteempty():
    pyautogui.press('enter')
    pyautogui.write('450')
    pyautogui.press('enter')
    pyautogui.press('down')


    pyautogui.press('enter')
    pyautogui.write('-120')
    pyautogui.press('down')

    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')

count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    print(count)