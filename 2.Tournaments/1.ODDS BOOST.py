import re
# Use the replace_patterns and exclude_patterns lists as needed in your main script
from patterns import replace_patterns, exclude_patterns
from tqdm import tqdm
import time
import tkinter as tk
import pyautogui

SURCHARGE_PERCENTAGE = 10  # 10% surcharge

# Function to extract the key for sorting based on "/TEAM WINS"
def sort_key(line_tuple):
    line = line_tuple[1]  # Get the line of text from the tuple
    parts = line.split('/')

    # Check if there are at least two parts (e.g., "1+GOALS" and "LAG WINS")
    if len(parts) >= 2:
        # Return the last part for sorting (e.g., "LAG WINS")
        return parts[-1].strip()
    else:
        # Handle the case where the line does not have the expected structure
        # You can choose to return a default value or handle it as needed
        return line.strip()

def enterodd(odd):
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(odd)))
    pyautogui.press('enter')
    pyautogui.press('down')

def deleteodd():
    pyautogui.press('enter')
    pyautogui.press('del')
    pyautogui.press('enter')
    pyautogui.press('down')

def extract_list():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAIBET.TXT', 'r', encoding='utf-8') as file:
        data2 = file.read().upper()
        lines = file.readlines()
        for pattern, replacement in replace_patterns:
            data2 = pattern.sub(replacement, data2)
    data3 = data2.strip().split('\n')
    names = []
    list3 = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)
    print(names)

    # Step 3: Process odds data and calculate adjusted odds
    # Open the text file
    with open('../DATAPROVIDER.TXT', 'r', encoding='utf-8') as file:
        data = file.read().upper()
        for pattern, replacement in replace_patterns:
            data = pattern.sub(replacement, data)
    lines = data.strip().split('\n')

    list1 = []
    list2 = []
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


    for line_number, line in enumerate(lines, start=1):
        if any(pattern.match(line) for pattern in exclude_patterns):
            continue
        char_count = len(line.strip())
        list1.append((line_number, line))  # Store line number and line
        if char_count > 50:
            list2.append((line_number, line, char_count))  # Store line number, line, and char_count

    print("CONTENDERS TO FIX:")
    print("****:")
    for line_number, line, char_count in list2:
        print(f"Line {line_number}: {line} ({char_count} characters)")


    print("\n**********:")
    print("PLAYER SPECIALS LIST EXTRACTED")
    print("*********:")

    # Create a set to store lines that have been printed
    printed_lines = set()

    for line_number, line_tuple in enumerate(list1):
        line = line_tuple[1]

        # Check if the line is a string, not empty, and not too long
        if isinstance(line, str) and line.strip() and len(line) < 50:
            # Check if the line has not been printed before
            if line not in list1:
                # Print the line
                print(line)
                # Add the line to the set of printed lines
                printed_lines.add(line)

def sorted_list_special_props():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAPROVIDER.TXT', 'r', encoding='utf-8') as file:
        data2 = file.read().upper()
        lines = file.readlines()
        for pattern, replacement in replace_patterns:
            data2 = pattern.sub(replacement, data2)
    data3 = data2.strip().split('\n')
    names = []
    list3 = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)
    print(names)

    # Step 3: Process odds data and calculate adjusted odds
    # Open the text file
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAPROVIDER.TXT', 'r', encoding='utf-8') as file:
        data = file.read().upper()
        for pattern, replacement in replace_patterns:
            data = pattern.sub(replacement, data)
    lines = data.strip().split('\n')

    list1 = []
    list2 = []
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


    for line_number, line in enumerate(lines, start=1):
        if any(pattern.match(line) for pattern in exclude_patterns):
            continue
        char_count = len(line.strip())
        list1.append((line_number, line))  # Store line number and line
        if char_count > 50:
            list2.append((line_number, line, char_count))  # Store line number, line, and char_count

    print("CONTENDERS TO FIX:")
    print("****:")
    for line_number, line, char_count in list2:
        print(f"Line {line_number}: {line} ({char_count} characters)")

    # Assuming list1 is a list of tuples where the string to be sorted is in the second element (index 1)
    sorted_list1 = sorted(list1, key=lambda x: x[1])

    print("\n**********:")
    print("PLAYER SPECIALS LIST (A to Z):")
    print("*********:")

    # Create a set to store lines that have been printed
    printed_lines = set()

    for line_number, line_tuple in enumerate(sorted_list1):
        line = line_tuple[1]

        # Check if the line is a string, not empty, and not too long
        if isinstance(line, str) and line.strip() and len(line) < 50:
            # Check if the line has not been printed before
            if line not in printed_lines:
                # Print the line
                print(line)
                # Add the line to the set of printed lines
                printed_lines.add(line)

