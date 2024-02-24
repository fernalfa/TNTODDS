import time
from tqdm import tqdm
import pyautogui
import tkinter as tk

DOWN = 3

# Function to calculate rotations based on ROT value
def calculate_rotation(ROT):
    # Define the variable, multiplier, and values
    a = 898999
    b = 900999
    c = 902999
    result = (ROT * 2) + a
    result2 = (ROT * 2) + a + 2
    result3 = (ROT * 2) + b
    result4 = (ROT * 2) + b + 2
    result5 = (ROT * 2) + c
    result6 = (ROT * 2) + c + 2

    results_message = f"FG ROTATION:\n{result}\n{result2}\n\n1ST HALF ROTATION:\n{result3}\n{result4}\n\n2ND HALF ROTATION:\n{result5}\n{result6}"
    return results_message

def prerot(ROT,repeat_value, increase_value):
    time.sleep(3)
    def replacepre():
        pyautogui.press('enter')
        pyautogui.press('home')
        pyautogui.press('backspace')
        pyautogui.typewrite(str(ROT))
        pyautogui.press('enter')
        pyautogui.press('down', presses = DOWN)
    count = 0

    # Wrap your loop with tqdm
    with tqdm(total=repeat_value) as pbar:
        while count < repeat_value:
            count = count + 1
            replacepre()
            pbar.update(1)  # Update the progress bar
            ROT += increase_value

def afterrot(ROT,repeat_value,increase_value):
    time.sleep(3)
    def replaceafter():
        pyautogui.press('enter')
        pyautogui.press('end')
        pyautogui.typewrite(str(ROT))
        pyautogui.press('enter')
        pyautogui.press('down', presses=DOWN)

    count = 0

    # Wrap your loop with tqdm
    with tqdm(total=repeat_value) as pbar:
        while count < repeat_value:
            count = count + 1
            replaceafter()
            pbar.update(1)  # Update the progress bar
            ROT += increase_value

def replace_rot(ROT,repeat_value,increase_value):
    time.sleep(3)
    def replace():
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.typewrite(str(ROT))
        pyautogui.press('enter')
        pyautogui.press('down', presses = DOWN)

    count = 0

    # Wrap your loop with tqdm
    with tqdm(total=repeat_value) as pbar:
        while count < repeat_value:
            count = count + 1
            replace()
            pbar.update(1)  # Update the progress bar
            ROT += increase_value

def show_popup():
    def start_prerot():
        ROT = entry_ROT.get()
        repeat_value = int(entry2.get())
        increase_value = int(entry3.get())
        prerot(int(ROT),repeat_value,increase_value)

    def start_afterrot():
        ROT = entry_ROT.get()
        repeat_value = int(entry2.get())
        increase_value = int(entry3.get())
        afterrot(int(ROT),repeat_value,increase_value)

    def rot_popup():
        ROT = entry_ROT.get()
        result_message = calculate_rotation(int(ROT))

        # Display the result in a new window or print it to the console
        result_window = tk.Toplevel(popup)
        result_window.geometry("300x200")
        result_window.title("Calculation Result")

        result_label = tk.Label(result_window, text=result_message)
        result_label.pack(padx=10, pady=10)

    def start_replace_rot():
        ROT = entry_ROT.get()
        repeat_value = int(entry2.get())
        increase_value = int(entry3.get())
        replace_rot(int(ROT),repeat_value,increase_value)


    popup = tk.Tk()
    popup.geometry("400x300")
    popup.title("REPLACE ROTATIONS")


    label_ROT = tk.Label(popup, text="Enter ROT:")
    label_ROT.grid(row=0, column=0)
    entry_ROT = tk.Entry(popup)
    entry_ROT.grid(row=0, column=1, padx=10, pady=8)

    label2 = tk.Label(popup, text="Times to Repeat")
    label2.grid(row=2, column=0, columnspan=1)
    entry2 = tk.Entry(popup)
    entry2.grid(row=2, column=1, padx=10, pady=8)

    label3 = tk.Label(popup, text="Increase Value")
    label3.grid(row=3, column=0, columnspan=1)
    entry3 = tk.Entry(popup)
    entry3.grid(row=3, column=1, padx=10, pady=8)


    button1 = tk.Button(popup, text="BEFORE ROTATION", command=start_prerot)
    button1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    button2 = tk.Button(popup, text="AFTER ROTATION", command=start_afterrot)
    button2.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    button3 = tk.Button(popup, text="REPLACE ROTATION", command=start_replace_rot)
    button3.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    button4 = tk.Button(popup, text="CALCULATE ROTATION", command=rot_popup)
    button4.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    popup.mainloop()


# Show the pop-up window
show_popup()