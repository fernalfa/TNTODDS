import re
import time
import pyautogui
time.sleep(3)
surcharge_percentage = 10  # 10% surcharge

data = '''
8663401

** ALL BETS ACTION **
8663402

SAO PAULO
8663403

SAN LORENZO
8663404

BRAGANTINO
8663405

SANTOS
8663406

FORTALEZA
8663407

BOTAFOGO
8663408

ESTUDIANTES LP
8663409

AMERICA MG
8663410

DEFENSA Y JUSTICIA
8663411

PENAROL
8663412

NEWELL'S
8663413

CA TIGRE
8663414

HURACAN
8663415

LDU QUITO
8663416

GOIAS
8663417

INDEPENDIENTE SANTA FE
8663418

MILLONARIOS
8663419

GIMNASIA LP
8663420

EMELEC
8663421

GUARANI ASUNCION
8663422

DEPORTES TOLIMA
8663423

UNIVERSITARIO DE DEPORTES
8663424

PALESTINO
8663425

DANUBIO
8663426

MAGALLANES
8663427

AUDAX ITALIANO
8663428

CESAR VALLEJO
8663429

TACUARY
8663430

BLOOMING
8663431

ORIENTE PETROLERO
8663432

ACADEMIA PUERTO CABELLO
8663433

ESTUDIANTES MERIDA
'''


odds_data = '''
SAO PAULO
+500
FORTALEZA
+700
BRAGANTINO
+700
BOTAFOGO
+900
NEWELL'S
+1200
DEFENSA Y JUSTICIA
+1200
CORINTHIANS
+1200
ESTUDIANTES LP
+1400
GOIAS
+1600
LDU QUITO
+1600
SAN LORENZO
+2000
LIBERTAD ASUNCION
+2200
AMERICA MG
+2200
CA TIGRE
+2800
COLO COLO
+2800
EMELEC
+4000
GUARANI ASUNCION
+5000
SPORTING CRISTAL
+5000
AUDAX ITALIANO
+5000
UNIVERSITARIO DE DEPORTES
+5000
INDEPENDIENTE MEDELLIN
+5000
BARCELONA GUAYAQUIL
+5000
NUBLENSE
+6600
PATRONATO PARANA
+8000
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

names = re.findall(r'\n\d+\n\n(.+)', data)
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









