import time
import pyautogui
time.sleep(4)


number = 1

TEAMS = 'BRAVES @ METS'
A = 5502329
B = 5502329

C = 5503329
D = 5504329

E = 5505293
F = 5506311
G = 5507329

H = 5508329


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
    pyautogui.write(str(H))
    pyautogui.press('tab', presses = 3)
    pyautogui.write(str(TEAMS))
    pyautogui.hotkey('alt', 'o')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

count = 0

while (count < number):
    count = count + 1
    print(deleteempty())