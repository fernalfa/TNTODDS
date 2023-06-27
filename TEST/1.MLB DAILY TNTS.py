import time
import pyautogui

time.sleep(3)
skip = 4

data = '''
CIN Reds-logoCIN Reds
at
BAL Orioles-logoBAL Orioles
TODAY 7:05PM
Moneyline / Total Runs

CIN Reds / Over 8.5
+285
CIN Reds / Under 8.5
+370
BAL Orioles / Over 8.5
+215
BAL Orioles / Under 8.5
+210
SF Giants-logoSF Giants
at
TOR Blue Jays-logoTOR Blue Jays
TODAY 7:07PM
Moneyline / Total Runs

SF Giants / Over 7.5
+320
SF Giants / Under 7.5
+400
TOR Blue Jays / Over 7.5
+175
TOR Blue Jays / Under 7.5
+220
MIL Brewers-logoMIL Brewers
at
NY Mets-logoNY Mets
TODAY 7:10PM
Moneyline / Total Runs

MIL Brewers / Over 9.5
+320
MIL Brewers / Under 9.5
+320
NY Mets / Over 9.5
+245
NY Mets / Under 9.5
+185
MIA Marlins-logoMIA Marlins
at
BOS Red Sox-logoBOS Red Sox
TODAY 7:10PM
Moneyline / Total Runs

MIA Marlins / Over 9.5
+275
MIA Marlins / Under 9.5
+290
BOS Red Sox / Over 9.5
+255
BOS Red Sox / Under 9.5
+220
MIN Twins-logoMIN Twins
at
ATL Braves-logoATL Braves
TODAY 7:20PM
Moneyline / Total Runs

MIN Twins / Over 8.5
+285
MIN Twins / Under 8.5
+380
ATL Braves / Over 8.5
+195
ATL Braves / Under 8.5
+225
HOU Astros-logoHOU Astros
at
STL Cardinals-logoSTL Cardinals
TODAY 7:45PM
Moneyline / Total Runs

HOU Astros / Over 7.5
+190
HOU Astros / Under 7.5
+310
STL Cardinals / Over 7.5
+265
STL Cardinals / Under 7.5
+275


PHI Phillies-logoPHI Phillies
at
CHI Cubs-logoCHI Cubs
TODAY 8:05PM
Moneyline / Total Runs

PHI Phillies / Over 8.5
+210
PHI Phillies / Under 8.5
+270
CHI Cubs / Over 8.5
+285
CHI Cubs / Under 8.5
+280


DET Tigers-logoDET Tigers
at
TEX Rangers-logoTEX Rangers
TODAY 8:05PM
Moneyline / Total Runs

DET Tigers / Over 9.5
+380
DET Tigers / Under 9.5
+390
TEX Rangers / Over 9.5
+190
TEX Rangers / Under 9.5
+180

CLE Guardians-logoCLE Guardians
at
KC Royals-logoKC Royals
TODAY 8:10PM
Moneyline / Total Runs

CLE Guardians / Over 8.5
+170
CLE Guardians / Under 8.5
+275
KC Royals / Over 8.5
+290
KC Royals / Under 8.5
+340
LA Dodgers-logoLA Dodgers
at
COL Rockies-logoCOL Rockies
TODAY 8:40PM
Moneyline / Total Runs

LA Dodgers / Over 11.5
+140
LA Dodgers / Under 11.5
+170
COL Rockies / Over 11.5
+600
COL Rockies / Under 11.5
+450
CHI White Sox-logoCHI White Sox
at
LA Angels-logoLA Angels
TODAY 9:38PM
Moneyline / Total Runs

CHI White Sox / Over 8.5
+380
CHI White Sox / Under 8.5
+400
LA Angels / Over 8.5
+195
LA Angels / Under 8.5
+170
NY Yankees-logoNY Yankees
at
OAK Athletics-logoOAK Athletics
TODAY 9:40PM
Moneyline / Total Runs

NY Yankees / Over 7.5
+185
NY Yankees / Under 7.5
+270
OAK Athletics / Over 7.5
+310
OAK Athletics / Under 7.5
+295

TB Rays-logoTB Rays
at
ARI Diamondbacks-logoARI Diamondbacks
TODAY 9:40PM
Moneyline / Total Runs

TB Rays / Over 7.5
+240
TB Rays / Under 7.5
+370
ARI Diamondbacks / Over 7.5
+210
ARI Diamondbacks / Under 7.5
+260
WAS Nationals-logoWAS Nationals
at
SEA Mariners-logoSEA Mariners
TODAY 9:40PM
Moneyline / Total Runs

WAS Nationals / Over 7.5
+390
WAS Nationals / Under 7.5
+500
SEA Mariners / Over 7.5
+140
SEA Mariners / Under 7.5
+200

'''

lines = data.strip().split('\n')
count = 0
for line in lines:
    if line.startswith('+'):
        pyautogui.press('enter')
        pyautogui.write(line[1:])
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('−'):
        pyautogui.press('enter')
        pyautogui.write('-')
        pyautogui.write(line[1:])
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
