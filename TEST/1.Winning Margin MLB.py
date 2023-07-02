import time
import pyautogui
time.sleep(3)

data = '''
SF Giants @ NY Mets
Sun 2 Jul 19:05
 
1
2
3
4+
SF Giants
+750
+700
+900
+365
NY Mets
+375
+750
+900
+390

MIN Twins @ BAL Orioles
Sun 2 Jul 12:05
 
1
2
3
4+
MIN Twins
+650
+700
+850
+310
BAL Orioles
+500
+750
+1000
+425

BOS Red Sox @ TOR Blue Jays
Sun 2 Jul 13:37
 
1
2
3
4+
BOS Red Sox
+800
+800
+1100
+600
TOR Blue Jays
+375
+650
+750
+265

HOU Astros @ TEX Rangers
Sun 2 Jul 14:35
 
1
2
3
4+
HOU Astros
+800
+750
+900
+390
TEX Rangers
+450
+700
+850
+325

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
        if count % 8 == 0:
            pyautogui.press('down')
            pyautogui.press('down')