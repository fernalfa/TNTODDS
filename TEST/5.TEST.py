import time
import re
import pyautogui
time.sleep(3)

def split_text_numbers(data):
    pattern = r'([A-Za-z\s]+)(\d+:\d+)([A-Za-z\s]+)\n([+-]?\d+)'
    matches = re.findall(pattern, data)
    result = []
    for match in matches:
        team1 = match[0].strip()
        score = match[1]
        team2 = match[2].strip()
        number = int(match[3])
        result.append((team1, score, team2, number))
    return result

def oddsprint():
    pyautogui.press('enter')
    pyautogui.typewrite(str(int(number)))
    pyautogui.press('enter')
    pyautogui.press('down')



# Example usage
data = '''
MIA Heat 83:78 BOS Celtics
+18000
MIA Heat 79:72 BOS Celtics
+18000
MIA Heat 80:88 BOS Celtics
+18000
MIA Heat 74:80 BOS Celtics
+18000
MIA Heat 83:78 BOS Celtics
+18000
MIA Heat 79:72 BOS Celtics
+18000
MIA Heat 80:88 BOS Celtics
+18000
MIA Heat 74:80 BOS Celtics
+18000
MIA Heat 83:78 BOS Celtics
+18000
MIA Heat 79:72 BOS Celtics
+18000
MIA Heat 80:88 BOS Celtics
+18000
MIA Heat 74:80 BOS Celtics
+18000
MIA Heat 83:78 BOS Celtics
+18000
MIA Heat 79:72 BOS Celtics
+18000
MIA Heat 80:88 BOS Celtics
+18000
MIA Heat 74:80 BOS Celtics
+18000
'''

split_result = split_text_numbers(data)
for item in split_result:
    team1, score, team2, number = item

    print(oddsprint())
    time.sleep(3)
    print(f'{team1} {score} {team2} {number}')