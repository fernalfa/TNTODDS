import re
import time
import pyautogui
time.sleep(3)


text = """

Aug 13 Sun 2023
12:05 PM
1959
Detroit Tigers
E. Rodriguez -L
O 27½
-115
1960
Boston Red Sox
K. Crawford -R
U 27½
-115
01:35 PM
1951
Cincinnati Reds - Game #1
B. Williamson -L
O 26½
-105
1952
Pittsburgh Pirates - Game #1
M. Keller -R
U 26½
-125
01:35 PM
1967
Oakland Athletics
K. Waldichuk -L
O 28½
-115
1968
Washington Nationals
T. Williams -R
U 28½
-115
01:35 PM
1969
Minnesota Twins
S. Gray -R
O 26½
-115
1970
Philadelphia Phillies
R. Suarez -L
U 26½
-115
01:37 PM
1971
Chicago Cubs
J. Taillon -R
O 27½
-115
1972
Toronto Blue Jays
H. Ryu -L
U 27½
-115
01:40 PM
1961
Cleveland Guardians
T. Bibee -R
O 25
+100
1962
Tampa Bay Rays
Z. Eflin -R
U 25
-130
01:40 PM
1973
New York Yankees
G. Cole -R
O 24½
+100
1974
Miami Marlins
E. Perez -R
U 24½
-130
02:10 PM
1963
Los Angeles Angels
C. Silseth -R
O 27½
+115
1964
Houston Astros
J. Urquidy -R
U 27½
-145
02:10 PM
1975
Milwaukee Brewers
F. Peralta -R
O 25½
-115
1976
Chicago White Sox
D. Cease -R
U 25½
-115
04:05 PM
1977
Texas Rangers
D. Dunning -R
O 25½
-115
1978
San Francisco Giants
L. Webb -R
U 25½
-115
04:10 PM
1955
Colorado Rockies
K. Freeland -L
O 27
+120
1956
Los Angeles Dodgers
J. Urias -L
U 27
-150
04:10 PM
1957
San Diego Padres
S. Lugo -R
O 28
+105
1958
Arizona Diamondbacks
B. Pfaadt -R
U 28
-135
04:10 PM
1965
Baltimore Orioles
K. Bradish -R
O 25½
+100
1966
Seattle Mariners
B. Miller -R
U 25½
-130
06:05 PM
1979
Cincinnati Reds - Game #2
L. Weaver -R
O 27½
-120
1980
Pittsburgh Pirates - Game #2
A. Jackson -R
U 27½
-110
07:10 PM
1953
Atlanta Braves
Y. Chirinos -R
O 28
-120
1954
New York Mets
K. Senga -R
U 28
-110

"""
def enterodds():
    pyautogui.press('enter')
    pyautogui.typewrite((number))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)

# Find all numbers following "O" (OVER) keyword using regular expressions
over_numbers = re.findall(r"O (\d+½|\d+)", text)
over_number = [number.replace("½", ".5") for number in over_numbers]

# Print the extracted OVER numbers
for number in over_number:
    print(number)
    enterodds()

