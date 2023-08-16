import re
import time
import pyautogui

time.sleep(5)
surcharge_percentage = 0  # 10% surcharge

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



# Create a second list with missing teams
print("\n************:")
print("CREATED CONTENDERS:")
print("************:")

missing_teams = []
for name in odds_dict:
    if name not in names:
        missing_teams.append(name)
        print(name)
        pyautogui.typewrite(name)
        pyautogui.press('tab')
        pyautogui.typewrite('-150')
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')