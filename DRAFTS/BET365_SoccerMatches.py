import time
import pandas
import pyautogui

# Read data from excel
sport = "bet365soccer"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
count = 0
time.sleep(3)

number = 5
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(str(excel_data['LEAGUE'][count]))
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(excel_data['VISITOR'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['HOME'][count]))
    pyautogui.hotkey('alt', 'o')
    time.sleep(10)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    # Set counter with the number of Rows
    if count == number - 1:
        print('BREAK')
        break
    count = count + 1
    print(count)