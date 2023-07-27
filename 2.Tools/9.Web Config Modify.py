import time
import pyautogui
time.sleep(3)


number = 8
value = 1100

def WebConfigMod():

    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace')

    pyautogui.typewrite(str(value))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab', presses = 4)
    pyautogui.press('down')



count = 0

while (count < number):
    count = count + 1
    WebConfigMod()
