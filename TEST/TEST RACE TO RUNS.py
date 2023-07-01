import re

text = """
SD Padres
-175
-160
-145
-110
+120
+170
CIN Reds
+145
+130
+135
+160
+210
+300
Neither
+5000
+3000
+1000
+400
+200
+105
WAS Nationals
+100
+110
+130
+170
+230
+320
PHI Phillies
-130
-140
-125
+105
+150
+220
Neither
+5000
+2000
+700
+300
+150
-125
MIL Brewers
-165
-150
-115
+120
+170
+250
PIT Pirates
+135
+130
+165
+220
+320
+450
Neither
+5000
+1200
+425
+190
+100
-180
MIN Twins
-140
-130
+100
+140
+200
+280
BAL Orioles
+110
+110
+130
+175
+240
+350
Neither
+5000
+1400
+450
+210
+105
-170
BOS Red Sox
-115
+100
+125
+170
+240
+350
TOR Blue Jays
-115
-115
+105
+145
+210
+300
Neither
+5000
+1400
+450
+200
+105
-180
"""


lines = text.strip().split("\n")  # Split the text into lines
values = [lines]


for i in range(len(lines) - 1):
    if lines[i].isalpha() and lines[i + 1].strip().isdigit():
        second_value = lines[i + 1].strip()
        values.append(second_value)

print(values)
