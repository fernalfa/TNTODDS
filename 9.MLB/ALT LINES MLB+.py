import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """
MAJOR LEAGUE BASEBALL  
Tuesday, July 4th  
NATIONAL LEAGUE  
 
953	ST. LOUIS CARDINALS

P: 10:10AM  C: 12:10PM  E: 1:10PM 
954	MIAMI MARLINS






955	NEW YORK METS

P: 1:10PM  C: 3:10PM  E: 4:10PM 
956	ARIZONA DIAMONDBACKS






957	CHICAGO CUBS

P: 1:10PM  C: 3:10PM  E: 4:10PM 
958	MILWAUKEE BREWERS






959	PITTSBURGH PIRATES

P: 6:10PM  C: 8:10PM  E: 9:10PM 
960	LOS ANGELES DODGERS






AMERICAN LEAGUE  
 
961	BALTIMORE ORIOLES

P: 10:05AM  C: 12:05PM  E: 1:05PM 
962	NEW YORK YANKEES






963	TEXAS RANGERS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
964	BOSTON RED SOX






965	KANSAS CITY ROYALS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
966	MINNESOTA TWINS






967	OAKLAND ATHLETICS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
968	DETROIT TIGERS






969	TORONTO BLUE JAYS

P: 5:10PM  C: 7:10PM  E: 8:10PM 
970	CHICAGO WHITE SOX






INTERLEAGUE  
 
971	SEATTLE MARINERS

P: 1:35PM  C: 3:35PM  E: 4:35PM 
972	SAN FRANCISCO GIANTS






973	COLORADO ROCKIES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
974	HOUSTON ASTROS






975	PHILADELPHIA PHILLIES

P: 1:10PM  C: 3:10PM  E: 4:10PM 
976	TAMPA BAY RAYS






977	LOS ANGELES ANGELS

P: 3:40PM  C: 5:40PM  E: 6:40PM 
978	SAN DIEGO PADRES






979	ATLANTA BRAVES

P: 4:10PM  C: 6:10PM  E: 7:10PM 
980	CLEVELAND GUARDIANS
"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''
01:05 PM
2961
Baltimore Orioles
K. Gibson -R
+2½
-325
2962
New York Yankees
C. Schmidt -R
-2½
+250
01:10 PM
2953
St. Louis Cardinals
A. Wainwright -R
+2½
-240
2954
Miami Marlins
J. Luzardo -L
-2½
+190
01:35 PM
2963
Texas Rangers
D. Dunning -R
-2½
+195
2964
Boston Red Sox
B. Bernardino -L
+2½
-245
02:10 PM
2965
Kansas City Royals
Z. Greinke -R
+2½
-200
2966
Minnesota Twins
K. Maeda -R
-2½
+160
04:10 PM
2955
New York Mets
K. Senga -R
-2½
+205
2956
Arizona Diamondbacks
Z. Davies -R
+2½
-265
04:10 PM
2957
Chicago Cubs
K. Hendricks -R
+2½
-300
2958
Milwaukee Brewers
W. Miley -L
-2½
+240
04:10 PM
2973
Colorado Rockies
K. Freeland -L
+2½
-200
2974
Houston Astros
B. Bielak -R
-2½
+160
04:10 PM
2975
Philadelphia Phillies
A. Nola -R
+2½
-290
2976
Tampa Bay Rays
Z. Eflin -R
-2½
+230
04:35 PM
2971
Seattle Mariners
L. Gilbert -R
-2½
+250
2972
San Francisco Giants
K. Winn -R
+2½
-325
06:40 PM
2967
Oakland Athletics
J. Sears -L
+2½
-225
2968
Detroit Tigers
T. Skubal -L
-2½
+185
06:40 PM
2977
Los Angeles Angels
S. Ohtani -R
+2½
-340
2978
San Diego Padres
J. Musgrove -R
-2½
+265
07:10 PM
2979
Atlanta Braves
K. Allard -R
-2½
+200
2980
Cleveland Guardians
S. Bieber -R
+2½
-260
08:10 PM
2969
Toronto Blue Jays
C. Bassitt -R
-2½
+215
2970
Chicago White Sox
L. Giolito -R
+2½
-275
09:10 PM
2959
Pittsburgh Pirates
L. Ortiz -R
+2½
-165
2960
Los Angeles Dodgers
E. Sheehan -R
-2½
+135
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


