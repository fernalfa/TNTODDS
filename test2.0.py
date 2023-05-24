import re

text = """CHI White Sox @ CLE Guardians
Tue 23 May 18:10
Solo HR
-115
2-Run HR
+200
3-Run HR
+750
Grand Slam
+3000
No HR Scored
+450
TEX Rangers @ PIT Pirates
Tue 23 May 18:35
Solo HR
-135
2-Run HR
+200
3-Run HR
+850
Grand Slam
+3500
No HR Scored
+550"""

lines = text.split('\n')

# Extract dates and remove them from the lines
dates = []
for i in range(1, len(lines), 6):
    date = lines[i]
    dates.append(date)
    lines[i] = ''

# Remove empty lines from the list
lines = [line for line in lines if line]

# Print the modified lines
for line in lines:
    print(line)

# Print the extracted dates
print("Dates:", dates)