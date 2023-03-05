import time
import pyautogui
time.sleep(3)

ROTATION = 821001
ADD = 2

REPEAT = 20
def deleteempty():
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.typewrite(str(ROTATION))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < REPEAT):
    count = count + 1
    print(str(ROTATION))
    print(deleteempty())
    ROTATION = ROTATION + ADD
