import re

# Read the code from a text file
with open('DATAIBET', 'r') as file:
    lines = file.readlines()

names = []

for line in lines:
    line = line.strip()
    if line.isdigit() or line.startswith('+') or line.startswith('-'):
        continue
    if line:
        names.append(line)

print(names)

# Print the first list of names
print("First List:")
for name in names:
    print(name)

