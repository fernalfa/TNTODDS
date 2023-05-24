import time
import pyautogui
import re

time.sleep(3)

text = """STL Cardinals @ CIN Reds
Tue 23 May 18:40
Solo HR
-150
2-Run HR
+175
3-Run HR
+700
Grand Slam
+3500
No HR Scored
+1200"""

lines = text.split('\n')

# Extract team names and date
teams = lines[0]
dates = re.findall(r"[\w\s]+ \d+ [A-Za-z]+\s\d+:\d+", text)
lines = lines[2:]  # Remove the team names and dates from lines

# Extract common options and number values
positive_values = []
negative_values = []
options = []
values = []
for i in range(0, len(lines), 2):
    option = lines[i]
    value = int(lines[i + 1])

    options.append(option)
    if value < 0:
        value = int(value * 1.1)  # Reduce negative values by 10%
        negative_values.append(value)
    elif value > 0:
        value = int(value * 0.9)  # Reduce positive values by 10%
        positive_values.append(value)

    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down')
    values.append(value)

# Print the extracted information
print("Teams:", teams)
print("Dates:", dates)
print("Options:", options)
print("Values:", values)
pyautogui.press('down')
pyautogui.press('down')
