import time
import pyautogui

time.sleep(3)
number = 0

repeat = 4
total = 7.5


def delete_empty():
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'end')
    pyautogui.press('backspace')
    pyautogui.write(str(total))
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    pyautogui.press('down')

count = 0

while count < repeat:
    if count == repeat - 1:
        print(count + 1)
        delete_empty()
        pyautogui.hotkey('alt', 'o')
        print('COMPLETED, PLEASE CHECK')
        break
    print(count + 1)
    delete_empty()
    count += 1