import time
import pyautogui
time.sleep(3)


repeat = 4
# ENTER GAME TOTAL
total = 8.5


def deleteempty():
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.press('backspace')
    pyautogui.write(str(total))
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    pyautogui.press('down')

count = 0

while (count < repeat):
    count = count + 1
    print(count)
    print(deleteempty())