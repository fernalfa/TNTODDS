import time
import pyautogui
time.sleep(5)

number = 300

# ENTER INITIAL ROTATION NUMBER
value = 5375001


def deleteempty():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('down', presses = 3)
count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    print(count)
    value = value + 2