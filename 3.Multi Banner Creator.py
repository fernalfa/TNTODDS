import time
import pyautogui
time.sleep(4)

number = 1

TEAMS = 'PIRATES @ TIGERS'

# ENTER PITCHER PROPS ROTATION
A = 5315001
# ENTER TOTAL BASES ROTATION
B = 5325001
# ENTER SINGLES ROTATION
C = 5335001
# ENTER DOUBLES ROTATION
D = 5345001
# ENTER STOLEN BASES ROTATION
E = 5355001
# ENTER TOTAL RUNS ROTATION
F = 5365001
# ENTER TOTAL HOME RUNS ROTATION
G = 5375001


def deleteempty():
    pyautogui.write(str(A))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(B))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(C))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(D))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(E))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(F))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.write(str(G))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('del')

count = 0

while (count < number):
    count = count + 1
    print(deleteempty())
    print(TEAMS + ' BANNERS CREATED, PLEASE CHECK')