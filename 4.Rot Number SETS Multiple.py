import time
import pyautogui

time.sleep(5)

sets = [3, 10, 5, 2]  # List of sets
values = [7255101, 7260000, 7281000, 7300000]  # List of values for each set

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