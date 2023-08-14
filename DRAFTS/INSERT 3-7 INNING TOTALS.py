text = """
Sun 13 Aug
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
-120
U 5.5
-120
O 6.5
-135
U 6.5
-105
O 5.5
-135
U 5.5
-105
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
-135
U 6.5
-105
O 7.5
-115
U 7.5
-125
O 7.5
-115
U 7.5
-125
Run Line
0.0
+100
0.0
-140
0.0
+115
0.0
-155
0.0
-105
0.0
-135
0.0
+105
0.0
-145
0.0
+100
0.0
-140
0.0
+170
0.0
-220
0.0
-140
0.0
+100
0.0
+115
0.0
-155
0.0
-140
0.0
+100
0.0
+115
0.0
-155
0.0
-125
0.0
-115
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
import pyautogui
import time
time.sleep(3)

# Extract values between "Total" and "Run Line"
total_values = text.split("Total\n")[1].split("Run Line")[0].strip()

# Split the values into lines
total_lines = total_values.split("\n")

# Create a list to store the formatted results
formatted_result = []

# Iterate over the lines and format the values
for line in total_lines:
    line = line.strip()
    if line.startswith("O") or line.startswith("U"):
        formatted_result.append([line.split()[0], float(line.split()[1])])
    else:
        formatted_result.append([line])

# Assign the formatted result to the data variable
data = formatted_result

# Define the specific functions and the function under O and U lines

def specific_function(value):
    # Replace this with your specific function logic
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(o_value))
    pyautogui.press('enter')

def function_under_u(number):
    # Replace this with your function logic for the number under O line
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(f_value))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')

def function_under_o(number):
    # Replace this with your function logic for the number under U line
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.write(str(u_value))
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.press('down')

# Process the data

i = 0
while i < len(data):
    o_value = data[i][1]
    u_value = data[i + 1][0]  # Get the number from the second line
    f_value = data[i + 3][0]  # Get the number from the fourth line

    if float(f_value) < float(u_value):
        specific_function(o_value)
        function_under_u(f_value)  # Use the number from the fourth line
    else:
        specific_function(o_value)
        function_under_o(u_value)  # Use the number from the second line

    i += 4