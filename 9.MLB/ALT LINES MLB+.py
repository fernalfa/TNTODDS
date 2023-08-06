import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """
901	WASHINGTON NATIONALS

P: 10:40AM  C: 12:40PM  E: 1:40PM 
902	CINCINNATI REDS






903	PITTSBURGH PIRATES

P: 11:10AM  C: 1:10PM  E: 2:10PM 
904	MILWAUKEE BREWERS






905	COLORADO ROCKIES

P: 11:15AM  C: 1:15PM  E: 2:15PM 
906	ST. LOUIS CARDINALS






907	ATLANTA BRAVES

P: 11:20AM  C: 1:20PM  E: 2:20PM 
908	CHICAGO CUBS






909	LOS ANGELES DODGERS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
910	SAN DIEGO PADRES






AMERICAN LEAGUE  
 
911	CHICAGO WHITE SOX

P: 9:05AM  C: 11:05AM  E: 12:05PM 
912	CLEVELAND GUARDIANS






913	HOUSTON ASTROS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
914	NEW YORK YANKEES






915	TORONTO BLUE JAYS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
916	BOSTON RED SOX






917	TAMPA BAY RAYS

P: 10:40AM  C: 12:40PM  E: 1:40PM 
918	DETROIT TIGERS






919	SEATTLE MARINERS

P: 1:07PM  C: 3:07PM  E: 4:07PM 
920	LOS ANGELES ANGELS






INTERLEAGUE  
 
921	KANSAS CITY ROYALS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
922	PHILADELPHIA PHILLIES






923	NEW YORK METS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
924	BALTIMORE ORIOLES






925	ARIZONA DIAMONDBACKS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
926	MINNESOTA TWINS






927	MIAMI MARLINS

P: 11:35AM  C: 1:35PM  E: 2:35PM 
928	TEXAS RANGERS






929	SAN FRANCISCO GIANTS

P: 1:07PM  C: 3:07PM  E: 4:07PM 
930	OAKLAND ATHLETICS



"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''

12:05 PM
2911
Chicago White Sox
J. Scholtens -R
+2½
-280
2912
Cleveland Guardians
X. Curry -R
-2½
+220
01:35 PM
2913
Houston Astros
J. Urquidy -R
+2½
-325
2914
New York Yankees
C. Rodon -L
-2½
+250
01:35 PM
2915
Toronto Blue Jays
C. Bassitt -R
+2½
-285
2916
Boston Red Sox
B. Bernardino -L
-2½
+225
01:35 PM
2921
Kansas City Royals
Z. Greinke -R
+2½
-185
2922
Philadelphia Phillies
T. Walker -R
-2½
+155
01:35 PM
2923
New York Mets
J. Quintana -L
+2½
-220
2924
Baltimore Orioles
K. Bradish -R
-2½
+180
01:40 PM
2901
Washington Nationals
J. Irvin -R
+2½
-220
2902
Cincinnati Reds
L. Richardson -R
-2½
+180
01:40 PM
2917
Tampa Bay Rays
T. Glasnow -R
-2½
+135
2918
Detroit Tigers
M. Manning -R
+2½
-165
02:10 PM
2903
Pittsburgh Pirates
J. Oviedo -R
+2½
-200
2904
Milwaukee Brewers
B. Woodruff -R
-2½
+160
02:10 PM
2925
Arizona Diamondbacks
Z. Gallen -R
-2½
+160
2926
Minnesota Twins
D. Keuchel -L
+2½
-200
02:15 PM
2905
Colorado Rockies
A. Gomber -L
+2½
-185
2906
St. Louis Cardinals
Z. Thompson -L
-2½
+155
02:20 PM
2907
Atlanta Braves
C. Morton -R
-2½
+205
2908
Chicago Cubs
J. Steele -L
+2½
-265
02:35 PM
2927
Miami Marlins
S. Alcantara -R
+2½
-305
2928
Texas Rangers
A. Heaney -L
-2½
+245
04:07 PM
2919
Seattle Mariners
B. Miller -R
+2½
-295
2920
Los Angeles Angels
C. Silseth -R
-2½
+235
04:07 PM
2929
San Francisco Giants
A. Cobb -R
-2½
+150
2930
Oakland Athletics
L. Medina -R
+2½
-180
07:10 PM
2909
Los Angeles Dodgers
L. Lynn -R
-2½
+200
2910
San Diego Padres
R. Hill -L
+2½
-260

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


