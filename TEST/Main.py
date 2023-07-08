import time
import pyautogui
time.sleep(3)

data = '''CIN Reds-logoCIN Reds
at
BAL Orioles-logoBAL Orioles
TODAY 7:05PM
Inning of First Run

1st Inning
−195
2nd Inning
+285
3rd Inning
+650
4th Inning
+1400
5th Inning
+2500
6th Inning
+4500
7th Inning
+5500
8th Inning
+7000
9th Inning
+7500
10th Inning or Later
+8000
Inning of Last Run

9th Inning
+135
8th Inning
+220
7th Inning
+550
10th Inning or Later
+800
6th Inning
+900
5th Inning
+1800
4th Inning
+3000
3rd Inning
+4500
2nd Inning
+7500
1st Inning
+8000'''

lines = data.split('\n')

for i in range(14, 24):
    inning_line = lines[i].split()
    value_line = lines[i+1].split()
    inning = inning_line[0]
    value = value_line[0]
    code = f"pyautogui.press('enter')\npyautogui.write('{value}')\npyautogui.press('enter')\npyautogui.press('down')"
    print(code)