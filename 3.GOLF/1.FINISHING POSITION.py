import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')


# Read data from excel
sport = "LINEAL"
excel_data = pandas.read_excel(file_path, sheet_name=sport)

count = 0
time.sleep(3)
# Iterate excel rows till to finish

repeat = 40

for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['FP'][count]))
    pyautogui.write(" - ")
    pyautogui.write(" FINISHING POSITION")
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['FP1'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['FP2'][count]))
    time.sleep(5)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('alt', 'o')
    time.sleep(15)
    # Set counter with the number of Rows
    if count == repeat - 1:
        print(count + 1)
        print(str(excel_data['FP'][count]))
        print('COMPLETED')
        break
    print(str(excel_data['FP'][count]))
    count = count + 1
