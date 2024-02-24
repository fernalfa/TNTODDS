import time
from tqdm import tqdm
import pyautogui
import tkinter as tk


# Default description
DESCRIPTION = 'INSERT DESCRIPTION'
DELAY = 12

def submit_values():
    global dropdown
    global popup
    global DESCRIPTION
    global selected_option  # Define selected_option as global
    DESCRIPTION = description_text.get("1.0", "end-1c")
    selected_option = dropdown.get()
    print("Description:", DESCRIPTION)
    print("Selected Option:", selected_option)
    show_popup()

def ask_variables():
    global dropdown
    global description_text
    global popup

    popup = tk.Tk()
    popup.title("Insert Description")

    # Set the size of the popup window
    popup.geometry("350x175")  # Width x Height

    # Description
    description_label = tk.Label(popup, text="Description:")
    description_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    description_text = tk.Text(popup, height=3, width=30)
    description_text.grid(row=0, column=1, padx=10, pady=5)
    description_text.insert("1.0", DESCRIPTION)

    # Dropdown
    dropdown_label = tk.Label(popup, text="Select an option:")
    dropdown_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    dropdown = tk.StringVar(popup)
    dropdown.set("REGULAR")
    dropdown_menu = tk.OptionMenu(popup, dropdown, "REGULAR", "MATCHUPS")
    dropdown_menu.grid(row=1, column=1, padx=10, pady=5)

    # Submit Button
    submit_button = tk.Button(popup, text="Submit", command=submit_values)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    popup.mainloop()

def slow_type(text, interval=0.01):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(interval)

def next_mu():
    pyautogui.hotkey('alt', 'o')
    time.sleep(DELAY)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

def next_mu2():
    pyautogui.hotkey('alt', 'o')
    time.sleep(DELAY)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

def get_description():
    global DESCRIPTION
    popup = tk.Tk()
    popup.title("Enter Description")

    label = tk.Label(popup, text="Enter Description:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(popup)
    entry.grid(row=0, column=1, padx=10, pady=5)

    # Submit Button
    submit_button = tk.Button(popup, text="Submit", command=submit_values)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    popup.mainloop()

def read_file():
    with open('C:\\Users\\User\\Desktop\\New folder\\TNTODDS\\INFO.txt', 'r') as file:
        data = [line.strip().upper() for line in file.readlines() if line.strip()]
    # Initialize lists to store player names
    pair_list = []
    unpair_list = []

    # Iterate through each line in the data
    for index, line in enumerate(data):
        if index % 2 == 0:
            pair_list.append(line)
        else:
            unpair_list.append(line)
    return pair_list, unpair_list

def main(pair, unpair):
    slow_type(DESCRIPTION)
    slow_type(f" ({pair} vs {unpair})")
    pyautogui.press('tab', presses=2)
    slow_type(pair)
    pyautogui.press('tab')
    slow_type(unpair)
    next_mu()

def mainmu(pair, unpair):
    slow_type(DESCRIPTION)
    slow_type(f" ({pair} vs {unpair})")
    pyautogui.press('tab', presses=3)
    slow_type(pair)
    pyautogui.press('tab')
    slow_type(unpair)
    next_mu2()

def show_popup():
    popup = tk.Tk()
    popup.geometry("400x300")
    popup.title("CREATE MATCH UPS")


    button1 = tk.Button(popup, text="Create Using Description", command=Create_H2H)
    button1.grid(row=1, column=0, padx=10, pady=10)


    popup.mainloop()

def Create_H2H():
    global selected_option
    # Sleep for 3 seconds before starting
    time.sleep(3)
    pair_list, unpair_list = read_file()

    for pair, unpair in tqdm(zip(pair_list, unpair_list), total=len(pair_list)):
        if selected_option == "REGULAR":
            # Apply logic for REGULAR option
            # For example:
            print(f"Processing: {pair} vs {unpair}")
            main(pair, unpair)
        elif selected_option == "MATCHUPS":
            # Apply logic for MATCHUPS option
            # For example:
            print(f"Processing: {pair} vs {unpair}")
            mainmu(pair, unpair)


# Show the pop-up window
ask_variables()