import time
import pyautogui
import tkinter as tk
from tkinter import ttk

# Global variables to store user input
selected_function = None
repeat_count = None


def run_selected_function():
    global selected_function, repeat_count

    # Get the selected function and repeat count from user input
    selected_function = function_combobox.get()
    repeat_count = int(repeat_entry.get())

    # Close the pop-up window
    root.destroy()


def full_game():
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')


def first_half():
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.write('9')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')


def second_half():
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('10')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')


# Create the main Tkinter window
root = tk.Tk()
root.title("Function Selector")

# Label and Combobox for selecting the function
function_label = tk.Label(root, text="Select Function:")
function_label.pack()

function_combobox = ttk.Combobox(root, values=["full_game", "first_half", "second_half"])
function_combobox.pack()

# Label and Entry for specifying the repeat count
repeat_label = tk.Label(root, text="Enter Repeat Count:")
repeat_label.pack()

repeat_entry = tk.Entry(root)
repeat_entry.pack()

# Button to run the selected function
run_button = tk.Button(root, text="Run Function", command=run_selected_function)
run_button.pack()

# Start the Tkinter main loop
root.mainloop()

# Now, after the user has selected the function and repeat count, you can use them in your loop
if selected_function and repeat_count:

    for _ in range(repeat_count):
        if selected_function == "full_game":
            full_game()
        elif selected_function == "first_half":
            first_half()
        elif selected_function == "second_half":
            second_half()
