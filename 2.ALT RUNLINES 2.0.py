import time
import pandas
import pyautogui
# Read data from excel
time.sleep(3)

VALUE = 1
TOTAL = 8.5
A = -150
B = -230
C = -285


def alternate():

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-1')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(str(A))
        pyautogui.press('enter')
        pyautogui.press('left')
        pyautogui.press('down', presses = 4)
        pyautogui.press('enter')
        pyautogui.write('-1.5')
        pyautogui.press('enter')
        pyautogui.press('up')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(str(B))
        pyautogui.press('enter')
        pyautogui.press('left')
        pyautogui.press('down', presses=4)
        pyautogui.press('enter')
        pyautogui.write('-2.5')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(str(C))
        pyautogui.press('enter')
        pyautogui.press('left')
        pyautogui.press('down', presses = 3)
        pyautogui.press('left', presses = 6)
        pyautogui.press('enter')
        pyautogui.write(str(TOTAL + 0.5))
        pyautogui.press('enter')
        pyautogui.press('down', presses = 3)
        pyautogui.press('enter')
        pyautogui.write(str(TOTAL - 0.5))
        pyautogui.press('enter')
        pyautogui.press('down')

def alternate2():
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('-1')
    pyautogui.press('enter')
    pyautogui.press('up')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(A))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=4)
    pyautogui.press('enter')
    pyautogui.write('-1.5')
    pyautogui.press('enter')

    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(B))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=4)

    pyautogui.press('enter')
    pyautogui.write('-2.5')
    pyautogui.press('enter')
    pyautogui.press('up')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(C))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=4)
    pyautogui.press('left', presses=6)
    pyautogui.press('enter')
    pyautogui.write(str(TOTAL + 0.5))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)
    pyautogui.press('enter')
    pyautogui.write(str(TOTAL - 0.5))
    pyautogui.press('enter')
    pyautogui.press('down')



if str(int(VALUE)) == '1':
    alternate()
else:
    alternate2()
