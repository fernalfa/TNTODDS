import pyautogui
import time

def modify_values(data):
    modified_values = []
    for value in data:
        modified_values.extend([value + 0.5, value - 0.5])
    return modified_values

# Totales de MLB
data = [8.5, 9]


modified_data = modify_values(data)

time.sleep(3)

for value in modified_data:
    print(value)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write(str(value))
    time.sleep(1)  # Add a slight delay after writing the value
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')

