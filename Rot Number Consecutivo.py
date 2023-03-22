import time
import pyautogui
time.sleep(5)


number = 100
value = 8113

def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('end')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    value = value + 2