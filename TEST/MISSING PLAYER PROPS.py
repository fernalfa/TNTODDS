from collections import Counter

# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.strip().split('\n')
regular_season_lines = []

for line in lines:
    if "REGULAR SEASON " in line:
        regular_season_lines.append(line)


# Count the occurrences of each line in the regular_season_lines
line_counts = Counter(regular_season_lines)

# Print the unique lines that appear only once
unique_lines = [line for line, count in line_counts.items() if count == 1]
for line in unique_lines:
    print(line)
