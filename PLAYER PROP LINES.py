import time
import pandas
import pyautogui

# Read data from excel
sport = "Player Props"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
number = 16
count = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID2'].tolist():
    pyautogui.press('enter')
    pyautogui.typewrite(str(excel_data['TOTAL'][count]))
    pyautogui.press('enter')
    pyautogui.press('right')
    if (str(int(excel_data['OVER'][count]))) == '-20':
        pyautogui.press('down')
    else:
        #type odds in the over
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['OVER'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
        #validate if there's odds in the UNDER
    if (str(int(excel_data['UNDER'][count]))) == '-20':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('left')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['UNDER'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('left')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1