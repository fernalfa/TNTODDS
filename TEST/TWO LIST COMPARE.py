import re
import time
import pyautogui

time.sleep(3)
surcharge_percentage = 10  # 10% surcharge


odds_data = '''

JONAS VINGEGAARD
+105
TADEJ POGACAR
+115
JAI HINDLEY
+1400
ENRIC MAS NICOLAU
+2200
RICHARD CARAPAZ
+2800
MATTIAS SKJELMOSE
+2800
BEN O'CONNOR
+3300
DAVID GAUDU
+4000
ADAM YATES
+4000
SIMON YATES
+5000
TOM PIDCOCK
+5000
MIKEL LANDA
+6600
FELIX GALL
+8000
ROMAIN BARDET
+8000
DANIEL MARTINEZ
+8000
CARLOS RODRIGUEZ
+8000
WOUT VAN AERT
+10000
EGAN BERNAL
+10000
WILCO KELDERMAN
+10000
JULIAN ALAPHILIPPE
+15000
SEPP KUSS
+15000
PELLO BILBAO
+15000
MATTEO JORGENSON
+15000
MARC SOLER
+20000
TORSTEIN TRAEEN
+30000
THIBAUT PINOT
+30000
RIGOBERTO URAN
+30000
GUILLAUME MARTIN
+30000
LOUIS MEINTJES
+30000
MICHAEL WOODS
+30000
TOBIAS HALLAND JOHANNESSEN
+40000
ALEXEY LUTSENKO
+40000
EMANUEL BUCHMANN
+40000
GIULIO CICCONE
+40000
MATHIEU VAN DER POEL
+40000
JACK HAIG
+50000
JOHAN ESTEBAN CHAVES
+50000
RUBEN GUERREIRO
+50000
RAFAL MAJKA
+50000
NEILSON POWLESS
+50000
VALENTIN MADOUAS
+50000
ION IZAGIRRE
+60000
BINIAM GIRMAY
+60000
CLEMENT CHAMPOUSSIN
+75000
JUAN PEDRO LOPEZ
+75000
TIESJ BENOOT
+75000
ANTONIO PEDRERO
+100000
WOUT POELS
+100000
PIERRE LATOUR
+100000
WARREN BARGUIL
+100000
MATEJ MOHORIC
+100000
FELIX GROSSSCHARTNER
+100000
JONATHAN CASTROVIEJO
+150000
AURELIEN PARET-PEINTRE
+150000
BOB JUNGELS
+150000
NICK SCHULTZ
+150000
PATRICK KONRAD
+150000
MICHAL KWIATKOWSKI
+150000
QUINN SIMMONS
+200000
KASPER ASGREEN
+200000
PETER SAGAN
+250000
FRED WRIGHT
+250000
NILS POLITT
+450000
MAGNUS CORT NIELSEN
+450000
MADS PEDERSEN
+450000


ELMAR REINDERS
+450000

'''

def enterodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(odd)))
    pyautogui.press('enter')
    pyautogui.press('down')
def deleteodd():
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')


with open('DATA IBET', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

print(names)

odds = re.findall(r'(.+)\n([-+]?\d+)', odds_data)

odds_dict = {}

for name, odd in odds:
    if 100 <= int(odd) <= 110:
        surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000) * -1
    else:
        if int(odd) > 100:
            surcharged_odd = min(int(odd) - int(odd) * (surcharge_percentage / 100), 10000)
        elif int(odd) < -100:
            surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000)
        else:
            surcharged_odd = (int(odd) * -1) * (surcharge_percentage / 100)
    odds_dict[name] = surcharged_odd

# Print the first list of names
print("First List:")
for name in names:
    print(name)

# Print the second list of names and odds
print("\nSecond List:")
for name in names:
    odd = odds_dict.get(name.strip())
    if odd is not None:
        print(f"{name}: {odd}")
        enterodd()
    else:
        print(f"{name}: NONE")
        deleteodd()