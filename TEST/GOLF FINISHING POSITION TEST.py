# Read the code from a text file
with open("../2.Tournaments/DATAPROVIDER", "r") as file:
    code = file.read()

# Split the code into lines
lines = code.strip().split("\n")

# Extract the player names
players = []
for line in lines:
    if not line.isdigit() and "or" not in line and not line.startswith("-"):
        players.append(line)

# Initialize empty lists for "better" and "worse" values
better_values = []
worse_values = []

# Iterate over the remaining lines
for line in lines:
    if "or Better" in line:
        better_values.append(line)
    elif "or Worse" in line:
        worse_values.append(line)

# Print the extracted information
print("Players:")
for player in players:
    print(player)

print("\nBetter Values:")
for value in better_values:
    print(value)

print("\nWorse Values:")
for value in worse_values:
    print(value)
