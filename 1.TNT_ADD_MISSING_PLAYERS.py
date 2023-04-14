import time
import pandas
import pyautogui
# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)

number = 1


# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite('-150')
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')
    # Set counter with the number of Rows
    if count == number - 1:
        print(count+1)
        print(str((excel_data['PLAYER'][count])))
        print('COMPLETED')
        break
    count = count + 1
    print(count)
    print(str((excel_data['PLAYER'][count])))
