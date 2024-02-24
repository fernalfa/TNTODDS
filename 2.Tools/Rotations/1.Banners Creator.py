import re
import time
import pyautogui
from patterns import replace_patterns, exclude_patterns
import pyautogui
import tkinter as tk
from tkinter.simpledialog import askinteger
import os
from tqdm import  tqdm

def slowtype(text, delay=0.01):
    for char in text:
        pyautogui.write(char, interval=delay)

def nba_Points():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                print(partes)
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                time.sleep(0.1)
                slowtype(str(resultado))

                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER POINTS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Assists():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER ASSISTS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Rebounds():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER REBOUNDS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Performance():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - PLAYER TRIPLE DOUBLE \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_AssistsAndRebounds():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER ASSISTS AND REBOUNDS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_PointsAndAssists():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER POINTS AND ASSISTS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_PointsAssistsAndRebounds():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER POINTS, ASSISTS AND REBOUNDS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_PointsAndRebounds():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER POINTS AND REBOUNDS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_PointsMade():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER 3 POINTS MADE \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Blocks():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER BLOCKS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Steals():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER STEALS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_StealsAndBlocks():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER STEALS AND BLOCKS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nba_Turnovers():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                slowtype(str(resultado))
                time.sleep(0.1)
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER TURNOVERS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()



def nhl_ShotsOnGoal():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    temp_name = " VS "
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                # Apply replacements
                if len(temp_name.split()) == 1:
                    pyautogui.write((str(int(money_line))))
                    pyautogui.press('tab', presses=3)
                    time.sleep(0.1)
                    print("Before:", game_name)
                    print("game_name tiene 1 miembro.")
                    # Realizar acciones si tiene 1 miembro
                    temp_name = game_name + " VS "
                    game_name = None

                elif len(temp_name.split()) == 2:
                    temp_name += game_name
                    print(temp_name)
                    for pattern, replacement in replace_patterns:
                        temp_name = pattern.sub(replacement, temp_name)
                    partes = temp_name.split(" VS ")
                    # Get the parts in the desired format
                    resultado = f'{partes[1]} @ {partes[0]}'
                    print("Final result:", resultado)
                    slowtype(str(resultado))
                    time.sleep(0.1)
                    pyautogui.hotkey('alt', 'o')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.press('del')
                    # Reset the game name variable for the next game
                    game_name = None
                    temp_name = " VS "
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'(.+?) \((.+?)\) - TOTAL SHOTS ON GOAL', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(2).strip()

