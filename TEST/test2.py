with open('DATA IBET', 'r') as file:
    lines = file.readlines()

player_names = []

for line in lines:
    if line.strip().isdigit():
        continue
    if line.strip():
        player_names.append(line.strip())

print(player_names)


