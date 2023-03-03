import time
import pandas
import pyautogui

# Read data from excel
sport = "update tnt"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
count = 0
number = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    if (str(int(excel_data['Odds'][count]))) == '-20':
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.press('enter')
        pyautogui.press('down')
    elif (str(int(excel_data['Odds'][count]))) == '-50':
        pyautogui.press('down')
        pyautogui.press('down')
    elif (str(int(excel_data['Odds'][count]))) == '-60':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    elif (str(int(excel_data['Odds'][count]))) == '-70':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['Odds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1
