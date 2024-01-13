import re
from tqdm import tqdm
import time
import pyautogui
import tkinter as tk

ROT_NUMBER = 8091171
add = 10
TIMEDELAY = 30

description = " - TEAM TO PROGRESS FURTHER IN THE PLAYOFFS"
header1 = "** WINNING THE SUPER BOWL IS"
header2 = "CONSIDERED AS PROGRESSING FURTHER **"

def category_headers():
    time.sleep(5)
    with open('../0.INFO', 'r') as file:
        data = file.read()

    def run_additional_function():
        print("New Tournament being Created...")
        pyautogui.press('tab', presses=4)
        pyautogui.press('enter')
        time.sleep(TIMEDELAY)
        pyautogui.keyDown('shift')
        pyautogui.press('tab', presses=7)
        pyautogui.keyUp('shift')
        print("Created...")

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

    def slow_type(text, delay=0.01):
        for char in text:
            pyautogui.write(char)
            time.sleep(delay)


    def process_category(category):
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        pyautogui.write(str(ROT_NUMBER))
        pyautogui.press('TAB')
        slow_type(f"{header1}")
        pyautogui.press('TAB')
        pyautogui.write(str(-120))
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('ENTER')
        slow_type(f"{header2}")
        pyautogui.press('TAB')
        pyautogui.write(str(-120))
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('ENTER')
        print(f"Processing category: {category}")


    def process_player(player):
        slow_type(player)
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

    # Calculate and store the surcharged odds for each player
    for category, players in players_by_category.items():
        process_category(category)
        for player_name, player_odds in players:
            process_player(player_name)
            surcharged_odd = calculate_surcharged_odd(player_odds)
            process_player_odds(str(int(surcharged_odd)))

        run_additional_function()
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        ROT_NUMBER = ROT_NUMBER + add
        print()

def category_1_header():
    time.sleep(5)
    with open('../../../Downloads/TNTODDS/0.INFO', 'r') as file:
        data = file.read()

    def run_additional_function():
        print("New Tournament being Created...")
        pyautogui.press('tab', presses=4)
        pyautogui.press('enter')
        time.sleep(TIMEDELAY)
        pyautogui.keyDown('shift')
        pyautogui.press('tab', presses=7)
        pyautogui.keyUp('shift')
        print("Created...")

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

    def slow_type(text, delay=0.01):
        for char in text:
            pyautogui.write(char)
            time.sleep(delay)


    def process_category(category):
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        pyautogui.write(str(ROT_NUMBER))
        pyautogui.press('TAB')
        slow_type(f"{header1}")
        pyautogui.press('TAB')
        pyautogui.write(str(-120))
        pyautogui.press('TAB')
        pyautogui.press('TAB')
        pyautogui.press('ENTER')
        print(f"Processing category: {category}")


    def process_player(player):
        slow_type(player)
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

    # Calculate and store the surcharged odds for each player
    for category, players in players_by_category.items():
        process_category(category)
        for player_name, player_odds in players:
            process_player(player_name)
            surcharged_odd = calculate_surcharged_odd(player_odds)
            process_player_odds(str(int(surcharged_odd)))

        run_additional_function()
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        ROT_NUMBER = ROT_NUMBER + add
        print()

def category_no_headers():
    time.sleep(5)
    with open('../../../Downloads/TNTODDS/0.INFO', 'r') as file:
        data = file.read()

    def run_additional_function():
        print("New Tournament being Created...")
        pyautogui.press('tab', presses=4)
        pyautogui.press('enter')
        time.sleep(TIMEDELAY)
        pyautogui.keyDown('shift')
        pyautogui.press('tab', presses=7)
        pyautogui.keyUp('shift')
        print("Created...")

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

    def slow_type(text, delay=0.01):
        for char in text:
            pyautogui.write(char)
            time.sleep(delay)

    def process_category(category):
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        slow_type(f"{category}{description}")
        pyautogui.press('TAB')
        pyautogui.write(str(ROT_NUMBER))
        pyautogui.press('TAB')
        print(f"Processing category: {category}")

    def process_player(player):
        slow_type(player)
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

    # Calculate and store the surcharged odds for each player
    for category, players in players_by_category.items():
        process_category(category)
        for player_name, player_odds in players:
            process_player(player_name)
            surcharged_odd = calculate_surcharged_odd(player_odds)
            process_player_odds(str(int(surcharged_odd)))

        run_additional_function()
        global ROT_NUMBER  # Add this line to access the global ROT_NUMBER variable
        ROT_NUMBER = ROT_NUMBER + add
        print()

def show_popup():
    popup = tk.Tk()
    popup.geometry("400x200")
    popup.title("TOP CATEGORY CREATOR")

    label = tk.Label(popup, text="Select an option:")
    label.grid(row=0, column=0, columnspan=2)

    button1 = tk.Button(popup, text="Create Using Headers", command=category_headers)
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2 = tk.Button(popup, text="Create 1 HEADER", command=category_1_header)
    button2.grid(row=2, column=0, padx=10, pady=10)

    button3 = tk.Button(popup, text="Create NO Headers", command=category_no_headers)
    button3.grid(row=3, column=0, padx=10, pady=10)

    popup.mainloop()

# Show the pop-up window
show_popup()