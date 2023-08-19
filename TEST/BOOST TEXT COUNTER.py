import re

exclude_patterns = [
    re.compile(r'^\s*\+'),
    re.compile(r'^\s*-\s*'),
    re.compile(r'^\s*YES'),
    re.compile(r'^\s*BOOSTED ODDS'),
    re.compile(r'^\s*SPECIALS'),
    re.compile(r'^\s*BOOSTED WIN PARLAY'),
    re.compile(r'^\s*ODDS BOOST - BOOSTED WIN PARLAY'),
    re.compile(r'^\s*ODDS BOOST - ODDS BOOST'),
    re.compile(r'^\s*ODDS BOOST'),
    re.compile(r'^\s*BET BUILDER'),
    re.compile(r'^\s*WINNER'),
    re.compile(r'^\s*REGULAR TIME ONLY'),
    re.compile(r'^\s*#BETYOURWAY - TEAM FOCUS'),
    re.compile(r'^\s*#BETYOURWAY UP TO 10.0'),
    re.compile(r'^\s*#BETYOURWAY UP TO 26.0'),
    re.compile(r'^\s*PARLAYS: ODDS < +1000'),
    re.compile(r'^\s*PARLAYS: ODDS +1000 TO +2000'),
    re.compile(r'^\s*REGULAR TIME ONLY. BETS SETTLED USING OPTA DATA. THE PLAYERS MUST START THE MATCH FOR BETS TO STAND.'),
    re.compile(r'^\s*BETS SETTLED USING OPTA DATA. THE PLAYER MUST START THE MATCH FOR BETS TO STAND.'),
    re.compile(r'^\s*BETS SETTLED USING OPTA DATA. THE PLAYERS MUST START THE MATCH FOR BETS TO STAND.'),
    re.compile(r'^\s*THE PLAYER MUST START THE MATCH FOR BETS TO STAND'),
    re.compile(r'^\s*THE PLAYERS MUST START THE MATCH FOR BETS TO STAND'),
    # Add more patterns here
]

replace_patterns = [
    (re.compile(r'\b , \b'), ','),
    (re.compile(r'\b\+ \b'), '+'),
    (re.compile(r'\bTO WIN\b'), 'WINS'),
    (re.compile(r'\bSHOTS ON GOAL\b'), 'SOT'),
    (re.compile(r'\b AND \b'), '/'),
    # Add more replacement patterns here
    (re.compile(r'\bKHVICHA KVARATSKHELIA\b'), 'K.KVARATSKHELIA '),
    (re.compile(r'\bVICTOR OSIMHEN\b'), 'V.OSIMHEN'),
    (re.compile(r'\bANDREA BELOTTI\b'), 'A.BELOTTI'),
    (re.compile(r'\bSTEPHAN EL SHAARAWY\b'), 'S.EL SHAARAWY'),
    # Add more replacement patterns here
    (re.compile(r'\bHOME RUNS\b'), 'HRS'),
    (re.compile(r'\bSTRIKEOUTS \b'), 'SO'),
    (re.compile(r'\bSTRIKEOUTS/\b'), 'SO/'),
    (re.compile(r'\bVINICIUS JUNIOR\b'), 'V.JUNIOR'),
]


# Open the text file
with open('../0.INFO', 'r', encoding='utf-8', errors='replace') as file:
    data = file.read()
    for pattern, replacement in replace_patterns:
        data = pattern.sub(replacement, data)

lines = data.strip().split('\n')

list1 = []
list2 = []

for line_number, line in enumerate(lines, start=1):
    if any(pattern.match(line) for pattern in exclude_patterns):
        continue
    char_count = len(line.strip())
    list1.append((line_number, line))  # Store line number and line
    if char_count > 50:
        list2.append((line_number, line, char_count))  # Store line number, line, and char_count

print("CONTENDERS TO FIX:")
print("**************************:")
for line_number, line, char_count in list2:
    print(f"Line {line_number}: {line} ({char_count} characters)")

print("\n************************:")
print("FINAL LIST:")
print("**************************:")
for line_number, line in list1:
    print(f"{line}")