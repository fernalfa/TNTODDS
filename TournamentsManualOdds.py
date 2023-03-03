import time
import pandas
import pyautogui

# Read data from excel
sport = "tntManual"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
count = 0
number = 76


time.sleep(5)
# Iterate excel rows till to finish
for column in excel_data['Row ID'].tolist():
    # DELETE IF NO ODDS IN EXCEL ROW
    if (str(int(excel_data['Odds'][count]))) == '-20':
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.press('enter')
        pyautogui.press('down')
    #JUMP WINNING MARGINS / DOUBLE RESULT / GAME EVENTS WITH LESS DESCRIPTIONS
    elif (str(int(excel_data['Odds'][count]))) == '-50':
        pyautogui.press('down', presses=2)
    elif (str(int(excel_data['Odds'][count]))) == '-60':
        pyautogui.press('down', presses=3)
        #all action
    elif (str(int(excel_data['Odds'][count]))) == '-70':
        pyautogui.press('down', presses=4)
        #ALL ACTION, DEAD HEAT RULE
    elif (str(int(excel_data['Odds'][count]))) == '-80':
        pyautogui.press('down', presses=5)
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['Odds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1
