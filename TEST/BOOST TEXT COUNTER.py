# Open the text file
with open('../0.INFO', 'r') as file:
    data = file.read()
lines = data.strip().split('\n')



for i, line in enumerate(lines, 1):
    if not line.startswith('+') and not line.startswith('-'):
        char_count = len(line)
        if char_count > 50:
            print(f"Line {i}: {line} ({char_count} characters)")