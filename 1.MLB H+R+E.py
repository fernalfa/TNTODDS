import re
import time
import pyautogui
time.sleep(3)

text = """
2:15 PM
1921
New York Yankees - Game #1
L. Severino -R
O 26½
-140
1922
St. Louis Cardinals - Game #1
J. Flaherty -R
U 26½
+110
03:07 PM
1911
Boston Red Sox
K. Crawford -R
O 27½
+110
1912
Toronto Blue Jays
Y. Kikuchi -L
U 27½
-140
04:05 PM
1903
Washington Nationals
M. Gore -L
O 25½
-130
1904
Philadelphia Phillies
Z. Wheeler -R
U 25½
+100
04:05 PM
1905
Milwaukee Brewers
C. Burnes -R
O 25½
-120
1906
Pittsburgh Pirates
J. Oviedo -R
U 25½
-110
04:05 PM
1913
Houston Astros
H. Brown -R
O 26
+110
1914
Texas Rangers
N. Eovaldi -R
U 26
-140
04:05 PM
1915
Minnesota Twins
B. Ober -R
O 26
-115
1916
Baltimore Orioles
K. Bradish -R
U 26
-115
04:07 PM
1917
Chicago White Sox
D. Cease -R
O 25½
-130
1918
Oakland Athletics
K. Muller -L
U 25½
+100
04:10 PM
1907
San Francisco Giants
A. DeSclafani -R
O 25½
-130
1908
New York Mets
J. Verlander -R
U 25½
+100
04:10 PM
1909
Miami Marlins
E. Perez -R
O 27
-130
1910
Atlanta Braves
C. Morton -R
U 27
+100
07:15 PM
1919
Tampa Bay Rays
T. Glasnow -R
O 24½
+100
1920
Seattle Mariners
G. Kirby -R
U 24½
-130
07:15 PM
1923
Cleveland Guardians
T. Bibee -R
O 24½
-130
1924
Chicago Cubs
M. Stroman -R
U 24½
+100
07:15 PM
1925
Los Angeles Dodgers
J. Urias -L
O 28
+104
1926
Kansas City Royals
D. Lynch -L
U 28
-134
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

