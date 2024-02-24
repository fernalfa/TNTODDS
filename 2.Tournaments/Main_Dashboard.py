import re
import subprocess
import time
import pandas as pd
from patterns import exclude_patterns, replace_patterns, ignore_patterns  # Import exclusion, replacement, and ignore patterns from patterns.py
from tqdm import tqdm
import pyautogui
import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import messagebox



import os

def clear_console():
    os.system('cls')

# Test the function
clear_console()


def start_TNT_Tools_py():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tournaments\1.TNT TOOLS.py'])

def start_odds_boost():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tournaments\1.ODDS BOOST.py'])

def General_Entry():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tournaments\1.General_Entry.py'])

def Extra_Tools():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tournaments\EXTRA_Tools.py'])


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
    popup.title("TOOLS")

    label_width = 20  # Adjust the width as needed

    # FIRST Column
    create_label(popup, "", 0, 0, columnspan=1, width=label_width)
    create_button(popup, "Start TNT Tools", 1, 0, start_TNT_Tools_py)
    create_button(popup, "BOOSTED ODDS ", 2, 0, start_odds_boost)
    create_button(popup, "General TNT Entry", 4, 0, General_Entry)
    # SECOND Column TEXT
    create_button(popup, "Clear Console", 1, 1, clear_console)
    create_button(popup, "Extra Tools", 2, 1, Extra_Tools)


    # SECOND Column Description
    create_label(popup, [""], 0, 1, columnspan=1, width=label_width)

    # THIRD Column Description
    create_label(popup, "", 0, 2, columnspan=1, width=label_width)

    popup.mainloop()
# Show the pop-up window
create_popup()

