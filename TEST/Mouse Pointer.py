import pyautogui
import time

# Example usage:
# Replace the coordinates (x, y) with the desired screen coordinates
# Note: The coordinates are specific to your screen resolution, adjust accordingly.
x_coordinate = 1800
y_coordinate = 380


def move(x, y, delay=1.0):
    """
    Move the mouse to the specified (x, y) coordinates and perform a click after a specified delay.
    """
    pyautogui.moveTo(x, y, duration=0.5)  # Move the mouse to the specified coordinates
    time.sleep(delay)  # Wait for the specified delay (in seconds)

def move_and_click(x, y, delay=1.0):
    """
    Move the mouse to the specified (x, y) coordinates and perform a click after a specified delay.
    """
    pyautogui.moveTo(x, y, duration=0.5)  # Move the mouse to the specified coordinates
    time.sleep(delay)  # Wait for the specified delay (in seconds)
    print("click")
    # pyautogui.click()  # Perform a mouse click



move_and_click(x_coordinate, y_coordinate, delay=1.5)
move((x_coordinate - 85) , y_coordinate, delay=1.5)
