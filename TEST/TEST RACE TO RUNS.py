import re

# Open the text file
with open('../0.INFO', 'r') as file:
    text = file.read()

lines = text.strip().split("\n")  # Split the text into lines
values = [lines]


for i in range(len(lines) - 1):
    if lines[i].isalpha() and lines[i + 1].strip().isdigit():
        second_value = lines[i + 1].strip()
        values.append(second_value)

print(values)
