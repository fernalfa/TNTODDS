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
MIA Marlins @ ATL Braves
Sun 2 Jul 13:35
 
2
3
4
5
6
7
MIA Marlins
+125
+140
+175
+240
+325
+450
ATL Braves
-155
-160
-125
+115
+170
+260
Neither
+5000
+1200
+425
+190
-105
-190
MIL Brewers @ PIT Pirates
Sun 2 Jul 13:35
 
2
3
4
5
6
7
MIL Brewers
-120
-115
+110
+150
+210
+300
PIT Pirates
-110
+100
+125
+170
+240
+350
Neither
+5000
+1200
+425
+190
+100
-180
WAS Nationals @ PHI Phillies
Sun 2 Jul 13:35
 
2
3
4
5
6
7
WAS Nationals
+145
+160
+190
+250
+350
+500
PHI Phillies
-175
-190
-160
-120
+120
+180
Neither
+5000
+1800
+600
+260
+130
-135
BOS Red Sox @ TOR Blue Jays
Sun 2 Jul 13:37
 
2
3
4
5
6
7
BOS Red Sox
+120
+135
+175
+240
+350
+500
TOR Blue Jays
-150
-150
-115
+125
+190
+280
Neither
+4000
+1000
+375
+165
-115
-200
SD Padres @ CIN Reds
Sun 2 Jul 13:40
 
2
3
4
5
6
7
SD Padres
-125
-115
+100
+120
+160
+220
CIN Reds
-105
-115
-105
+120
+160
+220
Neither
+5000
+3300
+1000
+400
+200
+105
LA Dodgers @ KC Royals
Sun 2 Jul 14:10
 
2
3
4
5
6
7
LA Dodgers
-200
-200
-170
-130
+105
+150
KC Royals
+165
+165
+180
+230
+320
+450
Neither
+5000
+2200
+700
+320
+160
-115
NY Yankees @ STL Cardinals
Sun 2 Jul 14:15
 
2
3
4
5
6
7
NY Yankees
-135
-115
+115
+165
+240
+350
STL Cardinals
+105
+120
+160
+230
+350
+500
Neither
+3300
+750
+280
+130
-145
-275
HOU Astros @ TEX Rangers
Sun 2 Jul 14:35
 
2
3
4
5
6
7
HOU Astros
-115
-105
+120
+155
+210
+300
TEX Rangers
-115
-120
+100
+130
+190
+275
Neither
+5000
+1800
+550
+250
+125
-145
DET Tigers @ COL Rockies
Sun 2 Jul 15:10
 
2
3
4
5
6
7
DET Tigers
-135
-125
-120
-105
+120
+160
COL Rockies
+105
-105
+100
+115
+150
+200
Neither
+5000
+5000
+1600
+600
+280
+150
ARI Diamondbacks @ LA Angels
Sun 2 Jul 16:07
 
2
3
4
5
6
7
ARI Diamondbacks
-125
-120
+105
+145
+200
+300
LA Angels
-105
+105
+135
+190
+275
+400
Neither
+4000
+1200
+400
+190
-105
-190
CHI White Sox @ OAK Athletics
Sun 2 Jul 16:07
 
2
3
4
5
6
7
CHI White Sox
-160
-150
-120
+115
+165
+240
OAK Athletics
+130
+125
+160
+220
+320
+450
Neither
+5000
+1400
+450
+200
+105
-170
TB Rays @ SEA Mariners
Sun 2 Jul 16:10
 
2
3
4
5
6
7
TB Rays
-120
+100
+130
+180
+260
+375
SEA Mariners
-110
+100
+135
+200
+300
+450
Neither
+3500
+800
+300
+140
-140
-250
CLE Guardians @ CHI Cubs
Sun 2 Jul 17:05
 
2
3
4
5
6
7
CLE Guardians
-150
-135
-105
+135
+200
+280
CHI Cubs
+120
+125
+165
+230
+325
+500
Neither
+4000
+1000
+350
+165
-120
-225
SF Giants @ NY Mets
Sun 2 Jul 19:05
 
2
3
4
5
6
7
SF Giants
-120
-110
+110
+145
+200
+280
NY Mets
-110
-110
+110
+150
+210
+320
Neither
+5000
+1600
+550
+230
+120
-155

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
