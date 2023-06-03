import time
import pandas
import pyautogui

SPORT_SHEET = "3-7 INNINGS"

excel_data = pandas.read_excel('Tools.xlsx', sheet_name=SPORT_SHEET)
number = 14

# Wait for 5 seconds
pyautogui.sleep(5)

# Iterate over rows in excel_data
for _, row in excel_data.iterrows():
    total = str(row['TOTAL'])
    over = str(int(row['OVER']))
    under = str(int(row['UNDER']))
    spread = str(row['SPREAD'])
    visitor = str(int(row['VISITOR']))
    home = str(int(row['HOME']))

    enter_key = 'enter'
    down_key = 'down'
    right_key = 'right'
    up_key = 'up'
    left_key = 'left'

    pyautogui.press(enter_key)
    pyautogui.typewrite(total)
    pyautogui.press(enter_key)
    pyautogui.press(right_key)

    if over == '-20':
        pyautogui.press(down_key)
    else:
        pyautogui.press(enter_key)
        pyautogui.typewrite(over)
        pyautogui.press(enter_key)
        pyautogui.press(down_key)

    if under == '-20':
        pyautogui.press(right_key, presses=5)
        pyautogui.press(up_key)
    else:
        pyautogui.press(enter_key)
        pyautogui.typewrite(under)
        pyautogui.press(enter_key)
        pyautogui.press(right_key, presses=5)
        pyautogui.press(up_key)

    pyautogui.press(enter_key)
    pyautogui.typewrite(spread)
    pyautogui.press(enter_key)
    pyautogui.press(right_key)

    if visitor == '-20':
        pyautogui.press(down_key)
    else:
        pyautogui.press(enter_key)
        pyautogui.typewrite(visitor)
        pyautogui.press(enter_key)
        pyautogui.press(down_key)

    if home == '-20':
        pyautogui.press(down_key, presses=2)
        pyautogui.press(left_key, presses=7)
    else:
        pyautogui.press(enter_key)
        pyautogui.typewrite(home)
        pyautogui.press(enter_key)
        pyautogui.press(down_key, presses=2)
        pyautogui.press(left_key, presses=7)

    if _ == number - 1:
        break