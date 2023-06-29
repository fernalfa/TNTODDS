data = """
07:05 PM
1951
San Diego Padres
B. Snell -L
O 25½
-120
1952
Pittsburgh Pirates
M. Keller -R
U 25½
-110
07:05 PM
1971
Cincinnati Reds
L. Weaver -R
O 28
-115
1972
Baltimore Orioles
K. Gibson -R
U 28
-115
"""

lines = data.split('\n')

rows = []
current_row = {}

for line in lines:
    line = line.strip()
    if line:
        if "PM" in line or "AM" in line:
            current_row["Time"] = line
        elif line.isdigit():
            current_row["Rot Number"] = int(line)
        elif line.startswith("O"):
            _, over_total, over_odds = line.split()
            current_row["Total Over"] = int(over_total)
            current_row["Over Odds"] = int(over_odds)
        elif line.startswith("U"):
            _, under_total, under_odds = line.split()
            current_row["Total Under"] = int(under_total)
            current_row["Under Odds"] = int(under_odds)
            rows.append(current_row)
            current_row = {}

# Print the collected rows
for row in rows:
    print("Time:", row["Time"])
    print("Rot Number:", row["Rot Number"])
    print("Total Over:", row["Total Over"])
    print("Over Odds:", row["Over Odds"])
    print("Total Under:", row["Total Under"])
    print("Under Odds:", row["Under Odds"])
