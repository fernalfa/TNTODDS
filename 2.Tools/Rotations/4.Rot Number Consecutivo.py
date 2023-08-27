import time
from tqdm import tqdm
import pyautogui
time.sleep(5)


number = 40
value = 5563001
add = 2


def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

# Wrap your loop with tqdm
with tqdm(total=number) as pbar:
    while count < number:
        count = count + 1
        deleteempty()
        value = value + add
        pbar.update(1)  # Update the progress bar