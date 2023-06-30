import time
import pandas
import pyautogui
# Read data from excel
sport = "BANNERS"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)

number = 2

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


    print((str(int(excel_data['ROT1'][count]))))
    print((str(int(excel_data['ROT2'][count]))))
    print((str(int(excel_data['ROT3'][count]))))
    print((str(int(excel_data['ROT4'][count]))))
    print((str(int(excel_data['ROT5'][count]))))
    print((str(int(excel_data['ROT6'][count]))))
    print((str(int(excel_data['ROT7'][count]))))


    # Set counter with the number of Rows
    if count == number - 1:
        print(count+1)
        print('COMPLETED')
        break
    count = count + 1
    print(count)