import time
import pyautogui
time.sleep(3)  # Starting delay

# Read player info from text file
with open('0.INFO', 'r') as file:
    player_info = file.readlines()

# Iterate through player info
for player in player_info:
    player = player.strip()  # Remove leading/trailing whitespaces

    pyautogui.typewrite(player)
    pyautogui.press('tab')
    pyautogui.typewrite('-150')
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')

    print(player)

    # Add any additional logic or actions you need here
    time.sleep(1)  # Add a delay if needed between iterations


