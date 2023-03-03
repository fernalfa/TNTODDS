import time
import pyautogui
time.sleep(3)
value = 0

number = 70



def deleteempty():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('up')
    pyautogui.press('down')

count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    print(count)