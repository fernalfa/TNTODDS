import time
import pyautogui
time.sleep(5)
count = 0


skip = 700





# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()
lines = data.strip().split('\n')

def jump():
    pyautogui.press('down', presses = skip)
    print("GAME SKIPPED")


for line in lines:
    if line == "SKIP":
        jump()  # Call the skip() function
        continue

    if line.startswith('+'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
    elif line.startswith('-') or line.startswith('−'):
        value = int(line)
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1





