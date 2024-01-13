import pyautogui
import time
time.sleep(5)


data = """
Tommy Fleetwood
Tony Finau
Tyrrell Hatton
Viktor Hovland
Wyndham Clark
Xander Schauffele
1
21 or Better
-120
24 or Better
-120
11 or Better
-120
30 or Better
-120
25 or Better
-120
25 or Better
-120
17 or Better
-120
25 or Better
-120
13 or Better
-120
20 or Better
-120
14 or Better
-120
12 or Better
-120
22 or Better
-120
24 or Better
-120
24 or Better
-120
6 or Better
-120
25 or Better
-120
21 or Better
-120
18 or Better
-120
21 or Better
-120
20 or Better
-120
20 or Better
-120
10 or Better
-125
26 or Better
-120
14 or Better
-120
2
22 or Worse
-120
25 or Worse
-120
12 or Worse
-120
31 or Worse
-120
26 or Worse
-120
26 or Worse
-120
18 or Worse
-120
26 or Worse
-120
14 or Worse
-120
21 or Worse
-120
15 or Worse
-120
13 or Worse
-120
23 or Worse
-120
25 or Worse
-120
25 or Worse
-120
7 or Worse
-120
26 or Worse
-120
22 or Worse
-120
19 or Worse
-120
22 or Worse
-120
21 or Worse
-120
21 or Worse
-120
11 or Worse
-110
27 or Worse
-120
15 or Worse
-120
"""


lines = data.strip().split("\n")
players = []
better = []
worse = []
current_category = None

for line in lines:
    if line.isnumeric():
        if current_category:
            current_category.append(line)
    elif line.startswith("-"):
        current_category[-1] += line
    else:
        if "or Better" in line:
            current_category = better
        elif "or Worse" in line:
            current_category = worse
        else:
            current_category = players
        if "-120" not in line:
            if current_category and "-120" in current_category[-1]:
                current_category[-1] = current_category[-1].replace("-120", "").strip()
            current_category.append(line)

def slow_type(text, delay=0.01):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)

HEADER = " - FINISHING POSITION"

# Define your function here
def your_function(arg1, arg2, arg3):
    slow_type(arg1)
    slow_type(HEADER)
    pyautogui.press('tab', presses=3)
    slow_type(arg2)
    pyautogui.press('tab')
    slow_type(arg3)
    pyautogui.hotkey('alt', 'o')
    time.sleep(10)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=4)
    pyautogui.keyUp('shift')
    # Your function implementation here
    print(f"Function called with args: {arg1}, {arg2}, {arg3}")

# Assuming each category has the same length
category_length = len(players)
for i in range(category_length):
    arg1 = players[i]
    arg2 = better[i]
    arg3 = worse[i]
    your_function(arg1, arg2, arg3)
