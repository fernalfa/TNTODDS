import time

import pyautogui
time.sleep(3)
value = "1.5"

with open('../0.INFO', 'r') as file:
    data = file.read()


def enterodds():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('down', presses=2)
    pyautogui.press('left')

lines = data.split("\n")
target_phrase = "Under"

numbers = []

for i, line in enumerate(lines):
    if target_phrase in line:
        position = i + 2  # Get the line number 2 positions down
        if position < len(lines):
            number = lines[position]
            numbers.append(number)

if numbers:
    print(f"The numbers 2 positions down from {target_phrase}:")
    for number in numbers:
        print(number)
        enterodds()
else:
    print(f"No numbers found 2 positions down from {target_phrase}.")


