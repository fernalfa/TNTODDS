import re

# Read the code from a text file
with open("../0.INFO", "r") as file:
    text = file.read()


player_names = re.findall(r"^[A-Z\s'.-]+", text, re.MULTILINE)

names = []

for line in player_names:
    if line.strip().isdigit():
        continue
    if line.strip():
        names.append(line.strip())

# Print the first list of names
print("First List:")
for name in names:
    print(name)

