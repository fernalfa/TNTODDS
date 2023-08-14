import pyautogui
import time
time.sleep(5)


# Define the two functions
def process_lowest_as_first(lowest_value):
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(lowest_value))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.press('down')
    print("Processing lowest as first:", lowest_value)
    # Your logic for the first case goes here


def process_lowest_as_second(lowest_value):
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(lowest_value))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')
    print("Processing lowest as second:", lowest_value)
    # Your logic for the second case goes here


data = """Sun 13 Aug
12:05
DET Tigers
BOS Red Sox
3
13:35
CIN Reds - Game 1
PIT Pirates - Game 1
13:35
MIN Twins
PHI Phillies
3
13:35
OAK Athletics
WAS Nationals
3
13:37
CHI Cubs
TOR Blue Jays
3
13:40
CLE Guardians
TB Rays
4
13:40
NY Yankees
MIA Marlins
3
14:10
LA Angels
HOU Astros
4
14:10
MIL Brewers
CHI White Sox
3
16:05
TEX Rangers
SF Giants
3
16:10
BAL Orioles
SEA Mariners
3
16:10
COL Rockies
LA Dodgers
4
16:10
SD Padres
ARI Diamondbacks
3
18:05
CIN Reds - Game 2
PIT Pirates - Game 2
19:10
ATL Braves
NY Mets
3
Total
O 6.5
-135
U 6.5
-105
O 6.5
-130
U 6.5
-110
O 6.5
-120
U 6.5
-120
O 7.5
-120
U 7.5
-120
O 7.5
-105
U 7.5
-135
O 5.5
-135
U 5.5
-105
O 5.5
-115
U 5.5
-125
O 6.5
-135
U 6.5
-105
O 6.5
+105
U 6.5
-145
O 6.5
+100
U 6.5
-140
O 6.5
-110
U 6.5
-130
O 6.5
-130
U 6.5
-110
O 6.5
-140
U 6.5
+100
O 7.5
-115
U 7.5
-125
O 7.5
-120
U 7.5
-120
Run Line
0.0
-105
0.0
-135
0.0
+110
0.0
-150
0.0
-110
0.0
-130
0.0
+105
0.0
-145
0.0
-105
0.0
-135
0.0
+170
0.0
-220
0.0
-145
0.0
+105
0.0
+110
0.0
-150
0.0
-145
0.0
+105
0.0
+115
0.0
-155
0.0
-120
0.0
-120
0.0
+285
0.0
-380
0.0
-145
0.0
+105
0.0
-115
0.0
-125
0.0
-145
0.0
+105
"""

lines = data.split('\n')  # Split the data into lines
run_line_index = lines.index("Run Line")  # Find the index of the line containing "Run Line"

extracted_values = []

# Iterate through the lines after the "Run Line" line and extract values with '+' or '-' sign
for line in lines[run_line_index + 1:]:
    if line.strip():  # Ignore empty lines
        if line.startswith('+') or line.startswith('-'):
            extracted_values.append(int(line.strip()))

# Compare the values in pairs, get the lowest value and call the appropriate function
for i in range(0, len(extracted_values), 2):
    value1 = extracted_values[i]
    value2 = extracted_values[i + 1]

    if value1 < 0 and value2 < 0:
        lowest_value = min(value1, value2)
        lowest_position = "first" if lowest_value == value1 else "second"
    elif value1 >= 0 and value2 >= 0:
        lowest_value = min(value1, value2)
        lowest_position = "first" if lowest_value == value1 else "second"
    else:
        if value1 < value2:
            lowest_value = value1
            lowest_position = "first"
        else:
            lowest_value = value2
            lowest_position = "second"

    print("Pair:", value1, value2)
    print("Lowest value:", lowest_value)
    print("Lowest value is the", lowest_position, "value of the pair")

    if lowest_position == "first":
        process_lowest_as_first(lowest_value)
    else:
        process_lowest_as_second(lowest_value)