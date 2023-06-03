data = """
07:05 PM
1911
Texas Rangers
J. Gray -R
O 26
-135
1912
Baltimore Orioles
G. Rodriguez -R
U 26
+105
07:05 PM
1919
San Diego Padres
J. Musgrove -R
O 27
-120
1920
New York Yankees
R. Vasquez -R
U 27
-110
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
