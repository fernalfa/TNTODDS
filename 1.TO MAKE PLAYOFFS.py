import time
import pandas
import pyautogui

# Read data from excel
sport = "Regular MU Create"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(5)
# Iterate excel rows till to finish

repeat = 32
rotation = 5001001
description = " TO MAKE NFL 2023/24 PLAYOFFS"

for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.typewrite(description)
    pyautogui.press('tab', presses=1)
    pyautogui.press('backspace', presses=8)
    pyautogui.typewrite(str(rotation))
    pyautogui.press('tab', presses=1)
    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.write(" YES MAKE PLAYOFFS")
    pyautogui.press('enter')
    pyautogui.typewrite(str(excel_data['PLAYER'][count]))
    pyautogui.write(" NO MAKE PLAYOFFS")
    pyautogui.press('tab', presses=1)
    pyautogui.press('enter', presses=2)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace', presses=200)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('backspace', presses=80)

    # Set counter with the number of Rows
    if count == repeat - 1:
        print(count + 1)
        print(str(excel_data['PLAYER'][count]))
        print('COMPLETED')
        rotation += 10
        break
    print(count + 1)
    print(str(excel_data['PLAYER'][count]))
    count = count + 1
    rotation += 10
