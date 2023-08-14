import re
import pyautogui
import time
time.sleep(5)

# COPIAR Y PEGAR DE BULLWAGER
text = """
CIN REDS GM#1
B WILLIAMSON L
+102
o9-117
+1½-180
952
PIT PIRATES GM#1
M KELLER R
-122
u9-103
-1½+160
(Schedule.aspx?WT=0&lg=5&id=,39046070&IDWT=-1)
MAJOR LEAGUE BASEBALL
ATL BRAVES @ NY METS
Aug 13 7:10 PM
Rot
Team
Pitcher
M Line
Total
Run Line
953
ATL BRAVES
Y CHIRINOS R
-132
o10+100
-1½+118
954
NY METS
K SENGA R
+112
u10-120
+1½-138
(Schedule.aspx?WT=0&lg=5&id=,39045711&IDWT=-1)
MAJOR LEAGUE BASEBALL
COL ROCKIES @ LA DODGERS
Aug 13 4:10 PM
Rot
Team
Pitcher
M Line
Total
Run Line
955
COL ROCKIES
K FREELAND L
+258
o8½-115
+1½+136
956
LA DODGERS
J URIAS L
-323
u8½-105
-1½-156
(Schedule.aspx?WT=0&lg=5&id=,39045712&IDWT=-1)
MAJOR LEAGUE BASEBALL
SD PADRES @ ARI DBACKS
Aug 13 4:10 PM
Rot
AMERICAN LEAGUE
Team
Pitcher
M Line
Total
Run Line
957
SD PADRES
S LUGO R
-140
o9+100
-1½+109
958
ARI DBACKS
B PFAADT R
+120
u9-120
+1½-129
(Schedule.aspx?WT=0&lg=5&id=,39045713&IDWT=-1)
MAJOR LEAGUE BASEBALL
DET TIGERS @ BOS RED SOX
Aug 13 12:05 PM
Rot
Team
Pitcher
M Line
Total
Run Line
959
DET TIGERS
E RODRIGUEZ L
+114
o9½-125
+1½-170
960
BOS RED SOX
K CRAWFORD R
-134
u9½+105
-1½+150
(Schedule.aspx?WT=0&lg=5&id=,39045714&IDWT=-1)
MAJOR LEAGUE BASEBALL
CLE GUARDIANS @ TB RAYS
Aug 13 1:40 PM
Rot
Team
Pitcher
M Line
Total
Run Line
961
CLE GUARDIANS
T BIBEE R
+148
o7-120
+1½-143
962
TB RAYS
Z EFLIN R
-168
u7+100
-1½+123
(Schedule.aspx?WT=0&lg=5&id=,39045715&IDWT=-1)
MAJOR LEAGUE BASEBALL
LA ANGELS @ HOU ASTROS
Aug 13 2:10 PM
Rot
Team
Pitcher
M Line
Total
Run Line
963
LA ANGELS
C SILSETH R
+112
o8½-120
+1½-165
964
HOU ASTROS
NATIONAL LEAGUE
J URQUIDY R
-132
u8½+100
-1½+145
(Schedule.aspx?WT=0&lg=5&id=,39045716&IDWT=-1)
MAJOR LEAGUE BASEBALL
BAL ORIOLES @ SEA MARINERS
Aug 13 4:10 PM
Rot
Team
Pitcher
M Line
Total
Run Line
965
BAL ORIOLES
K BRADISH R
-106
o8-110
-1½+155
966
SEA MARINERS
B MILLER R
-114
u8-110
+1½-175
(Schedule.aspx?WT=0&lg=5&id=,39045717&IDWT=-1)
MAJOR LEAGUE BASEBALL
OAK ATHLETICS @ WAS NATIONALS
Aug 13 1:35 PM
Rot
Team
Pitcher
M Line
Total
Run Line
967
OAK ATHLETICS
K WALDICHUK L
+119
o9½-113
+1½-163
968
WAS NATIONALS
T WILLIAMS R
-139
u9½-107
-1½+143
(Schedule.aspx?WT=0&lg=5&id=,39045718&IDWT=-1)
MAJOR LEAGUE BASEBALL
MIN TWINS @ PHI PHILLIES
Aug 13 1:35 PM
Rot
Team
Pitcher
M Line
Total
Run Line
969
MIN TWINS
S GRAY R
-107
o8½-112
+1½-198
970
PHI PHILLIES
R SUAREZ L
-113
u8½-108
-1½+168
(Schedule.aspx?WT=0&lg=5&id=,39045719&IDWT=-1)
MAJOR LEAGUE BASEBALL
CHI CUBS @ TOR BLUE JAYS
Aug 13 1:37 PM
Rot
Team
Pitcher
M Line
Total
Run Line
971
CHI CUBS
J TAILLON R
-106
o9-117
+1½-190
972
TOR BLUE JAYS
H RYU L
-114
u9-103
-1½+165
(Schedule.aspx?WT=0&lg=5&id=,39045720&IDWT=-1)
MAJOR LEAGUE BASEBALL
NY YANKEES @ MIA MARLINS
Aug 13 1:40 PM
Rot
Team
Pitcher
M Line
Total
Run Line
973
NY YANKEES
G COLE R
-122
o7-115
-1½+145
974
MIA MARLINS
E PEREZ R
+102
u7-105
+1½-165
(Schedule.aspx?WT=0&lg=5&id=,39045721&IDWT=-1)
MAJOR LEAGUE BASEBALL
MIL BREWERS @ CHI WHITE SOX
Aug 13 2:10 PM
Rot
Team
Pitcher
M Line
Total
Run Line
975
MIL BREWERS
F PERALTA R
-140
o8-110
-1½+120
976
CHI WHITE SOX
D CEASE R
INTERLEAGUE
+120
u8-110
+1½-140
(Schedule.aspx?WT=0&lg=5&id=,39045722&IDWT=-1)
MAJOR LEAGUE BASEBALL
TEX RANGERS @ SF GIANTS
Aug 13 4:05 PM
Rot
Team
Pitcher
M Line
Total
Run Line
977
TEX RANGERS
D DUNNING R
+104
o8-115
+1½-180
978
SF GIANTS
L WEBB R
-124
u8-105
-1½+160
(Schedule.aspx?WT=0&lg=5&id=,39045723&IDWT=-1)
Name
Hey, I really love the
site but I believe that
SEND
Favorites Continue Refresh
DOUBLE HEADER GM#2
MAJOR LEAGUE BASEBALL
CIN REDS GM#2 @ PIT PIRATES GM#2
Aug 13 6:05 PM
Rot
Team
Pitcher
M Line
Total
Run Line
979
CIN REDS GM#2
L WEAVER -R
-108
o9½-120
+1½-195
980
PIT PIRATES GM#2
A JACKSON R
-112
u9½+100
-1½+165
"""

text = re.sub(r'(\d+)½', r'\1.5', text)

pattern = r'o(\d*\.?\d+)'
matches = re.findall(pattern, text)

values = [float(match) for match in matches]

def modify_values(matches):
    modified_values = []
    for value in matches:
        modified_values.extend([value + 0.5, value - 0.5])
    return modified_values

modified_data = modify_values(values)

for value in modified_data:
    print(value)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(value))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')