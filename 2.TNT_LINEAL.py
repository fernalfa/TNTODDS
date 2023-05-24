import time
import pandas
import pyautogui
# Read data from excel
sport = "LINEAL"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)


number = 63




# Iterate excel r
# ws till to finish
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
        print('2 LINES JUMP')
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
        print('NEXT TOURNAMENT')
        print('DOUBLE HEADER')

    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['AdjOdds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')

    # Set counter with the number of Rows
    if count == number - 1:
        print(count + 1)
        print(str((excel_data['A'][count])))
        print(str(int(excel_data['AdjOdds'][count])))
        print('COMPLETED, PLEASE CHECK')
        break
    print(count + 1)
    print(str((excel_data['A'][count])))
    print(str(int(excel_data['AdjOdds'][count])))
    count = count + 1