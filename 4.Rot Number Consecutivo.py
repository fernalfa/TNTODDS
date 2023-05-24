import time
import pyautogui

time.sleep(3)
number = 15

value = 99901

def delete_empty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses=6)

for count in range(1, number + 1):
    delete_empty()
    print(count)
    value += 2