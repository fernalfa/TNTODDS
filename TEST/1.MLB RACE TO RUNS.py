import re


def remove_lines_with_at_symbol_and_dates(text):
    lines = text.split("\n")
    modified_lines = [line for line in lines if
                      "@" not in line and not re.search(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", line)]
    return "\n".join(modified_lines)


def remove_expression_from_text(text, expression):
    return text.replace(expression, "")


# Example usage
input_text = '''
SD Padres @ CIN Reds
Sat 1 Jul 13:40
 
2
3
4
5
6
7
SD Padres
-210
-190
-180
-150
-115
+120
CIN Reds
+170
+160
+155
+190
+240
+325
Neither
+5000
+4000
+1400
+500
+250
+135
NY Yankees - Game 1 @ STL Cardinals - Game 1
Sat 1 Jul 14:15
 
2
3
4
5
6
7
NY Yankees - Game 1
-115
-105
+120
+160
+225
+320
STL Cardinals - Game 1
-115
-115
+110
+150
+220
+325
Neither
+5000
+1400
+450
+200
+105
-175
BOS Red Sox @ TOR Blue Jays
Sat 1 Jul 15:07
 
2
3
4
5
6
7
BOS Red Sox
-110
+105
+140
+190
+260
+375
TOR Blue Jays
-120
-125
-105
+130
+190
+275
Neither
+5000
+1400
+450
+210
+105
-175
HOU Astros @ TEX Rangers
Sat 1 Jul 16:05
 
2
3
4
5
6
7
HOU Astros
-115
+105
+140
+190
+280
+400
TEX Rangers
-115
-105
+125
+180
+275
+400
Neither
+4000
+850
+300
+145
-135
-250
MIL Brewers @ PIT Pirates
Sat 1 Jul 16:05
 
2
3
4
5
6
7
MIL Brewers
-165
-150
-115
+120
+175
+260
PIT Pirates
+135
+140
+175
+250
+350
+500
Neither
+4000
+1000
+375
+170
-115
-200
MIN Twins @ BAL Orioles
Sat 1 Jul 16:05
 
2
3
4
5
6
7
MIN Twins
-115
+100
+130
+175
+250
+350
BAL Orioles
-115
-115
+105
+145
+210
+300
Neither
+5000
+1200
+425
+200
+100
-180
WAS Nationals @ PHI Phillies
Sat 1 Jul 16:05
 
2
3
4
5
6
7
WAS Nationals
+115
+130
+165
+225
+320
+450
PHI Phillies
-145
-145
-120
+115
+170
+250
Neither
+5000
+1200
+425
+190
+100
-180
CHI White Sox @ OAK Athletics
Sat 1 Jul 16:07
 
2
3
4
5
6
7
CHI White Sox
-240
-225
-180
-125
+120
+175
OAK Athletics
+195
+190
+250
+350
+500
+750
Neither
+4000
+1200
+450
+200
+105
-170
MIA Marlins @ ATL Braves
Sat 1 Jul 16:10
 
2
3
4
5
6
7
MIA Marlins
-115
+100
+125
+170
+230
+325
ATL Braves
-115
-125
-105
+125
+180
+260
Neither
+5000
+1600
+550
+240
+120
-150
SF Giants @ NY Mets
Sat 1 Jul 16:10
 
2
3
4
5
6
7
SF Giants
+100
+110
+135
+180
+250
+350
NY Mets
-130
-130
+100
+140
+200
+300
Neither
+5000
+1400
+450
+200
+105
-180
CLE Guardians @ CHI Cubs
Sat 1 Jul 19:15
 
2
3
4
5
6
7
CLE Guardians
-115
+105
+135
+190
+275
+400
CHI Cubs
-115
-105
+125
+180
+275
+400
Neither
+3500
+850
+300
+145
-135
-250
LA Dodgers @ KC Royals
Sat 1 Jul 19:15
 
2
3
4
5
6
7
LA Dodgers
-250
-245
-190
-140
+105
+150
KC Royals
+205
+200
+240
+320
+450
+650
Neither
+5000
+1600
+550
+250
+130
-140
TB Rays @ SEA Mariners
Sat 1 Jul 19:15
 
2
3
4
5
6
7
TB Rays
-145
-120
+115
+165
+250
+375
SEA Mariners
+115
+130
+180
+275
+400
+600
Neither
+2500
+650
+250
+115
-170
-300
ARI Diamondbacks @ LA Angels
Sat 1 Jul 22:07
 
2
3
4
5
6
7
ARI Diamondbacks
-125
-120
-105
+120
+155
+220
LA Angels
-105
-110
+105
+130
+180
+250
Neither
+5000
+2500
+850
+350
+175
-105
'''

expression_to_remove = '''
2
3
4
5
6
7
'''

# Removing lines with "@" symbol, dates, and the specified expression
text_without_at_and_dates = remove_lines_with_at_symbol_and_dates(input_text)
final_text = remove_expression_from_text(text_without_at_and_dates, expression_to_remove)

print(final_text)
