import time
import pyautogui
import tkinter as tk
from tkinter.simpledialog import askinteger

DELAY = 8

def entergame():
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'enter')
    print("Entering Game...")
    time.sleep(5)

def nhl_familyprops():
    with open('../0.INFO', 'r') as file:
        # Read player names from text file and split into sets
        sets = file.read().splitlines()
    def selectnhlfamily(value):
        print("Selecting Family...")
        time.sleep(1)
        pyautogui.press('tab', presses=25)
        # Iterate through the list of player names and type each name
        for name in value:
            time.sleep(1)
            pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
            # Add a delay between typing each name (adjust the sleep time as needed)
            # Press 'Tab' to move to the next field
            pyautogui.press('tab', presses = 9)
            pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
            time.sleep(1.5)
            pyautogui.hotkey('alt', 'o')
            print("Family Selected...")
            print("Game Family Categories Added")
            pyautogui.press('tab')
            pyautogui.press('down', presses=3)
            time.sleep(2)
    def addnhlfamily():
        for value_set in sets:
            value = value_set.splitlines()
            entergame()
            selectnhlfamily(value)

    # Call the addfamily function to iterate through the sets in the INFO file
    addnhlfamily()

def familyprops():
    with open('../0.INFO', 'r') as file:
        # Read player names from text file and split into sets
        sets = file.read().splitlines()
    def selectfamily(value):
        print("Selecting Family...")
        time.sleep(1)
        pyautogui.press('tab', presses=5)
        # Iterate through the list of player names and type each name
        for name in value:
            time.sleep(1)
            pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
            # Add a delay between typing each name (adjust the sleep time as needed)
            # Press 'Tab' to move to the next field
            pyautogui.press('tab', presses=2)
            pyautogui.typewrite(name.strip())  # Use name.strip() to remove newline characters
            time.sleep(1)
            pyautogui.hotkey('alt', 'o')
            time.sleep(DELAY)
            print("Family Selected...")
            print("Game Family Categories Added")
            pyautogui.press('tab')
            pyautogui.press('down', presses=3)
            time.sleep(2)

    def addfamily():
        for value_set in sets:
            value = value_set.splitlines()
            entergame()
            selectfamily(value)

    # Call the addfamily function to iterate through the sets in the INFO file
    addfamily()

def create_label(parent, text, row, column, columnspan=2, width=None):
    if isinstance(text, list):
        label = tk.Label(parent, text='\n'.join(text), width=width)
    else:
        label = tk.Label(parent, text=text, width=width)
    label.grid(row=row, column=column, columnspan=columnspan)

def create_button(parent, text, row, column, command, padx=10, pady=10):
    button = tk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady)

def create_popup():
    popup = tk.Tk()
    popup.title("Relate Props - ")

    label_width = 40  # Adjust the width as needed

    # FIRST Column
    create_label(popup, "FAMILY GAMES", 0, 0, columnspan=1, width=label_width)
    create_button(popup, "Relate Regular MU", 1, 0, familyprops)
    create_button(popup, "Relate NHL Games", 2, 0, nhl_familyprops)
    popup.mainloop()
# Show the pop-up window
create_popup()

