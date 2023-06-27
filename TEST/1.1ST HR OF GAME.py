import time
import pyautogui

time.sleep(3)

data = '''
SF Giants @ TOR Blue Jays
Tue 27 Jun 19:07
Solo HR
-145
2-Run HR
+200
3-Run HR
+800
Grand Slam
+4000
No HR Scored
+650
MIL Brewers @ NY Mets
Tue 27 Jun 19:10
Solo HR
-145
2-Run HR
+175
3-Run HR
+700
Grand Slam
+3500
No HR Scored
+1100
'''

lines = data.strip().split('\n')
count = 0
for line in lines:
    if line.startswith('+'):
        pyautogui.press('enter')
        pyautogui.write(line[1:])
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % 5 == 0:
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('-'):
        pyautogui.press('enter')
        pyautogui.write('-')
        pyautogui.write(line[1:])
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % 5 == 0:
            pyautogui.press('down')
            pyautogui.press('down')
