import time
import pandas
import pyautogui
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'Tools.xlsx')


# Read data from excel
sport = "3-7 INNINGS"
excel_data = pandas.read_excel(file_path, sheet_name=sport)
count = 0
number = 10

time.sleep(3)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    #type total
    pyautogui.press('enter')
    pyautogui.typewrite(str(excel_data['TOTAL'][count]))
    pyautogui.press('enter')
    pyautogui.press('right')
    #validate if there's odds in the OVER
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
        pyautogui.press('right', presses=5)
        pyautogui.press('up')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['UNDER'][count])))
        pyautogui.press('enter')
        pyautogui.press('right', presses=5)
        pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.typewrite(str(excel_data['SPREAD'][count]))
    pyautogui.press('enter')
    pyautogui.press('right')
    if (str(int(excel_data['VISITOR'][count]))) == '-20':
        pyautogui.press('down')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['VISITOR'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
    if (str(int(excel_data['HOME'][count]))) == '-20':
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=7)
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['HOME'][count])))
        pyautogui.press('enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=7)
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1