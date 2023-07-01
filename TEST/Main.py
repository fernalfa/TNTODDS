import re
import time
import pyautogui
time.sleep(3)

text = """
PM
1957
San Diego Padres
S. Lugo -R
O 29½
-115
1958
Cincinnati Reds
G. Ashcraft -R
U 29½
-115
06:05 PM
1951
Washington Nationals
J. Gray -R
O 27
-150
1952
Philadelphia Phillies
C. Sanchez -L
U 27
+120
07:05 PM
1953
Milwaukee Brewers
F. Peralta -R
O 26
-110
1954
Pittsburgh Pirates
O. Bido -R
U 26
-120
07:05 PM
1961
Minnesota Twins
P. Lopez -R
O 26
-110
1962
Baltimore Orioles
D. Kremer -R
U 26
-120
07:07 PM
1963
Boston Red Sox
J. Paxton -L
O 27½
+110
1964
Toronto Blue Jays
J. Berrios -R
U 27½
-140
07:10 PM
1955
San Francisco Giants
A. Cobb -R
O 27
-115
1956
New York Mets
C. Carrasco -R
U 27
-115
07:20 PM
1959
Miami Marlins
B. Hoeing -R
O 28
-130
1960
Atlanta Braves
M. Soroka -R
U 28
+100
08:05 PM
1965
Houston Astros
R. Blanco -R
O 27½
+100
1966
Texas Rangers
J. Gray -R
U 27½
-130
08:10 PM
1973
Detroit Tigers
M. Lorenzen -R
O 31½
-120
1974
Colorado Rockies
A. Gomber -L
U 31½
-110
08:10 PM
1975
Los Angeles Dodgers
B. Miller -R
O 28½
-105
1976
Kansas City Royals
A. Marsh -R
U 28½
-125
08:15 PM
1977
New York Yankees
L. Severino -R
O 28
-115
1978
St. Louis Cardinals
M. Liberatore -L
U 28
-115
09:38 PM
1979
Arizona Diamondbacks
T. Henry -L
O 28
-120
1980
Los Angeles Angels
G. Canning -R
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

