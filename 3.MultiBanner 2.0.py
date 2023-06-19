import time
import pandas
import pyautogui
# Read data from excel
sport = "BANNERS"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
count = 0
time.sleep(3)

number = 1


# Iterate excel r
# ws till to finish
for column in excel_data['Row ID'].tolist():
    pyautogui.typewrite(str(excel_data['ROT1'][count]))
    pyautogui.press('tab', presses = 3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.typewrite(str(excel_data['ROT2'][count]))
    pyautogui.press('tab', presses = 3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.typewrite(str(excel_data['ROT3'][count]))
    pyautogui.press('tab', presses = 3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.typewrite(str(excel_data['ROT4'][count]))
    pyautogui.press('tab', presses = 3)
    pyautogui.typewrite(str(excel_data['BANNER'][count]))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

count = 0

while (count < number):
    print((str(excel_data['BANNER'][count])) + ' BANNERS CREATED, PLEASE CHECK')
    count = count + 1
