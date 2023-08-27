import time
import pyautogui
from tqdm import tqdm  # Import tqdm
time.sleep(4)
times = 0
tab = 3


repeat = 35
def deleteempty():
    pyautogui.press('tab', presses = tab)
    pyautogui.press('space')

count = 0

# Wrap your loop with tqdm
with tqdm(total=repeat) as pbar:
    while (count < repeat):
        count = count + 1
        deleteempty()
        times = times + 1
        pbar.update(1)  # Update the progress bar
