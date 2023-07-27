import time
import pandas
import pyautogui

# Read data from excel
sport = "Player Props"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
number = 25
count = 0
time.sleep(3)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():

    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.write(" (")
    pyautogui.typewrite(str(excel_data['TEAM'][count]))
    pyautogui.write(") - ")
    pyautogui.typewrite(str(excel_data['STAT'][count]))
    pyautogui.press('tab', presses=3)
    pyautogui.write("OVER")
    pyautogui.press('tab')
    pyautogui.write("UNDER")
    pyautogui.hotkey('alt', 'o')
    time.sleep(10)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1