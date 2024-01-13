import time
import pyautogui
from tqdm import tqdm

time.sleep(5)
skip = 3


# Open the text file
data = """ 

BAL Ravens v BUF Bills - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-190
BUF Bills
+210
Tie
+800
BAL Ravens v CLE Browns - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-600
CLE Browns
+600
Tie
+1200
BAL Ravens v DAL Cowboys - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-185
DAL Cowboys
+270
Tie
+500
BAL Ravens v DET Lions - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-295
Tie
+450
DET Lions
+550
BAL Ravens v KC Chiefs - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-380
KC Chiefs
+500
Tie
+750
BAL Ravens v PHI Eagles - Which Team Will Progress Further in the Playoffs?

BAL Ravens
-380
Tie
+500
PHI Eagles
+750
BAL Ravens v SF 49ers - Which Team Will Progress Further in the Playoffs?

SF 49ers
-110
BAL Ravens
+150
Tie
+550
BUF Bills v DAL Cowboys - Which Team Will Progress Further in the Playoffs?

BUF Bills
+120
DAL Cowboys
+145
Tie
+330
BUF Bills v DET Lions - Which Team Will Progress Further in the Playoffs?

BUF Bills
-115
DET Lions
+240
Tie
+290
BUF Bills v KC Chiefs - Which Team Will Progress Further in the Playoffs?

BUF Bills
-165
KC Chiefs
+200
Tie
+700
BUF Bills v MIA Dolphins - Which Team Will Progress Further in the Playoffs?

BUF Bills
-190
Tie
+330
MIA Dolphins
+400
BUF Bills v SF 49ers - Which Team Will Progress Further in the Playoffs?

SF 49ers
-210
BUF Bills
+300
Tie
+550
CLE Browns v PIT Steelers - Which Team Will Progress Further in the Playoffs?

Tie
+115
CLE Browns
+120
PIT Steelers
+475
DAL Cowboys v DET Lions - Which Team Will Progress Further in the Playoffs?

DAL Cowboys
-140
DET Lions
+165
Tie
+700
DAL Cowboys v PHI Eagles - Which Team Will Progress Further in the Playoffs?

DAL Cowboys
-140
PHI Eagles
+250
Tie
+350
DET Lions v GB Packers - Which Team Will Progress Further in the Playoffs?

DET Lions
-140
Tie
+190
GB Packers
+550
DET Lions v PHI Eagles - Which Team Will Progress Further in the Playoffs?

DET Lions
+120
PHI Eagles
+200
Tie
+220
HOU Texans v GB Packers - Which Team Will Progress Further in the Playoffs?

Tie
+120
HOU Texans
+125
GB Packers
+425
HOU Texans v LA Rams - Which Team Will Progress Further in the Playoffs?

Tie
+130
HOU Texans
+140
LA Rams
+310
KC Chiefs v PHI Eagles - Which Team Will Progress Further in the Playoffs?

KC Chiefs
+160
Tie
+180
PHI Eagles
+185
LA Rams v GB Packers - Which Team Will Progress Further in the Playoffs?

Tie
-115
LA Rams
+200
GB Packers
+340
MIA Dolphins v DET Lions - Which Team Will Progress Further in the Playoffs?

DET Lions
+110
Tie
+180
MIA Dolphins
+280
MIA Dolphins v PHI Eagles - Which Team Will Progress Further in the Playoffs?

PHI Eagles
+145
Tie
+155
MIA Dolphins
+240
SF 49ers v DAL Cowboys - Which Team Will Progress Further in the Playoffs?

SF 49ers
-265
DAL Cowboys
+270
Tie
+1100
SF 49ers v PHI Eagles - Which Team Will Progress Further in the Playoffs?

SF 49ers
-600
PHI Eagles
+550
Tie
+1500

"""

lines = data.strip().split('\n')
count = 0

# Count the number of lines that need processing
num_lines = sum(1 for line in lines if line.startswith('+') or line.startswith('-') or line.startswith('−'))

# Initialize the tqdm progress bar
with tqdm(total=num_lines, desc="Processing lines", ncols=100) as pbar:
    for line in lines:
        if line.startswith('+'):
            value = int(line[1:])
            if value > 10000:
                value = 10000
            pyautogui.press('enter')
            pyautogui.write(str(value))
            pyautogui.press('enter')
            pyautogui.press('down')
            count += 1
            if count % skip == 0:
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
        elif line.startswith('-') or line.startswith('−'):
            value = int(line)
            if value > 10000:
                value = 10000
            pyautogui.press('enter')
            pyautogui.write(str(value))
            pyautogui.press('enter')
            pyautogui.press('down')
            count += 1
            if count % skip == 0:
                pyautogui.press('down')
                pyautogui.press('down')


        # Update the progress bar
        pbar.update(1)
