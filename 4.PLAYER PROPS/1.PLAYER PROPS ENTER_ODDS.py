import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')


# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel(file_path, sheet_name=sport)

count = 0
time.sleep(3)


extracents = 0
number = 32


# Iterate excel r
# ws till to finish
for column in excel_data['Row ID'].tolist():
    # DELETE IF NO ODDS IN EXCEL ROW
    if (str(int(excel_data['YES'][count]))) == '0':
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')


    elif (str(int(excel_data['YES'][count]))) == '-30':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-125')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')
        print('ALL BETS ACTION')

    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str((int(excel_data['YES'][count]))-(extracents)))
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

    # Set counter with the number of Rows
    if count == number - 1:
        print(count + 1)
        print(str(int(excel_data['YES'][count])))
        print('COMPLETED, PLEASE CHECK')
        break
    print(str(int(excel_data['YES'][count])))
    count = count + 1