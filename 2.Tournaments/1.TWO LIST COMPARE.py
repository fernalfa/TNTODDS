import re
import time
import pyautogui

time.sleep(3)
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
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

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
print("First List:")
for name in names:
    print(name)


# Create a second list with missing teams
print("\nSecond List - Missing Teams:")
missing_teams = []
for name in odds_dict:
    if name not in names:
        missing_teams.append(name)
        print(name)


# Print the third list of names and odds
print("\nThird List:")
for name in names:
    odd = odds_dict.get(name.strip())
    if odd is not None:
        print(f"{name}: {odd}")
        enterodd()
    else:
        print(f"{name}: NONE")
        deleteodd()


# Alternatively, you can use a list comprehension to achieve the same result:
# missing_teams = [name for name in odds_dict if name not in names]
