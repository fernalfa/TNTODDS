import re
import time

time.sleep(3)

# Example text containing the lines
text = '''
2023 MLB DRAFT- BLAKE MITCHELL DRAFT POSITION
MLB DRAFT 2023 - DRAFT POSITION
OVER @ UNDER
JUL 077:00 AM

ROT

TEAM

PITCHER

M LINE

TOTAL

RUN LINE
9595911

OVER
9595912

UNDER
2023 MLB DRAFT- BROCK WILKEN DRAFT POSITION
MLB DRAFT 2023 - DRAFT POSITION
OVER @ UNDER
JUL 077:00 AM

ROT

TEAM

PITCHER

M LINE

TOTAL

RUN LINE
9595913

OVER
9595914

UNDER
2023 MLB DRAFT- CHASE DAVIS DRAFT POSITION
MLB DRAFT 2023 - DRAFT POSITION
OVER @ UNDER
JUL 077:00 AM

ROT

TEAM

PITCHER

M LINE

TOTAL

RUN LINE
9595915

OVER
9595916

UNDER
2023 MLB DRAFT- ENRIQUE BRADFIELD JR. DRAFT POSITION
MLB DRAFT 2023 - DRAFT POSITION
OVER @ UNDER
JUL 077:00 AM

ROT

TEAM

PITCHER

M LINE

TOTAL

RUN LINE
9595917

OVER
9595918

UNDER
'''

# Define the pattern to match player names
pattern = r'2023 MLB DRAFT- [A-Z\s.]+ DRAFT POSITION'

# Find all matches in the text
matches = re.findall(pattern, text)

# Print the extracted lines with player names
for match in matches:
    print(match.strip())