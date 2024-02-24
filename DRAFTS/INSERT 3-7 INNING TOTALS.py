with open('../0.INFO', 'r') as file:
    text = file.read()


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