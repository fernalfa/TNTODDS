import time
import pyautogui
time.sleep(5)
def jump():
    pyautogui.press('down', presses = skip)
    pyautogui.press('down')
    pyautogui.press('down')
    print("GAME SKIPPED")


# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()
lines = data.strip().split('\n')


# Initialize variables
count = 0
skip = 10       # You can adjust the skip value as needed



for line_number, line in enumerate(lines, start=1):
    if line == "SKIP":
        jump()  # Call the jump() function
        continue
    if line.startswith('+'):
        value = int(line[1:])
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        print(f"Processing line: {line_number} / Total lines: {len(lines)}")
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
    elif line.startswith('-') or line.startswith('−'):
        value = int(line)
        if value > 10000:
            value = 10000
        pyautogui.press('enter')
        pyautogui.write(str(value))
        pyautogui.press('enter')
        pyautogui.press('down')
        print(f"Processing line: {line_number} / Total lines: {len(lines)}")
        count += 1
        if count % skip == 0:
            pyautogui.press('down')
            pyautogui.press('down')
