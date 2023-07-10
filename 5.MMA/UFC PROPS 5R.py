import re
import time
import pyautogui
time.sleep(3)

# COPIAR Y PEGAR DE BOOKMAKER
data = '''
Yair Rodriguez vrs Alexander Volkanovski: Will The Fight Go To Distance?
Yes
-105
No
-125
Yair Rodriguez vrs Alexander Volkanovski: Fight Distance
Fight ends In Rd-1
+425
Fight ends In Rd-2
+565
Fight ends In Rd-3
+745
Fight ends In Rd-4
+900
Fight ends In Rd-5
+1200
Fight By Decision
-105
Yair Rodriguez vrs Alexander Volkanovski: Who Will Win And When?
Yair Rodriguez wins in round 1
+1150
Yair Rodriguez wins in round 2
+1650
Yair Rodriguez wins in round 3
+2200
Yair Rodriguez wins in round 4
+2650
Yair Rodriguez wins in round 5
+3250
Yair Rodriguez by decisions
+900
Alexander Volkanovski wins in round 1
+600
Alexander Volkanovski wins in round 2
+750
Alexander Volkanovski wins in round 3
+950
Alexander Volkanovski wins in round 4
+1150
Alexander Volkanovski wins in round 5
+1500
Alexander Volkanovski by decisions
+125
Draw
+6500
Yair Rodriguez vrs Alexander Volkanovski: How Will The Fight End?
KO, TKO, DQ
+100
Submission
+460
Decisions
-105
Draw
+6500
Yair Rodriguez vrs Alexander Volkanovski:Fight Outcome
Yair Rodriguez By KO,TKO OR DQ
+500
Yair Rodriguez By Submission
+1000
Yair Rodriguez By Decision
+900
Alexander Volkanovski By KO,TKO OR DQ
+195
Alexander Volkanovski By Submission
+900
Alexander Volkanovski By Decision
+125
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

    if i + 1 in [2, 8, 21, 25]:  # Execute the function after 2, 4, and 9 numbers
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')