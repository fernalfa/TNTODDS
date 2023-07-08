import re
import time
import pyautogui
time.sleep(3)

# COPIAR Y PEGAR DE BOOKMAKER
data = '''
Val Woodburn vrs Bo Nickal: Will The Fight Go To Distance?
Yes
+750
No
-1650
Val Woodburn vrs Bo Nickal: Fight Distance
Fight ends In Rd-1
-325
Fight ends In Rd-2
+540
Fight ends In Rd-3
+925
Fight By Decision
+775
Val Woodburn vrs Bo Nickal: Who Will Win And When?
Val Woodburn wins in round 1
+2541
Val Woodburn wins in round 2
+3120
Val Woodburn wins in round 3
+4580
Val Woodburn by decisions
+2897
Bo Nickal wins in round 1
-477
Bo Nickal wins in round 2
+626
Bo Nickal wins in round 3
+1115
Bo Nickal by decisions
+1166
Draw
+6624
Val Woodburn vrs Bo Nickal:Fight Outcome
Val Woodburn By KO,TKO OR DQ
+1800
Val Woodburn By Submission
+4050
Val Woodburn By Decision
+2950
Bo Nickal By KO,TKO OR DQ
+225
Bo Nickal By Submission
-280
Bo Nickal By Decision
+1200
Draw
+6950
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