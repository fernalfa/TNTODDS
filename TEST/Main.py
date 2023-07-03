data = """
LA Dodgers-logoLA Dodgers
at
KC Royals-logoKC Royals
TODAY 2:10PM
Inning of First Run

1st Inning
−160
2nd Inning
+270
3rd Inning
+600
4th Inning
+1300
5th Inning
+2200
6th Inning
+3500
7th Inning
+5000
9th Inning
+7000
8th Inning
+7500
10th Inning or Later
+8000
Inning of Last Run

9th Inning
+105
8th Inning
+265
7th Inning
+550
10th Inning or Later
+800
6th Inning
+1100
5th Inning
+2200
4th Inning
+3500
3rd Inning
+5000
2nd Inning
+6500
1st Inning
+8000
NY Yankees-logoNY Yankees
at
STL Cardinals-logoSTL Cardinals
TODAY 2:15PM
Inning of First Run

1st Inning
−115
2nd Inning
+265
3rd Inning
+500
4th Inning
+950
5th Inning
+1800
6th Inning
+2500
7th Inning
+4500
8th Inning
+5500
9th Inning
+5500
10th Inning or Later
+6000
Inning of Last Run

9th Inning
+150
8th Inning
+245
7th Inning
+550
10th Inning or Later
+700
6th Inning
+850
5th Inning
+1600
4th Inning
+2500
3rd Inning
+3500
2nd Inning
+5000
1st Inning
+6000
"""

lines = data.strip().split("\n")

inning_data = []
game_data = []

for i, line in enumerate(lines):
    if "Inning of First Run" in line:
        start_index = i + 1
    elif "Inning of Last Run" in line:
        end_index = i
        game_data.append(inning_data)
        inning_data = []
    elif line.startswith("+") or line.startswith("-") or line.startswith("−"):
        inning_data.append(line)

print(game_data)
print(inning_data)