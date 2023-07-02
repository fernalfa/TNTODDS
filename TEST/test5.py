import re
import time
import pyautogui

time.sleep(3)

# First code
data = """09:10 PM
1927
Detroit Tigers
B. White -R
U 32
+105
1928
Colorado Rockies
P. Lambert -R
O 32
-155
10:07 PM
1929
Arizona Diamondbacks
R. Nelson -R
O 28½
-135
1930
Los Angeles Angels
T. Anderson -L
U 28½
+105
"""

order_list = ['ARIZONA DIAMONDBACKS', 'LOS ANGELES ANGELS', 'DETROIT TIGERS', 'COLORADO ROCKIES']

matches = re.findall(r"\d{4}\n(.*?)\n.*?\n([UO] \d+(?:½)?)\n(-?\d+)", data, re.DOTALL)

# Create a dictionary to store the matches by team name
matchups_by_team = {match[0].upper(): match for match in matches}

# Extracted data for PyAutoGUI actions
pyautogui_data = ""

# Iterate over the teams in the specified order and retrieve the corresponding match
for team in order_list:
    team_match = matchups_by_team.get(team.upper())
    if team_match:
        value = team_match[1].split(' ')[1]
        letter = team_match[1].split(' ')[0] if team_match[1] else ''
        negative_value_line = team_match[2]

        pyautogui_data += f"Matchup: {team_match[0]}\n"
        pyautogui_data += f"Value: {value}\n"
        pyautogui_data += f"Letter: {letter}\n"
        pyautogui_data += f"Negative Value Line: {negative_value_line}\n\n"

# Second code
# Split the data into individual matchups
matchups = re.split(r"\n\s*\n", pyautogui_data.strip())

for matchup in matchups:
    # Extract the values using regex
    value = re.search(r"Value:\s*([0-9½]+)", matchup).group(1)
    letter = re.search(r"Letter:\s*([OU])", matchup).group(1)
    negative_value_line = re.search(r"Negative Value Line:\s*(-?\d+)", matchup).group(1)

    # Press Enter
    pyautogui.press('enter')

    # Write Value and press Enter
    pyautogui.write(value)
    pyautogui.press('enter')

    # Check the letter and perform corresponding actions
    if letter == "O":
        # Press Left, Enter, write Negative Value Line, Enter
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(negative_value_line)
        pyautogui.press('enter')
        pyautogui.press('left')
    elif letter == "U":
        # Press Down, Left, Enter, write Negative Value Line, Enter
        pyautogui.press('down')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.write(negative_value_line)
        pyautogui.press('enter')
        pyautogui.press('left')

    # Perform common actions
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')