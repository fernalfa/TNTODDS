import pyautogui
import time
time.sleep(5)

# Example usage:
# Replace the coordinates (x, y) with the desired screen coordinates
# Note: The coordinates are specific to your screen resolution, adjust accordingly.
x_coordinate = 3750
y_coordinate = 150


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
    print("click")
    # pyautogui.click()  # Perform a mouse click



pyautogui.click()
move_and_click(x_coordinate, y_coordinate, delay=1.5)
pyautogui.click()
pyautogui.moveTo(3450,465)
pyautogui.click()
move_and_click(x_coordinate, y_coordinate, delay=1.5)
pyautogui.click()
pyautogui.move(-230,315)
pyautogui.click()
pyautogui.press('esc')

