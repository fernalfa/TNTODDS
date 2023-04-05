import time
import pyautogui
time.sleep(5)


a = 3
number = 10
value = 551161



def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = a)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    value = value + 2
