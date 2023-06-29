import time
import pyautogui

time.sleep(5)

sets = [3, 10, 5, 2]  # List of sets
value = 7255101

def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down' , presses = 3)

for num in sets:
    count = 0
    while count < num:
        value += 2
        count += 1
        deleteempty()
    pyautogui.press('down')
    pyautogui.press('down')