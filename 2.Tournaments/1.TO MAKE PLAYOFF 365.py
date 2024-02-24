import time
import pyautogui
from tqdm import tqdm

time.sleep(3)
EXTRACENTS = 0
JUMP_AMOUNT = 3


def jumper(jump_amount):
    pyautogui.press('down', presses=jump_amount)

def process_line(line):
    # Remove leading '−' (minus sign, if present)
    line = line.lstrip('−')
    # Check if the line starts with '+' or '-'
    if line.startswith('+') or line.startswith('-'):
        value = int(line)
        if value > 10000:
            value = 10000
        pyautogui.press('enter')

        # Check if the value is between 100 and 110
        if 100 <= value <= 110:
            value *= -1

        pyautogui.write(str(value - EXTRACENTS))
        pyautogui.press('enter')
        jumper(JUMP_AMOUNT)

# Open the "INFO" file
try:
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\INFO.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    exit(1)

count = 0

# Initialize the tqdm progress bar
with tqdm(total=len(lines), desc="Processing lines", ncols=100) as pbar:
    for line in lines:
        # Check if the line starts with '+' or '-' (including '−')
        if line.startswith('+') or line.startswith('-') or line.startswith('−'):
            process_line(line)
            count += 1

        # Update the progress bar
        pbar.update(1)