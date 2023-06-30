import time
import pyautogui

time.sleep(3)
skip = 10
data = '''
1st Inning
−115
2nd Inning
+275
3rd Inning
+500
4th Inning
+1000
5th Inning
+1700
6th Inning
+2200
7th Inning
+4000
8th Inning
+4500
9th Inning
+6000
10th Inning or Later
+5500
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
