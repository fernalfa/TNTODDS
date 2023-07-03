import time
import pyautogui

time.sleep(5)

sets = [103, 214, 213, 214, 170, 214, 214]  # List of sets
values = [7251001, 7252001, 7253001, 7254001, 7255001, 7256001, 7257001]  # List of values for each set

def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)

for i, num in enumerate(sets):
    count = 0
    value = values[i]  # Get the corresponding value for the current set
    while count < num:
        value += 2
        count += 1
        deleteempty()
    pyautogui.press('down')