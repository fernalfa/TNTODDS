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
    print(f"Processing: {game}")
    pyautogui.moveTo(3300,-30,1)
    pyautogui.doubleClick()
    pyautogui.press("del")
    pyautogui.write(str(game))
    pyautogui.press("enter")
    pyautogui.moveTo(3757,140, 1)
    pyautogui.click()
    move_and_click(x_coordinate, y_coordinate,1)
    pyautogui.moveTo(3450,465,1)
    pyautogui.click()
    move_and_click(x_coordinate, y_coordinate)
    pyautogui.move(-230,315,1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('esc')
    print(f"Processed Successfully")
    print(f"*****************************")
    time.sleep(2)

