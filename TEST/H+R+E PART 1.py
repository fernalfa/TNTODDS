import time

import pyautogui
import re
time.sleep(3)


text = """
3:07 PM
1965
Tampa Bay Rays
S. Armstrong -R
O 26
-106
1966
Toronto Blue Jays
H. Ryu -L
U 26
-124
06:35 PM
1951
Miami Marlins
J. Chargois -R
O 27
-120
1952
Pittsburgh Pirates
Q. Priester -R
U 27
-110
07:05 PM
1967
Miami Marlins
J. Chargois -R
O 27
-120
1952
Pittsburgh Pirates
Q. Priester -R
U 27
-110
07:05 PM
1967
Boston Red Sox
K. Crawford -R
O 25½
-115
1968
Baltimore Orioles
K. Gibson -R
U 25½
-115
07:10 PM
1953
Chicago Cubs
J. Wicks -L
O 26
-101
1954
Milwaukee Brewers
E. Lauer -L
U 26
-129
Chicago Cubs
J. Wicks -L
O 26
-101
1954
Milwaukee Brewers
E. Lauer -L
U 26
-129
:10 PM
1969
New York Yankees
C. Schmidt -R
O 27½
-119
1970
Kansas City Royals
S. Cruz -R
U 27½
-111
07:10 PM
1975
San Diego Padres
M. Wacha -R
O 26
-120
1976
Chicago White Sox
M. Clevinger -R
U 26
-110
07:15 PM
1957
Cincinnati Reds
C. Phillips -R
O 27
-126
1958
St. Louis Cardinals
D. Rom -L
U 27
-104
07:15 PM
1973
Texas Rangers
A. Heaney -L
O 24½
-106
1974
Seattle Mariners
L. Castillo -R
U 24½
-124
07:20 PM
1959
Washington Nationals
J. Adon -R
O 27
-106
1960
Atlanta Braves
S. Strider -R
U 27
-124
08:10 PM
1977
Houston Astros
J. Verlander -R
O 26½
-115
1978
Arizona Diamondbacks
M. Kelly -R
U 26½
-115
09:05 PM
1961
Los Angeles Dodgers
C. Kershaw -L
O 25½
-112
1962
San Francisco Giants
T. Beck -R
U 25½
-118
Los Angeles Dodgers
C. Kershaw -L
O 25½
-112
1962
San Francisco Giants
T. Beck -R
U 25½
-118
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
