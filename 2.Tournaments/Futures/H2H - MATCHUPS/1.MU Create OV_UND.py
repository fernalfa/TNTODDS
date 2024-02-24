import time
import pyautogui
from tqdm import tqdm
import tkinter as tk

# Default description
DESCRIPTION = 'INSERT DESCRIPTION'
VALUE = 'OVER'
VALUE1 = 'UNDER'
DELAY = 10

def submit_values():
    global DESCRIPTION, VALUE, VALUE1
    global popup

    DESCRIPTION = description_text.get("1.0", "end-1c")
    VALUE = value_entry.get()
    VALUE1 = value1_entry.get()
    show_popup()

def get_values():
    global DESCRIPTION, description_text, value_entry, value1_entry

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Enter Values")

    # Description
    description_label = tk.Label(root, text="Description:")
    description_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    description_text = tk.Text(root, height=3, width=30)
    description_text.grid(row=0, column=1, padx=10, pady=5)
    description_text.insert("1.0", DESCRIPTION)


    # Add labels and entry widgets for the values
    tk.Label(root, text="Value:").grid(row=1, column=0)
    value_entry = tk.Entry(root)
    value_entry.grid(row=1, column=1)
    value_entry.insert(0, VALUE)  # Insert default text

    tk.Label(root, text="Value1:").grid(row=2, column=0)
    value1_entry = tk.Entry(root)
    value1_entry.grid(row=2, column=1)
    value1_entry.insert(0, VALUE1)  # Insert default text

    # Add a button to submit the values
    submit_button = tk.Button(root, text="Submit", command=submit_values)
    submit_button.grid(row=4, columnspan=2)

    # Run the Tkinter event loop
    root.mainloop()

# Function to type slowly
def slow_typewrite(text, delay=0.1):
    pyautogui.write(text, interval=delay)

def next_mu():
    pyautogui.hotkey('alt', 'o')
    time.sleep(DELAY)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

def read_file():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\INFO.txt', 'r') as file:
        lines = file.readlines()

    # Filter out empty lines and non-numeric lines
    names = [line.strip() for line in lines if line.strip() and not line.strip().isdigit()]
    return names

def main(name, VALUE, VALUE1, DESCRIPTION):
    slow_typewrite(name)
    slow_typewrite(DESCRIPTION)
    pyautogui.press('tab', presses=2)
    slow_typewrite(str(VALUE))
    pyautogui.press('tab')
    slow_typewrite(str(VALUE1))
    next_mu()
    print(f"{name} : {DESCRIPTION}  ")

    print("Processing complete.")

def show_popup():
    global popup
    popup = tk.Tk()
    popup.geometry("400x300")
    popup.title("CREATE OVER VS UNDER")

    button1 = tk.Button(popup, text="Create Using Description", command=Create_OV_UND)
    button1.grid(row=1, column=0, padx=10, pady=10)

    popup.mainloop()

def Create_OV_UND():
    # Sleep for 3 seconds before starting
    time.sleep(3)
    if __name__ == "__main__":
        names = read_file()
    for index, name in enumerate(tqdm(names, desc="Processing", unit="player")):
        main(name, VALUE, VALUE1, DESCRIPTION)  # Pass only the name here, not the index


get_values()
