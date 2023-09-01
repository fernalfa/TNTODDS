import time
import pyautogui
time.sleep(3)


number = 9
ORDER = 205
add = 0


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



count = 0

while (count < number):
    count = count + 1
    WebConfigMod()
    ORDER = ORDER + add
