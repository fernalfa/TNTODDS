import re
import time
import pyautogui

# Constants
SLEEP_DURATION = 4
LEFT_ARROW_PRESS_COUNT = 2

def slowtype(text, delay=0.01):
    for char in text:
        pyautogui.write(char, interval=delay)

def extract_rot_number(target_date):
    # Sleep to give time to focus on the input field
    time.sleep(SLEEP_DURATION)

    pattern = r'Money Line\s+(\d+)'
    counter = 0
    matched_digits = ""  # Initialize outside the loop

    for line in lines:
        # Check if the line contains a date
        date_match = re.search(r'(\b\w+ \d{1,2}(?: \d{1,2}:\d{2} [APMapm]{2})?)', line)
        if date_match and date_match.group(1) == target_date:
            continue  # Skip the line containing the date

        money_match = re.match(r'(\d+)$', line)
        if counter % 2 == 0:
            if money_match:
                matched_digits = money_match.group(1)
                print("Matched Digits:", matched_digits)

                # Simulate user input
                pyautogui.press('tab')
                slowtype(str(matched_digits))
                pyautogui.press('enter')

                # Additional interaction
                for _ in range(LEFT_ARROW_PRESS_COUNT):
                    pyautogui.press('left')

                counter += 1

# Replace 'your_file_path_here.info' with the actual path to your .info file
with open('../../0.INFO', 'r') as file:
    data = file.read()
    lines = data.strip().split('\n')

# Set the target date
target_date = "Dec 31"  # Change this to the desired date

extract_rot_number(target_date)
