import time

import pyautogui
import re
time.sleep(3)


text = """
Aug 27 Sun 2023
12:05 PM
1975
Los Angeles Angels
G. Canning -R
O 26½
+100
1976
New York Mets
D. Peterson -L
U 26½
-130
01:35 PM
1951
St. Louis Cardinals
D. Rom -L
O 27½
-115
1952
Philadelphia Phillies
A. Nola -R
U 27½
-115
01:35 PM
1953
Chicago Cubs
J. Assad -R
O 27
-110
1954
Pittsburgh Pirates
B. Falter -L
U 27
-120
01:35 PM
1977
Los Angeles Dodgers
C. Ferguson -L
O 28½
-105
1978
Boston Red Sox
T. Houck -R
U 28½
-125
01:35 PM
1979
Colorado Rockies
T. Blach -L
O 26½
-110
1980
Baltimore Orioles
J. Flaherty -R
U 26½
-120
01:37 PM
1963
Cleveland Guardians
N. Syndergaard -R
O 27½
+110
1964
Toronto Blue Jays
Y. Kikuchi -L
U 27½
-140
01:40 PM
1955
Washington Nationals
T. Williams -R
O 26
-110
1956
Miami Marlins
J. Chargois -R
U 26
-120
01:40 PM
1965
Houston Astros
J. Verlander -R
O 26
-145
1966
Detroit Tigers
A. Faedo -R
U 26
+115
01:40 PM
1967
New York Yankees
C. Rodon -L
O 25½
-114
1968
Tampa Bay Rays
Z. Littell -R
U 25½
-116
02:10 PM
1957
San Diego Padres
M. Wacha -R
O 26½
-125
1958
Milwaukee Brewers
A. Houser -R
U 26½
-105
02:10 PM
1969
Oakland Athletics
P. Blackburn -R
O 27
-106
1970
Chicago White Sox
M. Clevinger -R
U 27
-124
02:10 PM
1971
Texas Rangers
J. Montgomery -L
O 25½
-123
1972
Minnesota Twins
B. Ober -R
U 25½
-107
04:10 PM
1961
Cincinnati Reds
G. Ashcraft -R
O 27½
-110
1962
Arizona Diamondbacks
S. Cecconi -R
U 27½
-120
04:10 PM
1973
Kansas City Royals
A. Marsh -R
O 25
-120
1974
Seattle Mariners
L. Castillo -R
U 25
-110
07:10 PM
1959
Atlanta Braves
J. Shuster -L
O 28
-115
1960
San Francisco Giants
T. Beck -R
U 28
-115
"""

def enteroverodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.typewrite(str(over_odds[i]))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=3)
def enterunderodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.typewrite(str(under_odds[i]))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=2)


over_numbers = re.findall(r"O (\d+½|\d+)", text)
over_number = [number.replace("½", ".5") for number in over_numbers]
under_numbers = re.findall(r"U (\d+½|\d+)", text)

over_odds = []
under_odds = []

for number in over_numbers:
    index = text.index("O " + number)
    next_line_index = text.index("\n", index) + 1
    next_line = text[next_line_index:].split("\n", 1)[0].strip()
    over_odds.append(next_line)

for number in under_numbers:
    index = text.index("U " + number)
    next_line_index = text.index("\n", index) + 1
    next_line = text[next_line_index:].split("\n", 1)[0].strip()
    under_odds.append(next_line)


# Print the extracted OVER numbers
print("TOTALS:")
for number in over_numbers:
    print(number)

print()

# Print the extracted OVER numbers and odds
print("OVER Odds:")
for number, odds in zip(over_numbers, over_odds):
    print(odds)

print()

# Print the extracted UNDER numbers and odds
print("UNDER Odds:")
for number, odds in zip(under_numbers, under_odds):
    print(odds)

for number in over_number:
    print(number)

# Compare the OVER and UNDER odds for each game
for i in range(len(over_odds)):
    if over_odds[i] > under_odds[i]:
        print(f"In game {i+1}, OVER odds are higher.")


    else:
        print(f"In game {i+1}, OVER and UNDER odds are the same.")
