import time
import pyautogui
time.sleep(3)


number = 8
ORDER = 1100
add = 10


def WebConfigMod():

    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(ORDER))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab', presses = 4)
    pyautogui.press('down')
    time.sleep(1)



count = 0

while (count < number):
    count = count + 1
    WebConfigMod()
    ORDER = ORDER + add
