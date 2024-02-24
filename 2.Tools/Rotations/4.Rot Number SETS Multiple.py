import time
import pyautogui

time.sleep(5)

sets = [103, 2531, 231, 230, 189, 231, 231]  # List of sets
values = [7101001, 7102001, 7103001, 7104001, 7105001, 7106001, 7107001]  # List of values for each set

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