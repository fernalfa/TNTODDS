import time
import pandas
import pyautogui

with open('../2.Tournaments/DATAPROVIDER', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

count = 0
time.sleep(3)

# Iterate through player data
number = 3

VALUE = "OVER"
VALUE1 = "UNDER"

for player in names:
    player = player.strip()  # Remove leading/trailing whitespace and newlines

    pyautogui.typewrite(player)
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(VALUE))
    pyautogui.press('tab')
    pyautogui.typewrite(str(VALUE1))
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('alt', 'o')
    time.sleep(20)

    if count == number - 1:
        print(player)
        print(count + 1)
        print('COMPLETED')
        break
    print(f"{player}: {count}")
    count += 1
