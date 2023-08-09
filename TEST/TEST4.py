import re
import pyautogui
import time
time.sleep(5)

text = """
2:10:00 P.M.

LogoLA DODGERS
+1½-162
o9-125
+130
@
LogoSD PADRES
-1½+142
u9+105
-142
 Live Streaming Live Betting 36 Props
4:40:00 P.M.

LogoWAS NATIONALS
+1½-101
o10-112
+206
@
LogoPHI PHILLIES
-1½-119
u10-108
-230
 Live Streaming Live Betting 36 Props
4:40:00 P.M.

LogoMIA MARLINS
-1½+102
o10½-110
-148
@
LogoCIN REDS
+1½-122
u10½-110
+136
 Live Streaming Live Betting 36 Props
5:05:00 P.M.

LogoATL BRAVES
-1½-170
o8½-130
-285
@
LogoPIT PIRATES
+1½+150
u8½+110
+250
 Live Streaming Live Betting 36 Props
5:10:00 P.M.

LogoCHI CUBS
+1½-193
o9-105
+102
@
LogoNY METS
-1½+168
u9-115
-112
 Live Streaming Live Betting 36 Props
6:10:00 P.M.

LogoCOL ROCKIES
+1½-105
o8½-106
+202
@
LogoMIL BREWERS
-1½-115
u8½-114
-225
 Live Streaming Live Betting 36 Props
4:40:00 P.M.

LogoMIN TWINS
-1½-110
o8½-102
-169
@
LogoDET TIGERS
+1½-110
u8½-118
+155
 Live Streaming Live Betting 36 Props
5:10:00 P.M.

LogoKC ROYALS
+1½-118
o10-105
+174
@
LogoBOS RED SOX
-1½-102
u10-115
-190
 Live Streaming Live Betting 36 Props
5:10:00 P.M.

LogoTOR BLUE JAYS
-1½+115
o8½-106
-132
@
LogoCLE GUARDIANS
+1½-135
u8½-114
+121
 Live Streaming Live Betting 36 Props
6:10:00 P.M.

LogoNY YANKEES
-1½-104
o8-105
-162
@
LogoCHI WHITE SOX
+1½-116
u8-115
+148
 Live Streaming Live Betting 36 Props
7:40:00 P.M.

LogoTEX RANGERS
-1½-135
o8½-128
-215
@
LogoOAK ATHLETICS
+1½+115
u8½+108
+194
 Live Streaming Live Betting 36 Props
7:38:00 P.M.

LogoSF GIANTS
-1½+139
o8½-105
-115
@
LogoLA ANGELS
+1½-159
u8½-115
+105
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