def nhl_PowerPlay():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                print(partes)
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                time.sleep(0.1)
                slowtype(str(resultado))
                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nhl_Assists():
    time.sleep(0.1)
    # Open the .info file
    with open('../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                pyautogui.write((str(int(money_line))))
                pyautogui.press('tab', presses=3)
                time.sleep(0.1)
                print("Before:", game_name)
                # Apply replacements
                for pattern, replacement in replace_patterns:
                    game_name = pattern.sub(replacement, game_name)
                partes = game_name.split(" VS ")
                print(partes)
                # Get the parts in the desired format
                resultado = f'{partes[1]} @ {partes[0]}'
                print("Final result:", resultado)
                time.sleep(0.1)
                slowtype(str(resultado))

                pyautogui.hotkey('alt', 'o')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.hotkey('shift', 'tab')
                pyautogui.press('del')
                # Reset the game name variable for the next game
                game_name = None
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'.+? - UNDER/OVER PLAYER ASSISTS \((.+?)\) -$', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(1).strip()

def nhl_Points():
    time.sleep(0.1)
    # Open the .info file
    with open('../../../0.INFO', 'r') as file:
        data = file.read()
    # Split the text into lines
    lines = data.strip().split('\n')
    # Initialize variables for the game name and money line
    game_name = None
    money_line = None
    temp_name = " VS "
    printed_games = set()  # Set to store already printed game names
    # Iterate over the lines
    for line in lines:
        # Look for the money line
        money_match = re.match(r'(\d+)$', line)
        if money_match:
            money_line = money_match.group(1).strip()
            # If the money line was found before the game name and the game has not been printed before, print them
            if game_name and money_line and game_name not in printed_games:
                print(f'{game_name}\t{money_line}')
                printed_games.add(game_name)  # Add the game name to the set of printed games
                # Apply replacements
                if len(temp_name.split()) == 1:
                    pyautogui.write((str(int(money_line))))
                    pyautogui.press('tab', presses=3)
                    time.sleep(0.1)
                    print("Before:", game_name)
                    print("game_name tiene 1 miembro.")
                    # Realizar acciones si tiene 1 miembro
                    temp_name = game_name + " VS "
                    game_name = None

                elif len(temp_name.split()) == 2:
                    temp_name += game_name
                    print(temp_name)
                    for pattern, replacement in replace_patterns:
                        temp_name = pattern.sub(replacement, temp_name)
                    partes = temp_name.split(" VS ")
                    # Get the parts in the desired format
                    resultado = f'{partes[1]} @ {partes[0]}'
                    print("Final result:", resultado)
                    slowtype(str(resultado))
                    time.sleep(0.1)
                    pyautogui.hotkey('alt', 'o')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.hotkey('shift', 'tab')
                    pyautogui.press('del')
                    # Reset the game name variable for the next game
                    game_name = None
                    temp_name = " VS "
        # Look for the game name
        # (r'.+? - UNDER/OVER PLAYER POWERPLAY POINTS \((.+?)\) -$', line) --THIS FOR LSPORTS PLAYER PROPS
        # (r'(.+?) \((.+?)\) - TOTAL POINTS', line) --THIS FOR ALVARO PLAYER PROPS
        game_match = re.match(r'(.+?) \((.+?)\) - TOTAL POINTS', line)
        if game_match:
            # 1 FOR LSPORTS PLAYER PROPS / 2 FOR ALVARO PLAYER PROPS
            game_name = game_match.group(2).strip()



def execute_selected():
    time.sleep(4)
    selected_functions = [
        ("NBA POINTS", nba_Points),
        ("NBA ASSISTS", nba_Assists),
        ("NBA REBOUNDS", nba_Rebounds),
        ("NBA PERFORMANCE", nba_Performance),
        ("NBA ASSISTS AND REBOUNDS", nba_AssistsAndRebounds),
        ("NBA POINTS AND ASSISTS", nba_PointsAndAssists),
        ("NBA POINTS, ASSISTS AND REBOUNDS", nba_PointsAssistsAndRebounds),
        ("NBA POINTS AND REBOUNDS", nba_PointsAndRebounds),
        ("NBA 3 POINTS MADE", nba_PointsMade),
        ("NBA BLOCKS", nba_Blocks),
        ("NBA STEALS", nba_Steals),
        ("NBA STEALS AND BLOCKS", nba_StealsAndBlocks),
        ("NBA TURNOVERS", nba_Turnovers),
        ("NHL SHOTS", nhl_ShotsOnGoal),
        ("NHL POWERPLAY", nhl_PowerPlay),
        ("NHL ASSISTS", nhl_Assists),
        ("NHL POINTS", nhl_Points)
    ]

    for function_name, function in selected_functions:
        if checkboxes[function_name].get():
            function()

def show_popup():
    global checkboxes
    popup = tk.Tk()
    popup.geometry("700x350")
    popup.title("BANNER CREATOR - TOOL")

    label = tk.Label(popup, text="Select options to execute:")
    label.grid(row=0, column=0, columnspan=3)

    checkboxes = {}
    row_counter = 1
    col_counter = 0

    functions = [
        "NBA POINTS", "NBA ASSISTS", "NBA REBOUNDS", "NBA PERFORMANCE",
        "NBA ASSISTS AND REBOUNDS", "NBA POINTS AND ASSISTS",
        "NBA POINTS, ASSISTS AND REBOUNDS", "NBA POINTS AND REBOUNDS",
        "NBA 3 POINTS MADE", "NBA BLOCKS", "NBA STEALS", "NBA STEALS AND BLOCKS",
        "NBA TURNOVERS", "NHL SHOTS", "NHL POWERPLAY", "NHL ASSISTS", "NHL POINTS"
    ]

    for function_name in functions:
        checkboxes[function_name] = tk.BooleanVar()
        checkbox = tk.Checkbutton(popup, text=function_name, variable=checkboxes[function_name])
        checkbox.grid(row=row_counter, column=col_counter, padx=10, pady=10, sticky=tk.W)

        col_counter += 1
        if col_counter > 2:
            col_counter = 0
            row_counter += 1

    execute_button = tk.Button(popup, text="Execute Selected", command=execute_selected)
    execute_button.grid(row=row_counter + 1, column=0, columnspan=3, pady=10)
    popup.mainloop()
# Ejecutar la interfaz
show_popup()