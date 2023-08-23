import time
import pandas
import pyautogui
from tqdm import tqdm
import os


# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')


# Read data from excel
sport = "BET365 MU Create"
excel_data = pandas.read_excel(file_path, sheet_name=sport)


count = 0
time.sleep(3)

number = 4

# Iterate excel rows till to finish
for count, column in tqdm(enumerate(excel_data['Row ID'].tolist())):
    pyautogui.typewrite(str(excel_data['DESCRIPTION'][count]))
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(excel_data['HOME'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['VISITOR'][count]))
    time.sleep(5)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('alt', 'o')
    time.sleep(15)
    # Set counter with the number of Rows
    if count == number - 1:
        print('COMPLETED')
        break