import time
import pyautogui

time.sleep(5)

sets = [113, 244, 244, 244, 185, 244, 244]  # List of sets
values = [7401001, 7402001, 7403001, 7404001, 7405001, 7406001, 7407001]  # List of values for each set

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