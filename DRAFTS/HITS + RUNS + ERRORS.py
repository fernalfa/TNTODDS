import re
import time
import pyautogui

time.sleep(3)

# First code
data = """
12:05 PM
1961
Minnesota Twins
S. Gray -R
O 26½
-125
1962
Baltimore Orioles
C. Irvin -L
U 26½
-105
01:35 PM
1951
Miami Marlins
S. Alcantara -R
O 25½
-130
1952
Atlanta Braves
S. Strider -R
U 25½
+100
01:35 PM
1953
Milwaukee Brewers
C. Rea -R
O 27
+105
1954
Pittsburgh Pirates
R. Hill -L
U 27
-135
01:35 PM
1955
Washington Nationals
T. Williams -R
O 27
-140
1956
Philadelphia Phillies
R. Suarez -L
U 27
+110
01:37 PM
1963
Boston Red Sox
G. Whitlock -R
O 25½
+105
1964
Toronto Blue Jays
K. Gausman -R
U 25½
-135
02:10 PM
1971
Los Angeles Dodgers
T. Gonsolin -R
O 27½
-140
1972
Kansas City Royals
B. Singer -R
U 27½
+110
02:15 PM
1973
New York Yankees
G. Cole -R
O 25½
-105
1974
St. Louis Cardinals
J. Montgomery -L
U 25½
-125
02:20 PM
1975
Cleveland Guardians
A. Civale -R
O 25
-113
1976
Chicago Cubs
J. Taillon -R
U 25
-117
02:35 PM
1965
Houston Astros
S. Dubin -R
O 27
-120
1966
Texas Rangers
A. Heaney -L
U 27
-110
03:10 PM
1977
Detroit Tigers
M. Manning -R
O 32
-115
1978
Colorado Rockies
C. Seabold -R
U 32
-115
04:07 PM
1979
Arizona Diamondbacks
Z. Gallen -R
O 26
-130
1980
Los Angeles Angels
R. Detmers -L
U 26
+100
04:10 PM
1969
Tampa Bay Rays
T. Bradley -R
O 25
-110
1970
Seattle Mariners
L. Castillo -R
U 25
-120
07:10 PM
1959
San Francisco Giants
R. Stripling -R
O 27
+100
1960
New York Mets
D. Peterson -L
U 27
-130

04:10 PM
1969
San Diego Padres
T. Bradley -R
O 25
-110
1970
Cincinnati Reds
L. Castillo -R
U 25
-120
07:10 PM
1959
Chicago White Sox
R. Stripling -R
O 27
+100
1960
Oakland Athletics
D. Peterson -L
U 27
-130


"""

order_list = ['MIAMI MARLINS', 'ATLANTA BRAVES', 'MILWAUKEE BREWERS', 'PITTSBURGH PIRATES', 'WASHINGTON NATIONALS', 'PHILADELPHIA PHILLIES', 'SAN DIEGO PADRES', 'CINCINNATI REDS', 'SAN FRANCISCO GIANTS', 'NEW YORK METS', 'MINNESOTA TWINS', 'BALTIMORE ORIOLES', 'BOSTON RED SOX', 'TORONTO BLUE JAYS', 'HOUSTON ASTROS', 'TEXAS RANGERS', 'CHICAGO WHITE SOX', 'OAKLAND ATHLETICS', 'TAMPA BAY RAYS', 'SEATTLE MARINERS', 'LOS ANGELES DODGERS', 'KANSAS CITY ROYALS', 'NEW YORK YANKEES', 'ST. LOUIS CARDINALS', 'CLEVELAND GUARDIANS', 'CHICAGO CUBS', 'DETROIT TIGERS', 'COLORADO ROCKIES', 'ARIZONA DIAMONDBACKS', 'LOS ANGELES ANGELS']

matches = re.findall(r"\d{4}\n(.*?)\n.*?\n([UO] \d+(?:½)?)\n(-?\d+)", data, re.DOTALL)

# Create a dictionary to store the matches by team name
matchups_by_team = {match[0].upper(): match for match in matches}

# Extracted data for PyAutoGUI actions
pyautogui_data = ""

# Iterate over the teams in the specified order and retrieve the corresponding match
for team in order_list:
    team_match = matchups_by_team.get(team.upper())
    if team_match:
        value = team_match[1].split(' ')[1]
        letter = team_match[1].split(' ')[0] if team_match[1] else ''
        negative_value_line = team_match[2]

        pyautogui_data += f"Matchup: {team_match[0]}\n"
        pyautogui_data += f"Value: {value}\n"
        pyautogui_data += f"Letter: {letter}\n"
        pyautogui_data += f"Negative Value Line: {negative_value_line}\n\n"

# Second code
# Split the data into individual matchups
matchups = re.split(r"\n\s*\n", pyautogui_data.strip())

for matchup in matchups:
    # Extract the values using regex
    value = re.search(r"Value:\s*([0-9½]+)", matchup).group(1)
    letter = re.search(r"Letter:\s*([OU])", matchup).group(1)
    negative_value_line = re.search(r"Negative Value Line:\s*(-?\d+)", matchup).group(1)

    # Press Enter
    pyautogui.press('enter')

    # Write Value and press Enter
    pyautogui.write(value)
    pyautogui.press('enter')

    # Check the letter and perform corresponding actions
    if letter == "O":
        # Press Left, Enter, write Negative Value Line, Enter
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(negative_value_line)
        pyautogui.press('enter')
        pyautogui.press('left')
    elif letter == "U":
        # Press Down, Left, Enter, write Negative Value Line, Enter
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(negative_value_line)
        pyautogui.press('enter')
        pyautogui.press('left')

    # Perform common actions
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')