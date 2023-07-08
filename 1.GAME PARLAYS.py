import time
import pyautogui

time.sleep(3)

totals = [8.5,
          8.5,
          7.5
          ]  # List of different total values

def entertnt():
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(3)
    pyautogui.press('tab', presses=15)
    pyautogui.press('down')


def delete_empty(total):
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.press('backspace')
    pyautogui.write(str(total))
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    pyautogui.press('down')

for total in totals:
    entertnt()
    delete_empty(total)
    delete_empty(total)
    delete_empty(total)
    delete_empty(total)
    pyautogui.hotkey('alt', 'o')
    pyautogui.press('tab')
    pyautogui.press('down', presses=6)
