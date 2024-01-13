import pyautogui
from tqdm import tqdm
import time

# Example usage:
# Replace the coordinates (x, y) with the desired screen coordinates
# Note: The coordinates are specific to your screen resolution, adjust accordingly.
x_coordinate = 3750
y_coordinate = 255
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
    pyautogui.moveTo(3300,60,1)
    pyautogui.doubleClick()
    pyautogui.press("del")
    pyautogui.write(str(game))
    pyautogui.press("enter")
    # Enter game
    pyautogui.moveTo(3033,251, 1)
    time.sleep(DELAY/3)
    pyautogui.click()
    # Hit STOP button
    time.sleep(3)
    move_and_click(x_coordinate, y_coordinate,1)
    pyautogui.moveTo(3450,570,1)
    pyautogui.click()
    time.sleep(DELAY)
    # Hit START button
    move_and_click(x_coordinate, y_coordinate)
    pyautogui.move(-230,315,1)
    pyautogui.click()
    print(f"{DELAY} SECONDS TO CANCEL IF NEEDED")
    time.sleep(DELAY)
    pyautogui.press('esc')
    # Exit Game ID
