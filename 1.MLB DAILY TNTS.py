import time
import pyautogui

time.sleep(3)
skip = 10

data = '''
Miami Marlins at Atlanta Braves:
-135
+275
+550
+1000
+1800
+2800
+4000
+6000
+7000
+7000

MIL Brewers at PIT Pirates:
-140
+265
+550
+1200
+1900
+3000
+5000
+6500
+7000
+7000

Washington Nationals at Philadelphia Phillies:
-145
+265
+550
+1200
+2200
+2800
+5000
+7000
+8000
+8000

SD Padres at CIN Reds:
-185
+270
+650
+1500
+2500
+4500
+6000
+7000
+7500
+8000

SF Giants at NY Mets:
-155
+280
+550
+1200
+2200
+3500
+5000
+7000
+7000
+7500

SF Giants at NY Mets:
-155
+280
+550
+1200
+2200
+3500
+5000
+7000
+7000
+7500

BOS Red Sox at TOR Blue Jays:
-115
+265
+500
+1000
+1700
+2200
+4000
+5500
+6000
+6500

HOU Astros at TEX Rangers:
-160
+270
+600
+1300
+2200
+4000
+5000
+6500
+7500
+8000

SF Giants at NY Mets:
-155
+280
+550
+1200
+2200
+3500
+5000
+7000
+7000
+7500

TB Rays at SEA Mariners:
-115
+270
+550
+1100
+1800
+2800
+4000
+5000
+6000
+6000

LA Dodgers at KC Royals:
-160
+270
+600
+1300
+2200
+3500
+5000
+7000
+7500
+8000

NY Yankees at STL Cardinals:
-115
+265
+500
+950
+1800
+2500
+4500
+5500
+5500
+6000

CLE Guardians at CHI Cubs:
-115
+270
+550
+1000
+1800
+2500
+4500
+5000
+6000
+7000

DET Tigers at COL Rockies:
-190
+265
+700
+1500
+2200
+4500
+6000
+8000
+9000
+9000

ARI Diamondbacks at LA Angels:
-130
+265
+550
+1100
+1800
+2500
+4500
+6000
+6000
+7000
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
