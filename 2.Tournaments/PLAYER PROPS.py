import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')


# Read data from excel
sport = "Hoja1"
excel_data = pandas.read_excel(file_path, sheet_name=sport)
count = 0
time.sleep(3)



number = 19

# Iterate excel rows till to finish
for count, column in enumerate(excel_data['Row ID'].tolist()):
    total_value = (excel_data['TOTAL'][count])

    if total_value == 0:
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down', presses = 3)

    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(total_value))
        pyautogui.press('enter')
        pyautogui.press('down', presses = 3)


    # Set counter with the number of Rows
    if count == number - 1:
        print(f"{(str((excel_data['A'][count])))}: {(str(excel_data['TOTAL'][count]))}")
        print('COMPLETED, PLEASE CHECK')
        break
    print(f"{(str((excel_data['A'][count])))}: {(str(excel_data['TOTAL'][count]))}")
    count = count + 1


