import time
import pyautogui
time.sleep(3)

data = '''
MIA Marlins @ ATL Braves
Sun 2 Jul 13:35
Solo HR
-145
2-Run HR
+190
3-Run HR
+800
Grand Slam
+4000
No HR Scored
+750
MIL Brewers @ PIT Pirates
Sun 2 Jul 13:35
Solo HR
-130
2-Run HR
+200
3-Run HR
+850
Grand Slam
+3500
No HR Scored
+550
WAS Nationals @ PHI Phillies
Sun 2 Jul 13:35
Solo HR
-170
2-Run HR
+190
3-Run HR
+800
Grand Slam
+4000
No HR Scored
+1100

SD Padres @ CIN Reds
Sun 2 Jul 13:40
Solo HR
-150
2-Run HR
+170
3-Run HR
+650
Grand Slam
+3500
No HR Scored
+1400

SF Giants @ NY Mets
Sun 2 Jul 19:05
Solo HR
-145
2-Run HR
+180
3-Run HR
+750
Grand Slam
+3500
No HR Scored
+1000


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