import time
import pyautogui

with open('../0.INFO', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

count = 0
time.sleep(5)

VALUE = "OVER"
VALUE1 = "UNDER"

for line in lines:
    player = line.strip()  # Remove leading/trailing whitespace and newlines

    pyautogui.typewrite(player)
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(VALUE))
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.typewrite(str(VALUE1))
    time.sleep(3)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    time.sleep(5)
    pyautogui.hotkey('alt', 'o')

    if count == len(lines) - 1:
        print(f"{player}: {count}")
        print('COMPLETED')
        break
    print(f"{player}: {count}")
    time.sleep(15)
    count += 1
