import time
import pyautogui
from tqdm import tqdm

time.sleep(5)
skip = 4

# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()

lines = data.strip().split('\n')
count = 0

# Count the number of lines that need processing
num_lines = sum(1 for line in lines if line.startswith('+') or line.startswith('-') or line.startswith('−'))

# Initialize the tqdm progress bar
with tqdm(total=num_lines, desc="Processing lines", ncols=100) as pbar:
    for line in lines:
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

        # Update the progress bar
        pbar.update(1)
