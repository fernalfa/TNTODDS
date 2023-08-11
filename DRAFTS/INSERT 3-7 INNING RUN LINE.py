import re
import pyautogui
import time
time.sleep(5)

with open('../0.INFO', 'r') as file:
    data = file.read()


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