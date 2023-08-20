import time
import pyautogui
from tqdm import tqdm

time.sleep(5)
skip = 10

# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()

lines = data.strip().split('\n')
total_lines = len(lines)
count = 0

# Wrap the loop with tqdm to create a progress bar
for index, line in enumerate(tqdm(lines, desc="Processing"), start=1):
    if line.startswith('+'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('-') or line.startswith('−'):
        value = int(line)
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')

print("Process completed!")
