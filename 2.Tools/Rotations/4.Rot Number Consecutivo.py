import time
from tqdm import tqdm
import pyautogui
time.sleep(3)

number = 79
value = 2001

JUMP = 3



add = 2



def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = JUMP)

count = 0


# Wrap your loop with tqdm
with tqdm(total=number) as pbar:
    while count < number:
        count = count + 1
        deleteempty()
        value = value + add
        pbar.update(1)  # Update the progress bar