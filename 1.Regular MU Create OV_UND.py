import time
import pandas
import pyautogui

# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)


# Iterate excel rows till to finish
number = 3


VALUE = "OVER"
VALUE1 = "UNDER"

for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(VALUE))
    pyautogui.press('tab')
    pyautogui.typewrite(str(VALUE1))
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('alt', 'o')
    time.sleep(15)
    # Set counter with the number of Rows
    if count == number - 1:
        print(str(excel_data['PLAYER'][count]))
        print(count+1)
        print('COMPLETED')
        break
    print(str(excel_data['PLAYER'][count]))
    count = count + 1
    print(count)
