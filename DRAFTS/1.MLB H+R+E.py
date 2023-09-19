import re
import time
import pyautogui
time.sleep(3)


text = """

Sep 15 Fri 2023
06:35 PM
1925
New York Yankees
G. Cole -R
O 25½
+105
1926
Pittsburgh Pirates
J. Oviedo -R
U 25½
-135
06:40 PM
1901
Atlanta Braves
B. Elder -R
O 27
-115
1902
Miami Marlins
J. Cueto -R
U 27
-115
07:05 PM
1913
Tampa Bay Rays
Z. Eflin -R
O 26
-120
1914
Baltimore Orioles
J. Flaherty -R
U 26
-110
07:07 PM
1915
Boston Red Sox
B. Bello -R
O 26
+100
1916
Toronto Blue Jays
J. Berrios -R
U 26
-130
07:10 PM
1903
Cincinnati Reds
H. Greene -R
O 25½
+105
1904
New York Mets
D. Peterson -L
U 25½
-135
07:10 PM
1917
Texas Rangers
J. Gray -R
O 26½
+130
1918
Cleveland Guardians
L. Giolito -R
U 26½
-160
07:40 PM
1919
Minnesota Twins
B. Ober -R
O 26½
-109
1920
Chicago White Sox
J. Scholtens -R
U 26½
-121
08:10 PM
1905
Washington Nationals
J. Irvin -R
O 26
-114
1906
Milwaukee Brewers
W. Miley -L
U 26
-116
08:10 PM
1921
Houston Astros
C. Javier -R
O 28
-155
1922
Kansas City Royals
Z. Greinke -R
U 28
+125
08:15 PM
1907
Philadelphia Phillies
A. Nola -R
O 26
-117
1908
St. Louis Cardinals
Z. Thompson -L
U 26
-113
08:40 PM
1909
San Francisco Giants
L. Webb -R
O 29½
-121
1910
Colorado Rockies
C. Anderson -R
U 29½
-109
09:38 PM
1923
Detroit Tigers
T. Skubal -L
O 25
+100
1924
Los Angeles Angels
G. Canning -R
U 25
-130
09:40 PM
1911
Chicago Cubs
J. Steele -L
O 26
-105
1912
Arizona Diamondbacks
B. Pfaadt -R
U 26
-125
09:40 PM
1927
San Diego Padres
S. Lugo -R
O 26
-112
1928
Oakland Athletics
S. Newcomb -L
U 26
-118
10:10 PM
1929
Los Angeles Dodgers
B. Miller -R
O 25
-117
1930
Seattle Mariners
G. Kirby -R
U 25
-113

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

