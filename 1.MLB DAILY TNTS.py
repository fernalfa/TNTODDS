import time
import pyautogui

time.sleep(3)
skip = 4

data = '''
ABC

'''

lines = data.strip().split('\n')
count = 0
for line in lines:
    if line.startswith('+'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('-') or line.startswith('−'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write('-')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')