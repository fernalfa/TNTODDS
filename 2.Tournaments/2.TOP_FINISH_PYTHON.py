import time
import pyautogui

with open('../0.INFO', 'r', encoding='utf-8', errors='replace') as file:
    text = file.read()

# Split the text into lines
lines = text.strip().split('\n')

# Create a dictionary to store the odds
odds_dict = {}

current_golfer = None
current_category = None

# Iterate through the lines and populate the dictionary
for line in lines:
    if line.startswith('+'):  # Odds line
        odds_dict[current_golfer][current_category].append(int(line))
    elif line.startswith('Top'):  # Category line
        current_category = line.strip()
        odds_dict[current_golfer][current_category] = []  # Initialize the odds list for the current category
    else:  # Golfer line
        current_golfer = line.strip()
        odds_dict[current_golfer] = {"Top 5": [], "Top 10": [], "Top 20": []}

# Order the odds without changing golfer order
for golfer, categories in odds_dict.items():
    print(f"{golfer}:")
    for category, odds in categories.items():
        print(f"{category}: {odds}")
        categories[category] = sorted(odds)
    print("\n")
