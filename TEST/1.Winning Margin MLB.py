import time
import pyautogui
time.sleep(3)

data = '''
MIN Twins @ ATL Braves
Tue 27 Jun 19:20
 
1
2
3
4+
MIN Twins
+800
+750
+1000
+425
ATL Braves
+500
+650
+800
+325
'''

lines = data.strip().split('\n')
count = 0
for line in lines:
    if line.startswith('+'):
        pyautogui.press('enter')
        pyautogui.write(line[1:])
        pyautogui.press('enter')
        pyautogui.press('down')
        count += 1
        if count % 8 == 0:
            pyautogui.press('down')
            pyautogui.press('down')