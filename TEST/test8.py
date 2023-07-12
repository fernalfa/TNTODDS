import time
import pyautogui
time.sleep(4)  # Starting delay

value = 1110151 # ROTATION NUMBER



# Read player info from text file
with open('TEST', 'r') as file:
    player_info = file.readlines()

# Iterate through player info
for count, player in enumerate(player_info, start=1):
    player = player.strip()  # Remove leading/trailing whitespace and newline characters
    pyautogui.typewrite(player)
    pyautogui.write(" - DIVISION FINISHING POSITION")
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(value))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    value = value + 10


print(f"{count}: {player}")








