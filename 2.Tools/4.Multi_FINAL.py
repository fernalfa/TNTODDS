import time
import pyautogui
from tqdm import tqdm  # Import tqdm
time.sleep(3)
times = 0
tab = 1
DELAY = 2


repeat = 4

def set_status_final():
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f')
    pyautogui.press('enter')
    time.sleep(DELAY)
    pyautogui.press('down', presses = 3)
    #pyautogui.press('space')

count = 0

# Wrap your loop with tqdm
with tqdm(total=repeat) as pbar:
    while (count < repeat):
        count = count + 1
        set_status_final()
        times = times + 1
        pbar.update(1)  # Update the progress bar
