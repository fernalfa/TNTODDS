import time
import pandas
import pyautogui
# Read data from excel
sport = "3WAY"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)


number = 12


# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    if (str(int(excel_data['AWAY'][count]))) == '0':
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['AWAY'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')

        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['HOME'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')

        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['X'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

    # Set counter with the number of Rows
    if count == number - 1:
        print(count)
        print(str((excel_data['A'][count])))
        print(str(int(excel_data['AdjOdds'][count])))
        print('COMPLETED, PLEASE CHECK')
        break
    print(count)
    print(str((excel_data['AWAY'][count])))
    print(str((excel_data['HOME'][count])))
    print(str(int(excel_data['X'][count])))
    count = count + 1
