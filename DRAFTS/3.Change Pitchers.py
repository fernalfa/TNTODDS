import time
import pyautogui
time.sleep(3)



number = 1

value = 8001401


def deleteempty():
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.press('tab', presses = 13)
    pyautogui.press('backspace')
    pyautogui.press('tab')
    pyautogui.press('backspace')
    pyautogui.hotkey('alt', 'o')
    pyautogui.press('enter')
    pyautogui.write('-109')
    pyautogui.press('tab')
    pyautogui.hotkey('alt', 'o')
    pyautogui.typewrite('YES')
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())