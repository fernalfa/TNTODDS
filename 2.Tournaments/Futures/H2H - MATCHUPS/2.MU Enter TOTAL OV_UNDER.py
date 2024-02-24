import re
import pyautogui
import time
time.sleep(3)

# Open the text file
with open('../../../INFO.txt', 'r') as file:
    data = file.readlines()

    # Extract non-negative numbers
extracted_values = []
for line in data:
    num = float(line.strip())  # Convert the line to a floating-point number
    if num >= 0:
        extracted_values.append(num)

print(extracted_values)

for value in extracted_values:
    print(value)
    pyautogui.press('enter')
    pyautogui.write(str(value))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')