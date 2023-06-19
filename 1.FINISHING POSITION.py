import time
import pandas
import pyautogui

# Read data from excel
sport = "LINEAL"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(5)
# Iterate excel rows till to finish

repeat = 14

for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['FP'][count]))
    pyautogui.write(" - ")
    pyautogui.write(" FINISHING POSITION")
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['FP1'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['FP2'][count]))
    pyautogui.hotkey('alt', 'o')
    time.sleep(8)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    # Set counter with the number of Rows
    if count == repeat - 1:
        print(count + 1)
        print(str(excel_data['PLAYER'][count]))
        print('COMPLETED')
        break
    print(count + 1)
    print(str(excel_data['PLAYER'][count]))
    count = count + 1