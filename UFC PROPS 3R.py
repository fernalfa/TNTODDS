import re
import time
import pyautogui
time.sleep(3)

# COPIAR Y PEGAR DE BOOKMAKER
data = '''
Dricus Du Plessis vrs Robert Whittaker: Will The Fight Go To Distance?
Yes
+155
No
-205
Dricus Du Plessis vrs Robert Whittaker: Fight Distance
Fight ends In Rd-1
+235
Fight ends In Rd-2
+325
Fight ends In Rd-3
+405
Fight By Decision
+155
Dricus Du Plessis vrs Robert Whittaker: Who Will Win And When?
Dricus Du Plessis wins in round 1
+875
Dricus Du Plessis wins in round 2
+1350
Dricus Du Plessis wins in round 3
+1750
Dricus Du Plessis by decisions
+700
Robert Whittaker wins in round 1
+350
Robert Whittaker wins in round 2
+425
Robert Whittaker wins in round 3
+500
Robert Whittaker by decisions
+175
Draw
+6500
Dricus Du Plessis vrs Robert Whittaker:Fight Outcome
Dricus Du Plessis By KO,TKO OR DQ
+450
Dricus Du Plessis By Submission
+1375
Dricus Du Plessis By Decision
+700
Robert Whittaker By KO,TKO OR DQ
+135
Robert Whittaker By Submission
+1150
Robert Whittaker By Decision
+175
Draw
+6500
'''

numbers = re.findall(r'[+-]?\d{2,}', data)

for i, num in enumerate(numbers):
    if num.startswith('-'):  # Write the sign for negative numbers
        sign = '-'
    else:
        sign = ''
    num = sign + num.lstrip('+-')  # Remove the sign from the number if it's positive
    pyautogui.press('enter')
    pyautogui.write(num)
    pyautogui.press('enter')
    pyautogui.press('down')

    if i + 1 in [2, 6, 15]:  # Execute the function after 2, 4, and 9 numbers
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')