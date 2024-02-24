import time
import pyautogui
time.sleep(3)

with open('../0.INFO', 'r') as file:
    # Read player names from text file and split into sets
    sets = file.read().splitlines()

def entergame():
    pyautogui.hotkey('ctrl', 'enter')
    print("Entering Game...")
    time.sleep(1)


def selectfamily(value):
    print("Selecting Family...")
    time.sleep(1)
    pyautogui.press('tab', presses=5)
    # Iterate through the list of player names and type each name
    for name in value:
        time.sleep(0.5)
        pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
        # Add a delay between typing each name (adjust the sleep time as needed)
        # Press 'Tab' to move to the next field
        pyautogui.press('tab', presses=20)
        pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
        time.sleep(1.5)
        pyautogui.hotkey('alt', 'o')
        print("Family Selected...")
        print("Game Family Categories Added")
        pyautogui.press('tab')
        pyautogui.press('down', presses=3)
        time.sleep(3)


def addfamily():
    for value_set in sets:
        value = value_set.splitlines()
        entergame()
        selectfamily(value)

# Call the addfamily function to iterate through the sets in the INFO file
addfamily()






