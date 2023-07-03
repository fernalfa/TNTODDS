import re
import time
import pyautogui

time.sleep(3)
surcharge_percentage = 10  # 10% surcharge


odds_data = '''AUGUSTE RODIN
+500
ACE IMPACT
+650
EMILY UPJOHN
+800
BLUE ROSE CEN
+1000
HUKUM
+1400
SAVETHELASTDANCE
+1400
SOUL SISTER
+1400
LUXEMBOURG
+1600
PYLEDRIVER
+1600
PADDINGTON
+1600
WESTOVER
+2000
DESERT CROWN
+2000
ADAYAR
+2000
VADENI
+2500
BAY BRIDGE
+2500
BIG ROCK
+2500
FREE WIND
+2500
PENSEE DU JOUR
+3300
FEED THE FLAME
+3300
HURRICANE LANE
+3300
RUBIS VENDOME
+3300
SIMCA MILLE
+3300
IMPERIAL EMPEROR
+4000
NEVER ENDING STORY
+4000
ONESTO
+4000
SALIERA
+4000
MILITARY ORDER
+4000
ABOVE THE CURVE
+4000
FIRST MINISTER
+4000
THROUGH SEVEN SEAS
+4000
TUNNES
+5000
LA PARISIENNE
+5000
JANNAH ROSE
+5000
RUNNING LION
+5000
CRYPTO FORCE
+5000
CHANGINGOFTHEGUARD
+5000
EMILY DICKINSON
+5000
FLYING HONOURS
+5000
LEFT SEA
+5000
LINDY
+5000
PLACE DU CARROUSEL
+5000
POINT LONSDALE
+5000
SPREWELL
+5000
TRUE TESTAMENT
+5000
FLIGHT LEADER
+6600
DURA EREDE
+6600
AMERICAN FLAG
+6600
FRANCESCO CLEMENTE
+6600
NEW LONDON
+6600
PIZ BADILE
+6600
SILVER CRACK
+6600
ZAGREY
+6600
AL ASIFAH
+6600
PADISHAKH
+10000
RAJAPOUR
+10000
HEARTACHE TONIGHT
+10000
SAMMARCO
+10000
ARREST
+10000
MR HOLLYWOOD
+10000
AL RIFFA
+10000
ALDER
+10000
CHESSPIECE
+10000
CLAYMORE
+10000
CROWN PRINCESSE
+10000
DUBAI MILE
+10000
ELZORA
+10000
HANS ANDERSEN
+10000
HAYA ZARK
+10000
PRETTY TIGER
+10000
SABIO CEN
+10000
SIRJAN
+10000
SISFAHAN
+10000
WINTER PUDDING
+10000
CANBERRA LEGEND
+12500
WIDA
+15000
DEAR MY FRIEND
+20000
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