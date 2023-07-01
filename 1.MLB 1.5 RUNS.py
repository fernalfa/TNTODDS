import time

import pyautogui
time.sleep(3)
value = "1.5"

data = """
SD Padres @ CIN Reds
Sat 1 Jul 13:40
 
0.5
1.5
2.5
3.5
Over
-175
+155
+425
+1025
Under
+145
-185
-600
-1800
NY Yankees - Game 1 @ STL Cardinals - Game 1
Sat 1 Jul 14:15
 
0.5
1.5
2.5
3.5
Over
-140
+195
+500
+1225
Under
+110
-240
-750
-2500
BOS Red Sox @ TOR Blue Jays
Sat 1 Jul 15:07
 
0.5
1.5
2.5
3.5
Over
-135
+195
+500
+1225
Under
+105
-240
-750
-2500
WAS Nationals @ PHI Phillies
Sat 1 Jul 16:05
 
0.5
1.5
2.5
3.5
Over
-120
+230
+625
+1500
Under
-110
-300
-1000
-4000


MIL Brewers @ PIT Pirates
Sat 1 Jul 16:05
 
0.5
1.5
2.5
3.5
Over
-115
+230
+650
+1450
Under
-115
-300
-1050
-3500

HOU Astros @ TEX Rangers
Sat 1 Jul 16:05
 
0.5
1.5
2.5
3.5
Over
-120
+220
+575
+1425
Under
-110
-280
-900
-3000

MIN Twins @ BAL Orioles
Sat 1 Jul 16:05
 
0.5
1.5
2.5
3.5
Over
-115
+225
+575
+1450
Under
-115
-290
-900
-3500


CHI White Sox @ OAK Athletics
Sat 1 Jul 16:07
 
0.5
1.5
2.5
3.5
Over
-115
+240
+650
+1500
Under
-115
-320
-1050
-4000

SF Giants @ NY Mets
Sat 1 Jul 16:10
 
0.5
1.5
2.5
3.5
Over
-125
+210
+550
+1425
Under
-105
-260
-850
-3000
MIA Marlins @ ATL Braves
Sat 1 Jul 16:10
 
0.5
1.5
2.5
3.5
Over
-130
+180
+475
+1225
Under
+100
-225
-700
-2500
"""
def enterodds():
    pyautogui.press('enter')
    pyautogui.typewrite(str(value))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('down', presses=2)
    pyautogui.press('left')

lines = data.split("\n")
target_phrase = "Under"

numbers = []

for i, line in enumerate(lines):
    if target_phrase in line:
        position = i + 2  # Get the line number 2 positions down
        if position < len(lines):
            number = lines[position]
            numbers.append(number)

if numbers:
    print(f"The numbers 2 positions down from {target_phrase}:")
    for number in numbers:
        print(number)
        enterodds()
else:
    print(f"No numbers found 2 positions down from {target_phrase}.")


