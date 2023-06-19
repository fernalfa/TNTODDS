import time
import pandas
import pyautogui
# Read data from excel
time.sleep(3)


# ENTER GAME FAVORITE SIDE
VALUE = 1
# ENTER GAME TOTAL

TOTAL = 7.5

# ENTER SIDE ODDS
A = -150
B = -200
C = -315

# ENTER OVER/UNDER JUICE
UNDER = -130
OVER = -160


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
        pyautogui.press('right')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write(str(UNDER))
        pyautogui.press('enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left')
        pyautogui.press('enter')
        pyautogui.write(str(TOTAL - 0.5))
        pyautogui.press('enter')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(str(OVER))
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
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(UNDER))
    pyautogui.press('enter')
    pyautogui.press('down', presses=2)
    pyautogui.press('left')
    pyautogui.press('enter')
    pyautogui.write(str(TOTAL - 0.5))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(OVER))
    pyautogui.press('enter')
    pyautogui.press('down')



if str(int(VALUE)) == '1':
    alternate()
else:
    alternate2()
