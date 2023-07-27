import time
import pandas
import pyautogui

# Read data from excel
sport = "bet365soccer"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
number = 7
count = 0
time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID2'].tolist():
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(excel_data['VISITORML'][count])))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(excel_data['HOMEML'][count])))
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(excel_data['DRAW'][count])))
    pyautogui.press('enter')
    pyautogui.press('right', presses=5)
    pyautogui.press('up', presses=2)
    pyautogui.press('enter')
    pyautogui.typewrite(str(excel_data['TOTAL'][count]))
    pyautogui.press('enter')
    pyautogui.press('right', presses=1)
    if (str(int(excel_data['OVER'][count]))) == '-20':
        pyautogui.press('down')
    else:
        #type odds in the over
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['OVER'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
        #validate if there's odds in the UNDER
    if (str(int(excel_data['UNDER'][count]))) == '-20':
        pyautogui.press('enter')
        pyautogui.press('enter')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['UNDER'][count])))
        pyautogui.press('enter')
    pyautogui.press('down', presses=3)
    pyautogui.press('left', presses=6)
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1