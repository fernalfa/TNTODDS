import time
import pandas
import pyautogui
# Read data from excel
sport = "INTERCALADO"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)


number = 15


# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    # DELETE IF NO ODDS IN EXCEL ROW
    if (str(int(excel_data['AdjOdds'][count]))) == '0':
        pyautogui.press('enter')
        pyautogui.press('del')
        pyautogui.press('enter')
        pyautogui.press('down')


    elif (str(int(excel_data['AdjOdds'][count]))) == '-20':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')

    elif (str(int(excel_data['AdjOdds'][count]))) == '-28':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        print('NEXT TOURNAMENT')


    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['AdjOdds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')

    # Set counter with the number of Rows
    if count == number - 1:
        print(count+1)
        print('COMPLETED')
        break
    count = count + 1
    print(count)
