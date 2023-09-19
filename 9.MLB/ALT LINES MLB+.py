import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """

951	ATLANTA BRAVES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
952	MIAMI MARLINS






953	CINCINNATI REDS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
954	NEW YORK METS






955	WASHINGTON NATIONALS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
956	MILWAUKEE BREWERS






957	PHILADELPHIA PHILLIES

P: 4:15PM  C: 6:15PM  E: 7:15PM 
958	ST. LOUIS CARDINALS






959	CHICAGO CUBS

P: 5:10PM  C: 7:10PM  E: 8:10PM 
960	ARIZONA DIAMONDBACKS








AMERICAN LEAGUE  
 
963	BOSTON RED SOX

P: 12:07PM  C: 2:07PM  E: 3:07PM 
964	TORONTO BLUE JAYS






965	TEXAS RANGERS

P: 3:10PM  C: 5:10PM  E: 6:10PM 
966	CLEVELAND GUARDIANS






967	TAMPA BAY RAYS

P: 4:05PM  C: 6:05PM  E: 7:05PM 
968	BALTIMORE ORIOLES






969	HOUSTON ASTROS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
970	KANSAS CITY ROYALS






971	MINNESOTA TWINS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
972	CHICAGO WHITE SOX






973	DETROIT TIGERS

P: 6:07PM  C: 8:07PM  E: 9:07PM 
974	LOS ANGELES ANGELS






INTERLEAGUE  
 
975	SAN DIEGO PADRES

P: 1:07PM  C: 3:07PM  E: 4:07PM 
976	OAKLAND ATHLETICS






977	NEW YORK YANKEES

P: 3:35PM  C: 5:35PM  E: 6:35PM 
978	PITTSBURGH PIRATES






979	LOS ANGELES DODGERS

P: 6:40PM  C: 8:40PM  E: 9:40PM 
980	SEATTLE MARINERS






WRITE-IN GAMES  
 
981	SAN FRANCISCO GIANTS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
982	COLORADO ROCKIES


"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''
03:07 PM
3963
San Francisco Giants
C. Sale -L
-1½
+175
3964
Colorado Rockies
C. Bassitt -R
+1½
-215
Sep 16 Sat 2023
03:07 PM
2963
Boston Red Sox
C. Sale -L
+2½
-305
2964
Toronto Blue Jays
C. Bassitt -R
-2½
+245
04:07 PM
2975
San Diego Padres
M. Waldron -R
-2½
+175
2976
Oakland Athletics
M. Miller -R
+2½
-215
04:10 PM
2951
Atlanta Braves
J. Shuster -L
-2½
+190
2952
Miami Marlins
B. Hoeing -R
+2½
-240
06:10 PM
2965
Texas Rangers
D. Dunning -R
+2½
-345
2966
Cleveland Guardians
T. Bibee -R
-2½
+270
06:35 PM
2977
New York Yankees
L. Weaver -R
-2½
+200
2978
Pittsburgh Pirates
L. Ortiz -R
+2½
-260
07:05 PM
2967
Tampa Bay Rays
T. Glasnow -R
-2½
+225
2968
Baltimore Orioles
G. Rodriguez -R
+2½
-285
07:10 PM
2953
Cincinnati Reds
A. Abbott -L
-2½
+235
2954
New York Mets
T. Megill -R
+2½
-295
07:10 PM
2955
Washington Nationals
T. Williams -R
+2½
-165
2956
Milwaukee Brewers
C. Burnes -R
-2½
+135
07:10 PM
2969
Houston Astros
J. France -R
-2½
+165
2970
Kansas City Royals
C. Ragans -L
+2½
-205
07:10 PM
2971
Minnesota Twins
P. Lopez -R
-2½
+125
2972
Chicago White Sox
T. Toussaint -R
+2½
-155
07:15 PM
2957
Philadelphia Phillies
R. Suarez -L
-2½
+215
2958
St. Louis Cardinals
M. Mikolas -R
+2½
-275
08:10 PM
2959
Chicago Cubs
K. Hendricks -R
-2½
+225
2960
Arizona Diamondbacks
Z. Davies -R
+2½
-285
09:07 PM
2973
Detroit Tigers
S. Gipson Long -R
-2½
+220
2974
Los Angeles Angels
T. Anderson -L
+2½
-280
09:40 PM
2979
Los Angeles Dodgers
C. Kershaw -L
-2½
+190
2980
Seattle Mariners
B. Miller -R
+2½
-240
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


