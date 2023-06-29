import re

data = '''

WTA - BAD HOMBURG WINNER - jun 29
WTA - BAD HOMBURG WINNER
WTA - BAD HOMBURG WINNER
WTA - BAD HOMBURG WINNER
Jun 29 - 6:00 AM

Rot

Description

Odds


8840101

**ALL ACTION**
8840102

IGA SWIATEK
8840103

LIUDMILA SAMSONOVA
8840108

ANNA BLINKOVA
8840112

LUCIA BRONZETTI
8840113

VARVARA GRACHEVA
8840115

EMMA NAVARRO
8840121

REBEKA MASAROVA
8840122

KATERINA SINIAKOVA

'''

# Extract the names using regular expressions
names = re.findall(r'\n\d+\n\n(.+)', data)

# Print the names vertically
for name in names:
    print(name)
