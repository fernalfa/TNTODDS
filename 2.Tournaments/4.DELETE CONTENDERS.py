import time
import pyautogui
time.sleep(5)

number = 101

def delete_empty():
    pyautogui.press(['tab', 'tab', 'enter', 'enter', 'up', 'down'])

for count in range(1, number + 1):
    delete_empty()
    print(count)