import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """


959	CHICAGO CUBS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
960	NEW YORK METS






961	COLORADO ROCKIES

P: 5:10PM  C: 7:10PM  E: 8:10PM 
962	MILWAUKEE BREWERS






AMERICAN LEAGUE  
 
963	MINNESOTA TWINS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
964	DETROIT TIGERS






965	KANSAS CITY ROYALS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
966	BOSTON RED SOX






967	TORONTO BLUE JAYS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
968	CLEVELAND GUARDIANS






969	NEW YORK YANKEES

P: 5:10PM  C: 7:10PM  E: 8:10PM 
970	CHICAGO WHITE SOX






971	TEXAS RANGERS

P: 6:40PM  C: 8:40PM  E: 9:40PM 
972	OAKLAND ATHLETICS






INTERLEAGUE  
 
973	SAN FRANCISCO GIANTS

P: 6:38PM  C: 8:38PM  E: 9:38PM 
974	LOS ANGELES ANGELS

"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''


Minnesota Twins
P. Lopez -R
-2½
+155
2964
Detroit Tigers
J. Wentz -L
+2½
-185
07:05 PM
2957
07:10 PM
2959
Chicago Cubs
D. Smyly -L
+2½
-325
2960
New York Mets
K. Senga -R
-2½
+250
07:10 PM
2965
Kansas City Royals
C. Ragans -L
+2½
-185
2966
Boston Red Sox
B. Bello -R
-2½
+155
07:10 PM
2967
Toronto Blue Jays
H. Ryu -L
-2½
+185
2968
Cleveland Guardians
G. Williams -R
+2½
-225
08:10 PM
2961
Colorado Rockies
P. Lambert -R
+2½
-175
2962
Milwaukee Brewers
F. Peralta -R
-2½
+145
08:10 PM
2969
New York Yankees
G. Cole -R
-2½
+160
2970
Chicago White Sox
D. Cease -R
+2½
-200
09:38 PM
2973
San Francisco Giants
L. Webb -R
-2½
+210
2974
Los Angeles Angels
P. Sandoval -L
+2½
-270
09:40 PM
2971
Texas Rangers
D. Dunning -R
-2½
+115
2972
Oakland Athletics
K. Waldichuk -L
+2½
-145
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


