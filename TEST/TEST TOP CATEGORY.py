import re
import pyautogui
import time
time.sleep(3)




data = """
*AMERICAN
Brooks Koepka
+550
Bryson DeChambeau
+600
Dustin Johnson
+650
Patrick Reed
+650
Talor Gooch
+700
Harold Varner III
+1000
Cameron Tringale
+1200
Jason Kokrak
+1400
Kevin Na
+1400
Peter Uihlein
+1600
Brendan Steele
+1600
Charles Howell III
+2000
Pat Perez
+2200
Bubba Watson
+3000
Matthew Wolff
+4500
Phil Mickelson
+5500
James Piot
+27500
Chase Koepka
+27500
Sihwan Kim
+70000

*AUSTRALASIAN
Cameron Smith
-130
Marc Leishman
+350
Danny Lee
+425
Matt Jones
+600
Jediah Morgan
+4000

*AUSTRALIAN
Cameron Smith
-190
Marc Leishman
+275
Matt Jones
+450
Jediah Morgan
+3000
"""


def run_additional_function():
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=5)
    pyautogui.keyUp('shift')
    pyautogui.typewrite('rot number')
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=2)
    pyautogui.keyUp('shift')
    print("Running additional function for the current category...")

def extract_players(data):
    players_by_category = {}
    sections = data.split('*')[1:]

    for section in sections:
        lines = section.strip().split('\n')
        category = lines[0].strip()
        players = lines[1:]
        player_names = [players[i] for i in range(0, len(players), 2)]
        player_odds = [players[i] for i in range(1, len(players), 2)]
        players_by_category[category] = list(zip(player_names, player_odds))

    return players_by_category

def calculate_surcharged_odd(odd):
    surcharge_percentage = 10  # 10% surcharge

    if 100 <= int(odd) <= 110:
        surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000) * -1
    else:
        if int(odd) > 100:
            surcharged_odd = min(int(odd) - int(odd) * (surcharge_percentage / 100), 10000)
        elif int(odd) < -100:
            surcharged_odd = min(int(odd) + int(odd) * (surcharge_percentage / 100), 10000)
        else:
            surcharged_odd = (int(odd) * -1) * (surcharge_percentage / 100)

    return surcharged_odd
def process_category(category):
    pyautogui.write(f"TOP {category} test test")
    pyautogui.press('TAB')
    pyautogui.write(f"TOP {category} test test")
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    print(f"Processing category: {category}")

def process_player(player):
    pyautogui.write(player)
    pyautogui.press('TAB')
    print(f"Processing player: {player}")


def process_player_odds(surcharged_odd):
    surcharged_odd = str(int(surcharged_odd))  # Convert surcharged_odd to integer and then back to string
    pyautogui.write(surcharged_odd)
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    print(f"Processing player surcharged odds: {surcharged_odd}")



players_by_category = extract_players(data)

# Initialize the dictionary to store surcharged odds
odds_dict = {}

# Calculate and store the surcharged odds for each player
for category, players in players_by_category.items():
    process_category(category)
    for player_name, player_odds in players:
        process_player(player_name)
        surcharged_odd = calculate_surcharged_odd(player_odds)
        process_player_odds(str(int(surcharged_odd)))

    run_additional_function()





    print()

# Print the calculated surcharged odds for each player
print("Calculated Surcharged Odds:")
for player, surcharged_odd in odds_dict.items():
    print(f"{player}: {surcharged_odd}")