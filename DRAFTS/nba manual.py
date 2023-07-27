import time
import pandas
import pyautogui

# Read data from excel
sport = "nba manual"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
number = 0
count = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['DESCRIPTION'][count]))
    pyautogui.press('tab', presses=2)
    pyautogui.typewrite(str(excel_data['VISITOR'][count]))
    pyautogui.press('tab')
    pyautogui.typewrite(str(excel_data['HOME'][count]))
    pyautogui.keyDown('alt')
    pyautogui.keyDown('o')
    pyautogui.keyUp('o')
    pyautogui.keyUp('alt')
    time.sleep(15)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=3)
    pyautogui.keyUp('shift')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1