import time
import pyautogui

# Read player names from text file
with open('../0.INFO', 'r') as file:
    player_names = file.readlines()

time.sleep(3)

for count, player in enumerate(player_names, start=1):
    player = player.strip()  # Remove leading/trailing whitespace and newline characters
    pyautogui.typewrite(player)
    pyautogui.write(" - ")
    pyautogui.write(" TO MAKE THE CUT")
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(player)
    pyautogui.write(" YES MAKE CUT")
    pyautogui.press('tab')
    pyautogui.typewrite(player)
    pyautogui.write(" NO MAKE CUT")
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('alt', 'o')
    time.sleep(8)

    print(f"{count}: {player}")

print('COMPLETED')
