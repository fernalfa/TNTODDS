data = """TEX Rangers
 
-6.5
+675
PIT Pirates
 
+6.5
−1100
TEX Rangers
 
-6
+650
PIT Pirates
 
+6
−1050
TEX Rangers
 
-5.5
+490
PIT Pirates
 
+5.5
−725
TEX Rangers
 
-5
+460
PIT Pirates
 
+5
−670
TEX Rangers
 
-4.5
+340
PIT Pirates
 
+4.5
−450
TEX Rangers
 
-4
+310
PIT Pirates
 
+4
−410
TEX Rangers
 
-3.5
+235
PIT Pirates
 
+3.5
−300
TEX Rangers
 
-3
+210
PIT Pirates
 
+3
−265
TEX Rangers
 
-2.5
+160
PIT Pirates
 
+2.5
−195
TEX Rangers
 
-2
+130
PIT Pirates
 
+2
−160
TEX Rangers
 
-1
−135
PIT Pirates
 
+1
+105
TEX Rangers
 
+1
−300
PIT Pirates
 
-1
+235
TEX Rangers
 
+1.5
−400
PIT Pirates
 
-1.5
+300
TEX Rangers
 
+2
−670
PIT Pirates
 
-2
+460
TEX Rangers
 
+2.5
−760
PIT Pirates
 
-2.5
+510
TEX Rangers
 
+3
−1300
PIT Pirates
 
-3
+750"""

lines = data.split('\n')

rows = []
current_row = {}
current_key = ""

for line in lines:
    line = line.strip()
    if line:
        if not current_key or current_key == "Team":
            current_row["Team"] = line
            current_key = "Spread"
        elif current_key == "Spread":
            current_row["Spread"] = float(line)
            current_key = "Odds"
        elif current_key == "Odds":
            odds_value = line.replace("−", "-")  # Replace minus sign character with regular hyphen
            current_row["Odds"] = int(odds_value)
            if current_row["Spread"] in [-2.5, -1.5, -1, 1, 1.5, 2.5]:
                rows.append(current_row)
            current_row = {}
            current_key = "Team"

# Print the collected rows
for row in rows:
    print("Team:", row["Team"])
    print("Spread:", row["Spread"])
    print("Odds:", row["Odds"])
    print()