import time
import pandas
import pyautogui
# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)



number = 9



# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    # DELETE IF NO ODDS IN EXCEL ROW
    if (str(int(excel_data['TOTALS2'][count]))) == '0':
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')

    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str((excel_data['TOTALS2'][count])))
        pyautogui.press('enter')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.typewrite('-110')
        pyautogui.press('enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left')

    # Set counter with the number of Rows
    if count == number - 1:
        print(count+1)
        print('COMPLETED')
        break
    count = count + 1
    print(count)
