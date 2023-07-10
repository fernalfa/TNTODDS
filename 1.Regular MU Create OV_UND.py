import time
import pyautogui

# Read data from text file
with open('0.INFO', 'r') as file:
    names = file.read().splitlines()

time.sleep(3)

# Iterate through the names
VALUE = "OVER"
VALUE1 = "UNDER"

for name in names:
    pyautogui.typewrite(str(name))
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(VALUE))
    pyautogui.press('tab')
    pyautogui.typewrite(str(VALUE1))
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    time.sleep(20)
    pyautogui.hotkey('alt', 'o')
    time.sleep(20)

    print(name)

print('COMPLETED')
