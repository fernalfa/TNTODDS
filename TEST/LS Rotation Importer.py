import time
import pyautogui
from tqdm import tqdm  # Import tqdm

time.sleep(4)

suffix = 88
add = 2

def insert_rot(value):
    pyautogui.typewrite(str(suffix))
    pyautogui.typewrite(str(value))
    pyautogui.press('tab')
    pyautogui.typewrite(str(suffix))
    pyautogui.typewrite(str(value + 1))
    pyautogui.press('tab')
    pyautogui.press('tab')

# Read the values from the file
with open('../0.INFO', 'r') as file:
    lines = file.readlines()
    values = [int(line.strip()) for line in lines]

# Wrap your loop with tqdm
with tqdm(total=len(values)) as pbar:
    for value in values:
        insert_rot(value)
        pbar.update(1)  # Update the progress bar

