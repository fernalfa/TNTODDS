import time
import pandas
import pyautogui

# Read data from excel
sport = "PlayerPropsUNIBET"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
number = 28
count = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['STAT'][count]))
    pyautogui.write(" - ")
    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.press('tab', presses=3)
    pyautogui.write("OVER")
    pyautogui.press('tab')
    pyautogui.write("UNDER")
    pyautogui.keyDown('alt')
    pyautogui.keyDown('o')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('o')
    time.sleep(10)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=4)
    pyautogui.keyUp('shift')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1