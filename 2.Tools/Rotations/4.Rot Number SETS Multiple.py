import time
import pyautogui

time.sleep(5)

sets = [109, 196, 203, 195, 156, 197, 197]  # List of sets
values = [7801001, 7802001, 7803001, 7804001, 7805001, 7806001, 7807001]  # List of values for each set

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