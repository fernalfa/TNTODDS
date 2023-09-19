import pyautogui
import time
time.sleep(5)


data = """
Abraham Ancer
Anirban Lahiri
Branden Grace
Brendan Steele
Brooks Koepka
Bryson DeChambeau
Cameron Smith
Cameron Tringale
Carlos Ortiz
Charles Howell III
Dean Burmester
Dustin Johnson
Harold Varner III
Jason Kokrak
Joaquin Niemann
Louis Oosthuizen
Marc Leishman
Mito Pereira
Patrick Reed
Paul Casey
Richard Bland
Sebastian Munoz
Sergio Garcia
Talor Gooch
Thomas Pieters
1
16 or Better
-120
18 or Better
-120
16 or Better
-120
18 or Better
-120
12 or Better
-120
10 or Better
-120
7 or Better
-120
17 or Better
-120
19 or Better
-120
18 or Better
-120
16 or Better
-120
11 or Better
-120
16 or Better
-120
18 or Better
-120
13 or Better
-120
20 or Better
-120
20 or Better
-120
13 or Better
-120
11 or Better
-120
21 or Better
-120
22 or Better
-120
17 or Better
-120
17 or Better
-120
11 or Better
-120
21 or Better
-120
2
17 or Worse
-120
19 or Worse
-120
17 or Worse
-120
19 or Worse
-120
13 or Worse
-120
11 or Worse
-120
8 or Worse
-120
18 or Worse
-120
20 or Worse
-120
19 or Worse
-120
17 or Worse
-120
12 or Worse
-120
17 or Worse
-120
19 or Worse
-120
14 or Worse
-120
21 or Worse
-120
21 or Worse
-120
14 or Worse
-120
12 or Worse
-120
22 or Worse
-120
23 or Worse
-120
18 or Worse
-120
18 or Worse
-120
12 or Worse
-120
22 or Worse
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

HEADER = " - test test"

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
