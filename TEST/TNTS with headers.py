import time
import pyautogui
time.sleep(3)

jump = 3
header = 1

skip = 4


def jumper():
    if header > 0:  # Check if header is greater than 0
        for _ in range(header):
            pyautogui.press('down', presses= (jump - header))
            for _ in range(header):
                enter_odd()

def enter_odd():
    pyautogui.press('enter')
    pyautogui.write('-125')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')

# Open the text file
with open('TEST', 'r') as file:
    data = file.read()

lines = data.strip().split('\n')
count = 0
for line in lines:
    if line.startswith('+'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            jumper()

    elif line.startswith('-') or line.startswith('−'):
        # Remove the minus sign from the line
        line = line.lstrip('−-')
        value = int(line)
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write('-')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            jumper()