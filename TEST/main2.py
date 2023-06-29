import re

# Lines data
lines_data = """
08:10 PM
1961
Cleveland Guardians
L. Allen -L
O 27
-140
1962
Kansas City Royals
A. Cox-L
U 27
+110
09:38 PM
1963
Chicago White Sox
L. Giolito -R
O 26
-140
1964
Los Angeles Angels
J. Barria -R
U 26
+110
09:40 PM
1965
New York Yankees
D. German -R
O 25½
+105
1966
Oakland Athletics
J. Sears -L
U 25½
-135
09:40 PM
1979
Tampa Bay Rays
Z. Eflin -R
O 27½
-130
1980
Arizona Diamondbacks
Z. Davies -R
U 27½
+100
"""

# Define the regex pattern
pattern = r"(O|U)\s+((\d+)(½)?)\n(-?\d+)"

# Find all matches in the lines data
matches = re.findall(pattern, lines_data)

# Initialize variables to store Over and Under prices
over_price = None
under_price = None

# Iterate over the matches and extract the relevant information
for i in range(len(matches)):
    over_under = matches[i][0]
    number = matches[i][2]
    line = matches[i][4]  # Updated index for line value

    if over_under == 'O':
        # Check if there is a next line
        if i + 1 < len(matches):
            next_line = matches[i + 1][4]  # Updated index for next line value
            # Check if the next line is an Under line and negative
            if matches[i + 1][4] == 'U' and int(next_line) < 0:
                under_price = next_line

        # Process the Over and Under prices together
        print(f"Total: {number}")
        print(f"Over Price: {line}")
        print(f"under Price: {under_price}")

        # Reset the Under price for the next iteration
        under_price = None