import pyautogui
import time

# Define a list of custom texts to use in each iteration
custom_texts = ['461', '463', '459', '467']
# Define the number of times to repeat the actions for each custom text
num_repeats_list = [2, 2, 2, 2]

# Delay to allow you to focus on the target window
time.sleep(5)

# Iterate through the custom texts and their corresponding num_repeats
for custom_text, num_repeats in zip(custom_texts, num_repeats_list):
    for _ in range(num_repeats):
        # Simulate CTRL+ENTER
        pyautogui.hotkey('ctrl', 'enter')

        # Simulate SHIFT+TAB three times
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')

        # Typing the custom text
        pyautogui.typewrite(custom_text)

        pyautogui.press('tab')
        pyautogui.press('tab')

        # Typing the custom text
        pyautogui.typewrite(custom_text)

        # Simulate ALT+O twice
        pyautogui.hotkey('alt', 'o')
        time.sleep(7)
        pyautogui.press('tab')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

    # Optionally, you can add a delay between iterations to give you time to switch to the next text
    time.sleep(2)