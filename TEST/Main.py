import time
import pyautogui
import re

time.sleep(3)

text = """
+4000
+1400
+1000
+400
+550
+1400
+600
"""

lines = text.split('\n')

# Extract common options and number values
positive_values = []
negative_values = []
options = []
values = []

for line in lines:
    option = lines
    value = int(lines[lines.index(line) + 1])

    if value < 0:
        value = int(value * 1.1)  # Reduce negative values by 10%
    elif value > 0:
        value = int(value * 0.9)  # Reduce positive values by 10%

    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down')

# Print the extracted information
print("Values:", positive_values)
print("Values:", negative_values)
pyautogui.press('down')
pyautogui.press('down')