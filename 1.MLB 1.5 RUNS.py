import time

import pyautogui
time.sleep(3)
value = "1.5"

data = """
CLE Guardians @ CHI Cubs
Fri 30 Jun 14:21
 
0.5
1.5
2.5
3.5
Over
-115
+225
+575
+1425
Under
-115
-290
-900
-3000
SD Padres @ CIN Reds
Fri 30 Jun 17:10
 
0.5
1.5
2.5
3.5
Over
-155
+175
+475
+1125
Under
+125
-220
-700
-2200
WAS Nationals @ PHI Phillies
Fri 30 Jun 18:06
 
0.5
1.5
2.5
3.5
Over
-135
+185
+500
+1225
Under
+105
-230
-750
-2500
MIL Brewers @ PIT Pirates
Fri 30 Jun 19:05
 
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
MIN Twins @ BAL Orioles
Fri 30 Jun 19:05
 
0.5
1.5
2.5
3.5
Over
-120
+220
+575
+1450
Under
-110
-280
-900
-3500
BOS Red Sox @ TOR Blue Jays
Fri 30 Jun 19:07
 
0.5
1.5
2.5
3.5
Over
-130
+200
+500
+1225
Under
+100
-245
-750
-2500
SF Giants @ NY Mets
Fri 30 Jun 19:11
 
0.5
1.5
2.5
3.5
Over
-125
+230
+500
+1225
Under
-110
-300
-750
-2500
MIA Marlins @ ATL Braves
Fri 30 Jun 19:20
 
0.5
1.5
2.5
3.5
Over
-145
+175
+475
+1225
Under
+115
-220
-700
-2500
HOU Astros @ TEX Rangers
Fri 30 Jun 20:06
 
0.5
1.5
2.5
3.5
Over
-150
+175
+475
+1125
Under
+120
-220
-700
-2200
DET Tigers @ COL Rockies
Fri 30 Jun 20:10
 
0.5
1.5
2.5
3.5
Over
-165
+160
+425
+1075
Under
+135
-190
-600
-2000
LA Dodgers @ KC Royals
Fri 30 Jun 20:11
 
0.5
1.5
2.5
3.5
Over
-135
+175
+475
+1225
Under
+105
-220
-700
-2500
NY Yankees @ STL Cardinals
Fri 30 Jun 20:15
 
0.5
1.5
2.5
3.5
Over
-140
+185
+500
+1125
Under
+110
-230
-750
-2200
ARI Diamondbacks @ LA Angels
Fri 30 Jun 21:38
 
0.5
1.5
2.5
3.5
Over
-145
+165
+425
+1025
Under
+115
-200
-600
-1800
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


