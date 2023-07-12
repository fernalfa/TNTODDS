import time
import pyautogui
time.sleep(4)  # Starting delay

value = 1109201 # ROTATION NUMBER

options = [
    " TO WIN EXACTLY 0 GAMES",
    " TO WIN EXACTLY 1 GAMES",
    " TO WIN EXACTLY 2 GAMES",
    " TO WIN EXACTLY 3 GAMES",
    " TO WIN EXACTLY 4 GAMES",
    " TO WIN EXACTLY 5 GAMES",
    " TO WIN EXACTLY 6 GAMES",
    " TO WIN EXACTLY 7 GAMES",
    " TO WIN EXACTLY 8 GAMES",
    " TO WIN EXACTLY 9 GAMES",
    " TO WIN EXACTLY 10 GAMES",
    " TO WIN EXACTLY 11 GAMES",
    " TO WIN EXACTLY 12 GAMES",
    " TO WIN EXACTLY 13 GAMES",
    " TO WIN EXACTLY 14 GAMES",
    " TO WIN EXACTLY 15 GAMES",
    " TO WIN EXACTLY 16 GAMES",
    " TO WIN EXACTLY 17 GAMES"
]



# Read player info from text file
with open('TEST', 'r') as file:
    player_info = file.readlines()

# Iterate through player info
for count, player in enumerate(player_info, start=1):
    player = player.strip()  # Remove leading/trailing whitespace and newline characters
    pyautogui.typewrite(player)
    pyautogui.write(" - EXACT REGULAR SEASONS WINS")
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(value))
    pyautogui.press('tab')
    pyautogui.write("** ALL BETS ACTION **")
    pyautogui.press('enter')
    for option in options:
        pyautogui.typewrite(str(player))
        time.sleep(1)
        pyautogui.write(option)
        pyautogui.press('enter')
    pyautogui.press('backspace')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

print(f"{count}: {player}")
value = value + 100








