import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """
951	CINCINNATI REDS - GAME #1

P: 10:35AM  C: 12:35PM  E: 1:35PM  
952	PITTSBURGH PIRATES - GAME #1






953	ATLANTA BRAVES

P: 4:10PM  C: 6:10PM  E: 7:10PM 
954	NEW YORK METS






955	COLORADO ROCKIES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
956	LOS ANGELES DODGERS






957	SAN DIEGO PADRES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
958	ARIZONA DIAMONDBACKS






AMERICAN LEAGUE  
 
959	DETROIT TIGERS

P: 9:05AM  C: 11:05AM  E: 12:05PM 
960	BOSTON RED SOX






961	CLEVELAND GUARDIANS

P: 10:40AM  C: 12:40PM  E: 1:40PM 
962	TAMPA BAY RAYS






963	LOS ANGELES ANGELS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
964	HOUSTON ASTROS






965	BALTIMORE ORIOLES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
966	SEATTLE MARINERS






INTERLEAGUE  
 
967	OAKLAND ATHLETICS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
968	WASHINGTON NATIONALS






969	MINNESOTA TWINS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
970	PHILADELPHIA PHILLIES






971	CHICAGO CUBS

P: 10:37AM  C: 12:37PM  E: 1:37PM 
972	TORONTO BLUE JAYS






973	NEW YORK YANKEES

P: 10:40AM  C: 12:40PM  E: 1:40PM 
974	MIAMI MARLINS






975	MILWAUKEE BREWERS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
976	CHICAGO WHITE SOX






977	TEXAS RANGERS

P: 1:05PM  C: 3:05PM  E: 4:05PM 
978	SAN FRANCISCO GIANTS






WRITE-IN GAMES  
 
979	CINCINNATI REDS - GAME #2

P: 3:05PM  C: 5:05PM  E: 6:05PM  
980	PITTSBURGH PIRATES - GAME #2

"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''

Aug 13 Sun 2023
12:05 PM
2959
Detroit Tigers
E. Rodriguez -L
+2½
-295
2960
Boston Red Sox
K. Crawford -R
-2½
+235
01:35 PM
2967
Oakland Athletics
K. Waldichuk -L
+2½
-270
2968
Washington Nationals
T. Williams -R
-2½
+210
01:35 PM
2969
Minnesota Twins
S. Gray -R
+2½
-335
2970
Philadelphia Phillies
R. Suarez -L
-2½
+260
01:37 PM
2971
Chicago Cubs
J. Taillon -R
+2½
-295
2972
Toronto Blue Jays
H. Ryu -L
-2½
+235
01:40 PM
2961
Cleveland Guardians
T. Bibee -R
+2½
-220
2962
Tampa Bay Rays
Z. Eflin -R
-2½
+180
01:40 PM
2973
New York Yankees
G. Cole -R
-2½
+215
2974
Miami Marlins
E. Perez -R
+2½
-275
02:10 PM
2963
Los Angeles Angels
C. Silseth -R
+2½
-260
2964
Houston Astros
J. Urquidy -R
-2½
+200
02:10 PM
2975
Milwaukee Brewers
F. Peralta -R
-2½
+195
2976
Chicago White Sox
D. Cease -R
+2½
-245
04:05 PM
2977
Texas Rangers
D. Dunning -R
+2½
-295
2978
San Francisco Giants
L. Webb -R
-2½
+235
04:10 PM
2965
Baltimore Orioles
K. Bradish -R
-2½
+240
2966
Seattle Mariners
B. Miller -R
+2½
-300
06:05 PM
2979
Cincinnati Reds - Game #2
L. Weaver -R
+2½
-325
2980
Pittsburgh Pirates - Game #2
A. Jackson -R
-2½
+250
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


