import time
import pyautogui
from tqdm import tqdm

# Wait for 4 seconds
time.sleep(4)

# Precomputed values
repeat = 60
tab = 3

def delete_empty():
    pyautogui.press('tab', presses=tab)
    pyautogui.press('space')

# Wrap your loop with tqdm
with tqdm(total=repeat) as pbar:
    for _ in range(repeat):
        delete_empty()
        pbar.update(1)
