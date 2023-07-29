import time
import pandas
import pyautogui

# Read data from excel
sport = "tntbet365odds"
excel_data = pandas.read_excel('Odds.xlsx', sheet_name=sport)
count = 0
number = 322

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
        pyautogui.press('down')
        pyautogui.press('down')
    #JUMP EVENTS WITH TWO DESCRIPTIONS
    elif (str(int(excel_data['Odds'][count]))) == '-60':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

        #all action with 2 descriptions
    elif (str(int(excel_data['Odds'][count]))) == '-70':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.typewrite('-120')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.press('enter')
        pyautogui.press('down')
        #ALL ACTION, DEAD HEAT RULE
    elif (str(int(excel_data['Odds'][count]))) == '-80':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    else:
        pyautogui.press('enter')
        pyautogui.typewrite(str(int(excel_data['Odds'][count])))
        pyautogui.press('enter')
        pyautogui.press('down')
    # Set counter with the number of Rows
    if count == number - 1:
        break
    count = count + 1
