import time
import pandas
import pyautogui

# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)


# Iterate excel rows till to finish
number = 2


for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.press('tab', presses=2)
    pyautogui.write("OVER")
    pyautogui.press('tab')
    pyautogui.write("UNDER")
    pyautogui.hotkey('alt', 'o')
    time.sleep(7)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    # Set counter with the number of Rows
    if count == number - 1:
        print(count+1)
        print('COMPLETED')
        break
    count = count + 1
    print(count)