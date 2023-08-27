import time
import pyautogui
from tqdm import tqdm  # Import tqdm

# Function to type slowly
def slow_typewrite(text, delay=0.1):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)

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

# Wrap the lines iteration with tqdm
for line in tqdm(lines, desc="Processing", unit="player"):
    player = line.strip()

    slow_typewrite(player)
    pyautogui.press('tab', presses=2)
    slow_typewrite(str(VALUE))
    pyautogui.press('tab')
    time.sleep(3)
    slow_typewrite(str(VALUE1))
    time.sleep(3)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    time.sleep(10)
    pyautogui.hotkey('alt', 'o')

    if count == len(lines) - 1:
        print(f"{player}: {count}")
        print('COMPLETED')
        break
    print(f"{player}: {count}")
    time.sleep(15)
    count += 1
