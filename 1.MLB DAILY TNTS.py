import time
import pyautogui

time.sleep(3)
skip = 8

data = '''

1st Inning
−170
2nd Inning
+275
3rd Inning
+650
4th Inning
+1300
5th Inning
+2200
6th Inning
+3500
7th Inning
+5000
8th Inning
+7000
9th Inning
+8000
10th Inning or Later
+8000

'''

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
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('-') or line.startswith('−'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write('-')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
