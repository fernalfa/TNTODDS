import re
from tqdm import tqdm
import time
import pyautogui

time.sleep(5)
surcharge_percentage = 10  # 10% surcharge

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


with open('DATAIBET', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    line = line.strip()
    if line.isdigit() or line.startswith('+') or line.startswith('-'):
        continue
    if line:
        names.append(line)

print(names)

with open('DATAPROVIDER', 'r') as file:
    data = file.read()

odds = re.findall(r'(.+)\n([-+]?\d+)', data)

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
print("\n************:")
print("CONTENDERS LIST:")
print("************:")
for name in names:
    print(name)

# Create a fourth list with names having NONE odds
print("\n************:")
print("CONTENDERS TO BE DELETED:")
print("************:")

none_odds_teams = []
for name in names:
    if odds_dict.get(name.strip()) is None:
        none_odds_teams.append(name.strip())
        print(name)


# Print the third list of names and odds

print("\n************:")
print("TOURNAMENT ADJUSTED ODDS:")
print("************:")

# Assuming `names` is a list of names
for name in tqdm(names, desc="Progress", ncols=100):
    odd = odds_dict.get(name.strip())
    if odd is not None:
        print(f"{name}: {odd}")
        enterodd()
    else:
        print(f"{name}: NONE")
        deleteodd()


# Create a second list with missing teams
print("\n************:")
print("MISSING CONTENDERS:")
print("************:")

missing_teams = []
for name in odds_dict:
    if name not in names:
        missing_teams.append(name)
        print(name)
