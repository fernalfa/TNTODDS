import re
import time
import pyautogui
time.sleep(3)

# COPIAR Y PEGAR DE BOOKMAKER
data = '''


'''

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

    if i + 1 in [2, 6, 14]:  # Execute the function after 2, 4, and 9 numbers
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')