import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """
901	SAN DIEGO PADRES

P: 4:45PM  C: 6:45PM  E: 7:45PM 
902	ST. LOUIS CARDINALS






903	MILWAUKEE BREWERS

P: 5:05PM  C: 7:05PM  E: 8:05PM 
904	CHICAGO CUBS






905	ATLANTA BRAVES

P: 5:40PM  C: 7:40PM  E: 8:40PM 
906	COLORADO ROCKIES






907	CINCINNATI REDS

P: 6:45PM  C: 8:45PM  E: 9:45PM 
908	SAN FRANCISCO GIANTS






909	ARIZONA DIAMONDBACKS

P: 7:10PM  C: 9:10PM  E: 10:10PM 
910	LOS ANGELES DODGERS






AMERICAN LEAGUE  
 
911	NEW YORK YANKEES

P: 3:40PM  C: 5:40PM  E: 6:40PM 
912	DETROIT TIGERS






913	CHICAGO WHITE SOX

P: 4:05PM  C: 6:05PM  E: 7:05PM 
914	BALTIMORE ORIOLES






915	HOUSTON ASTROS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
916	BOSTON RED SOX






917	CLEVELAND GUARDIANS

P: 4:40PM  C: 6:40PM  E: 7:40PM 
918	MINNESOTA TWINS






919	OAKLAND ATHLETICS

P: 6:40PM  C: 8:40PM  E: 9:40PM 
920	SEATTLE MARINERS






INTERLEAGUE  
 
921	LOS ANGELES ANGELS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
922	PHILADELPHIA PHILLIES






923	WASHINGTON NATIONALS

P: 4:07PM  C: 6:07PM  E: 7:07PM 
924	TORONTO BLUE JAYS






925	TEXAS RANGERS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
926	NEW YORK METS






927	PITTSBURGH PIRATES

P: 5:10PM  C: 7:10PM  E: 8:10PM 
928	KANSAS CITY ROYALS
"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''

06:40 PM
2921
LOS ANGELES ANGELS
L. GIOLITO -R
+2½
-260
2922
PHILADELPHIA PHILLIES
T. WALKER -R
-2½
+200
07:05 PM
2913
CHICAGO WHITE SOX
M. KOPECH -R
+2½
-170
2914
BALTIMORE ORIOLES
G. RODRIGUEZ -R
-2½
+140
07:07 PM
2923
WASHINGTON NATIONALS
J. GRAY -R
+2½
-170
2924
TORONTO BLUE JAYS
K. GAUSMAN -R
-2½
+140
07:10 PM
2915
HOUSTON ASTROS
C. JAVIER -R
+2½
-300
2916
BOSTON RED SOX
C. SALE -L
-2½
+240
07:10 PM
2925
TEXAS RANGERS
J. GRAY -R
-2½
+170
2926
NEW YORK METS
T. MEGILL -R
+2½
-210
07:40 PM
2917
CLEVELAND GUARDIANS
X. CURRY -R
+2½
-240
2918
MINNESOTA TWINS
K. MAEDA -R
-2½
+190
07:45 PM
2901
SAN DIEGO PADRES
B. SNELL -L
-2½
+130
2902
ST. LOUIS CARDINALS
A. WAINWRIGHT -R
+2½
-160
08:05 PM
2903
MILWAUKEE BREWERS
W. MILEY -L
+2½
-325
2904
CHICAGO CUBS
J. TAILLON -R
-2½
+250
08:10 PM
2927
PITTSBURGH PIRATES
J. OVIEDO -R
-2½
+220
2928
KANSAS CITY ROYALS
Z. GREINKE -R
+2½
-280
08:40 PM
2905
ATLANTA BRAVES
B. ELDER -R
-2½
-115
2906
COLORADO ROCKIES
A. GOMBER -L
+2½
-115
09:40 PM
2919
OAKLAND ATHLETICS
K. MULLER -L
+2½
-160
2920
SEATTLE MARINERS
B. WOO -R
-2½
+130
09:45 PM
2907
CINCINNATI REDS
A. ABBOTT -L
+2½
-350
2908
SAN FRANCISCO GIANTS
K. HARRISON -L
-2½
+275
10:10 PM
2909
ARIZONA DIAMONDBACKS
Z. GALLEN -R
+2½
-280
2910
LOS ANGELES DODGERS
B. MILLER -R-260
-2½
+220
'''

team_order = team_names

lines = data2.split('\n')
matchups = []
game_id = 1
i = 0
while i < len(lines):
    if any(team in lines[i].upper() for team in team_order):
        team = lines[i]
        pitcher = lines[i + 1]
        spread = lines[i + 2]
        odds = lines[i + 3]
        matchups.append((game_id, team, pitcher, spread, odds))
        game_id += 1
        i += 4
    else:
        i += 1

reordered_matchups = sorted(matchups, key=lambda x: team_order.index(x[1].upper()))

# Convert the `reordered_matchups` list to a string representation
data = '\n'.join(['\n'.join(str(item) for item in matchup) for matchup in reordered_matchups])

def Alt1(runline, odds):
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(runline))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(odds))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.press('down')

def Alt2(runline, odds):
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(runline))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(odds))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')


def Alt3(runline, odds):
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(runline))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(odds))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')

def Alt4(runline, odds):
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(runline))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.write(str(odds))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.press('down')

matchups = re.findall(r"([\w\s.-]+)\n([\w\s.-]+)\n([+-]?\d+½)\n([+-]\d+)", data)

num_matchups = len(matchups)
if num_matchups < 2:
    print("Insufficient matchups to process.")
else:
    for i in range(0, num_matchups, 2):
        team1_name = matchups[i][0].strip()
        team1_run_line = matchups[i][2].replace("½", ".5")
        team1_odds = matchups[i][3].strip()

        team2_name = matchups[i + 1][0].strip()
        team2_run_line = matchups[i + 1][2].replace("½", ".5")
        team2_odds = matchups[i + 1][3].strip()

        if '-' in team1_run_line and '-' in team1_odds:
            Alt1(float(team1_run_line), int(team1_odds))
        elif '-' in team1_run_line and '+' in team1_odds:
            Alt2(float(team1_run_line), int(team2_odds))
        elif '-' in team2_run_line and '-' in team2_odds:
            Alt3(float(team2_run_line), int(team2_odds))
        elif '-' in team2_run_line and '+' in team2_odds:
            Alt4(float(team2_run_line), int(team1_odds))

        print()