def sorted_list_player_doubles():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAIBET.TXT', 'r', encoding='utf-8') as file:
        data2 = file.read().upper()
        lines = file.readlines()
        for pattern, replacement in replace_patterns:
            data2 = pattern.sub(replacement, data2)
    data3 = data2.strip().split('\n')
    names = []
    list3 = []

    for line in lines:
        line = line.strip()
        if line.isdigit() or line.startswith('+') or line.startswith('-'):
            continue
        if line:
            names.append(line)
    print(names)

    # Step 3: Process odds data and calculate adjusted odds
    # Open the text file
    with open('../DATAPROVIDER.txt', 'r', encoding='utf-8') as file:
        data = file.read().upper()
        for pattern, replacement in replace_patterns:
            data = pattern.sub(replacement, data)
    lines = data.strip().split('\n')

    list1 = []
    list2 = []
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

    for line_number, line in enumerate(lines, start=1):
        if any(pattern.match(line) for pattern in exclude_patterns):
            continue
        char_count = len(line.strip())
        list1.append((line_number, line))  # Store line number and line
        if char_count > 50:
            list2.append((line_number, line, char_count))  # Store line number, line, and char_count

    print("CONTENDERS TO FIX:")
    print("****:")
    for line_number, line, char_count in list2:
        print(f"Line {line_number}: {line} ({char_count} characters)")


    # Assuming list1 is a list of tuples where the string to be sorted is in the second element (index 1)
    sorted_list1 = sorted(list1, key=lambda x: x[1])

    print("************:")
    print("SORTED PLAYER DOUBLES:")
    print("************:")

    # Create a set to store lines that have been printed
    printed_lines = set()

    # Sort the list based on "/TEAM WINS"
    sorted_list1.sort(key=sort_key)

    for line_number, line_tuple in enumerate(sorted_list1):
        line = line_tuple[1]

        # Check if the line is a string, not empty, and not too long
        if isinstance(line, str) and line.strip() and len(line) < 50:
            # Check if the line has not been printed before
            if line not in printed_lines:
                # Print the line
                print(line)
                # Add the line to the set of printed lines
                printed_lines.add(line)


def missing_teams():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAIBET.TXT', 'r', encoding='utf-8') as file:
        data2 = file.read().upper()
        lines = file.readlines()
        for pattern, replacement in replace_patterns:
            data2 = pattern.sub(replacement, data2)
    data3 = data2.strip().split('\n')
    data3 = [line for line in data3 if
             line.strip() and not line.strip().isdigit()]  # Remove empty and digit lines from data3
    names = []
    list3 = []

    for line in data3:
        line = line.strip()
        if not line.startswith('+') and not line.startswith('-'):
            names.append(line)
    print(names)

    # Step 3: Process odds data and calculate adjusted odds
    # Open the text file
    with open('../DATAPROVIDER.TXT', 'r', encoding='utf-8') as file:
        data = file.read().upper()
        for pattern, replacement in replace_patterns:
            data = pattern.sub(replacement, data)
    lines = data.strip().split('\n')

    list1 = []
    list2 = []
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

    for line_number, line in enumerate(lines, start=1):
        if any(pattern.match(line) for pattern in exclude_patterns):
            continue
        char_count = len(line.strip())
        list1.append((line_number, line))  # Store line number and line
        if char_count > 50:
            list2.append((line_number, line, char_count))  # Store line number, line, and char_count

    missing_teams = []
    print("\n************:")
    print("MISSING CONTENDERS:")
    print("************:")

    for name, surcharged_odd in odds_dict.items():
        if name not in names:
            missing_teams.append(name)

    missing_teams = sorted(missing_teams)

    for team in missing_teams:
        if len(team) < 50:
            print(team)

