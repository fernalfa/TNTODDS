import re
import time
import pyautogui
time.sleep(3)

# PEGAR SCHEDULE DE DBS
data1 = """
951	MIAMI MARLINS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
952	ATLANTA BRAVES






953	MILWAUKEE BREWERS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
954	PITTSBURGH PIRATES






955	WASHINGTON NATIONALS

P: 10:35AM  C: 12:35PM  E: 1:35PM 
956	PHILADELPHIA PHILLIES






957	SAN DIEGO PADRES

P: 10:40AM  C: 12:40PM  E: 1:40PM 
958	CINCINNATI REDS






959	SAN FRANCISCO GIANTS

P: 4:10PM  C: 6:10PM  E: 7:10PM 
960	NEW YORK METS






AMERICAN LEAGUE  
 
961	MINNESOTA TWINS

P: 9:05AM  C: 11:05AM  E: 12:05PM 
962	BALTIMORE ORIOLES






963	BOSTON RED SOX

P: 10:37AM  C: 12:37PM  E: 1:37PM 
964	TORONTO BLUE JAYS






965	HOUSTON ASTROS

P: 11:35AM  C: 1:35PM  E: 2:35PM 
966	TEXAS RANGERS






967	CHICAGO WHITE SOX

P: 1:07PM  C: 3:07PM  E: 4:07PM 
968	OAKLAND ATHLETICS






969	TAMPA BAY RAYS

P: 1:10PM  C: 3:10PM  E: 4:10PM 
970	SEATTLE MARINERS






INTERLEAGUE  
 
971	LOS ANGELES DODGERS

P: 11:10AM  C: 1:10PM  E: 2:10PM 
972	KANSAS CITY ROYALS






973	NEW YORK YANKEES

P: 11:15AM  C: 1:15PM  E: 2:15PM 
974	ST. LOUIS CARDINALS






975	CLEVELAND GUARDIANS

P: 2:05PM  C: 4:05PM  E: 5:05PM 
976	CHICAGO CUBS






977	DETROIT TIGERS

P: 12:10PM  C: 2:10PM  E: 3:10PM 
978	COLORADO ROCKIES






979	ARIZONA DIAMONDBACKS

P: 1:07PM  C: 3:07PM  E: 4:07PM 
980	LOS ANGELES ANGELS








"""

team_names = re.findall(r"\d+\s+(.*\S)\s*$", data1, re.MULTILINE)
team_names = [name.strip() for name in team_names]

# PEGAR ALT DE BETONLINE
data2 = '''

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