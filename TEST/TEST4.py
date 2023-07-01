import re

def remove_lines_with_at_symbol_and_dates(text):
    lines = text.split("\n")
    modified_lines = [line for line in lines if "@" not in line and not re.search(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", line)]
    return "\n".join(modified_lines)

def remove_expression_from_text(text, expression):
    return text.replace(expression, "")


# Example usage
input_text = '''
SD Padres @ CIN Reds
Fri 30 Jun 17:10
 
2
3
4
5
6
7
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
WAS Nationals @ PHI Phillies
Fri 30 Jun 18:06
 
2
3
4
5
6
7
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
MIL Brewers @ PIT Pirates
Fri 30 Jun 19:05
 
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
MIN Twins @ BAL Orioles
Fri 30 Jun 19:05
 
2
3
4
5
6
7
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
BOS Red Sox @ TOR Blue Jays
Fri 30 Jun 19:07
 
2
3
4
5
6
7
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
