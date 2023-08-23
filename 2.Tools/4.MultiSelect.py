import time
import pyautogui
from tqdm import tqdm  # Import tqdm

time.sleep(4)
times = 0
press = 3

number = 19
def deleteempty():
    pyautogui.press('tab', presses = press)
    pyautogui.press('space')

count = 0

# Wrap your loop with tqdm
with tqdm(total=number) as pbar:
    while (count < number):
        count = count + 1
        deleteempty()
        times = times + 1
        pbar.update(1)  # Update the progress bar
