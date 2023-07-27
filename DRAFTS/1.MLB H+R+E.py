import re
import time
import pyautogui
time.sleep(3)


text = """

Cincinnati Reds
L. Weaver -R
O 28½
+105
1958
Milwaukee Brewers
C. Rea -R
U 28½
-135
04:10 PM
1965
Oakland Athletics
P. Blackburn -R
O 28
+100
1966
Boston Red Sox
J. Paxton -L
U 28
-130
04:10 PM
1967
Kansas City Royals
B. Singer -R
O 26
-110
1968
Cleveland Guardians
G. Williams -R
U 26
-120
07:15 PM
1969
Seattle Mariners
B. Woo -R
O 25
+105
1970
Houston Astros
F. Valdez -L
U 25
-135
07:15 PM
1977
Atlanta Braves
S. Strider -R
O 26
+100
1978
Tampa Bay Rays
T. Bradley -R
U 26
-130
10:10 PM
1959

"""
def enterodds():
    pyautogui.press('enter')
    pyautogui.typewrite((number))
    pyautogui.press('enter')
    pyautogui.press('down', presses=3)

# Find all numbers following "O" (OVER) keyword using regular expressions
over_numbers = re.findall(r"O (\d+½|\d+)", text)
over_number = [number.replace("½", ".5") for number in over_numbers]

# Print the extracted OVER numbers
for number in over_number:
    print(number)
    enterodds()

