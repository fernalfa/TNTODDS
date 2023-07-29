import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')

# Read data from excel
sport = "BANNERS"
excel_data = pandas.read_excel(file_path, sheet_name=sport)

count = 0
time.sleep(4)

number = 4

# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    pyautogui.write((str(int(excel_data['ROT1'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT2'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT3'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT4'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT5'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT6'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    pyautogui.write((str(int(excel_data['ROT7'][count]))))
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))

    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('del')

    print(str(excel_data['BANNER'][count]))


    # Set counter with the number of Rows
    if count == number - 1:
        print(str(excel_data['BANNER'][count]))
        print('BANNERS COMPLETED, PLEASE CHECK!!')
        break
    count = count + 1
    print(count)