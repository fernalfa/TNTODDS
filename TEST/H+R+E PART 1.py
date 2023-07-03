import time

import pyautogui
import re
time.sleep(3)


text = """
PM
1901
San Diego Padres
M. Wacha -R
O 30½
-120
1902
Cincinnati Reds
B. Williamson -L
U 30½
-110
02:15 PM
1921
New York Yankees - Game #1
L. Severino -R
O 26½
-110
1922
St. Louis Cardinals - Game #1
J. Flaherty -R
U 26½
-120

"""

def enteroverodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.typewrite(str(over_odds[i]))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=3)
def enterunderodd():
    pyautogui.press('enter')
    pyautogui.typewrite(str(number))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.typewrite(str(under_odds[i]))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down', presses=2)


over_numbers = re.findall(r"O (\d+½|\d+)", text)
over_number = [number.replace("½", ".5") for number in over_numbers]
under_numbers = re.findall(r"U (\d+½|\d+)", text)

over_odds = []
under_odds = []

for number in over_numbers:
    index = text.index("O " + number)
    next_line_index = text.index("\n", index) + 1
    next_line = text[next_line_index:].split("\n", 1)[0].strip()
    over_odds.append(next_line)

for number in under_numbers:
    index = text.index("U " + number)
    next_line_index = text.index("\n", index) + 1
    next_line = text[next_line_index:].split("\n", 1)[0].strip()
    under_odds.append(next_line)


# Print the extracted OVER numbers
print("TOTALS:")
for number in over_numbers:
    print(number)

print()

# Print the extracted OVER numbers and odds
print("OVER Odds:")
for number, odds in zip(over_numbers, over_odds):
    print(odds)

print()

# Print the extracted UNDER numbers and odds
print("UNDER Odds:")
for number, odds in zip(under_numbers, under_odds):
    print(odds)

for number in over_number:
    print(number)

# Compare the OVER and UNDER odds for each game
for i in range(len(over_odds)):
    if over_odds[i] > under_odds[i]:
        print(f"In game {i+1}, OVER odds are higher.")


    else:
        print(f"In game {i+1}, OVER and UNDER odds are the same.")
