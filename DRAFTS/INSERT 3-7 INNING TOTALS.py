text = """
Mon 07 Aug
16:10
LA Dodgers
SD Padres
2
18:40
MIA Marlins
CIN Reds
4
18:40
MIN Twins
DET Tigers
4
18:40
WAS Nationals
PHI Phillies
5
19:05
ATL Braves
PIT Pirates
5
19:10
CHI Cubs
NY Mets
5
19:10
KC Royals
BOS Red Sox
4
19:10
TOR Blue Jays
CLE Guardians
4
20:10
COL Rockies
MIL Brewers
4
20:10
NY Yankees
CHI White Sox
4
21:38
SF Giants
LA Angels
4
21:40
TEX Rangers
OAK Athletics
4
Total
O 7.5
-110
U 7.5
-130
O 7.5
-130
U 7.5
-110
O 6.5
+105
U 6.5
-145
O 7.5
-135
U 7.5
-105
O 6.5
-120
U 6.5
-120
O 6.5
-135
U 6.5
-105
O 7.5
-120
U 7.5
-120
O 6.5
-120
U 6.5
-120
O 6.5
-120
U 6.5
-120
O 5.5
-130
U 5.5
-110
O 6.5
-105
U 6.5
-135
O 6.5
-135
U 6.5
-105
Run Line
0.0
+115
0.0
-155
0.0
-160
0.0
+120
0.0
-190
0.0
+145
0.0
+195
0.0
-250
0.0
-340
0.0
+250
0.0
-120
0.0
-120
0.0
+155
0.0
-205
0.0
-155
0.0
+115
0.0
+200
0.0
-260
0.0
-190
0.0
+145
0.0
-130
0.0
-110
0.0
-230
0.0
+180
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