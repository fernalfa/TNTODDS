import time
import pyautogui
times = 0
time.sleep(3)

repeat = 2

def deleteempty():

    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('right', presses=6)
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('right', presses=6)
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('left', presses=12)
    pyautogui.press('down', presses=2)


count = 0

while (count < repeat):
    count = count + 1
    print(deleteempty())
    times = times + 1
    print(times)