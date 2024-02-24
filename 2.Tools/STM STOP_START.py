import pyautogui
from tqdm import tqdm
import time

# Example usage:
# Replace the coordinates (x, y) with the desired screen coordinates
# Note: The coordinates are specific to your screen resolution, adjust accordingly.
x_coordinate = 3790
y_coordinate = 135
DELAY = 10

# Read game IDs from the file
game_ids_file_path = '../0.INFO'
with open(game_ids_file_path, 'r') as file:
    data = file.read()
    games = [int(game_id) for game_id in data.split()]


def move(x, y, delay=0.5):
    """
    Move the mouse to the specified (x, y) coordinates and perform a click after a specified delay.
    """
    pyautogui.moveTo(x, y, duration=0.5)  # Move the mouse to the specified coordinates
    time.sleep(delay)  # Wait for the specified delay (in seconds)

def move_and_click(x, y, delay=0.5):
    """
    Move the mouse to the specified (x, y) coordinates and perform a click after a specified delay.
    """
    pyautogui.moveTo(x, y, duration=0.5)  # Move the mouse to the specified coordinates
    time.sleep(delay)  # Wait for the specified delay (in seconds)
    pyautogui.click()  # Perform a mouse click


# Modify the loop to use tqdm for the progress bar
for game in tqdm(games, desc="Processing games"):
    # Rest of your code within the loop...
    print(f"Processing: {game}")
    pyautogui.moveTo(3300,-40,1)
    pyautogui.doubleClick()
    pyautogui.press("del")
    pyautogui.write(str(game))
    pyautogui.press("enter")
    # Enter game
    pyautogui.moveTo(3030,150, 1)
    pyautogui.click()
    time.sleep(3)
    move_and_click(x_coordinate, y_coordinate,1)
    pyautogui.moveTo(3450,475,1)
    time.sleep(1)
    pyautogui.click() # Hit START button
    time.sleep(DELAY)
    move_and_click(x_coordinate, y_coordinate)
    pyautogui.move(-280,325,1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.press('esc')
    # Exit Game ID
    print(f"Processed Successfully")
    print(f"***********")