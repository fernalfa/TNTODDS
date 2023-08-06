import re
import time
import pyautogui
time.sleep(3)

with open('../0.INFO', 'r') as file:
    data = file.read()

numbers = re.findall(r'[+-]?\d{2,}', data)

for i, num in enumerate(numbers):
    if num.startswith('-'):  # Write the sign for negative numbers
        sign = '-'
    else:
        sign = ''
    num = sign + num.lstrip('+-')  # Remove the sign from the number if it's positive
    pyautogui.press('enter')
    pyautogui.write(num)
    pyautogui.press('enter')
    pyautogui.press('down')

    if i + 1 in [2, 8, 21, 25]:  # Execute the function after 2, 4, and 9 numbers
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')