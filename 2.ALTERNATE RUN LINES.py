import time
import pandas
import pyautogui
# Read data from excel
time.sleep(3)


TOTAL = 8.5
VALUE = 2

def alternate():

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-1')
        pyautogui.press('enter')
        pyautogui.press('down', presses = 5)
        pyautogui.press('enter')
        pyautogui.write('-1.5')
        pyautogui.press('enter')
        pyautogui.press('down', presses = 3)
        pyautogui.press('enter')
        pyautogui.write('-2.5')
        pyautogui.press('enter')
        pyautogui.press('down', presses = 4)
        pyautogui.press('left', presses = 6)
        pyautogui.press('enter')
        pyautogui.write(str(TOTAL + 0.5))
        pyautogui.press('enter')
        pyautogui.press('down', presses = 3)
        pyautogui.press('enter')
        pyautogui.write(str(TOTAL - 0.5))
        pyautogui.press('enter')
def alternate2():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('-1')
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)
    pyautogui.press('enter')
    pyautogui.write('-1.5')
    pyautogui.press('enter')
    pyautogui.press('down', presses=5)
    pyautogui.press('enter')
    pyautogui.write('-2.5')
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)
    pyautogui.press('left', presses=6)
    pyautogui.press('enter')
    pyautogui.write(str(TOTAL + 0.5))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)
    pyautogui.press('enter')
    pyautogui.write(str(TOTAL - 0.5))
    pyautogui.press('enter')

if str(int(VALUE)) == '1':
    alternate()
else:
    alternate2()
