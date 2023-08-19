import pyautogui
import time

# Example usage:
# Replace the coordinates (x, y) with the desired screen coordinates
# Note: The coordinates are specific to your screen resolution, adjust accordingly.
x_coordinate = 3750
y_coordinate = 150


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



for game in games:
    # Enter Game ID on search bar
    print(f"Processing: {game}")
    pyautogui.moveTo(3300,-40,1)
    pyautogui.doubleClick()
    pyautogui.press("del")
    pyautogui.write(str(game))
    pyautogui.press("enter")
    # Enter game
    pyautogui.moveTo(3757,140, 1)
    pyautogui.click()
    # Hit STOP button
    move_and_click(x_coordinate, y_coordinate,1)
    pyautogui.moveTo(3450,465,1)
    pyautogui.click()
    # Hit START button
    move_and_click(x_coordinate, y_coordinate)
    pyautogui.move(-230,315,1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('esc')
    # Exit Game ID
    print(f"Processed Successfully")
    print(f"*****************************")

