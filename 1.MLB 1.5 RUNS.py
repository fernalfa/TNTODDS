import time

import pyautogui
time.sleep(3)
value = "1.5"

data = """

CIN Reds @ MIL Brewers
Sat 8 Jul 16:10
 
0.5
1.5
2.5
3.5
Over
-140
+200
+525
+1225
Under
+110
-245
-800
-2500
OAK Athletics @ BOS Red Sox
Sat 8 Jul 16:10
 
0.5
1.5
2.5
3.5
Over
-130
+195
+525
+1425
Under
+100
-240
-800
-3000

KC Royals @ CLE Guardians
Sat 8 Jul 16:10
 
0.5
1.5
2.5
3.5
Over
-110
+215
+575
+1425
Under
-120
-270
-900
-3000


SEA Mariners @ HOU Astros
Sat 8 Jul 19:15
 
0.5
1.5
2.5
3.5
Over
+105
+270
+725
+1500
Under
-135
-360
-1200
-4000


ATL Braves @ TB Rays
Sat 8 Jul 19:15
 
0.5
1.5
2.5
3.5
Over
-115
+225
+600
+1450
Under
-115
-290
-950
-3500

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


