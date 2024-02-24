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

SURCHARGE_PERCENTAGE = 10  # 10% surcharge

def start_rot_py():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tools\Rotations\4.ROT Number Daily.py'])

def start_games():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tools\STM STOP_START.py'])

def Multi_Banner():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tournaments\1.Multi Banner Creator.py'])

def TEXT_SEARCH():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tools\9.League Search.py'])

def Multi_Select():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tools\4.Multi_Select.py'])

def Multi_Final():
    # Replace 'path/to/your/other_script.py' with the actual path to your Python script
    subprocess.Popen(['python', r'C:\Users\User\Desktop\New folder\TNTODDS\2.Tools\4.Multi_Final.py'])


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
    popup.title("EXTRA TOOLS")

    label_width = 20  # Adjust the width as needed

    # FIRST Column
    create_label(popup, "", 0, 0, columnspan=1, width=label_width)
    create_button(popup, "Specific Text Search", 1, 0, TEXT_SEARCH)
    create_button(popup, "ROT Tools", 2, 0, start_rot_py)
    create_button(popup, "Stop / Start Games", 3, 0, start_games)


    # SECOND Column TEXT
    create_button(popup, "Player Props Banner Create", 1, 1, Multi_Banner)

    # THIRD Column TEXT
    create_button(popup, "Multi Select", 1, 2, Multi_Select)
    create_button(popup, "Multi Final", 2, 2, Multi_Final)

    # SECOND Column Description
    create_label(popup, [""], 0, 1, columnspan=1, width=label_width)

    # THIRD Column Description
    create_label(popup, "", 0, 2, columnspan=1, width=label_width)

    popup.mainloop()


# Show the pop-up window
create_popup()

