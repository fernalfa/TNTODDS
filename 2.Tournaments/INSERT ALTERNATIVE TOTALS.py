import re
import pyautogui
import time
time.sleep(5)

# Open the text file
with open('../0.INFO', 'r') as file:
    text = file.read()


text = re.sub(r'(\d+)½', r'\1.5', text)

pattern = r'o(\d*\.?\d+)'
matches = re.findall(pattern, text)

values = [float(match) for match in matches]

def modify_values(matches):
    modified_values = []
    for value in matches:
        modified_values.extend([value + 0.5, value - 0.5])
    return modified_values

modified_data = modify_values(values)

for value in modified_data:
    print(value)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(value))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')