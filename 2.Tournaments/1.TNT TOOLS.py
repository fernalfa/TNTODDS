import re
import time
from tqdm import tqdm
import pyautogui
import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import messagebox

SURCHARGE_PERCENTAGE = 10  # 10% surcharge


def slow_type(text, interval=0.01):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(interval)


def entertntplayer(name, surcharged_odd):
    slow_type(name)  # Slowly type the name
    pyautogui.press('tab')
    slow_type(str(int(surcharged_odd)))  # Slowly type the name
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')


def missing_players():
    with open('DATAIBET', 'r') as file:
        lines = file.readlines()

    names = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)

    with open('DATAPROVIDER', 'r') as file:
        data = file.read().upper()

    missing_teams = []
    print("\n************:")
    print("MISSING CONTENDERS:")
    print("************:")

    for name, surcharged_odd in odds_dict.items():
        if name not in names:
            missing_teams.append(name)

    for team in missing_teams:
        print(team)


def create_players():
    time.sleep(3)  # Adjust sleep time as needed
    with open('DATAIBET', 'r') as file:
        lines = file.readlines()

    names = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)

    with open('DATAPROVIDER', 'r') as file:
        data = file.read().upper()

    print("\n************:")
    print("CREATED CONTENDERS:")
    print("************:")

    # Create a list of names that are not in the 'names' list
    missing_names = [name for name in odds_dict.keys() if name not in names]

    for name in missing_names:
        surcharged_odd = odds_dict[name]
        try:
            print(f"Processing team: {name}, Surcharge Odd: {surcharged_odd}")
            entertntplayer(name, surcharged_odd)
        except Exception as e:
            print(f"Error processing team {name}: {str(e)}")


def players_to_delete():
    with open('DATAIBET', 'r') as file:
        lines = file.readlines()

    names = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)

    with open('DATAPROVIDER', 'r') as file:
        data = file.read()

    odds = re.findall(r'(.+)\n([-+]?\d+)', data)

    odds_dict = {}
    for name, odd in odds:
        if 100 <= int(odd) <= 110:
            surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000) * -1
        else:
            if int(odd) > 100:
                surcharged_odd = min(int(odd) - int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
            elif int(odd) < -100:
                surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
            else:
                surcharged_odd = (int(odd) * -1) * (SURCHARGE_PERCENTAGE / 100)
        odds_dict[name] = surcharged_odd

    # Create a fourth list with names having NONE odds
    print("\n************:")
    print("CONTENDERS TO BE DELETED:")
    print("************:")
    none_odds_teams = []
    for name in names:
        if odds_dict.get(name.strip()) is None:
            none_odds_teams.append(name.strip())
            print(name)


def odds_compare():
    time.sleep(5)

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

    with open('DATAPROVIDER', 'r') as file:
        data = file.read().upper()

    odds = re.findall(r'(.+)\n([-+]?\d+)', data)

    odds_dict = {}
    for name, odd in odds:
        if 100 <= int(odd) <= 110:
            surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000) * -1
        else:
            if int(odd) > 100:
                surcharged_odd = min(int(odd) - int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
            elif int(odd) < -100:
                surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
            else:
                surcharged_odd = (int(odd) * -1) * (SURCHARGE_PERCENTAGE / 100)
        odds_dict[name] = surcharged_odd

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


def list_extractor_provider():
    # Function built to extract contender list from text

    # Read the code from a text file
    with open("../2.Tournaments/DATAPROVIDER", "r") as file:  # Make sure to specify the correct file path
        text = file.read().upper()

    # Split the text into lines
    lines = text.split('\n')

    game_descriptions = []

    for line in lines:
        # Check if the line contains a game description (e.g., "CHI CUBS @ COL ROCKIES" for option 2)
        if re.match(r"^[A-Z\s'.-]+ @ [A-Z\s'.-]+", line):
            game_descriptions.append(line.strip())

        # Check if the line contains team names (e.g., "CHI CUBS" for option 1)
        elif re.match(r"^[A-Z\s'.-]+$", line):
            game_descriptions.append(line.strip())

    # Print the game descriptions
    print("\n************:")
    print("PROVIDER LIST")
    print("************:")
    for game in game_descriptions:
        print(game)


def list_extractor():
    # Function built to extract contender list from text

    # Read the code from a text file
    with open("../2.Tournaments/DATAIBET", "r") as file:
        text = file.read().upper()

    # Split the text into lines
    lines = text.split('\n')

    game_descriptions = []

    for line in lines:
        # Check if the line contains a game description (e.g., "CHI CUBS @ COL ROCKIES" for option 2)
        if re.match(r"^[A-Z\s'.-]+ @ [A-Z\s'.-]+", line):
            game_descriptions.append(line.strip())

        # Check if the line contains team names (e.g., "CHI CUBS" for option 1)
        elif re.match(r"^[A-Z\s'.-]+$", line):
            game_descriptions.append(line.strip())

    # Print the game descriptions
    print("\n************:")
    print("IN HOUSE LIST")
    print("************:")
    for game in game_descriptions:
        print(game)


def delete_contenders():
    # Create a tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to enter a number using a pop-up window
    number = askinteger("Enter Number", "Enter Times:")
    # Destroy the root window after input is received
    root.destroy()

    # Wait for 5 seconds before start
    time.sleep(5)

    def delete_contenders_with_odds():
        pyautogui.hotkey('alt', 'd')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('up')

    for _ in range(number):
        delete_contenders_with_odds()


def show_popup():
    popup = tk.Tk()
    popup.geometry("400x200")
    popup.title("TOURNAMENTS - TOOL")

    label = tk.Label(popup, text="Select an option:")
    label.grid(row=0, column=0, columnspan=2)

    button7 = tk.Button(popup, text="Extract Data List", command=list_extractor)
    button7.grid(row=1, column=0, padx=10, pady=10)

    button6 = tk.Button(popup, text="Extract Provider List", command=list_extractor_provider)
    button6.grid(row=2, column=0, padx=10, pady=10)

    button1 = tk.Button(popup, text="Check Missing Players", command=missing_players)
    button1.grid(row=3, column=0, padx=10, pady=10)

    button2 = tk.Button(popup, text="Create Missing Players", command=create_players)
    button2.grid(row=4, column=0, padx=10, pady=10)

    button3 = tk.Button(popup, text="Players to Delete", command=players_to_delete)
    button3.grid(row=1, column=1, padx=10, pady=10)

    button4 = tk.Button(popup, text="Enter Compared Odds", command=odds_compare)
    button4.grid(row=3, column=1, padx=10, pady=10)

    button5 = tk.Button(popup, text="Delete Empty Players", command=delete_contenders)
    button5.grid(row=2, column=1, padx=10, pady=10)

    popup.mainloop()


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
    data = file.read().upper()
odds = re.findall(r'(.+)\n([-+]?\d+)', data)

odds_dict = {}
for name, odd in odds:
    if 100 <= int(odd) <= 110:
        surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000) * -1
    else:
        if int(odd) > 100:
            surcharged_odd = min(int(odd) - int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
        elif int(odd) < -100:
            surcharged_odd = min(int(odd) + int(odd) * (SURCHARGE_PERCENTAGE / 100), 10000)
        else:
            surcharged_odd = (int(odd) * -1) * (SURCHARGE_PERCENTAGE / 100)
    odds_dict[name] = surcharged_odd

# Show the pop-up window
show_popup()


