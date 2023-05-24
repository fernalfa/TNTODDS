import time
import pandas
import pyautogui

# Read data from excel
sport = "BANNERS"
excel_data = pandas.read_excel('Tools.xlsx', sheet_name=sport)
time.sleep(3)

number = 2

# Iterate through excel rows
for count, row in excel_data.iterrows():
    for i in range(1, 8):
        rot_value = int(row[f'ROT{i}'])
        banner_value = str(row['BANNER'])

        pyautogui.write(str(rot_value))
        pyautogui.press('tab', presses=3)
        pyautogui.typewrite(banner_value)
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('alt', 'o')
        pyautogui.press('del')

    print(f"{banner_value} BANNERS CREATED, PLEASE CHECK")

    # Check if the desired number of rows is reached
    if count == number - 1:
        print(count + 1)
        print('COMPLETED')
        break

    print(count + 1)