import time
import pyautogui

# Sleep for 3 seconds before starting to type
time.sleep(3)

# Define the path to your INFO file
info_file_path = 'C:\Users\clerk3\PycharmProjects\TNTODDS\INFO'

# Open the INFO file for reading
with open(info_file_path, 'r') as info_file:
    lines = info_file.readlines()

# Define your data and settings
rotation = 5003241
description = " TO MAKE MLB 2024 PLAYOFFS"

# Function to type text with a delay
def slow_type(text, delay=0.001):
    for char in text:
        pyautogui.typewrite(char, interval=delay)

# Iterate through the lines in the INFO file
for line in lines:
    player_name = line.strip()  # Remove leading/trailing whitespace
    slow_type(player_name)  # Type player_name with a delay
    slow_type(description)  # Type description with a delay
    pyautogui.press('tab', presses=1)
    pyautogui.press('backspace', presses=8)
    slow_type(str(rotation))  # Type rotation with a delay
    pyautogui.press('tab', presses=1)
    slow_type(player_name)  # Type player_name again with a delay
    slow_type(" YES MAKE PLAYOFFS")  # Type the next message with a delay
    pyautogui.press('enter')
    slow_type(player_name)  # Type player_name again with a delay
    slow_type(" NO MAKE PLAYOFFS")  # Type the next message with a delay
    pyautogui.press('tab', presses=1)
    pyautogui.press('enter', presses=2)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace', presses=200)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace', presses=80)


    print(player_name)
    rotation += 10
