import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '../..', 'Tools.xlsx')


# Read data from excel
sport = "INTERCALADO"
excel_data = pandas.read_excel(file_path, sheet_name=sport)
count = 0
time.sleep(3)



number = 156



# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    # DELETE IF NO ODDS IN EXCEL ROW
    if (str(int(excel_data['AdjOdds'][count]))) == '0':
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
        print('ODDS DELETED')


    elif (str(int(excel_data['AdjOdds'][count]))) == '-20':
        pyautogui.press('down')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')
        print('2 LINES JUMP')

    elif (str(int(excel_data['AdjOdds'][count]))) == '-25':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')
        print('3 LINES JUMP')

    elif (str(int(excel_data['AdjOdds'][count]))) == '-28':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')
        print('4 LINES JUMP')

    elif (str(int(excel_data['AdjOdds'][count]))) == '-30':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-125')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
        print('ALL BETS ACTION HEADER')

    elif (str(int(excel_data['AdjOdds'][count]))) == '-40':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-125')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('-125')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')
        print('DOUBLE HEADER')

    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['AdjOdds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')

    # Set counter with the number of Rows
    if count == number - 1:
        print(f"{(str((excel_data['A'][count])))}: {(str(int(excel_data['AdjOdds'][count])))}")
        print('COMPLETED, PLEASE CHECK')
        break
    print(f"{(str((excel_data['A'][count])))}: {(str(int(excel_data['AdjOdds'][count])))}")
    count = count + 1