def boosted_odds_enter():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAIBET.TXT', 'r', encoding='utf-8') as file:
        data2 = file.read().upper()
        lines = file.readlines()
        for pattern, replacement in replace_patterns:
            data2 = pattern.sub(replacement, data2)
    data3 = data2.strip().split('\n')
    data3 = [line for line in data3 if
             line.strip() and not line.strip().isdigit()]  # Remove empty and digit lines from data3
    names = []
    list3 = []

    for line in data3:
        line = line.strip()
        if not line.startswith('+') and not line.startswith('-'):
            names.append(line)
    print(names)

    # Step 3: Process odds data and calculate adjusted odds
    # Open the text file
    with open('../DATAPROVIDER.TXT', 'r', encoding='utf-8') as file:
        data = file.read().upper()
        for pattern, replacement in replace_patterns:
            data = pattern.sub(replacement, data)
    lines = data.strip().split('\n')

    list1 = []
    list2 = []
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

    for line_number, line in enumerate(lines, start=1):
        if any(pattern.match(line) for pattern in exclude_patterns):
            continue
        char_count = len(line.strip())
        list1.append((line_number, line))  # Store line number and line
        if char_count > 50:
            list2.append((line_number, line, char_count))  # Store line number, line, and char_count

    missing_teams = []
    print("\n************:")
    print("MISSING CONTENDERS:")
    print("************:")

    for name, surcharged_odd in odds_dict.items():
        if name not in names:
            missing_teams.append(name)

    missing_teams = sorted(missing_teams)

    for team in missing_teams:
        print(team)

    print("\n************:")
    print("TOURNAMENT ADJUSTED ODDS:")
    print("************:")
    time.sleep(3)
    # Assuming `names` is a list of names
    for line in tqdm(data3, desc="Progress", ncols=100):
        odd = odds_dict.get(line.strip())
        if odd is not None:
            print(f"{line}: {odd}")
            enterodd(odd)
        else:
            print(f"{line}: NONE")
            deleteodd()

def linealodds():
    # Open the 'DATAIBET' file for reading
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\DATAIBET.TXT', 'r', encoding='utf-8') as file:
        # Read the contents of the file
        text = file.read()

    # Split the text into lines
    lines = text.split('\n')

    # Iterate through each line and format it as expected
    formatted_lines = []
    for line in lines:
        last_plus_index = line.rfind('+')
        if last_plus_index != -1:
            name_part = line[:last_plus_index]
            number_part = line[last_plus_index:]
            formatted_lines.append(f"{name_part}\n{number_part}")
        else:
            formatted_lines.append(line)

    # Join the formatted lines back into a single string
    result = '\n'.join(formatted_lines)


    print("\n************:")
    print("CONTENDER ODDS:")
    print("************:")
    # Print or save the result as needed
    print(result)

def show_popup():
    popup = tk.Tk()
    popup.geometry("400x225")  # Increased window size to fit the buttons better
    popup.title("ODDS BOOSTS - PLAYER SPECIALS")

    # Create the first column of buttons
    label = tk.Label(popup, text="Select an option:")
    label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    button6 = tk.Button(popup, text="Extract LIST", command=extract_list)
    button6.grid(row=1, column=0, padx=10, pady=10)

    button4 = tk.Button(popup, text="Extract PLAYER DOUBLES (A-Z)", command=sorted_list_player_doubles)
    button4.grid(row=2, column=0, padx=10, pady=10)

    button1 = tk.Button(popup, text="Extract PLAYER SPECIALS (A-Z)", command=sorted_list_special_props)
    button1.grid(row=3, column=0, padx=10, pady=10)

    button5 = tk.Button(popup, text="Missing Teams", command=missing_teams)
    button5.grid(row=4, column=0, padx=10, pady=10)

    # Create the second column of buttons
    button2 = tk.Button(popup, text="Enter Compared Odds", command=boosted_odds_enter)
    button2.grid(row=2, column=1, padx=10, pady=10)

    button3 = tk.Button(popup, text="Transform Lineal Odds", command=linealodds)
    button3.grid(row=1, column=1, padx=10, pady=10)

    popup.mainloop()

# Show the pop-up window
show_popup()