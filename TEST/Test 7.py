import pyautogui
import time

# Your list of values
values = [
    -1200, -1200, -1200, -700, -600, -600, -500, -500, -450, -450,
    -400, -334, -334, -334, -334, -334, -334, -334, -334, -300, -300,
    -275, -275, -250, -225, -225, -225, -225, -225, -225, -200, -200,
    -200, -200, -188, -175
]

# Delay before starting
time.sleep(5)

# Loop through the values
for value in values:
    # Press Enter
    pyautogui.press('enter')
    # Type the current value
    pyautogui.typewrite(str(value))
    # Press Enter again
    pyautogui.press('enter')
    # Press Down key three times
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')