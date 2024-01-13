import time
import pyautogui


time.sleep(5)

sets = [67, 79, 80, 80, 79]  # List of sets
values = [5001, 5501, 6001, 6501, 7001]  # List of values for each set

def deleteempty():

    pyautogui.press('enter')
    pyautogui.press('right')
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
