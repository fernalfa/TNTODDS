import re
import pyautogui
import time
time.sleep(5)

with open('../0.INFO', 'r') as file:
    data = file.read()

pattern = r"Moneyline / Total Runs\n\n.*?(\d+\.\d+)\n"

matches = re.findall(pattern, data)

for match in matches:
    print(match)


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

for match in matches:
    entertnt()
    delete_empty(match)
    delete_empty(match)
    delete_empty(match)
    delete_empty(match)
    pyautogui.hotkey('alt', 'o')
    pyautogui.press('tab')
    pyautogui.press('down', presses=6)